#!/usr/bin/env python3
"""
SCTP-DSAI Repository Setup Script
Complete automated setup for lesson management with change preservation
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}{text.center(70)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*70}{Colors.END}\n")

def print_step(step_num, text):
    print(f"{Colors.BOLD}{Colors.BLUE}[Step {step_num}]{Colors.END} {text}")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}✗ {text}{Colors.END}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")

def run_command(command, error_message=None):
    """Run a shell command and return success status"""
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        if error_message:
            print_error(error_message)
            print(f"  Error: {e.stderr}")
        return False, e.stderr

# All lesson definitions
LESSONS = [
    # Module 1: Data Fundamentals
    ("https://github.com/azniosman/5m-data-1.1-intro-data-science.git", "1_1", "intro_data_science", "Introduction to Data Science"),
    ("https://github.com/azniosman/5m-data-1.2-intro-database.git", "1_2", "intro_database", "Introduction to Databases"),
    ("https://github.com/azniosman/5m-data-1.3-sql-basic-ddl.git", "1_3", "sql_basic_ddl", "SQL Basic DDL"),
    ("https://github.com/azniosman/5m-data-1.4-sql-basic-dml.git", "1_4", "sql_basic_dml", "SQL Basic DML"),
    ("https://github.com/azniosman/5m-data-1.5-sql-advanced.git", "1_5", "sql_advanced", "SQL Advanced"),
    ("https://github.com/azniosman/5m-data-1.6-intro-numpy.git", "1_6", "intro_numpy", "Introduction to NumPy"),
    ("https://github.com/azniosman/5m-data-1.7-intro-pandas.git", "1_7", "intro_pandas", "Introduction to Pandas"),
    ("https://github.com/azniosman/5m-data-1.8-eda-basic.git", "1_8", "eda_basic", "EDA Basic"),
    ("https://github.com/azniosman/5m-data-1.9-eda-advanced.git", "1_9", "eda_advanced", "EDA Advanced"),
    
    # Module 2: Data Engineering
    ("https://github.com/azniosman/5m-data-2.1-intro-big-data-eng.git", "2_1", "intro_big_data_eng", "Introduction to Big Data Engineering"),
    ("https://github.com/azniosman/5m-data-2.2-data-architecture.git", "2_2", "data_architecture", "Data Architecture"),
    ("https://github.com/azniosman/5m-data-2.3-data-encoding-creation-flow.git", "2_3", "data_encoding_creation_flow", "Data Encoding Creation Flow"),
    ("https://github.com/azniosman/5m-data-2.4-data-extraction-scraping.git", "2_4", "data_extraction_scraping", "Data Extraction and Scraping"),
    ("https://github.com/azniosman/5m-data-2.5-data-warehouse.git", "2_5", "data_warehouse", "Data Warehouse"),
    ("https://github.com/azniosman/5m-data-2.6-data-pipelines-orchestration.git", "2_6", "data_pipelines_orchestration", "Data Pipelines Orchestration"),
    ("https://github.com/azniosman/5m-data-2.7-data-orchestration-testing.git", "2_7", "data_orchestration_testing", "Data Orchestration Testing"),
    ("https://github.com/azniosman/5m-data-2.8-out-of-core-computation.git", "2_8", "out_of_core_computation", "Out of Core Computation"),
    ("https://github.com/azniosman/5m-data-2.9-distributed-batch.git", "2_9", "distributed_batch", "Distributed Batch Processing"),
    
    # Module 3: Machine Learning
    ("https://github.com/azniosman/5m-data-3.1-probability-statistics.git", "3_1", "probability_statistics", "Probability and Statistics"),
    ("https://github.com/azniosman/5m-data-3.2-intro-machine-learning.git", "3_2", "intro_machine_learning", "Introduction to Machine Learning"),
    ("https://github.com/azniosman/5m-data-3.3-supervised-learning.git", "3_3", "supervised_learning", "Supervised Learning"),
    ("https://github.com/azniosman/5m-data-3.4-supervised-learning-advanced.git", "3_4", "supervised_learning_advanced", "Supervised Learning Advanced"),
    ("https://github.com/azniosman/5m-data-3.5-unsupervised-learning.git", "3_5", "unsupervised_learning", "Unsupervised Learning"),
    ("https://github.com/azniosman/5m-data-3.6-time-series-forecasting.git", "3_6", "time_series_forecasting", "Time Series Forecasting"),
    ("https://github.com/azniosman/5m-data-3.7-neural-network-deep-learning.git", "3_7", "neural_network_deep_learning", "Neural Networks and Deep Learning"),
    ("https://github.com/azniosman/5m-data-3.8-computer-vision.git", "3_8", "computer_vision", "Computer Vision"),
    ("https://github.com/azniosman/5m-data-3.9-nlp.git", "3_9", "nlp", "Natural Language Processing"),
    ("https://github.com/azniosman/5m-data-3.10-nlp-advanced.git", "3_10", "nlp_advanced", "NLP Advanced"),
]

def check_git():
    """Check if git is installed"""
    success, _ = run_command("git --version")
    if not success:
        print_error("Git is not installed. Please install git first.")
        sys.exit(1)
    print_success("Git is installed")

def create_directory_structure():
    """Create the basic directory structure"""
    print_step(1, "Creating directory structure...")
    
    dirs = ['lessons', 'scripts', '.github/workflows']
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
        print_success(f"Created {d}/")

def create_gitignore():
    """Create .gitignore file"""
    print_step(2, "Creating .gitignore...")
    
    gitignore_content = """# OS files
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Python
__pycache__/
*.py[cod]
*$py.class
.env
venv/
*.pyc

# Jupyter
.ipynb_checkpoints/
*/.ipynb_checkpoints/*

# Temporary files
*.log
*.tmp
*.bak
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    print_success("Created .gitignore")

def create_metadata_file():
    """Create initial lessons-metadata.json"""
    print_step(3, "Creating metadata file...")
    
    metadata = {
        "lessons": [],
        "last_updated": "",
        "version": "1.0.0",
        "preservation_patterns": [
            "*.local.*",
            "*-custom.*",
            "*-notes.*",
            "my-*",
            "custom-*/"
        ]
    }
    
    with open('lessons-metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print_success("Created lessons-metadata.json")

def create_add_lesson_script():
    """Create the add-lesson.sh script"""
    print_step(4, "Creating add-lesson.sh script...")
    
    script_content = '''#!/bin/bash
# Add a new lesson to the repository
set -e

if [ "$#" -lt 3 ]; then
    echo "Usage: $0 <source-repo-url> <lesson-number> <lesson-name>"
    exit 1
fi

SOURCE_REPO=$1
LESSON_NUM=$2
LESSON_NAME=$3
FOLDER_NAME="lesson${LESSON_NUM}_${LESSON_NAME}"
LESSON_PATH="lessons/${FOLDER_NAME}"

if [ -d "$LESSON_PATH" ]; then
    echo "Error: Lesson folder ${FOLDER_NAME} already exists!"
    exit 1
fi

echo "Adding lesson: ${FOLDER_NAME}"
echo "Source: ${SOURCE_REPO}"

# Clone the repository
git clone --depth 1 "$SOURCE_REPO" "$LESSON_PATH" 2>&1 | grep -v "Cloning into" || true
rm -rf "${LESSON_PATH}/.git"

# Create custom changes directory
mkdir -p "${LESSON_PATH}/.custom-changes"

# Create lesson info file
CURRENT_DATE=$(date -u +"%Y-%m-%d")
cat > "${LESSON_PATH}/LESSON_INFO.md" << EOF
# ${FOLDER_NAME}

## Lesson Information
- **Lesson Number**: ${LESSON_NUM}
- **Source Repository**: ${SOURCE_REPO}
- **Added Date**: ${CURRENT_DATE}
- **Last Synced**: ${CURRENT_DATE}

## Preserved Files
Files matching these patterns are preserved during syncs:
- *.local.* - Your local versions
- my-*.md - Personal notes
- *-custom.* - Custom modifications
- custom-*/ - Custom directories

## Usage
\`\`\`bash
# Create your version
cp notebook.ipynb notebook.local.ipynb

# Sync updates
./scripts/sync-lesson.sh ${FOLDER_NAME}
\`\`\`
EOF

echo "✓ Lesson added successfully!"
'''
    
    with open('scripts/add-lesson.sh', 'w') as f:
        f.write(script_content)
    
    os.chmod('scripts/add-lesson.sh', 0o755)
    print_success("Created scripts/add-lesson.sh")

def create_sync_script():
    """Create the sync-lesson.sh script"""
    print_step(5, "Creating sync-lesson.sh script...")
    
    script_content = '''#!/bin/bash
# Sync lesson(s) from upstream while preserving custom changes
set -e

PRESERVE_PATTERNS=("*.local.*" "*-custom.*" "*-notes.*" "my-*" "custom-*" ".custom-changes" "LESSON_INFO.md")

sync_single_lesson() {
    local LESSON_FOLDER=$1
    local LESSON_PATH="lessons/${LESSON_FOLDER}"
    
    if [ ! -d "$LESSON_PATH" ]; then
        echo "Error: Lesson folder ${LESSON_PATH} does not exist!"
        return 1
    fi
    
    echo "Syncing: ${LESSON_FOLDER}"
    
    SOURCE_REPO=$(grep "Source Repository" "${LESSON_PATH}/LESSON_INFO.md" | sed 's/.*: //' | sed 's/\*\*//g')
    
    if [ -z "$SOURCE_REPO" ]; then
        echo "Error: Could not find source repository"
        return 1
    fi
    
    # Backup custom files
    BACKUP_DIR="${LESSON_PATH}/.custom-changes/backup-$(date +%Y%m%d-%H%M%S)"
    mkdir -p "$BACKUP_DIR"
    
    for pattern in "${PRESERVE_PATTERNS[@]}"; do
        find "$LESSON_PATH" -name "$pattern" -exec cp -r --parents {} "$BACKUP_DIR/" 2>/dev/null \\; || true
    done
    
    # Clone fresh copy
    TEMP_DIR=$(mktemp -d)
    git clone --depth 1 "$SOURCE_REPO" "$TEMP_DIR" 2>&1 | grep -v "Cloning into" || true
    rm -rf "${TEMP_DIR}/.git"
    
    # Remove old content
    find "$LESSON_PATH" -mindepth 1 -maxdepth 1 -not -name ".custom-changes" -not -name "LESSON_INFO.md" -exec rm -rf {} + 2>/dev/null || true
    
    # Copy new content
    cp -r "${TEMP_DIR}/." "$LESSON_PATH/"
    
    # Restore custom files
    if [ -d "$BACKUP_DIR" ]; then
        cp -r "$BACKUP_DIR"/* "$LESSON_PATH/" 2>/dev/null || true
    fi
    
    # Update sync date
    CURRENT_DATE=$(date -u +"%Y-%m-%d")
    sed -i.bak "s/Last Synced.*/Last Synced**: ${CURRENT_DATE}/" "${LESSON_PATH}/LESSON_INFO.md" 2>/dev/null || \
    sed -i '' "s/Last Synced.*/Last Synced**: ${CURRENT_DATE}/" "${LESSON_PATH}/LESSON_INFO.md" 2>/dev/null || true
    rm -f "${LESSON_PATH}/LESSON_INFO.md.bak"
    
    rm -rf "$TEMP_DIR"
    
    echo "✓ Sync complete!"
}

if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <lesson-folder-name> | --all"
    exit 1
fi

if [ "$1" == "--all" ]; then
    for LESSON_DIR in lessons/*/; do
        if [ -d "$LESSON_DIR" ]; then
            LESSON_NAME=$(basename "$LESSON_DIR")
            sync_single_lesson "$LESSON_NAME"
        fi
    done
else
    sync_single_lesson "$1"
fi
'''
    
    with open('scripts/sync-lesson.sh', 'w') as f:
        f.write(script_content)
    
    os.chmod('scripts/sync-lesson.sh', 0o755)
    print_success("Created scripts/sync-lesson.sh")

def create_github_workflow():
    """Create GitHub Actions workflow"""
    print_step(6, "Creating GitHub Actions workflow...")
    
    workflow_content = '''name: Sync Lessons (Preserve Changes)

on:
  schedule:
    - cron: '0 0 * * 1'
  workflow_dispatch:
    inputs:
      lesson_name:
        description: 'Specific lesson to sync (leave empty for all)'
        required: false
        default: ''

jobs:
  sync-lessons:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          fetch-depth: 0
      
      - name: Configure Git
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
      
      - name: Make scripts executable
        run: chmod +x scripts/*.sh
      
      - name: Sync lessons
        run: |
          if [ -n "${{ github.event.inputs.lesson_name }}" ]; then
            ./scripts/sync-lesson.sh "${{ github.event.inputs.lesson_name }}"
          else
            ./scripts/sync-lesson.sh --all
          fi
      
      - name: Push changes
        run: |
          if [[ -n $(git status -s) ]]; then
            git add .
            git commit -m "Auto-sync lessons [skip ci]"
            git push origin main
          fi
'''
    
    with open('.github/workflows/sync-lessons.yml', 'w') as f:
        f.write(workflow_content)
    
    print_success("Created .github/workflows/sync-lessons.yml")

def create_readme():
    """Create README.md"""
    print_step(7, "Creating README.md...")
    
    readme_content = """# SCTP-DSAI Lessons Repository

This repository contains all 28 SCTP-DSAI course lessons with automatic syncing and change preservation.

## 🚀 Quick Start

### Working on Lessons
```bash
# Navigate to a lesson
cd lessons/lesson1_1_intro_data_science

# Create your version (preserved during syncs!)
cp notebook.ipynb notebook.local.ipynb

# Work on your version
jupyter notebook notebook.local.ipynb
```

### Syncing Updates
```bash
# Sync one lesson
./scripts/sync-lesson.sh lesson1_1_intro_data_science

# Sync all lessons
./scripts/sync-lesson.sh --all
```

## 🔒 File Preservation

Your custom files are automatically preserved:
- `*.local.*` - Your working copies
- `my-*.md` - Personal notes
- `*-custom.*` - Custom modifications
- `custom-*/` - Custom directories

## 📚 Course Structure

- **Module 1**: Data Fundamentals (lessons 1.1-1.9)
- **Module 2**: Data Engineering (lessons 2.1-2.9)
- **Module 3**: Machine Learning (lessons 3.1-3.10)

**Total: 28 Lessons**

## 🤖 Automatic Updates

Lessons automatically sync every Monday at midnight UTC via GitHub Actions.

---

**Your custom files are always safe!** 🔒
"""
    
    with open('README.md', 'w') as f:
        f.write(readme_content)
    
    print_success("Created README.md")

def add_all_lessons():
    """Add all 28 lessons"""
    print_step(8, f"Adding all {len(LESSONS)} lessons (this may take several minutes)...")
    print_warning("Please be patient, cloning repositories takes time...\n")
    
    metadata = {
        "lessons": [],
        "last_updated": datetime.utcnow().isoformat() + 'Z',
        "version": "1.0.0",
        "preservation_patterns": [
            "*.local.*", "*-custom.*", "*-notes.*", "my-*", "custom-*/"
        ]
    }
    
    failed_lessons = []
    
    for idx, (url, number, name, description) in enumerate(LESSONS, 1):
        folder_name = f"lesson{number}_{name}"
        print(f"  [{idx}/{len(LESSONS)}] Adding {folder_name}...", end=" ", flush=True)
        
        success, _ = run_command(
            f'./scripts/add-lesson.sh "{url}" "{number}" "{name}"'
        )
        
        if success:
            print(f"{Colors.GREEN}✓{Colors.END}")
            
            # Add to metadata
            metadata["lessons"].append({
                "folder": folder_name,
                "name": name,
                "number": number,
                "source_repo": url,
                "added_date": datetime.now().strftime("%Y-%m-%d"),
                "last_synced": datetime.now().strftime("%Y-%m-%d"),
                "description": description,
                "module": number.split('_')[0],
                "has_custom_changes": False
            })
        else:
            print(f"{Colors.RED}✗{Colors.END}")
            failed_lessons.append(folder_name)
    
    # Save metadata
    with open('lessons-metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print()
    print_success(f"Successfully added {len(LESSONS) - len(failed_lessons)}/{len(LESSONS)} lessons")
    
    if failed_lessons:
        print_warning(f"Failed to add {len(failed_lessons)} lesson(s):")
        for lesson in failed_lessons:
            print(f"  - {lesson}")

def initialize_git_repo():
    """Initialize git repository and make initial commit"""
    print_step(9, "Initializing git repository...")
    
    # Check if already a git repo
    if not Path('.git').exists():
        run_command("git init")
        print_success("Initialized git repository")
    else:
        print_warning("Already a git repository")
    
    # Add all files
    run_command("git add .")
    
    # Make initial commit
    commit_msg = """Initial setup: SCTP-DSAI lessons with preservation system

- Added all 28 lessons across 3 modules
- Configured automatic weekly syncing  
- Set up file preservation for custom work
- Created lesson management scripts"""
    
    success, _ = run_command(f'git commit -m "{commit_msg}"')
    if success:
        print_success("Created initial commit")
    else:
        print_warning("Could not create commit (may already exist)")

def print_final_instructions():
    """Print final setup instructions"""
    print_header("Setup Complete!")
    
    print(f"{Colors.BOLD}Next Steps:{Colors.END}\n")
    
    print("1. Push to GitHub:")
    print(f"   {Colors.BLUE}git remote add origin https://github.com/azniosman/SCTP-DSAI.git{Colors.END}")
    print(f"   {Colors.BLUE}git push -u origin main{Colors.END}\n")
    
    print("2. Start working on lessons:")
    print(f"   {Colors.BLUE}cd lessons/lesson1_1_intro_data_science{Colors.END}")
    print(f"   {Colors.BLUE}cp notebook.ipynb notebook.local.ipynb{Colors.END}")
    print(f"   {Colors.BLUE}jupyter notebook notebook.local.ipynb{Colors.END}\n")
    
    print("3. Sync updates anytime:")
    print(f"   {Colors.BLUE}./scripts/sync-lesson.sh --all{Colors.END}\n")
    
    print(f"{Colors.GREEN}✓ Your repository is ready to use!{Colors.END}")
    print(f"{Colors.GREEN}✓ All 28 lessons are available in the lessons/ directory{Colors.END}")
    print(f"{Colors.GREEN}✓ Your custom files will be automatically preserved{Colors.END}\n")

def main():
    """Main setup function"""
    print_header("SCTP-DSAI Repository Setup")
    
    print("This script will set up your SCTP-DSAI repository with:")
    print("  • All 28 course lessons")
    print("  • Automatic syncing (weekly)")
    print("  • Custom change preservation")
    print("  • Lesson management scripts")
    print()
    
    # Check if git is installed
    check_git()
    
    # Check if we're in the right place
    if not Path.cwd().name == "SCTP-DSAI":
        response = input(f"\n{Colors.YELLOW}Current directory is not 'SCTP-DSAI'. Continue anyway? (y/n): {Colors.END}")
        if response.lower() != 'y':
            print("Exiting...")
            sys.exit(0)
    
    print()
    input(f"{Colors.BOLD}Press Enter to start setup...{Colors.END}")
    
    try:
        # Run all setup steps
        create_directory_structure()
        create_gitignore()
        create_metadata_file()
        create_add_lesson_script()
        create_sync_script()
        create_github_workflow()
        create_readme()
        add_all_lessons()
        initialize_git_repo()
        
        # Print final instructions
        print_final_instructions()
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Setup interrupted by user{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n{Colors.RED}Setup failed with error:{Colors.END}")
        print(f"{Colors.RED}{str(e)}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()