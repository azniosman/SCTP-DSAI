#!/bin/bash
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
        find "$LESSON_PATH" -name "$pattern" -exec cp -r --parents {} "$BACKUP_DIR/" 2>/dev/null \; || true
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
    sed -i.bak "s/Last Synced.*/Last Synced**: ${CURRENT_DATE}/" "${LESSON_PATH}/LESSON_INFO.md" 2>/dev/null ||     sed -i '' "s/Last Synced.*/Last Synced**: ${CURRENT_DATE}/" "${LESSON_PATH}/LESSON_INFO.md" 2>/dev/null || true
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
