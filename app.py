from flask import Flask, jsonify, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'Hello World!',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/info')
def app_info():
    return jsonify({
        'app_name': 'CI/CD Demo App',
        'description': 'A simple Flask app demonstrating CI/CD pipeline',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'version': '1.0.0'
    })

@app.route('/html')
def html_page():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Demo App</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f0f0f0; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; text-align: center; }
            .feature { margin: 20px 0; padding: 15px; background: #f8f9fa; border-left: 4px solid #007bff; }
            .status { padding: 10px; border-radius: 5px; margin: 10px 0; }
            .success { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 CI/CD Demo Application</h1>
            <div class="feature">
                <h3>✅ Successfully Deployed!</h3>
                <p>This application demonstrates a complete CI/CD pipeline with:</p>
                <ul>
                    <li>Docker containerization</li>
                    <li>GitHub Actions automation</li>
                    <li>Automated testing</li>
                    <li>Cloud deployment</li>
                </ul>
            </div>
            <div class="status success">
                <strong>Status:</strong> Application is running successfully!
            </div>
            <div class="feature">
                <h3>📊 API Endpoints:</h3>
                <ul>
                    <li><a href="/">/</a> - Main endpoint</li>
                    <li><a href="/health">/health</a> - Health check</li>
                    <li><a href="/info">/info</a> - App information</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
