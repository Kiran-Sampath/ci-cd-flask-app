# Azure Web App Deployment Guide

This project demonstrates a complete CI/CD pipeline with Azure Web App deployment.

## Features

- ✅ Flask application with health checks
- ✅ Automated testing and linting
- ✅ GitHub Actions CI/CD pipeline
- ✅ Azure Web App deployment
- ✅ Docker containerization support

## Deployment Flow

1. **Push to azure-deployment branch**
2. **CI/CD Pipeline runs:**
   - Install dependencies
   - Run tests
   - Run linting
3. **If successful → Azure deployment starts**
4. **App deployed to Azure Web App**

## Azure Configuration

- **Runtime**: Python 3.11
- **Platform**: Linux
- **Deployment**: GitHub Actions
- **Authentication**: Publish Profile

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Run tests
python -m unittest test_app.py
```

## Environment Variables

- `ENVIRONMENT`: development/production
- `FLASK_APP`: app.py
- `PORT`: 5000 (local), 8000 (Azure)

## API Endpoints

- `/` - Main endpoint
- `/health` - Health check
- `/info` - App information
- `/html` - HTML page

## Troubleshooting

- Check GitHub Actions logs
- Verify Azure Web App configuration
- Ensure publish profile is set correctly
