# CI/CD Demo Web Application

A simple Flask web application demonstrating a complete CI/CD pipeline with Docker containerization, automated testing, and cloud deployment.

## 🚀 Features

- **Flask Web Application** with multiple endpoints
- **Docker Containerization** with optimized multi-stage build
- **Automated Testing** with pytest
- **GitHub Actions CI/CD Pipeline**
- **Cloud Deployment** to Heroku
- **Load Balancer** setup with Nginx
- **Health Checks** and monitoring

## 📋 API Endpoints

- `GET /` - Main endpoint returning JSON response
- `GET /health` - Health check endpoint
- `GET /info` - Application information
- `GET /html` - HTML page with application details

## 🛠️ Local Development

### Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ci-cd-webapp
   ```

2. **Run with Docker Compose (Recommended)**
   ```bash
   docker-compose up --build
   ```
   Access the application at: http://localhost:80

3. **Run locally with Python**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
   Access the application at: http://localhost:5000

4. **Run tests**
   ```bash
   python -m pytest test_app.py -v
   ```

## 🐳 Docker Commands

### Build the image
```bash
docker build -t ci-cd-webapp .
```

### Run the container
```bash
docker run -p 5000:5000 ci-cd-webapp
```

### Run with Docker Compose
```bash
docker-compose up --build
```

## 🔄 CI/CD Pipeline

The GitHub Actions workflow includes:

1. **Testing Phase**
   - Code checkout
   - Python environment setup
   - Dependency installation
   - Automated testing with pytest
   - Code linting with flake8

2. **Build Phase**
   - Docker image building
   - Push to GitHub Container Registry
   - Image tagging and metadata

3. **Deployment Phase**
   - Automatic deployment to Heroku
   - Health checks and monitoring

### Required Secrets

Add these secrets to your GitHub repository:

- `HEROKU_API_KEY` - Your Heroku API key
- `HEROKU_APP_NAME` - Your Heroku app name
- `HEROKU_EMAIL` - Your Heroku email

## 🌐 Deployment Options

### Heroku Deployment

1. Create a Heroku account
2. Install Heroku CLI
3. Create a new app:
   ```bash
   heroku create your-app-name
   ```
4. Set up GitHub Actions secrets
5. Push to main branch to trigger deployment

### Alternative: Render Deployment

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Use the Dockerfile for deployment
4. Set environment variables as needed

### Alternative: Azure Web App

1. Create an Azure Web App
2. Configure for Docker deployment
3. Set up GitHub Actions for Azure deployment
4. Use Azure Container Registry if needed

## 📊 Monitoring and Health Checks

The application includes:

- Health check endpoint (`/health`)
- Docker health checks
- Application metrics
- Error handling and logging

## 🧪 Testing

### Run all tests
```bash
python -m pytest test_app.py -v
```

### Test coverage
```bash
pip install pytest-cov
python -m pytest test_app.py --cov=app --cov-report=html
```

## 📁 Project Structure

```
ci-cd-webapp/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── test_app.py           # Automated tests
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── nginx.conf           # Nginx configuration
├── .dockerignore        # Docker ignore file
├── .github/
│   └── workflows/
│       └── ci-cd.yml    # GitHub Actions workflow
└── README.md            # This file
```

## 🔧 Configuration

### Environment Variables

- `ENVIRONMENT` - Set to 'production' or 'development'
- `PORT` - Port number (default: 5000)
- `FLASK_APP` - Flask application entry point

### Docker Configuration

- Multi-stage build for optimization
- Non-root user for security
- Health checks for monitoring
- Volume mounting for development

## 🚀 Performance Optimization

- Docker layer caching
- Multi-stage builds
- Optimized base images
- Health checks and monitoring
- Load balancing with Nginx

## 🔒 Security Features

- Non-root user in Docker container
- Environment variable configuration
- Input validation
- Error handling
- Secure headers

## 📈 Scaling

The application can be scaled using:

- Docker Compose with multiple instances
- Kubernetes deployment
- Cloud-native scaling features
- Load balancer configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **Port already in use**
   - Change the port in docker-compose.yml
   - Kill existing processes on port 5000

2. **Docker build fails**
   - Check Dockerfile syntax
   - Verify requirements.txt format
   - Clear Docker cache: `docker system prune`

3. **Tests failing**
   - Check Python version compatibility
   - Verify all dependencies are installed
   - Run tests individually to isolate issues

4. **Deployment issues**
   - Verify GitHub secrets are set correctly
   - Check Heroku app configuration
   - Review GitHub Actions logs

### Getting Help

- Check the GitHub Actions logs for detailed error messages
- Review the application logs: `docker-compose logs web`
- Verify environment variables are set correctly
