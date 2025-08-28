"""
Main CLI interface for DevOpsForge
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from pathlib import Path

from devopsforge.core.analyzer import RepositoryAnalyzer
from devopsforge.templates.dockerfile_generator import DockerfileGenerator
from devopsforge.templates.cicd_generator import CICDGenerator

console = Console()

# DevOpsForge Logo
LOGO = """╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                        🔧 DevOpsForge 🔧                     ║
║                                                              ║
║                    Professional DevOps Automation             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝"""


@click.group()
@click.version_option(version="0.1.0", prog_name="DevOpsForge")
def cli():
    """🧞‍♂️ DevOpsForge - AI-powered DevOps companion"""
    pass


@cli.command()
@click.argument('repo_path', type=click.Path(exists=True))
@click.option('-o', '--output', type=click.Path(), help='Output directory for results')
@click.option('-f', '--format', type=click.Choice(['table', 'json', 'summary']), default='table', help='Output format')
def analyze(repo_path, output, format):
    """Analyze a repository and detect project characteristics"""
    try:
        console.print(Panel(LOGO, style="bold blue"))
        console.print(f"\n🔍 Analyzing repository: {repo_path}")
        
        analyzer = RepositoryAnalyzer(repo_path)
        project_info = analyzer.analyze()
        
        if format == 'json':
            import json
            result = {
                'repository_path': repo_path,
                'analysis': project_info.__dict__
            }
            if output:
                with open(output, 'w') as f:
                    json.dump(result, f, indent=2)
                console.print(f"✅ Analysis results saved to: {output}")
            else:
                console.print(json.dumps(result, indent=2))
        elif format == 'summary':
            console.print(analyzer.get_summary())
        else:
            # Table format (default)
            table = Table(title="🔍 Repository Analysis Results")
            table.add_column("Property", style="cyan", no_wrap=True)
            table.add_column("Value", style="magenta")
            
            for field, value in project_info.__dict__.items():
                if field != 'project_name':  # Skip project_name for cleaner display
                    table.add_row(field.replace('_', ' ').title(), str(value))
            
            console.print(table)
            
        if output:
            console.print(f"✅ Analysis results saved to: {output}")
            
    except Exception as e:
        console.print(f"❌ Error analyzing repository: {e}", style="bold red")
        raise click.Abort()


@cli.command()
@click.argument('repo_path', type=click.Path(exists=True))
@click.option('-o', '--output', type=click.Path(), required=True, help='Output directory for generated files')
@click.option('--dockerfile', is_flag=True, help='Generate only Dockerfile')
@click.option('--ci-cd', is_flag=True, help='Generate only CI/CD pipeline')
@click.option('--kubernetes', is_flag=True, help='Generate only Kubernetes manifests')
def generate(repo_path, output, dockerfile, ci_cd, kubernetes):
    """Generate DevOps configurations for a repository"""
    try:
        console.print(Panel(LOGO, style="bold blue"))
        console.print(f"\n🛠️ Generating DevOps configurations for: {repo_path}")
        
        # Analyze repository first
        analyzer = RepositoryAnalyzer(repo_path)
        project_info = analyzer.analyze()
        
        # Create output directory
        output_path = Path(output)
        output_path.mkdir(parents=True, exist_ok=True)
        
        generated_files = []
        
        # Generate Dockerfile
        if not ci_cd and not kubernetes:
            dockerfile_gen = DockerfileGenerator()
            dockerfile_content = dockerfile_gen.generate(project_info.__dict__)
            
            dockerfile_path = output_path / "Dockerfile"
            with open(dockerfile_path, 'w') as f:
                f.write(dockerfile_content)
            generated_files.append("Dockerfile")
            console.print("✅ Generated Dockerfile")
        
        # Generate CI/CD pipeline
        if not dockerfile and not kubernetes:
            cicd_gen = CICDGenerator()
            
            # Create .github/workflows directory
            workflows_dir = output_path / ".github" / "workflows"
            workflows_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate GitHub Actions workflow
            workflow_content = cicd_gen.generate_github_actions(project_info.__dict__)
            workflow_path = workflows_dir / "ci.yml"
            with open(workflow_path, 'w') as f:
                f.write(workflow_content)
            generated_files.append(".github/workflows/ci.yml")
            console.print("✅ Generated GitHub Actions workflow")
        
        # Generate README-DEVOPS.md
        readme_content = f"""# DevOps Configuration for {project_info.project_name or 'Project'}

This directory contains DevOps configurations generated by DevOpsForge.

## Generated Files

{chr(10).join(f"- {file}" for file in generated_files)}

## Usage

1. Review the generated configurations
2. Customize as needed for your project
3. Commit to version control
4. Deploy and enjoy!

Generated by [DevOpsForge](https://github.com/Nick1200000/DevOpsForge)
"""
        
        readme_path = output_path / "README-DEVOPS.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        generated_files.append("README-DEVOPS.md")
        
        console.print(f"\n🎉 Successfully generated DevOps configurations!")
        console.print(f"📁 Output directory: {output}")
        console.print(f"📋 Generated files:")
        for file in generated_files:
            console.print(f"   • {file}")
            
    except Exception as e:
        console.print(f"❌ Error generating configurations: {e}", style="bold red")
        raise click.Abort()


@cli.command()
@click.argument('repo_path', type=click.Path(exists=True))
def suggest(repo_path):
    """Get optimization suggestions for a repository"""
    try:
        console.print(Panel(LOGO, style="bold blue"))
        console.print(f"\n💡 Getting optimization suggestions for: {repo_path}")
        
        # Analyze repository first
        analyzer = RepositoryAnalyzer(repo_path)
        project_info = analyzer.analyze()
        
        # Generate suggestions based on analysis
        suggestions = []
        
        if not project_info.has_docker:
            suggestions.append("🐳 Add Docker support for containerization")
        if not project_info.has_ci_cd:
            suggestions.append("🔄 Set up CI/CD pipeline for automated testing")
        if not project_info.has_kubernetes:
            suggestions.append("☸️ Consider adding Kubernetes manifests")
        
        # Language-specific suggestions
        if project_info.project_type == 'python':
            suggestions.extend([
                "📦 Use virtual environments for dependency management",
                "🧪 Ensure test coverage with pytest",
                "🔒 Add security scanning with Safety and Bandit"
            ])
        elif project_info.project_type == 'nodejs':
            suggestions.extend([
                "📦 Use npm ci for production builds",
                "🧪 Set up Jest for testing",
                "🔒 Add security scanning with npm audit"
            ])
        
        # Display suggestions
        if suggestions:
            console.print("\n💡 Optimization Suggestions:")
            for suggestion in suggestions:
                console.print(f"   • {suggestion}")
        else:
            console.print("\n✅ Your project looks well-configured!")
            
    except Exception as e:
        console.print(f"❌ Error getting suggestions: {e}", style="bold red")
        raise click.Abort()


if __name__ == '__main__':
    cli()
