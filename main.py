from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal, Optional
import os
from datetime import datetime, timezone
import json
from detector import detector

app = FastAPI(title="MidShield API", version="1.0")

#Pydantic models for request/response validation
class DetectionRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=4000)
    agent_id: Optional[str] = "unknown"
    source: Optional[Literal["user", "tool", "document"]] = "user"
    
class DetectionResponse(BaseModel):
    risk: Literal["safe", "suspicious", "malicious"]
    score: int = Field(..., ge=0, le=100)
    reason: str
    rule_triggered: bool
    blocked: bool
    
LOG_PATH = os.getenv("LOG_PATH", "audit.jsonl")

def append_audit_log(entry: dict):
    """Append result to append-only JSONL audit log."""
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
        
        
# routes        
@app.post("/scan", response_model=DetectionResponse)
async def scan_input(request: DetectionRequest):
    """Scan input for prompt injection attacks."""
    try:
        result = detector(request.text)
        blocked = result["risk"] == "malicious"
        
        audit_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent_id": request.agent_id,
            "source": request.source,
            "input_preview": request.text[:100],
            "risk": result['risk'],
            "score": result['score'],
            "reason": result['reason'],
            "rule_triggered": result["rule_triggered"],
            "blocked": blocked
        }
        append_audit_log(audit_entry)
        
        return DetectionResponse(
            risk=result['risk'],
            score=result["score"],
            reason=result['reason'],
            rule_triggered=result["rule_triggered"],
            blocked=blocked
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Scan failed: {str(e)}")

@app.get("/health")
def health_check():
    """Liveness probe for deployment platforms."""
    return {
        "status": "ok",
        "model": "llama-3.3-70b-versatile (Groq)",
        "version": "1.0"
    }
    
@app.get("/")
def root():
    """API landing page."""
    return {
        "message": "MidShield API — Prompt Injection Detection",
    }
        