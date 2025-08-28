# Installation Guide

This guide will help you install DevOpsForge on your system.

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for version control)

## 🚀 Quick Installation

### Using pip (Recommended)

```bash
pip install devopsforge
```

### From Source

```bash
# Clone the repository
git clone https://github.com/Nick1200000/DevOpsForge.git
cd DevOpsForge

# Install in development mode
pip install -e .
```

## 🔧 Development Installation

If you want to contribute to DevOpsForge or run it from source:

```bash
# Clone the repository
git clone https://github.com/Nick1200000/DevOpsForge.git
cd DevOpsForge

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install development dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## ✅ Verification

After installation, verify that DevOpsForge is working:

```bash
# Check if the command is available
devopsforge --help

# Check version
devopsforge --version
```

You should see output similar to:
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

## 🐛 Troubleshooting

### Common Issues

#### 1. Command Not Found
If you get a "command not found" error:

```bash
# Check if pip installed to a directory in your PATH
pip show devopsforge

# If not, you may need to add the Scripts directory to your PATH
# Or use the full path to the executable
```

#### 2. Permission Errors
If you get permission errors on Linux/macOS:

```bash
# Use pip with --user flag
pip install --user devopsforge

# Or use sudo (not recommended)
sudo pip install devopsforge
```

#### 3. Python Version Issues
Ensure you're using Python 3.8+:

```bash
python --version
# Should show Python 3.8.x or higher
```

### Getting Help

If you encounter issues:

1. Check the [Troubleshooting Guide](troubleshooting.md)
2. Open an issue on [GitHub](https://github.com/Nick1200000/DevOpsForge/issues)
3. Check the [README](../README.md) for common solutions

## 🔄 Updating

To update to the latest version:

```bash
pip install --upgrade devopsforge
```

## 🗑️ Uninstallation

To remove DevOpsForge:

```bash
pip uninstall devopsforge
```

## 📚 Next Steps

Now that you have DevOpsForge installed, check out:

- [User Guide](user-guide.md) - Learn how to use DevOpsForge
- [Examples](examples.md) - See DevOpsForge in action
- [API Reference](api-reference.md) - Detailed API documentation
