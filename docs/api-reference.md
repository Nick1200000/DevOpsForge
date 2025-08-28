# API Reference

This page provides detailed information about the DevOpsForge API for programmatic usage.

## 🔧 Core Classes

### ProjectInfo

The main data class that holds project information.

```python
from devopsforge.core.analyzer import ProjectInfo

@dataclass
class ProjectInfo:
    project_type: str
    language: str
    version: Optional[str]
    dependencies: List[str]
    build_tools: List[str]
    test_frameworks: List[str]
    has_docker: bool
    has_kubernetes: bool
    has_ci_cd: bool
    framework: Optional[str]
    database: Optional[str]
    web_framework: Optional[str]
```

**Attributes:**
- `project_type`: Type of project (python, nodejs, java, go, rust)
- `language`: Primary programming language
- `version`: Project version (if available)
- `dependencies`: List of project dependencies
- `build_tools`: List of build tools and package managers
- `test_frameworks`: List of testing frameworks
- `has_docker`: Whether Docker files exist
- `has_kubernetes`: Whether Kubernetes manifests exist
- `has_ci_cd`: Whether CI/CD configurations exist
- `framework`: Main application framework
- `database`: Database dependencies
- `web_framework`: Web framework being used

### RepositoryAnalyzer

Main class for analyzing repository structure.

```python
from devopsforge.core.analyzer import RepositoryAnalyzer

analyzer = RepositoryAnalyzer("/path/to/repository")
project_info = analyzer.analyze()
summary = analyzer.get_summary()
```

**Methods:**
- `analyze()`: Analyze repository and return ProjectInfo
- `get_summary()`: Get formatted summary of analysis
- `_detect_project_type()`: Detect project type
- `_detect_language()`: Detect primary language
- `_detect_dependencies()`: Detect project dependencies
- `_detect_build_tools()`: Detect build tools
- `_detect_test_frameworks()`: Detect testing frameworks
- `_detect_framework()`: Detect application framework
- `_detect_database()`: Detect database dependencies
- `_detect_web_framework()`: Detect web framework
- `_has_file(filename)`: Check if file exists in repository

### DockerfileGenerator

Generates Dockerfiles for different project types.

```python
from devopsforge.templates.dockerfile_generator import DockerfileGenerator

generator = DockerfileGenerator()
dockerfile = generator.generate(project_info_dict)
```

**Methods:**
- `generate(project_info)`: Generate Dockerfile for project
- `_get_python_template()`: Get Python Dockerfile template
- `_get_nodejs_template()`: Get Node.js Dockerfile template
- `_get_java_template()`: Get Java Dockerfile template
- `_get_go_template()`: Get Go Dockerfile template
- `_get_rust_template()`: Get Rust Dockerfile template

### CICDGenerator

Generates CI/CD pipeline configurations.

```python
from devopsforge.templates.cicd_generator import CICDGenerator

generator = CICDGenerator()
workflow = generator.generate_github_actions(project_info_dict)
pipeline = generator.generate_gitlab_ci(project_info_dict)
```

**Methods:**
- `generate_github_actions(project_info)`: Generate GitHub Actions workflow
- `generate_gitlab_ci(project_info)`: Generate GitLab CI pipeline
- `_get_github_actions_template()`: Get GitHub Actions template
- `_get_gitlab_ci_template()`: Get GitLab CI template

## 📊 Usage Examples

### Basic Repository Analysis

```python
from devopsforge.core.analyzer import RepositoryAnalyzer

# Create analyzer instance
analyzer = RepositoryAnalyzer("./my-project")

# Analyze repository
try:
    project_info = analyzer.analyze()
    print(f"Project type: {project_info.project_type}")
    print(f"Language: {project_info.language}")
    print(f"Dependencies: {project_info.dependencies}")
except ValueError as e:
    print(f"Analysis failed: {e}")
```

### Generate Dockerfile

```python
from devopsforge.templates.dockerfile_generator import DockerfileGenerator

# Create generator
generator = DockerfileGenerator()

# Project info dictionary
project_info = {
    "project_type": "python",
    "language": "python",
    "dependencies": ["flask"],
    "build_tools": ["pip"],
    "test_frameworks": ["pytest"],
    "framework": "flask",
    "web_framework": "flask",
    "project_name": "my-app"
}

# Generate Dockerfile
dockerfile = generator.generate(project_info)
print(dockerfile)
```

### Generate CI/CD Pipeline

```python
from devopsforge.templates.cicd_generator import CICDGenerator

# Create generator
generator = CICDGenerator()

# Project info
project_info = {
    "project_type": "python",
    "project_name": "my-app",
    "dependencies": ["flask", "pytest"]
}

# Generate GitHub Actions workflow
workflow = generator.generate_github_actions(project_info)
print(workflow)

# Generate GitLab CI pipeline
pipeline = generator.generate_gitlab_ci(project_info)
print(pipeline)
```

### Complete Workflow

```python
from devopsforge.core.analyzer import RepositoryAnalyzer
from devopsforge.templates.dockerfile_generator import DockerfileGenerator
from devopsforge.templates.cicd_generator import CICDGenerator
import json

def setup_devops(repo_path, output_dir):
    """Complete DevOps setup for a repository."""
    
    # 1. Analyze repository
    analyzer = RepositoryAnalyzer(repo_path)
    project_info = analyzer.analyze()
    
    # 2. Generate Dockerfile
    dockerfile_gen = DockerfileGenerator()
    dockerfile = dockerfile_gen.generate(project_info.__dict__)
    
    # 3. Generate CI/CD pipeline
    cicd_gen = CICDGenerator()
    workflow = cicd_gen.generate_github_actions(project_info.__dict__)
    
    # 4. Save files
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    with open(f"{output_dir}/Dockerfile", "w") as f:
        f.write(dockerfile)
    
    os.makedirs(f"{output_dir}/.github/workflows", exist_ok=True)
    with open(f"{output_dir}/.github/workflows/ci.yml", "w") as f:
        f.write(workflow)
    
    # 5. Save analysis results
    with open(f"{output_dir}/analysis.json", "w") as f:
        json.dump(project_info.__dict__, f, indent=2)
    
    return project_info

# Usage
project_info = setup_devops("./my-project", "./devops-config")
print(f"DevOps setup complete for {project_info.project_type} project")
```

## 🔍 Error Handling

### Common Exceptions

```python
from devopsforge.core.analyzer import RepositoryAnalyzer

try:
    analyzer = RepositoryAnalyzer("./nonexistent-path")
    project_info = analyzer.analyze()
except ValueError as e:
    print(f"Repository error: {e}")
    # Repository path does not exist

try:
    analyzer = RepositoryAnalyzer("./empty-directory")
    project_info = analyzer.analyze()
except Exception as e:
    print(f"Analysis error: {e}")
    # Analysis failed due to empty directory or other issues
```

### Validation

```python
def validate_project_info(project_info):
    """Validate ProjectInfo object."""
    required_fields = [
        'project_type', 'language', 'dependencies', 
        'build_tools', 'test_frameworks'
    ]
    
    for field in required_fields:
        if not hasattr(project_info, field):
            raise ValueError(f"Missing required field: {field}")
    
    if not project_info.project_type:
        raise ValueError("Project type cannot be empty")
    
    return True
```

## 📝 Template Customization

### Custom Dockerfile Template

```python
from devopsforge.templates.dockerfile_generator import DockerfileGenerator

class CustomDockerfileGenerator(DockerfileGenerator):
    def _get_custom_template(self):
        return """
# Custom Dockerfile template
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "main.py"]
"""
    
    def generate(self, project_info):
        if project_info.get("project_type") == "custom":
            return self._get_custom_template()
        return super().generate(project_info)
```

### Custom CI/CD Template

```python
from devopsforge.templates.cicd_generator import CICDGenerator

class CustomCICDGenerator(CICDGenerator):
    def generate_custom_ci(self, project_info):
        return """
# Custom CI/CD pipeline
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - echo "Building custom project"
    - echo "Project: {project_name}"
""".format(**project_info)
```

## 🔗 Related Documentation

- [User Guide](user-guide.md) - High-level usage instructions
- [Examples](examples.md) - Real-world usage examples
- [Installation Guide](installation.md) - Setup instructions
