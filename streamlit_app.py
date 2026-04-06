# Streamlit Cloud entry point
import streamlit as st
import requests
import pandas as pd
import os
import json
from datetime import datetime

# Configuration
API_URL = os.getenv("API_URL", "http://localhost:8000")
LOG_PATH = os.getenv("LOG_PATH", "audit.jsonl")

st.set_page_config(page_title="🛡️ MidShield Demo", page_icon="🛡️", layout="wide")

st.title("🛡️ MidShield")
st.markdown("*Prompt Injection Detection Middleware for Agentic AI*")

# Sidebar: Agent context
st.sidebar.header("Agent Context")
agent_id = st.sidebar.selectbox("Agent Type", ["Sales", "HR", "Finance", "IT", "Support", "Custom"])
source = st.sidebar.radio("Input Source", ["user", "tool", "document"])

# Main scan interface
st.subheader("🔍 Scan Input")
user_input = st.text_area("Enter text to scan:", height=150, placeholder="Type or paste any input...")

col1, col2 = st.columns([1, 4])
with col1:
    scan_btn = st.button("🚀 Scan", type="primary", use_container_width=True)

if scan_btn and user_input.strip():
    with st.spinner("Analyzing..."):
        try:
            response = requests.post(
                f"{API_URL}/scan",
                json={"text": user_input, "agent_id": agent_id, "source": source},
                timeout=10
            )
            if response.status_code == 200:
                result = response.json()
                
                # Visual result display with color coding
                color_map = {"safe": "🟢", "suspicious": "🟠", "malicious": "🔴"}
                st.markdown(f"### {color_map[result['risk']]} Risk: **{result['risk'].upper()}**")
                st.metric("Score", f"{result['score']}/100")
                st.info(f"📝 {result['reason']}")
                st.json({
                    "rule_triggered": result["rule_triggered"],
                    "blocked": result["blocked"],
                    "agent_id": agent_id,
                    "source": source
                })
            else:
                st.error(f"API Error: {response.status_code} — {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Connection failed: {e}. Is the API running at {API_URL}?")

# Live audit log viewer
st.subheader("📋 Live Audit Log")
if os.path.exists(LOG_PATH):
    try:
        logs = []
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    logs.append(json.loads(line))
        if logs:
            df = pd.DataFrame(logs[-20:])  # Show last 20 entries
            df["timestamp"] = pd.to_datetime(df["timestamp"]).dt.strftime("%H:%M:%S")
            df["status"] = df["risk"].map({"safe": "🟢", "suspicious": "🟠", "malicious": "🔴"})
            st.dataframe(
                df[["timestamp", "status", "risk", "score", "input_preview", "blocked"]],
                use_container_width=True,
                hide_index=True
            )
            if st.button("🗑️ Clear Log"):
                open(LOG_PATH, "w").close()
                st.rerun()
        else:
            st.caption("No scans yet — try an input above!")
    except Exception as e:
        st.warning(f"Could not read log: {e}")
else:
    st.caption("Audit log will appear here after first scan.")

# Footer
st.markdown("---")
st.caption(f"MidShield v1.0 • Groq-powered • {datetime.now().strftime('%Y-%m-%d %H:%M')}")
