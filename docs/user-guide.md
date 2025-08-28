# User Guide

This guide will walk you through using DevOpsForge to analyze repositories and generate DevOps configurations.

## 🚀 Getting Started

### Basic Commands

DevOpsForge provides three main commands:

```bash
devopsforge analyze <repository_path>    # Analyze a repository
devopsforge generate <repository_path>   # Generate configurations
devopsforge suggest <repository_path>    # Get optimization suggestions
```

## 📊 Repository Analysis

### Command: `analyze`

The `analyze` command examines a repository and detects its characteristics.

#### Basic Usage

```bash
devopsforge analyze /path/to/repository
```

#### Options

- `-o, --output PATH`: Output directory for analysis results
- `-f, --format [json|table|summary]`: Output format (default: table)

#### Examples

```bash
# Analyze current directory
devopsforge analyze .

# Analyze with JSON output
devopsforge analyze /path/to/repo -f json

# Save results to specific directory
devopsforge analyze /path/to/repo -o ./analysis_results
```

#### Output

The analysis provides information about:

- **Project Type**: Python, Node.js, Java, Go, Rust, etc.
- **Language**: Primary programming language
- **Dependencies**: Package dependencies and versions
- **Build Tools**: Package managers and build systems
- **Test Frameworks**: Testing libraries and frameworks
- **Frameworks**: Web frameworks and application frameworks
- **Database**: Database dependencies
- **DevOps Tools**: Existing Docker, Kubernetes, and CI/CD files

## 🛠️ Configuration Generation

### Command: `generate`

The `generate` command creates DevOps configurations for your repository.

#### Basic Usage

```bash
devopsforge generate /path/to/repository -o ./output
```

#### Options

- `-o, --output PATH`: Output directory for generated files (required)
- `--dockerfile`: Generate Dockerfile
- `--ci-cd`: Generate CI/CD pipeline
- `--kubernetes`: Generate Kubernetes manifests

#### Examples

```bash
# Generate all configurations
devopsforge generate /path/to/repo -o ./devops_config

# Generate only Dockerfile
devopsforge generate /path/to/repo -o ./output --dockerfile

# Generate CI/CD pipeline
devopsforge generate /path/to/repo -o ./output --ci-cd
```

#### Generated Files

Depending on your project type, DevOpsForge generates:

- **Dockerfile**: Multi-stage, optimized Dockerfile
- **CI/CD Pipeline**: GitHub Actions or GitLab CI configuration
- **Kubernetes Manifests**: Deployment, service, and ingress files
- **Documentation**: Setup and usage instructions

## 💡 Optimization Suggestions

### Command: `suggest`

The `suggest` command provides tailored recommendations for your project.

#### Basic Usage

```bash
devopsforge suggest /path/to/repository
```

#### Examples

```bash
# Get suggestions for current directory
devopsforge suggest .

# Get suggestions for specific repository
devopsforge suggest /path/to/repo
```

#### Types of Suggestions

DevOpsForge provides recommendations for:

- **Docker Optimization**: Image size reduction, security improvements
- **CI/CD Enhancement**: Pipeline optimization, testing strategies
- **Security**: Vulnerability scanning, best practices
- **Performance**: Build optimization, caching strategies
- **Monitoring**: Health checks, logging, metrics

## 🔧 Advanced Usage

### Working with Different Project Types

#### Python Projects

```bash
# Analyze Python project
devopsforge analyze ./python_project

# Generate Python-specific configurations
devopsforge generate ./python_project -o ./output
```

#### Node.js Projects

```bash
# Analyze Node.js project
devopsforge analyze ./nodejs_project

# Generate Node.js configurations
devopsforge generate ./nodejs_project -o ./output
```

#### Java Projects

```bash
# Analyze Java project
devopsforge analyze ./java_project

# Generate Java configurations
devopsforge generate ./java_project -o ./output
```

### Customizing Output

#### Output Formats

```bash
# Table format (default)
devopsforge analyze ./repo -f table

# JSON format
devopsforge analyze ./repo -f json

# Summary format
devopsforge analyze ./repo -f summary
```

#### Output Directories

```bash
# Custom output directory
devopsforge generate ./repo -o ./my_devops_config

# Create timestamped directories
devopsforge generate ./repo -o ./config_$(date +%Y%m%d_%H%M%S)
```

## 📋 Best Practices

### Repository Structure

Ensure your repository has:

- Clear project structure
- Dependency files (requirements.txt, package.json, etc.)
- README with project description
- License file

### Generated Configurations

After generation:

1. **Review**: Check generated files for accuracy
2. **Customize**: Modify configurations for your specific needs
3. **Test**: Validate configurations in your environment
4. **Commit**: Version control your DevOps configurations

### Security Considerations

- Review generated Dockerfiles for security best practices
- Check CI/CD pipelines for proper secret management
- Validate Kubernetes manifests for security policies

## 🐛 Troubleshooting

### Common Issues

#### Analysis Failures

```bash
# Check repository path
ls -la /path/to/repository

# Verify file permissions
chmod +r /path/to/repository

# Check for hidden files
ls -la /path/to/repository | grep "^\."
```

#### Generation Errors

```bash
# Ensure output directory exists
mkdir -p ./output

# Check write permissions
chmod +w ./output

# Verify disk space
df -h
```

#### Command Not Found

```bash
# Check installation
pip show devopsforge

# Verify PATH
echo $PATH

# Reinstall if needed
pip install --force-reinstall devopsforge
```

## 📚 Examples

See the [Examples](examples.md) section for real-world usage scenarios and sample outputs.

## 🔗 Related Documentation

- [Installation Guide](installation.md)
- [API Reference](api-reference.md)
- [Troubleshooting](troubleshooting.md)
- [Contributing Guide](contributing.md)
