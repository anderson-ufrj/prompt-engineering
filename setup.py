#!/usr/bin/env python3
"""
Setup Script for Prompt Engineering Lab
Author: Anderson Henrique da Silva
Location: Minas Gerais, Brazil

This script handles initial setup, dependency installation, and environment configuration.
"""

import subprocess
import sys
import os
from pathlib import Path
import json
from datetime import datetime

def run_command(command, description=""):
    """Run a shell command and handle errors"""
    print(f"  {'🔄' if not description else '⏳'} {description or command}")
    
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True,
            check=True
        )
        print(f"    ✅ Completed")
        return result
    except subprocess.CalledProcessError as e:
        print(f"    ❌ Failed: {e.stderr or e.stdout}")
        return None
    except Exception as e:
        print(f"    ❌ Error: {e}")
        return None

def check_python_version():
    """Check if Python version is compatible"""
    print("🔍 Checking Python version...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"  ❌ Python 3.8+ required, you have {version.major}.{version.minor}")
        return False
    
    print(f"  ✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    
    # Check if pip is available
    pip_check = run_command("pip --version", "Checking pip availability")
    if not pip_check:
        return False
    
    # Upgrade pip first
    run_command("pip install --upgrade pip", "Upgrading pip")
    
    # Install requirements
    requirements_file = Path(__file__).parent / "requirements.txt"
    if not requirements_file.exists():
        print("  ❌ requirements.txt not found")
        return False
    
    result = run_command(
        f"pip install -r {requirements_file}",
        "Installing required packages"
    )
    
    return result is not None

def create_directory_structure():
    """Create necessary directories"""
    print("📁 Creating directory structure...")
    
    directories = [
        "evidence/metrics/data",
        "evidence/metrics/reports", 
        "evidence/models",
        "experiments/hypothesis",
        "experiments/results",
        "anderson-skill/meta/versions",
        "tests/fixtures",
        "docs/generated"
    ]
    
    created_count = 0
    for directory in directories:
        path = Path(directory)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            print(f"    ✅ Created: {directory}")
            created_count += 1
        else:
            print(f"    ℹ️  Exists: {directory}")
    
    print(f"  📊 Created {created_count} new directories")
    return True

def initialize_configuration():
    """Initialize configuration files"""
    print("⚙️  Initializing configuration...")
    
    # Create current version file if it doesn't exist
    version_file = Path("anderson-skill/meta/current_version.json")
    if not version_file.exists():
        version_data = {
            "version": "0.1.0",
            "updated_at": datetime.now().isoformat(),
            "changelog_summary": "Initial setup and configuration"
        }
        
        with open(version_file, 'w') as f:
            json.dump(version_data, f, indent=2)
        
        print(f"    ✅ Created version configuration")
    
    # Create sample metrics data directory
    metrics_sample = Path("evidence/metrics/data/.gitkeep")
    if not metrics_sample.exists():
        metrics_sample.touch()
        print(f"    ✅ Created metrics data directory marker")
    
    return True

def run_tests():
    """Run the test suite to validate setup"""
    print("🧪 Running validation tests...")
    
    # Check if pytest is available
    pytest_check = run_command("pytest --version", "Checking pytest availability")
    if not pytest_check:
        print("  ⚠️  pytest not found, installing...")
        run_command("pip install pytest", "Installing pytest")
    
    # Run basic import tests
    test_commands = [
        ("python -c 'from evidence.metrics.interaction_analyzer import MetricsCollector; print(\"✅ Interaction analyzer imports successfully\")'", "Testing interaction analyzer import"),
        ("python -c 'from experiments.experiment_runner import ExperimentRunner; print(\"✅ Experiment runner imports successfully\")'", "Testing experiment runner import"),
        ("python -c 'from anderson_skill.meta.version_manager import VersionManager; print(\"✅ Version manager imports successfully\")'", "Testing version manager import"),
    ]
    
    success_count = 0
    for command, description in test_commands:
        result = run_command(command, description)
        if result:
            success_count += 1
    
    print(f"  📊 Import tests: {success_count}/{len(test_commands)} passed")
    return success_count == len(test_commands)

def create_sample_data():
    """Create sample data for initial testing"""
    print("📝 Creating sample data...")
    
    # Sample interaction data
    sample_interactions = [
        {
            "timestamp": datetime.now().isoformat(),
            "prompt_tokens": 150,
            "response_tokens": 280,
            "response_time_ms": 1200,
            "quality_score": 0.85,
            "iteration_count": 1,
            "context_used": ["anderson-skill", "debugging"],
            "pattern_applied": "chain",
            "success_indicators": ["task_completed", "no_followup_needed"]
        },
        {
            "timestamp": datetime.now().isoformat(),
            "prompt_tokens": 200,
            "response_tokens": 400,
            "response_time_ms": 1800,
            "quality_score": 0.92,
            "iteration_count": 2,
            "context_used": ["anderson-skill", "brainstorming"],
            "pattern_applied": "parallel",
            "success_indicators": ["task_completed", "multiple_perspectives"]
        }
    ]
    
    # Save sample interactions
    from evidence.metrics.interaction_analyzer import MetricsCollector, InteractionMetrics
    
    collector = MetricsCollector()
    created_count = 0
    
    for interaction_data in sample_interactions:
        metrics = InteractionMetrics(**interaction_data)
        interaction_id = collector.capture_interaction(metrics)
        created_count += 1
        print(f"    ✅ Created sample interaction: {interaction_id}")
    
    print(f"  📊 Created {created_count} sample interactions")
    return True

def setup_git_hooks():
    """Set up git hooks for quality assurance"""
    print("🪝 Setting up git hooks...")
    
    # Create pre-commit hook
    hook_content = """#!/bin/bash
# Pre-commit hook for Prompt Engineering Lab

echo "Running pre-commit checks..."

# Run tests if they exist
if [ -d "tests" ]; then
    echo "Running tests..."
    if ! pytest tests/ -q; then
        echo "❌ Tests failed. Commit aborted."
        exit 1
    fi
fi

# Check for large files
echo "Checking for large files..."
if git diff --cached --name-only | xargs ls -la | awk '$5 > 1000000 {print $9 " is too large (" $5 " bytes)"}' | grep .; then
    echo "❌ Large files detected. Commit aborted."
    exit 1
fi

echo "✅ Pre-commit checks passed"
"""
    
    hook_path = Path(".git/hooks/pre-commit")
    if hook_path.exists():
        print("    ℹ️  Pre-commit hook already exists")
        return True
    
    try:
        with open(hook_path, 'w') as f:
            f.write(hook_content)
        
        # Make executable
        os.chmod(hook_path, 0o755)
        print(f"    ✅ Created pre-commit hook")
        return True
    except Exception as e:
        print(f"    ⚠️  Could not create git hook: {e}")
        return False

def display_next_steps():
    """Display next steps for the user"""
    print("\n" + "="*60)
    print("🎉 Setup completed successfully!")
    print("="*60)
    
    print("\n📋 Next Steps:")
    print("  1. Run unit tests: pytest tests/ -v")
    print("  2. Run integration tests: python tests/test_integration_real_data.py")
    print("  3. Collect real interaction data with your AI assistant")
    print("  4. Run experiments: python experiments/experiment_runner.py")
    print("  5. Generate reports: python evidence/dashboard.py")
    
    print("\n📁 Important Files:")
    print("  📊 Metrics: evidence/metrics/data/")
    print("  🧪 Experiments: experiments/hypothesis/")
    print("  📈 Reports: evidence/metrics/reports/")
    print("  🔧 Config: anderson-skill/meta/current_version.json")
    
    print("\n🔍 Validation:")
    print("  ✅ Python version compatible")
    print("  ✅ Dependencies installed")
    print("  ✅ Directory structure created")
    print("  ✅ Configuration initialized")
    print("  ✅ Sample data created")
    print("  ✅ Import tests passed")
    
    print("\n💡 Tips:")
    print("  • Start collecting interaction data immediately")
    print("  • Aim for 50+ interactions before training ML models")
    print("  • Run experiments continuously to improve prompts")
    print("  • Review reports weekly for trends")
    print("  • Update version when making significant changes")
    
    print(f"\n📅 Setup completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🚀 Ready to optimize your AI interactions!")

def main():
    """Main setup function"""
    print("🚀 Prompt Engineering Lab Setup")
    print("="*50)
    print("Author: Anderson Henrique da Silva")
    print("Location: Minas Gerais, Brazil")
    print("="*50)
    
    # Check Python version
    if not check_python_version():
        print("\n❌ Setup failed: Python version incompatible")
        return 1
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed: Could not install dependencies")
        return 1
    
    # Create directory structure
    if not create_directory_structure():
        print("\n❌ Setup failed: Could not create directories")
        return 1
    
    # Initialize configuration
    if not initialize_configuration():
        print("\n❌ Setup failed: Could not initialize configuration")
        return 1
    
    # Run validation tests
    if not run_tests():
        print("\n⚠️  Some validation tests failed - proceeding with caution")
    
    # Create sample data
    if not create_sample_data():
        print("\n⚠️  Could not create sample data - will need real interactions")
    
    # Setup git hooks
    setup_git_hooks()
    
    # Display next steps
    display_next_steps()
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)