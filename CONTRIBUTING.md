# Contributing to MidShield

Thank you for your interest in contributing to MidShield!

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone <your-fork-url>`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes thoroughly
6. Commit with clear messages: `git commit -m "Add: feature description"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Development Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your GROQ_API_KEY to .env
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

## Testing

Before submitting a PR:

1. Test the API: `uvicorn main:app --reload`
2. Test the dashboard: `streamlit run app.py`
3. Try various injection patterns
4. Verify audit logging works

## Pull Request Guidelines

- Describe what your PR does
- Reference any related issues
- Include screenshots for UI changes
- Ensure no secrets are committed
- Update documentation if needed

## Questions?

Open an issue for discussion before starting major changes.
