# SCTP-DSAI Lessons Repository

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
