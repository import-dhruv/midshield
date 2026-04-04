# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in MidShield, please report it by:

1. **DO NOT** open a public GitHub issue
2. Email the maintainers directly (add your contact email)
3. Include detailed steps to reproduce the vulnerability
4. Allow up to 48 hours for initial response

## Security Best Practices

### API Key Protection

- Never commit `.env` files to version control
- Use environment variables for all sensitive data
- Rotate API keys regularly
- Use different keys for development and production

### Deployment Security

- Enable HTTPS in production
- Implement rate limiting on API endpoints
- Use authentication/authorization for production deployments
- Monitor audit logs for suspicious activity
- Keep dependencies updated

### Audit Logging

- Audit logs (`audit.jsonl`) contain input previews
- Ensure logs are stored securely
- Implement log rotation for production
- Review logs regularly for attack patterns

## Known Security Considerations

1. **Input Length**: Inputs are limited to 4000 characters to prevent abuse
2. **API Rate Limiting**: Not implemented by default - add middleware for production
3. **Authentication**: Not included - implement based on your deployment needs
4. **Log Storage**: Audit logs grow indefinitely - implement rotation in production

## Dependencies

We use `pip` and `requirements.txt` for dependency management. Run security audits regularly:

```bash
pip install safety
safety check -r requirements.txt
```

## Updates

Security updates will be released as patch versions. Subscribe to repository releases for notifications.
