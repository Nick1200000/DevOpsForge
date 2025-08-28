# Troubleshooting Guide

This guide helps you resolve common issues when using DevOpsForge.

## 🚨 Common Issues

### Installation Problems

#### Issue: Command Not Found
**Error:** `devopsforge: command not found`

**Solutions:**
```bash
# Check if installed
pip show devopsforge

# Reinstall if needed
pip install --force-reinstall devopsforge

# Check PATH
echo $PATH

# Install with --user flag
pip install --user devopsforge
```

#### Issue: Permission Denied
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
```

#### Issue: Python Version Too Old
**Error:** `Python 3.8+ required`

**Solutions:**
```bash
# Check Python version
python --version

# Update Python (if possible)
# Or use pyenv to manage versions
pyenv install 3.11.0
pyenv global 3.11.0
```

### Analysis Problems

#### Issue: Repository Path Not Found
**Error:** `Repository path does not exist`

**Solutions:**
```bash
# Check if path exists
ls -la /path/to/repository

# Use absolute path
devopsforge analyze /absolute/path/to/repo

# Use relative path from current directory
devopsforge analyze ./relative/path
```

#### Issue: Empty Repository
**Error:** `Analysis failed` or no output

**Solutions:**
```bash
# Check repository contents
ls -la /path/to/repo

# Ensure repository has files
# Add basic project files:
# - requirements.txt (Python)
# - package.json (Node.js)
# - pom.xml (Java)
# - go.mod (Go)
# - Cargo.toml (Rust)
```

#### Issue: Hidden Files Not Detected
**Error:** Missing dependencies or project type

**Solutions:**
```bash
# Check for hidden files
ls -la /path/to/repo | grep "^\."

# Common hidden files:
# .python-version, .node-version, .tool-versions
# .gitignore, .dockerignore
```

### Generation Problems

#### Issue: Output Directory Not Found
**Error:** `Output directory does not exist`

**Solutions:**
```bash
# Create output directory
mkdir -p ./output

# Use absolute path
devopsforge generate ./repo -o /absolute/path/output

# Check permissions
chmod +w ./output
```

#### Issue: Generated Files Are Empty
**Error:** Generated files contain no content

**Solutions:**
```bash
# Check project analysis first
devopsforge analyze ./repo

# Ensure project type is detected
# Check if templates exist for your project type
# Verify project_info has required fields
```

#### Issue: Template Not Found
**Error:** `Template not found for project type`

**Solutions:**
```bash
# Check supported project types
# Currently supported: python, nodejs, java, go, rust

# If your project type isn't supported:
# 1. Open an issue on GitHub
# 2. Contribute a template
# 3. Use custom templates
```

### CLI Problems

#### Issue: Help Command Not Working
**Error:** `--help` shows no output

**Solutions:**
```bash
# Check installation
pip show devopsforge

# Try alternative help
devopsforge -h
devopsforge --help

# Check if entry point is correct
which devopsforge
```

#### Issue: Version Command Not Working
**Error:** `--version` shows no output

**Solutions:**
```bash
# Check if version is set in setup.py
# Verify package metadata
pip show devopsforge

# Try alternative
python -m devopsforge --version
```

## 🔧 Debug Mode

### Enable Verbose Output
```bash
# Set debug environment variable
export DEVOPSFORGE_DEBUG=1
devopsforge analyze ./repo

# Or use Python directly
python -m devopsforge.core.analyzer ./repo
```

### Check Logs
```bash
# Look for log files
find . -name "*.log" -type f

# Check system logs
tail -f /var/log/syslog  # Linux
tail -f /var/log/system.log  # macOS
```

## 🐛 Specific Error Messages

### FileNotFoundError
**Error:** `FileNotFoundError: [Errno 2] No such file or directory`

**Cause:** File or directory doesn't exist
**Solution:** Verify path exists and is accessible

### PermissionError
**Error:** `PermissionError: [Errno 13] Permission denied`

**Cause:** Insufficient permissions
**Solution:** Check file/directory permissions, use `--user` flag

### ImportError
**Error:** `ImportError: No module named 'devopsforge'`

**Cause:** Package not installed or wrong Python environment
**Solution:** Install package, activate correct virtual environment

### ValueError
**Error:** `ValueError: Repository path does not exist`

**Cause:** Invalid repository path
**Solution:** Check path spelling and existence

### TypeError
**Error:** `TypeError: 'NoneType' object is not subscriptable`

**Cause:** Project analysis failed
**Solution:** Check repository contents and structure

## 🔍 Diagnostic Commands

### Check System Information
```bash
# Python version
python --version

# pip version
pip --version

# Installed packages
pip list | grep devopsforge

# System info
uname -a  # Linux/macOS
systeminfo  # Windows
```

### Check Repository Structure
```bash
# List all files
find /path/to/repo -type f

# Check file types
file /path/to/repo/*

# Check for common project files
ls -la /path/to/repo | grep -E "(requirements|package|pom|go\.mod|Cargo)"
```

### Test Individual Components
```bash
# Test analyzer
python -c "from devopsforge.core.analyzer import RepositoryAnalyzer; print('OK')"

# Test generator
python -c "from devopsforge.templates.dockerfile_generator import DockerfileGenerator; print('OK')"

# Test CLI
python -c "from devopsforge.cli.main import cli; print('OK')"
```

## 📞 Getting Help

### Before Asking for Help

1. **Check this guide** for your specific error
2. **Search existing issues** on GitHub
3. **Check the documentation** for usage examples
4. **Verify your environment** meets requirements

### When Reporting Issues

Include:
- **Error message** (exact text)
- **Command used**
- **Operating system** and version
- **Python version**
- **DevOpsForge version**
- **Repository structure** (if relevant)
- **Steps to reproduce**

### Useful Commands for Bug Reports

```bash
# System information
python --version
pip --version
uname -a  # Linux/macOS
systeminfo  # Windows

# Package information
pip show devopsforge

# Environment
env | grep -i python
env | grep -i pip

# Repository structure
tree /path/to/repo  # if available
find /path/to/repo -type f | head -20
```

## 🔗 Related Resources

- [Installation Guide](installation.md) - Setup instructions
- [User Guide](user-guide.md) - Usage instructions
- [Examples](examples.md) - Working examples
- [API Reference](api-reference.md) - Programmatic usage
- [GitHub Issues](https://github.com/Nick1200000/DevOpsForge/issues) - Report bugs
- [GitHub Discussions](https://github.com/Nick1200000/DevOpsForge/discussions) - Ask questions

## 🆘 Emergency Solutions

### Complete Reset
```bash
# Uninstall completely
pip uninstall devopsforge -y

# Clear pip cache
pip cache purge

# Reinstall fresh
pip install devopsforge
```

### Alternative Installation
```bash
# Install from source
git clone https://github.com/Nick1200000/DevOpsForge.git
cd DevOpsForge
pip install -e .

# Or use development version
pip install git+https://github.com/Nick1200000/DevOpsForge.git
```

### Manual Analysis
```bash
# Use Python directly if CLI fails
python -c "
from devopsforge.core.analyzer import RepositoryAnalyzer
analyzer = RepositoryAnalyzer('./repo')
info = analyzer.analyze()
print(info)
"
```
