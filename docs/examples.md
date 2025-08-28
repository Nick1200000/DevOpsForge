# Examples

This page provides real-world examples of using DevOpsForge with different types of projects.

## 🐍 Python Project Example

### Project Structure
```
my-python-app/
├── main.py
├── requirements.txt
├── tests/
│   └── test_main.py
└── README.md
```

### Analysis
```bash
devopsforge analyze ./my-python-app
```

**Output:**
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

### Generation
```bash
devopsforge generate ./my-python-app -o ./devops-config
```

**Generated Files:**
- `Dockerfile` - Multi-stage Python Dockerfile
- `.github/workflows/ci.yml` - GitHub Actions pipeline
- `README-DEVOPS.md` - Setup instructions

## 🟢 Node.js Project Example

### Project Structure
```
my-nodejs-app/
├── package.json
├── index.js
├── tests/
│   └── test.js
└── README.md
```

### Analysis
```bash
devopsforge analyze ./my-nodejs-app
```

**Output:**
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

### Generation
```bash
devopsforge generate ./my-nodejs-app -o ./devops-config
```

**Generated Files:**
- `Dockerfile` - Multi-stage Node.js Dockerfile
- `.github/workflows/ci.yml` - GitHub Actions pipeline
- `README-DEVOPS.md` - Setup instructions

## ☕ Java Project Example

### Project Structure
```
my-java-app/
├── pom.xml
├── src/
│   ├── main/java/
│   │   └── com/example/App.java
│   └── test/java/
│       └── com/example/AppTest.java
└── README.md
```

### Analysis
```bash
devopsforge analyze ./my-java-app
```

**Output:**
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

### Generation
```bash
devopsforge generate ./my-java-app -o ./devops-config
```

**Generated Files:**
- `Dockerfile` - Multi-stage Java Dockerfile
- `.github/workflows/ci.yml` - GitHub Actions pipeline
- `README-DEVOPS.md` - Setup instructions

## 🚀 Advanced Usage Examples

### Custom Output Formats

#### JSON Output
```bash
devopsforge analyze ./my-project -f json -o ./analysis.json
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

#### Summary Output
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

## 📚 Next Steps

- Check out the [User Guide](user-guide.md) for detailed usage instructions
- See the [API Reference](api-reference.md) for programmatic usage
- Visit the [Troubleshooting](troubleshooting.md) guide if you encounter issues
