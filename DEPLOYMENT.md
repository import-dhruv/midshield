# Deployment Guide

## Pre-Deployment Checklist

### Security
- [ ] All API keys are in environment variables
- [ ] `.env` file is gitignored
- [ ] No secrets in code or config files
- [ ] HTTPS enabled for production
- [ ] Rate limiting configured
- [ ] Authentication/authorization implemented (if needed)

### Configuration
- [ ] `GROQ_API_KEY` set in deployment environment
- [ ] `API_URL` points to production endpoint
- [ ] `LOG_PATH` configured for production storage
- [ ] Log rotation enabled

### Testing
- [ ] API endpoints tested
- [ ] Dashboard loads correctly
- [ ] Detection patterns validated
- [ ] Audit logging verified

## Deployment Options

### Option 1: Docker

```bash
# Build image
docker build -t midshield .

# Run API
docker run -d -p 8000:8000 \
  -e GROQ_API_KEY=your_key \
  -e LOG_PATH=/app/logs/audit.jsonl \
  --name midshield-api \
  midshield

# Run Dashboard
docker run -d -p 8501:8501 \
  -e API_URL=http://midshield-api:8000 \
  --link midshield-api \
  --name midshield-ui \
  midshield streamlit run app.py
```

### Option 2: Cloud Platforms

#### Heroku

```bash
heroku create midshield-api
heroku config:set GROQ_API_KEY=your_key
git push heroku main
```

#### Railway

1. Connect GitHub repository
2. Add environment variables in dashboard
3. Deploy automatically on push

#### Render

1. Create new Web Service
2. Connect repository
3. Set environment variables
4. Deploy

### Option 3: VPS (Ubuntu)

```bash
# Install dependencies
sudo apt update
sudo apt install python3-pip python3-venv nginx

# Clone and setup
git clone <your-repo>
cd midshield
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Create systemd service
sudo nano /etc/systemd/system/midshield.service
```

Service file:
```ini
[Unit]
Description=MidShield API
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/midshield
Environment="GROQ_API_KEY=your_key"
ExecStart=/path/to/midshield/.venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable midshield
sudo systemctl start midshield
```

## Environment Variables

Required:
- `GROQ_API_KEY` - Your Groq API key

Optional:
- `API_URL` - API endpoint (default: http://localhost:8000)
- `LOG_PATH` - Audit log path (default: audit.jsonl)

## Monitoring

### Health Check

```bash
curl http://your-domain.com/health
```

### Logs

```bash
# View audit logs
tail -f audit.jsonl

# View application logs
journalctl -u midshield -f
```

## Scaling

- Use load balancer for multiple API instances
- Centralize audit logs (e.g., S3, CloudWatch)
- Implement Redis for caching
- Add rate limiting middleware

## Backup

```bash
# Backup audit logs
cp audit.jsonl audit-$(date +%Y%m%d).jsonl

# Automated backup (cron)
0 0 * * * cp /path/to/audit.jsonl /backup/audit-$(date +\%Y\%m\%d).jsonl
```

## Troubleshooting

### API not responding
- Check if service is running: `systemctl status midshield`
- Verify environment variables are set
- Check logs for errors

### Dashboard can't connect
- Verify `API_URL` is correct
- Check network connectivity
- Ensure API is accessible from dashboard

### High latency
- Check Groq API status
- Implement caching for repeated inputs
- Scale horizontally with load balancer
