#!/bin/bash
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
