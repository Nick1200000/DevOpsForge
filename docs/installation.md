# Installation Guide

This guide will help you install DevOpsForge on your system with detailed requirements and troubleshooting solutions.

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+, CentOS 7+)
- **Python**: 3.8 or higher (3.11+ recommended)
- **Memory**: Minimum 2GB RAM (4GB+ recommended)
- **Disk Space**: At least 100MB free space

### Required Software
- **Python**: Latest stable version from [python.org](https://python.org)
- **pip**: Python package installer (usually comes with Python)
- **Git**: Version control system (optional but recommended)
- **Virtual Environment**: For development installations

### Python Version Check
```bash
# Check Python version
python --version
# or
python3 --version

# Should show Python 3.8.x or higher
# Example: Python 3.11.5
```

## 🚀 Quick Installation

### Using pip (Recommended)

#### Standard Installation
```bash
pip install devopsforge
```

#### User Installation (if you don't have admin rights)
```bash
pip install --user devopsforge
```

#### Specific Version Installation
```bash
pip install devopsforge==0.1.0
```

### From Source

#### Clone and Install
```bash
# Clone the repository
git clone https://github.com/Nick1200000/DevOpsForge.git
cd DevOpsForge

# Install in development mode
pip install -e .
```

#### Download and Install
```bash
# Download source code
wget https://github.com/Nick1200000/DevOpsForge/archive/refs/heads/main.zip
unzip main.zip
cd DevOpsForge-main

# Install
pip install -e .
```

## 🔧 Development Installation

### Complete Development Setup

#### 1. Clone Repository
```bash
git clone https://github.com/Nick1200000/DevOpsForge.git
cd DevOpsForge
```

#### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install development dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

#### 4. Setup Development Tools
```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Install additional development tools
pip install black isort flake8 mypy pytest
```

## ✅ Verification

### Basic Verification
```bash
# Check if the command is available
devopsforge --help

# Check version
devopsforge --version
```

### Expected Output
```
Usage: devopsforge [OPTIONS] COMMAND [ARGS]...

🧞‍♂️ DevOpsForge - AI-powered DevOps companion

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  analyze   Analyze a repository and detect project characteristics
  generate  Generate DevOps configurations for a repository
  suggest   Get optimization suggestions for a repository
```

### Advanced Verification
```bash
# Test basic functionality
devopsforge analyze . --help
devopsforge generate . --help
devopsforge suggest . --help

# Check Python path
which devopsforge
# or on Windows:
where devopsforge
```

## 🐛 Troubleshooting

### Common Issues

#### 1. Command Not Found
**Error:** `devopsforge: command not found`

**Solutions:**
```bash
# Check if installed
pip show devopsforge

# Check PATH
echo $PATH  # Linux/macOS
echo %PATH% # Windows

# Find installation location
pip show -f devopsforge | grep "Location"

# Add to PATH manually if needed
export PATH="$HOME/.local/bin:$PATH"  # Linux/macOS
set PATH=%PATH%;%USERPROFILE%\AppData\Local\Programs\Python\Scripts  # Windows
```

#### 2. Permission Errors
**Error:** `Permission denied` during installation

**Solutions:**
```bash
# Use --user flag
pip install --user devopsforge

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install devopsforge

# Fix permissions (Linux/macOS)
sudo chown -R $USER:$USER ~/.local
chmod +x ~/.local/bin/*
```

#### 3. Python Version Issues
**Error:** `Python 3.8+ required`

**Solutions:**
```bash
# Check Python version
python --version

# Use py launcher on Windows
py -3.11 -m pip install devopsforge

# Use python3 on Linux/macOS
python3 --version
python3 -m pip install devopsforge

# Install specific Python version
# On Ubuntu/Debian:
sudo apt update
sudo apt install python3.11 python3.11-pip

# On macOS with Homebrew:
brew install python@3.11
```

#### 4. Dependency Conflicts
**Error:** `ERROR: Could not find a version that satisfies the requirement`

**Solutions:**
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Clear pip cache
pip cache purge

# Install with --force-reinstall
pip install --force-reinstall devopsforge

# Check for conflicting packages
pip list | grep -i conflicting-package-name
```

#### 5. Virtual Environment Issues
**Error:** `ModuleNotFoundError: No module named 'devopsforge'`

**Solutions:**
```bash
# Ensure virtual environment is activated
# You should see (venv) in your prompt

# Reinstall in virtual environment
pip uninstall devopsforge
pip install -e .

# Check Python path
which python
# Should point to your virtual environment
```

### Platform-Specific Issues

#### Windows Issues
```bash
# Use py launcher
py -3.11 -m pip install devopsforge

# Check Windows PATH
echo %PATH%

# Use Windows Subsystem for Linux (WSL) if needed
wsl
pip install devopsforge
```

#### macOS Issues
```bash
# Use Homebrew Python
brew install python@3.11
brew link python@3.11

# Check for multiple Python versions
which python
which python3

# Use specific Python version
python3.11 -m pip install devopsforge
```

#### Linux Issues
```bash
# Install system dependencies
sudo apt update  # Ubuntu/Debian
sudo apt install python3-pip python3-venv

# Use system Python
python3 -m pip install --user devopsforge

# Add to PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Getting Help

#### Before Asking for Help
1. **Check this guide** for your specific error
2. **Verify Python version** meets requirements
3. **Check if virtual environment** is activated
4. **Try basic troubleshooting** steps above

#### When Reporting Issues
Include:
- **Error message** (exact text)
- **Operating system** and version
- **Python version** (`python --version`)
- **pip version** (`pip --version`)
- **Installation method** used
- **Steps to reproduce**

#### Useful Commands for Bug Reports
```bash
# System information
python --version
pip --version
uname -a  # Linux/macOS
systeminfo # Windows

# Package information
pip show devopsforge
pip list | grep devopsforge

# Environment
env | grep -i python
pip debug
```

## 🔄 Updating

### Check Current Version
```bash
devopsforge --version
pip show devopsforge
```

### Update to Latest Version
```bash
# Update using pip
pip install --upgrade devopsforge

# Update from source
cd DevOpsForge
git pull origin main
pip install -e .
```

### Update Dependencies
```bash
# Update all packages
pip install --upgrade -r requirements.txt

# Update specific packages
pip install --upgrade click rich jinja2
```

## 🗑️ Uninstallation

### Remove Package
```bash
# Uninstall DevOpsForge
pip uninstall devopsforge

# Remove all related packages
pip uninstall -y devopsforge click rich jinja2 pyyaml
```

### Clean Up
```bash
# Remove configuration files
rm -rf ~/.config/devopsforge  # Linux/macOS
rmdir /s %APPDATA%\devopsforge  # Windows

# Remove from PATH (if manually added)
# Edit your shell profile file (.bashrc, .zshrc, etc.)
```

## 📚 Next Steps

Now that you have DevOpsForge installed, check out:

- [User Guide](user-guide.md) - Learn how to use DevOpsForge
- [Examples](examples.md) - See DevOpsForge in action
- [API Reference](api-reference.md) - Detailed API documentation
- [Troubleshooting](troubleshooting.md) - Common issues and solutions

## 🔗 Related Resources

- **GitHub Repository**: [https://github.com/Nick1200000/DevOpsForge](https://github.com/Nick1200000/DevOpsForge)
- **Issues**: [https://github.com/Nick1200000/DevOpsForge/issues](https://github.com/Nick1200000/DevOpsForge/issues)
- **Discussions**: [https://github.com/Nick1200000/DevOpsForge/discussions](https://github.com/Nick1200000/DevOpsForge/discussions)
- **Documentation**: [https://nick1200000.github.io/DevOpsForge/](https://nick1200000.github.io/DevOpsForge/)
