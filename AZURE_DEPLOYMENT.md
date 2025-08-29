# Deploy to Azure Web App

This guide will help you deploy your Flask application to Azure Web App.

## Prerequisites

1. Azure account (free tier available)
2. Azure CLI installed
3. Git repository with your code

## Method 1: Azure Portal (Easiest)

### Step 1: Create Azure Web App
1. Go to [Azure Portal](https://portal.azure.com)
2. Click "Create a resource"
3. Search for "Web App"
4. Click "Create"
5. Fill in the details:
   - **Resource Group**: Create new or use existing
   - **Name**: Your app name (e.g., `your-app-name`)
   - **Publish**: Code
   - **Runtime stack**: Python 3.11
   - **Operating System**: Linux (recommended)
   - **Region**: Choose closest to you
   - **App Service Plan**: Free (F1) for testing
6. Click "Review + create" then "Create"

### Step 2: Deploy from GitHub
1. In your Azure Web App, go to "Deployment Center"
2. Choose "GitHub" as source
3. Connect your GitHub account
4. Select your repository and branch
5. Azure will automatically deploy your app

## Method 2: Azure CLI

### Step 1: Login to Azure
```bash
az login
```

### Step 2: Create Resource Group
```bash
az group create --name myResourceGroup --location eastus
```

### Step 3: Create App Service Plan
```bash
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku F1 --is-linux
```

### Step 4: Create Web App
```bash
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name your-app-name --runtime "PYTHON|3.11"
```

### Step 5: Deploy from Local Git
```bash
az webapp deployment source config-local-git --name your-app-name --resource-group myResourceGroup
```

### Step 6: Push to Azure
```bash
git remote add azure <git-url-from-previous-step>
git push azure main
```

## Method 3: GitHub Actions (Recommended)

### Step 1: Get Publish Profile
1. In Azure Portal, go to your Web App
2. Click "Get publish profile"
3. Download the file

### Step 2: Add Secret to GitHub
1. Go to your GitHub repository
2. Settings → Secrets and variables → Actions
3. Add new secret: `AZURE_WEBAPP_PUBLISH_PROFILE`
4. Paste the content of the downloaded publish profile file

### Step 3: Update Workflow
1. Edit `.github/workflows/azure-deploy.yml`
2. Change `your-app-name` to your actual Azure Web App name
3. Commit and push

## Configuration

### Environment Variables
Set these in Azure Portal → Configuration → Application settings:
- `ENVIRONMENT`: production
- `FLASK_APP`: app.py

### Custom Domain (Optional)
1. Go to "Custom domains" in your Web App
2. Add your domain
3. Configure DNS records

## Troubleshooting

### Common Issues
1. **App not starting**: Check startup command in Configuration
2. **Import errors**: Ensure all dependencies are in requirements.txt
3. **Port issues**: Azure uses port 8000 by default

### Logs
View logs in Azure Portal → Log stream or use:
```bash
az webapp log tail --name your-app-name --resource-group myResourceGroup
```

## Cost Optimization

- Use **Free tier (F1)** for development/testing
- **Basic tier (B1)** for production (~$13/month)
- **Consumption plan** for serverless (pay per use)

## Next Steps

1. Set up custom domain
2. Configure SSL certificate
3. Set up monitoring and alerts
4. Configure backup strategy
