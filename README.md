# DevOpsForge

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                        🔧 DevOpsForge 🔧                     ║
║                                                              ║
║                    Professional DevOps Automation             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

[![PyPI version](https://badge.fury.io/py/devopsforge.svg)](https://badge.fury.io/py/devopsforge)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI/CD](https://github.com/Nick1200000/DevOpsForge/workflows/CI%2FCD/badge.svg)](https://github.com/Nick1200000/DevOpsForge/actions)
[![Documentation](https://github.com/Nick1200000/DevOpsForge/workflows/Deploy%20Documentation/badge.svg)](https://nick1200000.github.io/DevOpsForge/)

Professional DevOps automation tool that automatically generates CI/CD pipelines, Dockerfiles, and Kubernetes configurations for your projects.

## 🚀 Features

- **🔍 Automatic Project Analysis**: Detects project type, language, dependencies, and frameworks
- **🐳 Dockerfile Generation**: Creates optimized, multi-stage Dockerfiles for various languages
- **🔄 CI/CD Pipeline Generation**: Generates GitHub Actions and GitLab CI configurations
- **🔒 DevSecOps Integration**: Includes security scanning and best practices
- **💡 Optimization Suggestions**: Provides tailored recommendations for your project
- **🌐 Multi-Language Support**: Works with Python, Node.js, Java, Go, and Rust projects

## 📦 Installation

```bash
pip install devopsforge
```

## 🚀 Quick Start

### Analyze Your Project
```bash
# Analyze current directory
devopsforge analyze .

# Analyze specific repository
devopsforge analyze /path/to/repository
```

### Generate DevOps Configurations
```bash
# Generate all configurations
devopsforge generate . -o ./devops-config

# Generate only Dockerfile
devopsforge generate . -o ./output --dockerfile

# Generate only CI/CD pipeline
devopsforge generate . -o ./output --ci-cd
```

### Get Optimization Suggestions
```bash
devopsforge suggest .
```

## 🌟 Supported Technologies

### Languages & Frameworks
- **Python**: Django, Flask, FastAPI, pytest
- **Node.js**: Express, React, Jest, npm/yarn
- **Java**: Spring Boot, Maven, Gradle, JUnit
- **Go**: Go modules, testing
- **Rust**: Cargo, testing

### DevOps Tools
- **CI/CD**: GitHub Actions, GitLab CI
- **Containers**: Docker, Kubernetes
- **Security**: Trivy, Safety, Bandit
- **Testing**: pytest, Jest, JUnit, Go testing

## 📚 Documentation

📖 **Complete documentation available at**: [https://nick1200000.github.io/DevOpsForge/](https://nick1200000.github.io/DevOpsForge/)

- [Installation Guide](https://nick1200000.github.io/DevOpsForge/installation/)
- [User Guide](https://nick1200000.github.io/DevOpsForge/user-guide/)
- [Examples](https://nick1200000.github.io/DevOpsForge/examples/)
- [Enhanced Examples](https://nick1200000.github.io/DevOpsForge/examples-enhanced/)
- [API Reference](https://nick1200000.github.io/DevOpsForge/api-reference/)

## 🔧 Example Output

### Project Analysis
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
└─────────────┴─────────────────────┘
```

### Generated Files
```
devops-config/
├── Dockerfile                    # ← Generated
├── .github/workflows/ci.yml      # ← Generated
└── README-DEVOPS.md             # ← Generated
```

## 🛠️ Development

### Setup Development Environment
```bash
# Clone repository
git clone https://github.com/Nick1200000/DevOpsForge.git
cd DevOpsForge

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

### Run Tests
```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=devopsforge --cov-report=html
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](https://nick1200000.github.io/DevOpsForge/contributing/) for details.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Click](https://click.palletsprojects.com/) for CLI
- Styled with [Rich](https://rich.readthedocs.io/) for beautiful terminal output
- Templates powered by [Jinja2](https://jinja.palletsprojects.com/)
- Documentation built with [MkDocs](https://www.mkdocs.org/)

## 📞 Support

- **Documentation**: [https://nick1200000.github.io/DevOpsForge/](https://nick1200000.github.io/DevOpsForge/)
- **Issues**: [GitHub Issues](https://github.com/Nick1200000/DevOpsForge/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Nick1200000/DevOpsForge/discussions)
- **Email**: kumarn7570@gmail.com

---

**Made with ❤️ by the DevOpsForge Team**

[![GitHub stars](https://img.shields.io/github/stars/Nick1200000/DevOpsForge?style=social)](https://github.com/Nick1200000/DevOpsForge)
[![GitHub forks](https://img.shields.io/github/forks/Nick1200000/DevOpsForge?style=social)](https://github.com/Nick1200000/DevOpsForge)
[![GitHub watchers](https://img.shields.io/github/watchers/Nick1200000/DevOpsForge?style=social)](https://github.com/Nick1200000/DevOpsForge)
