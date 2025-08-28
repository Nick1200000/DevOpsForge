#!/usr/bin/env python3
"""
Demo script for DevOpsForge
"""

import os
import sys
from pathlib import Path

# Add the devopsforge package to the path
sys.path.insert(0, str(Path(__file__).parent))

def main():
    """Run the DevOpsForge demo"""
    print("🔨 Welcome to DevOpsForge!")
    print("=" * 50)
    print()
    print("This tool automatically generates DevOps configurations for your projects.")
    print()
    print("Available commands:")
    print("  devopsforge analyze <repo_path>     - Analyze a repository")
    print("  devopsforge generate <repo_path> -o <output>  - Generate configurations")
    print("  devopsforge suggest <repo_path>     - Get optimization suggestions")
    print()
    print("Example usage:")
    print("  devopsforge analyze sample_python_project")
    print("  devopsforge generate sample_python_project -o ./output")
    print()
    print("Try running the test script to see it in action:")
    print("  python test_devopsforge.py")
    print()

if __name__ == "__main__":
    main()
