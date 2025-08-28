# Contributing Guide

Thank you for your interest in contributing to DevOpsForge! This guide will help you get started.

## 🤝 How to Contribute

### Types of Contributions

We welcome contributions in many forms:

- **Bug Reports**: Report issues you encounter
- **Feature Requests**: Suggest new features or improvements
- **Code Contributions**: Submit pull requests with code changes
- **Documentation**: Improve or add documentation
- **Testing**: Help test the project
- **Examples**: Add usage examples or tutorials

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- pip (Python package installer)

### Development Setup

1. **Fork the repository**
   ```bash
   # Go to GitHub and fork the repository
   # Then clone your fork
   git clone https://github.com/YOUR_USERNAME/DevOpsForge.git
   cd DevOpsForge
   ```

2. **Set up development environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   # Install development dependencies
   pip install -r requirements.txt
   
   # Install in development mode
   pip install -e .
   ```

3. **Set up pre-commit hooks**
   ```bash
   # Install pre-commit
   pip install pre-commit
   
   # Install hooks
   pre-commit install
   ```

## 🔧 Development Workflow

### Branch Strategy

We follow a GitFlow-inspired branching strategy:

- **main**: Production-ready code
- **develop**: Development branch
- **feature/***: New features
- **bugfix/***: Bug fixes
- **hotfix/***: Critical fixes
- **docs/***: Documentation updates

### Creating a Feature Branch

```bash
# Start from develop branch
git checkout develop
git pull origin develop

# Create feature branch
git checkout -b feature/your-feature-name

# Make your changes
# ... edit files ...

# Commit changes
git add .
git commit -m "feat: add your new feature"

# Push to your fork
git push origin feature/your-feature-name
```

### Code Style

We use several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **pre-commit**: Automated checks

Run these before committing:
```bash
# Format code
black devopsforge/ tests/

# Sort imports
isort devopsforge/ tests/

# Check linting
flake8 devopsforge/ tests/

# Type checking
mypy devopsforge/
```

### Testing

Always run tests before submitting:

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=devopsforge --cov-report=html

# Run specific test file
python -m pytest tests/test_analyzer.py -v
```

## 📝 Adding New Features

### Adding New Project Types

1. **Update the analyzer**
   ```python
   # In devopsforge/core/analyzer.py
   def _detect_project_type(self) -> str:
       if self._has_file("your_file.extension"):
           return "your_project_type"
       # ... existing code ...
   ```

2. **Add detection methods**
   ```python
   def _detect_your_dependencies(self) -> List[str]:
       # Implementation for your project type
       pass
   ```

3. **Update templates**
   ```python
   # In devopsforge/templates/dockerfile_generator.py
   def _get_your_template(self) -> str:
       return """
       # Your project type Dockerfile
       FROM your-base-image
       # ... rest of template
       """
   ```

4. **Add tests**
   ```python
   # In tests/test_analyzer.py
   def test_detect_your_project_type(self, sample_your_project):
       analyzer = RepositoryAnalyzer(str(sample_your_project))
       assert analyzer._detect_project_type() == "your_project_type"
   ```

### Adding New Templates

1. **Create template method**
   ```python
   def _get_your_template(self) -> str:
       return """
       # Your template content
       # Use Jinja2 syntax for variables: {{ variable_name }}
       """
   ```

2. **Update generate method**
   ```python
   def generate(self, project_info: Dict[str, Any]) -> str:
       project_type = project_info.get("project_type", "unknown")
       
       if project_type == "your_type":
           return self._get_your_template()
       # ... existing code ...
   ```

3. **Add tests**
   ```python
   def test_generate_your_template(self, project_info_dict):
       generator = YourGenerator()
       result = generator.generate(project_info_dict)
       assert "expected_content" in result
   ```

## 🐛 Reporting Bugs

### Before Reporting

1. **Check existing issues** - Search for similar problems
2. **Try to reproduce** - Ensure the bug is consistent
3. **Check documentation** - Verify you're using the tool correctly

### Bug Report Template

```markdown
**Bug Description**
Brief description of the issue

**Steps to Reproduce**
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior**
What you expected to happen

**Actual Behavior**
What actually happened

**Environment**
- OS: [e.g., Ubuntu 20.04, Windows 10]
- Python version: [e.g., 3.9.7]
- DevOpsForge version: [e.g., 0.1.0]

**Additional Information**
Any other context, logs, or screenshots
```

## 💡 Suggesting Features

### Feature Request Template

```markdown
**Feature Description**
Brief description of the feature

**Use Case**
Why this feature would be useful

**Proposed Implementation**
How you think it could be implemented

**Alternatives Considered**
Other approaches you've considered

**Additional Context**
Any other relevant information
```

## 🔄 Pull Request Process

### Before Submitting

1. **Ensure tests pass**
   ```bash
   python -m pytest tests/ -v
   ```

2. **Check code quality**
   ```bash
   black --check devopsforge/ tests/
   isort --check-only devopsforge/ tests/
   flake8 devopsforge/ tests/
   mypy devopsforge/
   ```

3. **Update documentation**
   - Update relevant docstrings
   - Add/update user documentation
   - Update examples if needed

### Pull Request Template

```markdown
**Description**
Brief description of changes

**Type of Change**
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Test addition/update
- [ ] Other (please describe)

**Testing**
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] All existing tests pass

**Documentation**
- [ ] Code is documented
- [ ] User documentation updated
- [ ] Examples updated if needed

**Breaking Changes**
- [ ] This PR introduces breaking changes
- [ ] No breaking changes

**Additional Notes**
Any other information reviewers should know
```

### Review Process

1. **Automated checks** must pass
2. **Code review** by maintainers
3. **Tests** must pass
4. **Documentation** must be updated
5. **Approval** from at least one maintainer

## 📚 Documentation Guidelines

### Code Documentation

- Use **docstrings** for all public methods
- Follow **Google docstring format**
- Include **examples** for complex methods
- Document **parameters** and **return values**

```python
def analyze_repository(self, repo_path: str) -> ProjectInfo:
    """Analyze a repository and return project information.
    
    Args:
        repo_path: Path to the repository to analyze
        
    Returns:
        ProjectInfo object containing analysis results
        
    Raises:
        ValueError: If repository path is invalid
        
    Example:
        >>> analyzer = RepositoryAnalyzer("./my-project")
        >>> info = analyzer.analyze_repository("./my-project")
        >>> print(info.project_type)
        'python'
    """
    pass
```

### User Documentation

- Write **clear, concise** instructions
- Include **examples** for common use cases
- Use **consistent formatting**
- Keep **navigation logical**

## 🧪 Testing Guidelines

### Test Structure

- **Unit tests** for individual functions
- **Integration tests** for component interactions
- **End-to-end tests** for complete workflows

### Test Naming

```python
def test_function_name_scenario_expected_result():
    """Test description."""
    pass

# Examples:
def test_analyzer_detect_python_project_returns_python():
    """Test that Python projects are correctly detected."""
    pass

def test_generator_create_dockerfile_contains_from_statement():
    """Test that generated Dockerfiles contain FROM statement."""
    pass
```

### Test Data

- Use **fixtures** for common test data
- Create **minimal test cases**
- Test **edge cases** and **error conditions**
- Use **descriptive test names**

## 🚀 Release Process

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, backward compatible

### Release Steps

1. **Update version** in `setup.py` and `__init__.py`
2. **Update CHANGELOG.md** with new version
3. **Create release branch** from develop
4. **Run full test suite**
5. **Merge to main** and tag release
6. **Deploy to PyPI**
7. **Update documentation**

## 🤝 Community Guidelines

### Code of Conduct

- **Be respectful** and inclusive
- **Help newcomers** get started
- **Provide constructive feedback**
- **Follow project conventions**

### Communication

- **GitHub Issues** for bugs and features
- **GitHub Discussions** for questions
- **Pull Requests** for code changes
- **Discord/Slack** for real-time chat (if available)

## 📞 Getting Help

### Questions?

- **Check documentation** first
- **Search existing issues** and discussions
- **Ask in GitHub Discussions**
- **Open an issue** if it's a bug

### Want to Help?

- **Good first issues** are labeled as such
- **Documentation** always needs improvement
- **Testing** helps ensure quality
- **Examples** help users understand usage

## 🙏 Recognition

Contributors are recognized in:

- **README.md** contributors section
- **CHANGELOG.md** for each release
- **GitHub contributors** page
- **Release notes** for significant contributions

---

Thank you for contributing to DevOpsForge! Your help makes this project better for everyone. 🚀
