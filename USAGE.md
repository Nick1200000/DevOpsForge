# DevOpsForge Usage Guide 🔨

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd devopsforge

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Basic Usage

```bash
# Analyze a repository
devopsforge analyze /path/to/repo

# Generate DevOps configurations
devopsforge generate /path/to/repo -o ./output

# Get optimization suggestions
devopsforge suggest /path/to/repo
```

## 📋 Commands

### `analyze` Command

Analyzes a repository and detects project characteristics.

```bash
devopsforge analyze <repo_path> [options]
```

**Options:**
- `--output, -o`: Output directory for analysis results
- `--format, -f`: Output format (json, table, summary)

**Examples:**
```bash
# Basic analysis
devopsforge analyze my-project

# Save analysis to file
devopsforge analyze my-project -o ./results -f json

# Get summary format
devopsforge analyze my-project -f summary
```

### `generate` Command

Generates DevOps configurations based on repository analysis.

```bash
devopsforge generate <repo_path> -o <output_dir> [options]
```

**Options:**
- `--output, -o`: Output directory (required)
- `--ci-type`: CI/CD type (github_actions, gitlab_ci)
- `--dockerfile/--no-dockerfile`: Generate Dockerfile
- `--cicd/--no-cicd`: Generate CI/CD pipeline

**Examples:**
```bash
# Generate everything
devopsforge generate my-project -o ./devops

# Generate only Dockerfile
devopsforge generate my-project -o ./devops --no-cicd

# Generate GitLab CI instead of GitHub Actions
devopsforge generate my-project -o ./devops --ci-type gitlab_ci
```

### `suggest` Command

Provides optimization suggestions for a repository.

```bash
devopsforge suggest <repo_path>
```

## 🔧 Supported Project Types

### Python Projects
- **Frameworks**: Django, Flask, FastAPI
- **Build Tools**: pip, poetry
- **Testing**: pytest, unittest
- **Docker**: Multi-stage builds with Alpine images

### Node.js Projects
- **Frameworks**: Express, Next.js, React, Vue.js
- **Build Tools**: npm, yarn, pnpm
- **Testing**: Jest, Mocha
- **Docker**: Multi-stage builds with Alpine images

### Java Projects
- **Build Tools**: Maven, Gradle
- **Testing**: JUnit
- **Docker**: Multi-stage builds with OpenJDK

### Go Projects
- **Build Tools**: Go modules
- **Docker**: Multi-stage builds with Alpine

### Rust Projects
- **Build Tools**: Cargo
- **Docker**: Multi-stage builds with Debian

## 🐳 Generated Dockerfiles

DevOpsGenie generates optimized Dockerfiles with:

- **Multi-stage builds** for smaller production images
- **Security best practices** (non-root users, minimal base images)
- **Health checks** for container monitoring
- **Framework-specific optimizations**
- **Dependency caching** for faster builds

## 🔄 Generated CI/CD Pipelines

### GitHub Actions
- Automated testing
- Security scanning with Trivy
- Docker image building
- Conditional deployments

### GitLab CI
- Multi-stage pipeline
- Security scanning
- Docker-in-Docker support
- Artifact management

## 🛡️ Security Features

- **Trivy integration** for vulnerability scanning
- **Non-root containers** by default
- **Minimal base images** to reduce attack surface
- **Dependency scanning** in CI/CD
- **Security best practices** in generated configurations

## 💡 Optimization Suggestions

The tool provides tailored recommendations for:

- **Docker optimizations**: Multi-stage builds, .dockerignore files
- **CI/CD improvements**: Caching, parallel testing, security scanning
- **Language-specific tips**: Framework best practices, dependency management
- **Performance enhancements**: Build caching, image size reduction

## 📁 Output Structure

```
output/
├── Dockerfile                    # Generated Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions workflow
└── .gitlab-ci.yml              # GitLab CI configuration (if selected)
```

## 🔍 Analysis Output

The analyzer detects:

- **Project type** and programming language
- **Framework** and dependencies
- **Build tools** and package managers
- **Testing frameworks**
- **Database dependencies**
- **Existing DevOps configurations**

## 🚨 Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed
2. **Path issues**: Use absolute paths or relative paths from project root
3. **Template errors**: Check that project type is supported

### Debug Mode

```bash
# Run with verbose output
python -m devopsgenie analyze my-project --verbose
```

## 🤝 Contributing

To add support for new project types:

1. Update `RepositoryAnalyzer` in `core/analyzer.py`
2. Add templates in `templates/` directory
3. Update CLI commands in `cli/main.py`
4. Add tests and documentation

## 📚 Examples

See the `sample_python_project/` directory for a complete example of:

- Flask application with tests
- Requirements.txt file
- Generated Dockerfile
- Generated CI/CD pipeline

## 🔗 Related Tools

- **Trivy**: Container vulnerability scanner
- **Docker**: Container platform
- **GitHub Actions**: CI/CD platform
- **GitLab CI**: CI/CD platform
- **Jinja2**: Template engine
