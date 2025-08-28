# Contributing to DevOpsForge 🤝

Thank you for your interest in contributing to DevOpsForge! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Adding New Project Types](#adding-new-project-types)
- [Code Style](#code-style)
- [Testing](#testing)
- [Documentation](#documentation)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## 🤔 How Can I Contribute?

### Reporting Bugs
- Use the [GitHub issue tracker](https://github.com/devopsforge/devopsforge/issues)
- Include detailed steps to reproduce the bug
- Provide system information and error messages
- Use the bug report template

### Suggesting Enhancements
- Open a feature request issue
- Describe the enhancement and its benefits
- Provide use cases and examples
- Discuss implementation approaches

### Contributing Code
- Fork the repository
- Create a feature branch
- Make your changes
- Add tests
- Submit a pull request

### Improving Documentation
- Fix typos and clarify text
- Add examples and use cases
- Improve code comments
- Update README and guides

## 🛠️ Development Setup

### Prerequisites
- Python 3.8 or higher
- Git
- pip

### Local Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/devopsforge.git
cd devopsforge

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Verify installation
devopsforge --help
```

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
python -m pytest

# Run tests with coverage
python -m pytest --cov=devopsforge

# Run specific test file
python -m pytest tests/test_analyzer.py
```

## 📝 Contributing Guidelines

### General Principles
- **Be respectful** and inclusive in all interactions
- **Follow existing patterns** and conventions
- **Write clear, descriptive commit messages**
- **Test your changes** thoroughly
- **Update documentation** when needed

### Code Quality Standards
- **Python 3.8+ compatibility** required
- **Type hints** encouraged for new code
- **Docstrings** for all public functions and classes
- **Error handling** for edge cases
- **Logging** for debugging information

### Commit Message Format

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Maintenance tasks

**Examples:**
```
feat(analyzer): add support for Go modules
fix(cli): resolve path handling issue on Windows
docs(readme): update installation instructions
```

## 🔄 Pull Request Process

### Before Submitting
1. **Test your changes** thoroughly
2. **Update documentation** if needed
3. **Add tests** for new functionality
4. **Check code style** with flake8 and black
5. **Ensure all tests pass**

### Pull Request Checklist
- [ ] **Description** clearly explains the changes
- [ ] **Tests added** for new functionality
- [ ] **Documentation updated** if needed
- [ ] **Code follows** project style guidelines
- [ ] **All tests pass** locally
- [ ] **No merge conflicts** exist

### Review Process
1. **Automated checks** must pass
2. **Code review** by maintainers
3. **Address feedback** and make changes
4. **Maintainer approval** required
5. **Merge** after approval

## 🐛 Reporting Bugs

### Bug Report Template

```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Actual behavior**
A clear and concise description of what actually happened.

**Environment:**
- OS: [e.g. Ubuntu 20.04, Windows 10]
- Python version: [e.g. 3.9.7]
- DevOpsForge version: [e.g. 0.1.0]

**Additional context**
Add any other context about the problem here.
```

## 💡 Suggesting Enhancements

### Enhancement Request Template

```markdown
**Is your feature request related to a problem?**
A clear and concise description of what the problem is.

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions.

**Additional context**
Add any other context or screenshots about the feature request.
```

## 🔧 Adding New Project Types

### 1. Update Repository Analyzer

Add detection logic in `devopsforge/core/analyzer.py`:

```python
def _detect_new_language(self) -> str:
    """Detect new programming language"""
    if self._has_file("newfile.extension"):
        return "newlanguage"
    return None
```

### 2. Create Templates

Add templates in `devopsforge/templates/`:

```python
def _get_new_language_template(self) -> str:
    return (
        "# New Language Dockerfile\n"
        "FROM newlanguage:latest\n"
        # ... template content
    )
```

### 3. Update CLI Support

Add language support in `devopsforge/cli/main.py`:

```python
# Add new language to supported types
SUPPORTED_LANGUAGES = ["python", "nodejs", "java", "go", "rust", "newlanguage"]
```

### 4. Add Tests

Create tests in `tests/` directory:

```python
def test_new_language_detection():
    """Test new language detection"""
    analyzer = RepositoryAnalyzer("sample_newlanguage_project")
    result = analyzer.analyze()
    assert result.project_type == "newlanguage"
```

## 🎨 Code Style

### Python Style Guide
- **PEP 8** compliance required
- **Black** formatting for code
- **Flake8** for linting
- **isort** for import sorting

### Running Style Checks

```bash
# Format code with Black
black devopsforge/

# Sort imports with isort
isort devopsforge/

# Check style with flake8
flake8 devopsforge/

# Run all style checks
make style-check
```

## 🧪 Testing

### Test Structure
```
tests/
├── test_analyzer.py      # Core analyzer tests
├── test_templates.py     # Template generation tests
├── test_cli.py          # CLI command tests
└── conftest.py          # Test configuration
```

### Writing Tests
- **Unit tests** for individual functions
- **Integration tests** for complete workflows
- **Edge case testing** for error conditions
- **Mock external dependencies** when possible

### Test Coverage
- **Minimum 80%** coverage required
- **100% coverage** for critical paths
- **Coverage reports** generated automatically

## 📚 Documentation

### Documentation Standards
- **Clear and concise** language
- **Code examples** for all features
- **Screenshots** for UI elements
- **Regular updates** with code changes

### Documentation Structure
- **README.md** - Project overview and quick start
- **USAGE.md** - Comprehensive usage guide
- **API.md** - Code-level documentation
- **EXAMPLES.md** - Real-world examples

## 🚀 Release Process

### Version Management
- **Semantic versioning** (MAJOR.MINOR.PATCH)
- **Changelog** maintained for each release
- **Release notes** for significant changes
- **Git tags** for each release

### Release Checklist
- [ ] **All tests pass**
- [ ] **Documentation updated**
- [ ] **Changelog updated**
- [ ] **Version bumped**
- [ ] **Git tag created**
- [ ] **PyPI package published**

## 📞 Getting Help

### Communication Channels
- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - General questions and discussions
- **Pull Requests** - Code contributions and reviews

### Maintainer Contact
- **Core team** available for questions
- **Response time** typically within 24-48 hours
- **Code review** feedback provided promptly

## 🙏 Recognition

### Contributors
- **All contributors** listed in README
- **Significant contributions** acknowledged in releases
- **Contributor badges** for active participants

### Contribution Levels
- **Bug fixes** - Bug hunter badge
- **Feature additions** - Feature developer badge
- **Documentation** - Documentation hero badge
- **Testing** - Quality assurance badge

---

**Thank you for contributing to DevOpsForge! 🎉**

Your contributions help make DevOps automation accessible to developers worldwide.
