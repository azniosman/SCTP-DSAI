# SCTP-DSAI Lessons Repository

This repository contains all 28 SCTP-DSAI course lessons with automatic syncing and change preservation.

## 🎯 Management System

Interactive management system:

```bash
./dsai_management.py
```

### Quick Start (30 seconds)

```bash
# 1. Make executable
chmod +x dsai_management.py

# 2. Run it!
./dsai_management.py
```

### Main Features

- 📁 **Browse Lessons** - View all 28 lessons by module or search
- 🔄 **Sync System** - Single lesson, module, or all lessons sync
- 🔍 **Search** - Find lessons by name or description keywords
- 📊 **Statistics** - Repository overview and analytics dashboard
- 🔒 **Custom Files** - Automatic preservation during sync operations
- ⚙️ **Settings** - Metadata, Git status, and configuration

---

## 📚 Course Structure

- **Module 1**: Data Fundamentals (lessons 1.1-1.9)
- **Module 2**: Data Engineering (lessons 2.1-2.9)
- **Module 3**: Machine Learning (lessons 3.1-3.10)

**Total: 28 Lessons**

---

## 🚀 Working with Lessons

### Create Your Local Copy (Preserved During Sync!)

```bash
# Navigate to a lesson
cd lessons/lesson1_7_intro_pandas

# Create your local version (will be preserved!)
cp notebook.ipynb notebook.local.ipynb

# Work on your version
jupyter notebook notebook.local.ipynb
```

### Protected File Patterns

Files matching these patterns are **automatically preserved** during sync:

- `*.local.*` → `notebook.local.ipynb` ✓
- `my-*` → `my-solutions.py` ✓
- `*-custom.*` → `config-custom.json` ✓
- `custom-*/` → `custom-scripts/` ✓

---

## 🔄 Syncing Lessons

### Option 1: Management System (Recommended)

```bash
./dsai_management.py
# Select: 2 (Sync Lessons) → Choose your option
```

**Sync Options:**
- Single lesson
- Entire module
- All 28 lessons
- Check sync status

### Option 2: Direct Scripts

```bash
# Sync one lesson
./scripts/sync-lesson.sh lesson1_7_intro_pandas

# Sync all lessons
./scripts/sync-lesson.sh --all
```

### How Sync Works

1. **Before Sync** - Backs up custom files to `.custom-changes/backup-[timestamp]/`
2. **During Sync** - Pulls fresh content from source repository
3. **After Sync** - Restores custom files automatically

**Custom work is always safe!** 🔒

---

## 📖 Management System Guide

### Main Menu

```
╔═══════════════════════════════════════════════════════════════════════════╗
║               📚  SCTP-DSAI LESSONS MANAGEMENT SYSTEM  📚                 ║
╚═══════════════════════════════════════════════════════════════════════════╝

Total Lessons: 28  |  Module 1: 9  |  Module 2: 9  |  Module 3: 10

1. 📁 Browse Lessons
2. 🔄 Sync Lessons
3. 🔍 Search Lessons
4. 📊 View Statistics
5. 🔒 Manage Custom Files
6. ⚙️  Settings
0. ← Exit
```

### Navigation

- **Number keys** → Select menu options
- **0** → Go back / Exit
- **Enter** → Confirm selection
- **y/n** → Confirm/cancel actions
- **Ctrl+C** → Emergency exit

### 1. Browse Lessons 📁

View lessons organized by module:

**Module 1: Data Fundamentals (9 lessons)**
- 1.1: Introduction to Data Science
- 1.2: Introduction to Databases
- 1.3: SQL Basic DDL
- 1.4: SQL Basic DML
- 1.5: SQL Advanced
- 1.6: Introduction to NumPy
- 1.7: Introduction to Pandas
- 1.8: EDA Basic
- 1.9: EDA Advanced

**Module 2: Data Engineering (9 lessons)**
- 2.1: Introduction to Big Data Engineering
- 2.2: Data Architecture
- 2.3: Data Encoding Creation Flow
- 2.4: Data Extraction and Scraping
- 2.5: Data Warehouse
- 2.6: Data Pipelines Orchestration
- 2.7: Data Orchestration Testing
- 2.8: Out of Core Computation
- 2.9: Distributed Batch Processing

**Module 3: Machine Learning (10 lessons)**
- 3.1: Probability and Statistics
- 3.2: Introduction to Machine Learning
- 3.3: Supervised Learning
- 3.4: Supervised Learning Advanced
- 3.5: Unsupervised Learning
- 3.6: Time Series Forecasting
- 3.7: Neural Networks and Deep Learning
- 3.8: Computer Vision
- 3.9: Natural Language Processing
- 3.10: NLP Advanced

**Lesson Details Include:**
- Lesson number, name, and description
- Module assignment
- Folder location and path
- Source repository URL
- Added date and last sync date
- Custom files status
- List of custom/protected files

**Status Indicators:**
- ✓ (green) - Lesson exists locally
- ✗ (red) - Lesson missing
- 🔒 (yellow) - Has custom changes

### 2. Sync Lessons 🔄

**Sync Options:**

1. **Single Lesson** - Update one specific lesson
2. **Module Sync** - Update all lessons in a module
3. **Sync All** - Update entire repository (28 lessons)
4. **Check Status** - View sync status without syncing

**Smart Sync Process:**
1. Identifies and backs up custom files
2. Pulls fresh content from source repository
3. Restores custom files automatically
4. Updates sync timestamp
5. Maintains file permissions

### 3. Search Lessons 🔍

Search by keyword across all lessons:

**Example Searches:**
- "pandas" → Finds Introduction to Pandas
- "SQL" → Finds all SQL lessons
- "neural" → Finds neural network lessons
- "data" → Finds data-related lessons

**Search Features:**
- Case-insensitive matching
- Search by name or description
- View results with full details

### 4. View Statistics 📊

**Repository Overview:**
- Total lesson count (28)
- Lessons with custom changes
- Lessons synced today
- Overall sync status

**Module Breakdown:**
- Lesson count per module
- Module names and descriptions

**Disk Usage:**
- Total repository size
- Lessons directory size

**Recent Activity:**
- Last 5 synced lessons
- Sync timestamps

### 5. Manage Custom Files 🔒

**View Preservation Patterns:**
```
• *.local.*
• *-custom.*
• *-notes.*
• my-*
• custom-*/
• .custom-changes/
• LESSON_INFO.md
```

**Scan for Custom Files:**
- Search all lessons for custom files
- Count custom files per lesson
- Identify modified lessons

**View Custom Changes:**
- List lessons with custom files
- Preview custom file names
- Track modifications

**Automatic Protection:**
- Files backed up before sync
- Restored after sync
- Never overwritten

### 6. Settings ⚙️

**Metadata Management:**
- View repository metadata
- Check version information
- Refresh from disk

**Git Integration:**
- Check repository status
- View modified files
- Monitor working directory

**About Information:**
- Application version
- Feature overview
- Usage information

---

## 🎨 Visual Design

### Color Coding

- **🟢 Green** - Success, available, active
- **🔴 Red** - Error, missing, unavailable
- **🟡 Yellow** - Warning, needs attention
- **🔵 Cyan** - Information, headers
- **🔵 Blue** - Navigation, sections
- **⚫ Dim** - Secondary information

### Icons Reference

| Icon | Meaning | Usage |
|------|---------|-------|
| 📁 | Folder | Directories, browsing |
| 📄 | File | Individual files |
| 📚 | Book | Lessons, learning |
| 🔄 | Sync | Synchronization |
| 🔍 | Search | Search functionality |
| 🔒 | Lock | Protected files |
| 📊 | Chart | Statistics |
| ⚙️ | Gear | Settings |
| ✓ | Check | Success, exists |
| ✗ | Cross | Error, missing |
| ⚠️ | Warning | Attention needed |
| ℹ️ | Info | Information |

---

## 💡 Daily Workflow Examples

### Morning: Start Your Day

```bash
./dsai_management.py

# 1. Check stats (Option 4)
#    - See your progress
#    - Review sync status

# 2. Search today's topic (Option 3)
#    - Type: "machine learning" (or today's topic)
#    - Note the lesson folder

# 3. Navigate to lesson
cd lessons/lesson3_2_intro_machine_learning

# 4. Create local copy
cp notebook.ipynb notebook.local.ipynb

# 5. Start learning!
jupyter notebook notebook.local.ipynb
```

### Evening: Wrap Up

```bash
./dsai_management.py

# 1. Sync lessons (Option 2 → 3)
#    - Updates all lessons
#    - Preserves your work

# 2. Check custom files (Option 5 → 2)
#    - See what you've created

# 3. View stats (Option 4)
#    - Track your progress
```

---

## 🛠️ Technical Details

### Requirements

- **Python 3.7+** - Main application runtime
- **Git** - Version control and syncing
- **Bash** - Shell scripts execution
- **Terminal with ANSI color support** - Beautiful UI

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd SCTP-DSAI

# Make scripts executable
chmod +x dsai_management.py
chmod +x scripts/*.sh

# Run the application
./dsai_management.py
```

### Architecture

**Design Patterns:**
- **MVC Pattern** - Clean separation of concerns
- **Command Pattern** - Menu navigation system
- **Repository Pattern** - Data access abstraction
- **Factory Pattern** - Dynamic menu creation

**Core Components:**

1. **Data Models**
   - `Lesson` - Individual lesson representation
   - `LessonMetadata` - Repository metadata
   - `ModuleType` - Module enumeration

2. **Business Logic**
   - `LessonManager` - Core operations
   - `CommandRunner` - Shell execution
   - `Terminal` - UI utilities

3. **Menu System**
   - `Menu` - Base menu class
   - `MainMenu` - Primary navigation
   - Specialized menus for features

**Code Quality:**
- ✅ Full type hints (Python 3.7+)
- ✅ Dataclasses for clean models
- ✅ Comprehensive error handling
- ✅ PEP 8 compliant
- ✅ Extensive documentation
- ✅ Best programming practices

### Files Structure

```
SCTP-DSAI/
├── dsai_management.py          # Main application (1,097 lines)
├── README.md                   # This file
├── lessons-metadata.json       # Repository metadata
├── lessons/                    # All 28 lessons
│   ├── lesson1_1_intro_data_science/
│   ├── lesson1_2_intro_database/
│   └── ...
├── scripts/
│   ├── add-lesson.sh          # Add new lesson script
│   └── sync-lesson.sh         # Sync lesson script
└── .github/
    └── workflows/
        └── sync-lessons.yml   # Auto-sync workflow
```

---

## 🔧 Troubleshooting

### "Permission denied"
```bash
chmod +x dsai_management.py
python3 dsai_management.py
```

### "lessons directory not found"
```bash
# Make sure you're in the right directory
pwd  # Should show: /path/to/SCTP-DSAI

# If not, navigate there
cd /path/to/SCTP-DSAI
```

### "No lessons found"
```bash
# Check if lessons exist
ls lessons/

# Refresh metadata from the app
./dsai_management.py
# Select: 6 (Settings) → 2 (Refresh Metadata)
```

### "Sync script not found"
```bash
# Make scripts executable
chmod +x scripts/*.sh

# Verify they exist
ls -l scripts/
```

### "Python version too old"
```bash
# Check Python version
python3 --version  # Should be 3.7 or higher

# Update Python if needed
# (method varies by OS)
```

### Custom Files Not Preserved

**If files were overwritten:**
1. Check `.custom-changes/backup-*/` for backups
2. Verify file names match preservation patterns
3. Use proper naming conventions (*.local.*, my-*, etc.)

---

## 📋 Best Practices

### File Management
1. **Always create local copies** before modifying
   ```bash
   cp original.ipynb original.local.ipynb
   ```

2. **Use consistent naming** for custom files
   ```bash
   my-solutions.py
   notebook.local.ipynb
   config-custom.json
   ```

3. **Organize custom work** in dedicated directories
   ```bash
   mkdir custom-scripts
   mkdir custom-data
   ```

### Sync Operations
1. **Check status before syncing** to avoid unnecessary updates
2. **Sync regularly** (weekly recommended)
3. **Review custom files** after sync
4. **Verify important changes** are preserved

### Workflow Tips
1. **Start with statistics** to see overview
2. **Browse or search** to find lessons
3. **Work on local copies** for safety
4. **Sync when needed** to get updates
5. **Track progress** using statistics

---

## 🤖 Automatic Updates

Lessons automatically sync every Monday at midnight UTC via GitHub Actions.

The workflow:
1. Checks for updates in source repositories
2. Syncs lessons while preserving custom files
3. Commits and pushes changes
4. Keeps repository up-to-date

Manual trigger: Go to Actions tab → Sync Lessons → Run workflow

---

## 🎓 Learning Path

### Week 1-3: Data Fundamentals
```bash
./dsai_management.py
# Browse Module 1 lessons
# Work through 1.1 to 1.9
```

### Week 4-6: Data Engineering
```bash
./dsai_management.py
# Browse Module 2 lessons
# Work through 2.1 to 2.9
```

### Week 7-10: Machine Learning
```bash
./dsai_management.py
# Browse Module 3 lessons
# Work through 3.1 to 3.10
```

---

## 🆘 Support

### Documentation
- This README - Comprehensive guide
- Inline help - Available in the application
- About section - In Settings menu

### Common Questions

**Q: How do I update the management system?**
```bash
git pull origin main
chmod +x dsai_management.py
```

**Q: Can I customize the preservation patterns?**
Edit `lessons-metadata.json` → `preservation_patterns` array

**Q: How do I add a new lesson manually?**
```bash
./scripts/add-lesson.sh <repo-url> <lesson-number> <lesson-name>
```

**Q: Where are my backups stored?**
In `.custom-changes/backup-[timestamp]/` within each lesson folder

---

## 🚀 Quick Reference

### Most Used Commands

```bash
# Launch management system
./dsai_management.py

# Sync all lessons (script)
./scripts/sync-lesson.sh --all

# Sync one lesson (script)
./scripts/sync-lesson.sh lesson1_7_intro_pandas

# Create local copy
cp notebook.ipynb notebook.local.ipynb

# Check what's modified
git status
```

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| 0-9 | Select menu option |
| 0 | Go back / Exit |
| Enter | Confirm |
| y/n | Yes/No |
| Ctrl+C | Emergency exit |

---

## 📜 Version History

### v1.0.0 (Current)
- ✅ Beautiful menu-driven interface
- ✅ Browse all 28 lessons by module
- ✅ Smart sync with file preservation
- ✅ Search functionality
- ✅ Statistics dashboard
- ✅ Custom files management
- ✅ Settings and configuration
- ✅ Comprehensive documentation

---

## 📝 License

Part of the SCTP-DSAI course materials.
Created for educational purposes.

---
