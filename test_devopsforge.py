#!/usr/bin/env python3
"""
Test script to demonstrate DevOpsForge functionality
"""

import sys
from pathlib import Path

# Add the devopsforge package to the path
sys.path.insert(0, str(Path(__file__).parent))

from devopsforge.core.analyzer import RepositoryAnalyzer
from devopsforge.templates.dockerfile_generator import DockerfileGenerator
from devopsforge.templates.cicd_generator import CICDGenerator

def test_analysis():
    """Test repository analysis"""
    print("🔍 Testing Repository Analysis...")
    
    analyzer = RepositoryAnalyzer("sample_python_project")
    project_info = analyzer.analyze()
    
    print(f"Project Type: {project_info.project_type}")
    print(f"Language: {project_info.language}")
    print(f"Framework: {project_info.framework}")
    print(f"Build Tools: {project_info.build_tools}")
    print(f"Test Frameworks: {project_info.test_frameworks}")
    print(f"Has Docker: {project_info.has_docker}")
    print(f"Has CI/CD: {project_info.has_ci_cd}")
    print()

def test_dockerfile_generation():
    """Test Dockerfile generation"""
    print("🐳 Testing Dockerfile Generation...")
    
    analyzer = RepositoryAnalyzer("sample_python_project")
    project_info = analyzer.analyze()
    
    # Convert to dict for template rendering
    project_dict = {
        "project_type": project_info.project_type,
        "language": project_info.language,
        "version": project_info.version,
        "dependencies": project_info.dependencies,
        "build_tools": project_info.build_tools,
        "test_frameworks": project_info.test_frameworks,
        "framework": project_info.framework,
        "database": project_info.database,
        "project_name": "sample_python_project"
    }
    
    dockerfile_gen = DockerfileGenerator()
    dockerfile_content = dockerfile_gen.generate(project_dict)
    
    print("Generated Dockerfile content:")
    print("=" * 50)
    print(dockerfile_content)
    print("=" * 50)
    print()

def test_cicd_generation():
    """Test CI/CD generation"""
    print("🔄 Testing CI/CD Generation...")
    
    analyzer = RepositoryAnalyzer("sample_python_project")
    project_info = analyzer.analyze()
    
    # Convert to dict for template rendering
    project_dict = {
        "project_type": project_info.project_type,
        "language": project_info.language,
        "version": project_info.version,
        "dependencies": project_info.dependencies,
        "build_tools": project_info.build_tools,
        "test_frameworks": project_info.test_frameworks,
        "framework": project_info.framework,
        "database": project_info.database,
        "project_name": "sample_python_project"
    }
    
    cicd_gen = CICDGenerator()
    github_actions_content = cicd_gen.generate(project_dict, ci_type="github_actions")
    
    print("Generated GitHub Actions workflow:")
    print("=" * 50)
    print(github_actions_content)
    print("=" * 50)
    print()

def main():
    """Run all tests"""
    print("🔨 DevOpsForge Test Suite")
    print("=" * 50)
    print()
    
    try:
        test_analysis()
        test_dockerfile_generation()
        test_cicd_generation()
        print("✅ All tests completed successfully!")
    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
