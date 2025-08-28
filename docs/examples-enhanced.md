# Enhanced Examples & Walkthroughs

This page provides comprehensive, real-world examples of using DevOpsForge with step-by-step walkthroughs and actual command outputs.

## 🐍 Complete Python Project Walkthrough

### Step 1: Project Setup
```bash
mkdir my-flask-app
cd my-flask-app
mkdir tests
touch main.py requirements.txt README.md
```

### Step 2: Sample Code
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

### Step 3: Analysis
```bash
devopsforge analyze .
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

### Step 4: Generate Configurations
```bash
devopsforge generate . -o ./devops-config
```

**Generated Files:**
```
devops-config/
├── Dockerfile
├── .github/workflows/ci.yml
└── README-DEVOPS.md
```

### Step 5: Test Generated Configuration
```bash
cd devops-config
docker build -t my-flask-app .
docker run -p 8000:8000 my-flask-app
curl http://localhost:8000/health
```

## 🟢 Node.js Project Walkthrough

### Step 1: Project Setup
```bash
mkdir my-express-app
cd my-express-app
npm init -y
npm install express jest
mkdir src tests
```

### Step 2: Sample Code
**`src/index.js`:**
```javascript
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.json({ message: 'Hello from DevOpsForge!' });
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy' });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
```

### Step 3: Analysis & Generation
```bash
devopsforge analyze .
devopsforge generate . -o ./devops-config
```

## 💡 Advanced Usage Examples

### Custom Output Formats
```bash
# JSON output for automation
devopsforge analyze ./my-project -f json -o ./analysis.json

# Summary output for quick overview
devopsforge analyze ./my-project -f summary
```

### Selective Generation
```bash
# Generate only Dockerfile
devopsforge generate ./my-project -o ./output --dockerfile

# Generate only CI/CD pipeline
devopsforge generate ./my-project -o ./output --ci-cd
```

## 🔧 Real-World Workflow

### Complete DevOps Setup
```bash
# 1. Analyze project
devopsforge analyze ./my-project

# 2. Generate configurations
devopsforge generate ./my-project -o ./devops-config

# 3. Get suggestions
devopsforge suggest ./my-project

# 4. Review and customize
ls -la ./devops-config/

# 5. Commit and push
git add ./devops-config/
git commit -m "Add DevOps configurations"
git push origin main
```

## 📊 Before & After Examples

### Before DevOpsForge
```
my-project/
├── main.py
├── requirements.txt
└── tests/
```

### After DevOpsForge
```
my-project/
├── main.py
├── requirements.txt
├── tests/
├── Dockerfile                    # ← Generated
├── .github/workflows/ci.yml      # ← Generated
└── README-DEVOPS.md             # ← Generated
```

## 🎯 Customization Examples

### Custom Dockerfile Modifications
```dockerfile
# Add custom modifications to generated Dockerfile
RUN apt-get update && apt-get install -y curl

# Add health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8000/health || exit 1
```

### Custom CI/CD Pipeline Modifications
```yaml
# Add custom steps to generated workflow
- name: Custom Security Scan
  run: |
    echo "Running custom security checks..."
    # Your security scanning logic
```

## 📚 Next Steps

- **View the source on GitHub**: [DevOpsForge Repository](https://github.com/Nick1200000/DevOpsForge)
- **Open an issue**: [GitHub Issues](https://github.com/Nick1200000/DevOpsForge/issues)
- **Contribute**: [Contributing Guide](contributing.md)
