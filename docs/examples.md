# Examples

This page provides real-world examples of using DevOpsForge with different types of projects, including step-by-step walkthroughs and actual command outputs.

## 🐍 Python Project Walkthrough

### Project Setup
Let's start with a real Python project and walk through the complete DevOps setup process.

#### 1. Create Sample Python Project
```bash
# Create a new directory for our example
mkdir my-flask-app
cd my-flask-app

# Create basic project structure
mkdir tests
touch main.py requirements.txt README.md
```

#### 2. Add Sample Code
**`main.py`:**
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from DevOpsForge!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

**`requirements.txt`:**
```
flask==2.3.0
pytest==7.4.0
```

**`README.md`:**
```markdown
# My Flask App

A simple Flask application for DevOpsForge demonstration.
```

#### 3. Analyze with DevOpsForge
```bash
# Install DevOpsForge (if not already installed)
pip install devopsforge

# Analyze the project
devopsforge analyze .
```

**Expected Output:**
```
┌─────────────────────────────────────┐
│ 🔍 Repository Analysis Results      │
└─────────────────────────────────────┘

┌─────────────┬─────────────────────┐
│ Property    │ Value               │
├─────────────┼─────────────────────┤
│ Project Type│ python              │
│ Language    │ python              │
│ Dependencies│ flask, pytest       │
│ Build Tools │ pip                 │
│ Test Framew.│ pytest             │
│ Framework   │ flask               │
│ Database    │ None                │
│ Has Docker  │ False               │
│ Has K8s     │ False               │
│ Has CI/CD   │ False               │
└─────────────┴─────────────────────┘
```

#### 4. Generate DevOps Configurations
```bash
# Generate all configurations
devopsforge generate . -o ./devops-config
```

**Generated Files Structure:**
```
devops-config/
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
└── README-DEVOPS.md
```

**Generated Dockerfile:**
```dockerfile
# Multi-stage Python Dockerfile
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000

CMD ["python", "main.py"]
```

**Generated GitHub Actions Workflow:**
```yaml
name: CI/CD Pipeline

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest tests/
```

#### 5. Test the Generated Configuration
```bash
# Build Docker image
cd devops-config
docker build -t my-flask-app .

# Run the container
docker run -p 8000:8000 my-flask-app

# Test the application
curl http://localhost:8000/health
```

## 🟢 Node.js Project Walkthrough

### Project Setup
Let's create a Node.js project and set it up with DevOpsForge.

#### 1. Create Sample Node.js Project
```bash
mkdir my-express-app
cd my-express-app

# Initialize npm project
npm init -y

# Install dependencies
npm install express jest
npm install --save-dev nodemon

# Create project structure
mkdir src tests
touch src/index.js package.json
```

#### 2. Add Sample Code
**`src/index.js`:**
```javascript
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.json({ message: 'Hello from DevOpsForge Node.js!' });
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', timestamp: new Date().toISOString() });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
```

**`package.json`:**
```json
{
  "name": "my-express-app",
  "version": "1.0.0",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.18.0"
  },
  "devDependencies": {
    "jest": "^29.0.0",
    "nodemon": "^3.0.0"
  }
}
```

#### 3. Analyze with DevOpsForge
```bash
devopsforge analyze .
```

**Expected Output:**
```
┌─────────────────────────────────────┐
│ 🔍 Repository Analysis Results      │
└─────────────────────────────────────┘

┌─────────────┬─────────────────────┐
│ Property    │ Value               │
├─────────────┼─────────────────────┤
│ Project Type│ nodejs              │
│ Language    │ javascript          │
│ Dependencies│ express, jest       │
│ Build Tools │ npm                 │
│ Test Framew.│ jest                │
│ Framework   │ express             │
│ Database    │ None                │
│ Has Docker  │ False               │
│ Has K8s     │ False               │
│ Has CI/CD   │ False               │
└─────────────┴─────────────────────┘
```

#### 4. Generate DevOps Configurations
```bash
devopsforge generate . -o ./devops-config
```

**Generated Dockerfile:**
```dockerfile
# Multi-stage Node.js Dockerfile
FROM node:18-alpine as builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .

EXPOSE 3000
CMD ["npm", "start"]
```

## ☕ Java Project Walkthrough

### Project Setup
Let's create a Spring Boot project and configure it with DevOpsForge.

#### 1. Create Sample Java Project
```bash
mkdir my-spring-app
cd my-spring-app

# Create Maven project structure
mkdir -p src/main/java/com/example/app
mkdir -p src/test/java/com/example/app
touch pom.xml
```

#### 2. Add Sample Code
**`pom.xml`:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.example</groupId>
    <artifactId>my-spring-app</artifactId>
    <version>1.0.0</version>
    
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.1.0</version>
    </parent>
    
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

**`src/main/java/com/example/app/App.java`:**
```java
package com.example.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class App {
    
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
    
    @GetMapping("/")
    public String hello() {
        return "Hello from DevOpsForge Java!";
    }
    
    @GetMapping("/health")
    public String health() {
        return "{\"status\": \"healthy\"}";
    }
}
```

#### 3. Analyze with DevOpsForge
```bash
devopsforge analyze .
```

**Expected Output:**
```
┌─────────────────────────────────────┐
│ 🔍 Repository Analysis Results      │
└─────────────────────────────────────┘

┌─────────────┬─────────────────────┐
│ Property    │ Value               │
├─────────────┼─────────────────────┤
│ Project Type│ java                │
│ Language    │ java                │
│ Dependencies│ spring-boot-starter │
│ Build Tools │ maven               │
│ Test Framew.│ junit               │
│ Framework   │ spring-boot         │
│ Database    │ None                │
│ Has Docker  │ False               │
│ Has K8s     │ False               │
│ Has CI/CD   │ False               │
└─────────────┴─────────────────────┘
```

#### 4. Generate DevOps Configurations
```bash
devopsforge generate . -o ./devops-config
```

**Generated Dockerfile:**
```dockerfile
# Multi-stage Java Dockerfile
FROM maven:3.9-eclipse-temurin-17 as builder

WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar

EXPOSE 8080
CMD ["java", "-jar", "app.jar"]
```

## 🚀 Advanced Usage Examples

### Custom Output Formats

#### JSON Output for Automation
```bash
# Get structured output for CI/CD integration
devopsforge analyze ./my-project -f json -o ./analysis.json

# Use the output in scripts
PROJECT_TYPE=$(jq -r '.analysis.project_type' ./analysis.json)
echo "Detected project type: $PROJECT_TYPE"
```

**Output:**
```json
{
  "repository_path": "./my-project",
  "analysis": {
    "project_type": "python",
    "language": "python",
    "dependencies": ["flask", "pytest"],
    "build_tools": ["pip"],
    "test_frameworks": ["pytest"],
    "framework": "flask",
    "database": null,
    "has_docker": false,
    "has_kubernetes": false,
    "has_ci_cd": false
  }
}
```

#### Summary Output for Quick Overview
```bash
devopsforge analyze ./my-project -f summary
```

**Output:**
```
🔍 Repository Analysis Summary

📁 Project: my-project
🐍 Type: Python application using Flask
📦 Dependencies: flask, pytest
🔧 Build Tool: pip
🧪 Testing: pytest
🌐 Framework: Flask web framework
🐳 Docker: Not configured
☸️ Kubernetes: Not configured
🔄 CI/CD: Not configured

💡 Recommendations:
• Add Docker support for containerization
• Set up CI/CD pipeline for automated testing
• Consider adding Kubernetes manifests
```

### Selective Generation

#### Generate Only Dockerfile
```bash
devopsforge generate ./my-project -o ./output --dockerfile
```

#### Generate Only CI/CD Pipeline
```bash
devopsforge generate ./my-project -o ./output --ci-cd
```

#### Generate Everything
```bash
devopsforge generate ./my-project -o ./output
```

## 💡 Optimization Suggestions

### Get Tailored Recommendations
```bash
devopsforge suggest ./my-project
```

**Example Output:**
```
💡 Optimization Suggestions for my-project

🐳 Docker Optimizations:
• Use multi-stage builds to reduce image size
• Consider using Alpine-based images for smaller footprint
• Add .dockerignore file to exclude unnecessary files
• Use non-root user for security

🔄 CI/CD Enhancements:
• Set up automated testing in CI/CD
• Add code quality checks (linting, formatting)
• Implement security scanning in pipeline
• Use dependency caching for faster builds

🔒 Security Improvements:
• Run security scans in CI/CD pipeline
• Use Trivy for container vulnerability scanning
• Implement automated dependency updates
• Add security policy enforcement

📊 Performance Tips:
• Use layer caching in Docker builds
• Implement parallel testing in CI/CD
• Add build artifact caching
• Use optimized base images
```

## 🔧 Real-World Workflow

### Complete DevOps Setup
```bash
# 1. Analyze your project
devopsforge analyze ./my-project

# 2. Generate all configurations
devopsforge generate ./my-project -o ./devops-config

# 3. Get optimization suggestions
devopsforge suggest ./my-project

# 4. Review generated files
ls -la ./devops-config/

# 5. Customize configurations as needed
# 6. Commit to version control
git add ./devops-config/
git commit -m "Add DevOps configurations"

# 7. Push and let CI/CD run
git push origin main
```

## 📊 Directory Structure Examples

### Before DevOpsForge
```
my-project/
├── main.py
├── requirements.txt
├── tests/
│   └── test_main.py
└── README.md
```

### After DevOpsForge
```
my-project/
├── main.py
├── requirements.txt
├── tests/
│   └── test_main.py
├── README.md
├── Dockerfile                    # ← Generated
├── .github/
│   └── workflows/
│       └── ci.yml               # ← Generated
├── .dockerignore                 # ← Generated
└── README-DEVOPS.md             # ← Generated
```

## 🎯 Customization Examples

### Custom Dockerfile Modifications
```dockerfile
# Generated Dockerfile
FROM python:3.11-slim

# Add your custom modifications
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Add health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8000/health || exit 1

# Rest of generated content...
```

### Custom CI/CD Pipeline Modifications
```yaml
# Generated GitHub Actions workflow
name: CI/CD Pipeline

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      # Generated steps...
      
      # Add your custom steps
      - name: Custom Security Scan
        run: |
          echo "Running custom security checks..."
          # Your security scanning logic
      
      - name: Custom Notifications
        run: |
          echo "Sending notifications..."
          # Your notification logic
```

## 📚 Next Steps

- Check out the [User Guide](user-guide.md) for detailed usage instructions
- See the [API Reference](api-reference.md) for programmatic usage
- Visit the [Troubleshooting](troubleshooting.md) guide if you encounter issues
- **View the source on GitHub**: [DevOpsForge Repository](https://github.com/Nick1200000/DevOpsForge)
- **Open an issue**: [GitHub Issues](https://github.com/Nick1200000/DevOpsForge/issues)
