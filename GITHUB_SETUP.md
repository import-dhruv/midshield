# GitHub Setup Guide

## Initial Setup

### 1. Create GitHub Repository

```bash
# Go to GitHub and create a new repository (don't initialize with README)
# Then run these commands:

git add .
git commit -m "Initial commit: MidShield prompt injection detection system"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/midshield.git
git push -u origin main
```

### 2. Configure Repository Settings

#### Secrets (for GitHub Actions)

Go to: Settings → Secrets and variables → Actions → New repository secret

Add:
- `GROQ_API_KEY` - Your Groq API key (for testing in CI/CD)

#### Branch Protection

Go to: Settings → Branches → Add rule

Configure:
- Branch name pattern: `main`
- ✅ Require pull request reviews before merging
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging

#### Security

Go to: Settings → Security → Code security and analysis

Enable:
- ✅ Dependency graph
- ✅ Dependabot alerts
- ✅ Dependabot security updates
- ✅ Secret scanning

### 3. Add Repository Topics

Settings → General → Topics

Suggested topics:
- `prompt-injection`
- `ai-security`
- `llm-security`
- `fastapi`
- `streamlit`
- `groq`
- `security-middleware`

### 4. Create Initial Release

```bash
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0
```

Then go to: Releases → Draft a new release
- Tag: v1.0.0
- Title: MidShield v1.0.0 - Initial Release
- Description: First stable release with dual-layer detection

## Repository Structure

```
midshield/
├── .github/
│   └── workflows/
│       └── security-check.yml    # Automated security scanning
├── .git/
│   └── hooks/
│       └── pre-commit             # Local commit validation
├── app.py                         # Streamlit dashboard
├── main.py                        # FastAPI server
├── detector.py                    # Detection engine
├── requirements.txt               # Dependencies
├── .env.example                   # Environment template
├── .gitignore                     # Git ignore rules
├── README.md                      # Main documentation
├── SECURITY.md                    # Security policy
├── CONTRIBUTING.md                # Contribution guidelines
├── DEPLOYMENT.md                  # Deployment guide
├── LICENSE                        # MIT License
└── GITHUB_SETUP.md               # This file
```

## Verification Checklist

Before pushing to GitHub:

### Security
- [ ] `.env` file is gitignored
- [ ] No API keys in code
- [ ] `.env.example` has placeholder values only
- [ ] Pre-commit hook is executable
- [ ] Security workflow is configured

### Documentation
- [ ] README.md is complete
- [ ] SECURITY.md has contact info
- [ ] LICENSE is included
- [ ] CONTRIBUTING.md is clear

### Code Quality
- [ ] All files have proper formatting
- [ ] No TODO comments with sensitive info
- [ ] Dependencies are up to date
- [ ] Code follows PEP 8

### Testing
- [ ] API runs without errors
- [ ] Dashboard connects to API
- [ ] Detection works correctly
- [ ] Audit logging functions

## Post-Push Steps

1. Verify GitHub Actions run successfully
2. Check security scanning results
3. Add repository description and website
4. Create project board for issues
5. Add collaborators if needed

## Maintenance

### Regular Updates

```bash
# Update dependencies
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt

# Commit and push
git add requirements.txt
git commit -m "Update dependencies"
git push
```

### Security Audits

```bash
# Run locally
pip install safety bandit
safety check -r requirements.txt
bandit -r . -f json

# Review GitHub security alerts regularly
```

## Troubleshooting

### Pre-commit hook not running
```bash
chmod +x .git/hooks/pre-commit
```

### GitHub Actions failing
- Check secrets are configured
- Verify workflow syntax
- Review action logs

### Can't push .env accidentally
- It's gitignored, but if you force-added it:
```bash
git rm --cached .env
git commit -m "Remove .env from tracking"
```

## Support

For issues:
1. Check existing GitHub issues
2. Review documentation
3. Open new issue with details
