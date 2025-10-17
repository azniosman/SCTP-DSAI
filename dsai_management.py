#!/usr/bin/env python3
"""
SCTP-DSAI Lessons Management System
A beautiful, interactive CLI tool for managing DSAI course lessons

Author: SCTP-DSAI Team
Version: 1.0.0
"""

import os
import sys
import json
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


# ============================================================================
# Color System - Beautiful Terminal Output
# ============================================================================

class Color:
    """ANSI color codes for beautiful terminal output"""
    # Basic colors
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'

    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    # Reset
    RESET = '\033[0m'
    END = '\033[0m'


class Icon:
    """Unicode icons for visual appeal"""
    CHECKMARK = '✓'
    CROSS = '✗'
    ARROW_RIGHT = '→'
    ARROW_LEFT = '←'
    BULLET = '•'
    STAR = '★'
    FOLDER = '📁'
    FILE = '📄'
    BOOK = '📚'
    ROCKET = '🚀'
    LOCK = '🔒'
    SYNC = '🔄'
    SEARCH = '🔍'
    CHART = '📊'
    GEAR = '⚙️'
    WARNING = '⚠️'
    INFO = 'ℹ️'
    QUESTION = '❓'
    HOURGLASS = '⏳'


# ============================================================================
# Data Models
# ============================================================================

class ModuleType(Enum):
    """Course module types"""
    MODULE_1 = "1"
    MODULE_2 = "2"
    MODULE_3 = "3"


@dataclass
class Lesson:
    """Represents a single lesson"""
    folder: str
    name: str
    number: str
    source_repo: str
    added_date: str
    last_synced: str
    description: str
    module: str
    has_custom_changes: bool

    @property
    def module_name(self) -> str:
        """Get human-readable module name"""
        module_names = {
            "1": "Data Fundamentals",
            "2": "Data Engineering",
            "3": "Machine Learning"
        }
        return module_names.get(self.module, "Unknown")

    @property
    def path(self) -> Path:
        """Get lesson directory path"""
        return Path("lessons") / self.folder

    def exists(self) -> bool:
        """Check if lesson directory exists"""
        return self.path.exists() and self.path.is_dir()


@dataclass
class LessonMetadata:
    """Repository metadata"""
    lessons: List[Lesson]
    last_updated: str
    version: str
    preservation_patterns: List[str]

    @classmethod
    def load(cls, filepath: str = "lessons-metadata.json") -> 'LessonMetadata':
        """Load metadata from JSON file"""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)

            lessons = [Lesson(**lesson_data) for lesson_data in data.get('lessons', [])]

            return cls(
                lessons=lessons,
                last_updated=data.get('last_updated', ''),
                version=data.get('version', '1.0.0'),
                preservation_patterns=data.get('preservation_patterns', [])
            )
        except FileNotFoundError:
            return cls(lessons=[], last_updated='', version='1.0.0', preservation_patterns=[])

    def save(self, filepath: str = "lessons-metadata.json") -> None:
        """Save metadata to JSON file"""
        data = {
            'lessons': [vars(lesson) for lesson in self.lessons],
            'last_updated': self.last_updated,
            'version': self.version,
            'preservation_patterns': self.preservation_patterns
        }

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)


# ============================================================================
# Utility Functions
# ============================================================================

class Terminal:
    """Terminal utilities for beautiful output"""

    @staticmethod
    def clear():
        """Clear terminal screen"""
        os.system('clear' if os.name != 'nt' else 'cls')

    @staticmethod
    def print_header(text: str, width: int = 80):
        """Print a beautiful header"""
        print(f"\n{Color.BOLD}{Color.CYAN}{'═' * width}{Color.RESET}")
        print(f"{Color.BOLD}{Color.CYAN}{text.center(width)}{Color.RESET}")
        print(f"{Color.BOLD}{Color.CYAN}{'═' * width}{Color.RESET}\n")

    @staticmethod
    def print_section(text: str, width: int = 80):
        """Print a section header"""
        print(f"\n{Color.BOLD}{Color.BLUE}{'─' * width}{Color.RESET}")
        print(f"{Color.BOLD}{Color.BLUE}{text}{Color.RESET}")
        print(f"{Color.BOLD}{Color.BLUE}{'─' * width}{Color.RESET}\n")

    @staticmethod
    def print_success(text: str):
        """Print success message"""
        print(f"{Color.GREEN}{Icon.CHECKMARK} {text}{Color.RESET}")

    @staticmethod
    def print_error(text: str):
        """Print error message"""
        print(f"{Color.RED}{Icon.CROSS} {text}{Color.RESET}")

    @staticmethod
    def print_warning(text: str):
        """Print warning message"""
        print(f"{Color.YELLOW}{Icon.WARNING} {text}{Color.RESET}")

    @staticmethod
    def print_info(text: str):
        """Print info message"""
        print(f"{Color.CYAN}{Icon.INFO} {text}{Color.RESET}")

    @staticmethod
    def print_box(text: str, width: int = 80):
        """Print text in a box"""
        lines = text.split('\n')
        print(f"{Color.BOLD}╔{'═' * (width - 2)}╗{Color.RESET}")
        for line in lines:
            padding = width - len(line) - 4
            print(f"{Color.BOLD}║{Color.RESET} {line}{' ' * padding} {Color.BOLD}║{Color.RESET}")
        print(f"{Color.BOLD}╚{'═' * (width - 2)}╝{Color.RESET}")

    @staticmethod
    def prompt(text: str, default: str = "") -> str:
        """Prompt user for input"""
        if default:
            prompt_text = f"{Color.YELLOW}{Icon.QUESTION} {text} [{default}]: {Color.RESET}"
        else:
            prompt_text = f"{Color.YELLOW}{Icon.QUESTION} {text}: {Color.RESET}"

        response = input(prompt_text).strip()
        return response if response else default

    @staticmethod
    def confirm(text: str, default: bool = False) -> bool:
        """Ask for yes/no confirmation"""
        default_str = "Y/n" if default else "y/N"
        response = Terminal.prompt(f"{text} ({default_str})", "y" if default else "n")
        return response.lower() in ['y', 'yes']

    @staticmethod
    def pause(text: str = "Press Enter to continue..."):
        """Pause and wait for user"""
        input(f"\n{Color.DIM}{text}{Color.RESET}")


class CommandRunner:
    """Execute shell commands with proper error handling"""

    @staticmethod
    def run(command: str, capture_output: bool = True, verbose: bool = False) -> Tuple[bool, str, str]:
        """
        Run a shell command

        Returns:
            Tuple[bool, str, str]: (success, stdout, stderr)
        """
        try:
            if verbose:
                Terminal.print_info(f"Running: {command}")

            result = subprocess.run(
                command,
                shell=True,
                capture_output=capture_output,
                text=True,
                timeout=300  # 5 minute timeout
            )

            success = result.returncode == 0
            return success, result.stdout, result.stderr

        except subprocess.TimeoutExpired:
            return False, "", "Command timed out after 5 minutes"
        except Exception as e:
            return False, "", str(e)

    @staticmethod
    def run_script(script_path: str, *args) -> Tuple[bool, str]:
        """Run a bash script with arguments"""
        if not Path(script_path).exists():
            return False, f"Script not found: {script_path}"

        cmd = f"{script_path} {' '.join(args)}"
        success, stdout, stderr = CommandRunner.run(cmd)

        return success, stdout if success else stderr


# ============================================================================
# Lesson Manager - Core Business Logic
# ============================================================================

class LessonManager:
    """Manages all lesson operations"""

    def __init__(self):
        self.metadata = LessonMetadata.load()
        self.root_dir = Path.cwd()

    def get_all_lessons(self) -> List[Lesson]:
        """Get all lessons"""
        return self.metadata.lessons

    def get_lesson_by_folder(self, folder: str) -> Optional[Lesson]:
        """Get lesson by folder name"""
        for lesson in self.metadata.lessons:
            if lesson.folder == folder:
                return lesson
        return None

    def get_lessons_by_module(self, module: str) -> List[Lesson]:
        """Get all lessons in a module"""
        return [l for l in self.metadata.lessons if l.module == module]

    def search_lessons(self, query: str) -> List[Lesson]:
        """Search lessons by name or description"""
        query = query.lower()
        return [
            l for l in self.metadata.lessons
            if query in l.name.lower() or query in l.description.lower()
        ]

    def sync_lesson(self, lesson: Lesson) -> Tuple[bool, str]:
        """Sync a single lesson"""
        if not lesson.exists():
            return False, f"Lesson directory not found: {lesson.folder}"

        Terminal.print_info(f"Syncing {lesson.folder}...")
        success, output = CommandRunner.run_script(
            "./scripts/sync-lesson.sh",
            lesson.folder
        )

        if success:
            lesson.last_synced = datetime.now().strftime("%Y-%m-%d")
            self.metadata.save()

        return success, output

    def sync_all_lessons(self) -> Tuple[int, int]:
        """Sync all lessons"""
        success_count = 0
        failed_count = 0

        for lesson in self.metadata.lessons:
            Terminal.print_info(f"Syncing {lesson.folder}...")
            success, _ = self.sync_lesson(lesson)

            if success:
                success_count += 1
                Terminal.print_success(f"Synced {lesson.folder}")
            else:
                failed_count += 1
                Terminal.print_error(f"Failed to sync {lesson.folder}")

        return success_count, failed_count

    def check_custom_changes(self, lesson: Lesson) -> List[str]:
        """Check for custom files in lesson directory"""
        if not lesson.exists():
            return []

        custom_files = []
        patterns = self.metadata.preservation_patterns

        for pattern in patterns:
            # Simple glob matching
            if pattern.endswith('/'):
                # Directory pattern
                pattern = pattern.rstrip('/')
                for item in lesson.path.rglob(pattern):
                    if item.is_dir():
                        custom_files.append(str(item.relative_to(lesson.path)))
            else:
                # File pattern
                for item in lesson.path.rglob(pattern.replace('*', '*')):
                    if item.is_file():
                        custom_files.append(str(item.relative_to(lesson.path)))

        return custom_files

    def get_statistics(self) -> Dict:
        """Get repository statistics"""
        total_lessons = len(self.metadata.lessons)

        modules = {}
        for lesson in self.metadata.lessons:
            if lesson.module not in modules:
                modules[lesson.module] = 0
            modules[lesson.module] += 1

        lessons_with_custom = sum(1 for l in self.metadata.lessons if l.has_custom_changes)
        lessons_synced_today = sum(
            1 for l in self.metadata.lessons
            if l.last_synced == datetime.now().strftime("%Y-%m-%d")
        )

        return {
            'total_lessons': total_lessons,
            'modules': modules,
            'lessons_with_custom': lessons_with_custom,
            'lessons_synced_today': lessons_synced_today
        }


# ============================================================================
# Menu System
# ============================================================================

class Menu:
    """Base menu class"""

    def __init__(self, manager: LessonManager):
        self.manager = manager

    def display(self):
        """Display menu - must be implemented by subclass"""
        raise NotImplementedError

    def run(self):
        """Run menu loop"""
        while True:
            Terminal.clear()
            choice = self.display()

            if choice == 'q' or choice == '0':
                break

            self.handle_choice(choice)

    def handle_choice(self, choice: str):
        """Handle menu choice - must be implemented by subclass"""
        raise NotImplementedError


class MainMenu(Menu):
    """Main application menu"""

    def display(self) -> str:
        """Display main menu"""
        Terminal.print_header(f"{Icon.BOOK} SCTP-DSAI LESSONS MANAGEMENT SYSTEM {Icon.BOOK}")

        stats = self.manager.get_statistics()

        # Display statistics box
        stats_text = f"Total Lessons: {stats['total_lessons']}  |  "
        stats_text += f"Module 1: {stats['modules'].get('1', 0)}  |  "
        stats_text += f"Module 2: {stats['modules'].get('2', 0)}  |  "
        stats_text += f"Module 3: {stats['modules'].get('3', 0)}"

        print(f"{Color.DIM}{stats_text}{Color.RESET}\n")

        # Menu options
        print(f"{Color.BOLD}{Color.GREEN}1.{Color.RESET} {Icon.FOLDER} Browse Lessons")
        print(f"{Color.BOLD}{Color.GREEN}2.{Color.RESET} {Icon.SYNC} Sync Lessons")
        print(f"{Color.BOLD}{Color.GREEN}3.{Color.RESET} {Icon.SEARCH} Search Lessons")
        print(f"{Color.BOLD}{Color.GREEN}4.{Color.RESET} {Icon.CHART} View Statistics")
        print(f"{Color.BOLD}{Color.GREEN}5.{Color.RESET} {Icon.LOCK} Manage Custom Files")
        print(f"{Color.BOLD}{Color.GREEN}6.{Color.RESET} {Icon.GEAR} Settings")
        print(f"{Color.BOLD}{Color.RED}0.{Color.RESET} {Icon.ARROW_LEFT} Exit")

        print()
        return Terminal.prompt("Select an option", "0")

    def handle_choice(self, choice: str):
        """Handle main menu choice"""
        menu_map = {
            '1': BrowseLessonsMenu,
            '2': SyncMenu,
            '3': SearchMenu,
            '4': StatisticsMenu,
            '5': CustomFilesMenu,
            '6': SettingsMenu,
        }

        menu_class = menu_map.get(choice)
        if menu_class:
            submenu = menu_class(self.manager)
            submenu.run()
        else:
            Terminal.print_error("Invalid option. Please try again.")
            Terminal.pause()


class BrowseLessonsMenu(Menu):
    """Browse lessons by module"""

    def display(self) -> str:
        """Display browse menu"""
        Terminal.print_header(f"{Icon.FOLDER} BROWSE LESSONS")

        print(f"{Color.BOLD}{Color.GREEN}1.{Color.RESET} Module 1: Data Fundamentals (9 lessons)")
        print(f"{Color.BOLD}{Color.GREEN}2.{Color.RESET} Module 2: Data Engineering (9 lessons)")
        print(f"{Color.BOLD}{Color.GREEN}3.{Color.RESET} Module 3: Machine Learning (10 lessons)")
        print(f"{Color.BOLD}{Color.GREEN}4.{Color.RESET} All Lessons")
        print(f"{Color.BOLD}{Color.RED}0.{Color.RESET} {Icon.ARROW_LEFT} Back")

        print()
        return Terminal.prompt("Select module", "0")

    def handle_choice(self, choice: str):
        """Handle browse choice"""
        if choice in ['1', '2', '3']:
            self.show_module_lessons(choice)
        elif choice == '4':
            self.show_all_lessons()
        elif choice != '0':
            Terminal.print_error("Invalid option.")
            Terminal.pause()

    def show_module_lessons(self, module: str):
        """Show lessons for a specific module"""
        Terminal.clear()
        lessons = self.manager.get_lessons_by_module(module)

        if not lessons:
            Terminal.print_warning(f"No lessons found for module {module}")
            Terminal.pause()
            return

        module_names = {
            "1": "Data Fundamentals",
            "2": "Data Engineering",
            "3": "Machine Learning"
        }

        Terminal.print_section(f"{Icon.BOOK} Module {module}: {module_names.get(module, 'Unknown')}")

        for idx, lesson in enumerate(lessons, 1):
            status = f"{Color.GREEN}{Icon.CHECKMARK}{Color.RESET}" if lesson.exists() else f"{Color.RED}{Icon.CROSS}{Color.RESET}"
            custom = f"{Color.YELLOW}{Icon.LOCK}{Color.RESET}" if lesson.has_custom_changes else ""

            print(f"{Color.BOLD}{idx:2d}.{Color.RESET} {status} {custom} {lesson.number}: {lesson.description}")
            print(f"     {Color.DIM}Folder: {lesson.folder}{Color.RESET}")
            print(f"     {Color.DIM}Last synced: {lesson.last_synced}{Color.RESET}\n")

        print()
        choice = Terminal.prompt("Enter lesson number to view details (or 0 to go back)", "0")

        if choice.isdigit() and 0 < int(choice) <= len(lessons):
            self.show_lesson_details(lessons[int(choice) - 1])

    def show_all_lessons(self):
        """Show all lessons"""
        Terminal.clear()
        Terminal.print_section(f"{Icon.BOOK} ALL LESSONS")

        lessons = self.manager.get_all_lessons()

        for idx, lesson in enumerate(lessons, 1):
            status = f"{Color.GREEN}{Icon.CHECKMARK}{Color.RESET}" if lesson.exists() else f"{Color.RED}{Icon.CROSS}{Color.RESET}"
            custom = f"{Color.YELLOW}{Icon.LOCK}{Color.RESET}" if lesson.has_custom_changes else ""

            print(f"{Color.BOLD}{idx:2d}.{Color.RESET} {status} {custom} {lesson.number}: {lesson.description}")

        print()
        Terminal.pause()

    def show_lesson_details(self, lesson: Lesson):
        """Show detailed lesson information"""
        Terminal.clear()
        Terminal.print_header(f"{Icon.BOOK} LESSON DETAILS")

        print(f"{Color.BOLD}Lesson Number:{Color.RESET} {lesson.number}")
        print(f"{Color.BOLD}Name:{Color.RESET} {lesson.name}")
        print(f"{Color.BOLD}Description:{Color.RESET} {lesson.description}")
        print(f"{Color.BOLD}Module:{Color.RESET} {lesson.module} - {lesson.module_name}")
        print(f"{Color.BOLD}Folder:{Color.RESET} {lesson.folder}")
        print(f"{Color.BOLD}Path:{Color.RESET} {lesson.path}")
        print(f"{Color.BOLD}Added:{Color.RESET} {lesson.added_date}")
        print(f"{Color.BOLD}Last Synced:{Color.RESET} {lesson.last_synced}")
        print(f"{Color.BOLD}Source Repo:{Color.RESET} {lesson.source_repo}")
        print(f"{Color.BOLD}Exists:{Color.RESET} {'Yes' if lesson.exists() else 'No'}")
        print(f"{Color.BOLD}Custom Changes:{Color.RESET} {'Yes' if lesson.has_custom_changes else 'No'}")

        # Check for custom files
        custom_files = self.manager.check_custom_changes(lesson)
        if custom_files:
            print(f"\n{Color.BOLD}Custom Files:{Color.RESET}")
            for file in custom_files[:10]:  # Show first 10
                print(f"  {Icon.FILE} {file}")
            if len(custom_files) > 10:
                print(f"  {Color.DIM}...and {len(custom_files) - 10} more{Color.RESET}")

        print()
        Terminal.pause()


class SyncMenu(Menu):
    """Sync lessons menu"""

    def display(self) -> str:
        """Display sync menu"""
        Terminal.print_header(f"{Icon.SYNC} SYNC LESSONS")

        print(f"{Color.BOLD}{Color.GREEN}1.{Color.RESET} Sync Single Lesson")
        print(f"{Color.BOLD}{Color.GREEN}2.{Color.RESET} Sync Module")
        print(f"{Color.BOLD}{Color.GREEN}3.{Color.RESET} Sync All Lessons")
        print(f"{Color.BOLD}{Color.GREEN}4.{Color.RESET} Check Sync Status")
        print(f"{Color.BOLD}{Color.RED}0.{Color.RESET} {Icon.ARROW_LEFT} Back")

        print()
        return Terminal.prompt("Select an option", "0")

    def handle_choice(self, choice: str):
        """Handle sync menu choice"""
        if choice == '1':
            self.sync_single_lesson()
        elif choice == '2':
            self.sync_module()
        elif choice == '3':
            self.sync_all_lessons()
        elif choice == '4':
            self.check_sync_status()
        elif choice != '0':
            Terminal.print_error("Invalid option.")
            Terminal.pause()

    def sync_single_lesson(self):
        """Sync a single lesson"""
        Terminal.clear()
        Terminal.print_section(f"{Icon.SYNC} SYNC SINGLE LESSON")

        lessons = self.manager.get_all_lessons()

        for idx, lesson in enumerate(lessons, 1):
            print(f"{idx:2d}. {lesson.number}: {lesson.description}")

        print()
        choice = Terminal.prompt("Enter lesson number to sync (or 0 to cancel)", "0")

        if choice.isdigit() and 0 < int(choice) <= len(lessons):
            lesson = lessons[int(choice) - 1]

            if Terminal.confirm(f"Sync {lesson.folder}?"):
                print()
                success, output = self.manager.sync_lesson(lesson)

                if success:
                    Terminal.print_success(f"Successfully synced {lesson.folder}")
                else:
                    Terminal.print_error(f"Failed to sync {lesson.folder}")
                    print(output)

                Terminal.pause()

    def sync_module(self):
        """Sync all lessons in a module"""
        Terminal.clear()
        Terminal.print_section(f"{Icon.SYNC} SYNC MODULE")

        print("1. Module 1: Data Fundamentals")
        print("2. Module 2: Data Engineering")
        print("3. Module 3: Machine Learning")

        print()
        choice = Terminal.prompt("Select module to sync (or 0 to cancel)", "0")

        if choice in ['1', '2', '3']:
            lessons = self.manager.get_lessons_by_module(choice)

            if Terminal.confirm(f"Sync all {len(lessons)} lessons in module {choice}?"):
                print()
                success_count = 0
                failed_count = 0

                for lesson in lessons:
                    Terminal.print_info(f"Syncing {lesson.folder}...")
                    success, _ = self.manager.sync_lesson(lesson)

                    if success:
                        success_count += 1
                        Terminal.print_success(f"Synced {lesson.folder}")
                    else:
                        failed_count += 1
                        Terminal.print_error(f"Failed {lesson.folder}")

                print()
                Terminal.print_info(f"Completed: {success_count} succeeded, {failed_count} failed")
                Terminal.pause()

    def sync_all_lessons(self):
        """Sync all lessons"""
        Terminal.clear()
        Terminal.print_section(f"{Icon.SYNC} SYNC ALL LESSONS")

        total = len(self.manager.get_all_lessons())

        if Terminal.confirm(f"Sync all {total} lessons? This may take several minutes."):
            print()
            success_count, failed_count = self.manager.sync_all_lessons()

            print()
            Terminal.print_info(f"Completed: {success_count} succeeded, {failed_count} failed")
            Terminal.pause()

    def check_sync_status(self):
        """Check sync status of all lessons"""
        Terminal.clear()
        Terminal.print_section(f"{Icon.SYNC} SYNC STATUS")

        today = datetime.now().strftime("%Y-%m-%d")

        synced_today = []
        needs_sync = []

        for lesson in self.manager.get_all_lessons():
            if lesson.last_synced == today:
                synced_today.append(lesson)
            else:
                needs_sync.append(lesson)

        print(f"{Color.BOLD}{Color.GREEN}Synced Today ({len(synced_today)}):{Color.RESET}")
        for lesson in synced_today[:5]:
            print(f"  {Icon.CHECKMARK} {lesson.folder}")
        if len(synced_today) > 5:
            print(f"  {Color.DIM}...and {len(synced_today) - 5} more{Color.RESET}")

        print(f"\n{Color.BOLD}{Color.YELLOW}Needs Sync ({len(needs_sync)}):{Color.RESET}")
        for lesson in needs_sync[:5]:
            print(f"  {Icon.WARNING} {lesson.folder} (last: {lesson.last_synced})")
        if len(needs_sync) > 5:
            print(f"  {Color.DIM}...and {len(needs_sync) - 5} more{Color.RESET}")

        print()
        Terminal.pause()


class SearchMenu(Menu):
    """Search lessons menu"""

    def display(self) -> str:
        """Display search menu"""
        Terminal.clear()
        Terminal.print_header(f"{Icon.SEARCH} SEARCH LESSONS")

        query = Terminal.prompt("Enter search query (or 0 to cancel)", "")

        if query == '0' or not query:
            return '0'

        results = self.manager.search_lessons(query)

        if not results:
            Terminal.print_warning(f"No lessons found matching '{query}'")
            Terminal.pause()
            return '0'

        print(f"\n{Color.BOLD}Found {len(results)} lesson(s):{Color.RESET}\n")

        for idx, lesson in enumerate(results, 1):
            status = f"{Color.GREEN}{Icon.CHECKMARK}{Color.RESET}" if lesson.exists() else f"{Color.RED}{Icon.CROSS}{Color.RESET}"
            print(f"{idx}. {status} {lesson.number}: {lesson.description}")
            print(f"   {Color.DIM}Module: {lesson.module_name}{Color.RESET}")
            print(f"   {Color.DIM}Folder: {lesson.folder}{Color.RESET}\n")

        Terminal.pause()
        return '0'

    def handle_choice(self, choice: str):
        """Handle search menu choice"""
        pass  # Search menu is single-use


class StatisticsMenu(Menu):
    """Statistics and reporting menu"""

    def display(self) -> str:
        """Display statistics"""
        Terminal.clear()
        Terminal.print_header(f"{Icon.CHART} REPOSITORY STATISTICS")

        stats = self.manager.get_statistics()

        # Overview
        print(f"{Color.BOLD}OVERVIEW{Color.RESET}")
        print(f"  Total Lessons: {Color.GREEN}{stats['total_lessons']}{Color.RESET}")
        print(f"  Lessons with Custom Changes: {Color.YELLOW}{stats['lessons_with_custom']}{Color.RESET}")
        print(f"  Lessons Synced Today: {Color.CYAN}{stats['lessons_synced_today']}{Color.RESET}")

        # Module breakdown
        print(f"\n{Color.BOLD}MODULE BREAKDOWN{Color.RESET}")
        module_names = {
            "1": "Data Fundamentals",
            "2": "Data Engineering",
            "3": "Machine Learning"
        }

        for module, count in sorted(stats['modules'].items()):
            print(f"  Module {module} ({module_names.get(module, 'Unknown')}): {Color.GREEN}{count}{Color.RESET} lessons")

        # Disk usage
        print(f"\n{Color.BOLD}DISK USAGE{Color.RESET}")
        lessons_dir = Path("lessons")
        if lessons_dir.exists():
            total_size = sum(f.stat().st_size for f in lessons_dir.rglob('*') if f.is_file())
            size_mb = total_size / (1024 * 1024)
            print(f"  Lessons Directory: {Color.CYAN}{size_mb:.2f} MB{Color.RESET}")

        # Recent activity
        print(f"\n{Color.BOLD}RECENT SYNCS{Color.RESET}")
        recent = sorted(self.manager.get_all_lessons(), key=lambda x: x.last_synced, reverse=True)[:5]
        for lesson in recent:
            print(f"  {Icon.SYNC} {lesson.folder}: {lesson.last_synced}")

        print()
        Terminal.pause()
        return '0'

    def handle_choice(self, choice: str):
        """Handle statistics menu choice"""
        pass  # Statistics menu is display-only


class CustomFilesMenu(Menu):
    """Manage custom files menu"""

    def display(self) -> str:
        """Display custom files menu"""
        Terminal.print_header(f"{Icon.LOCK} MANAGE CUSTOM FILES")

        print(f"{Color.BOLD}{Color.GREEN}1.{Color.RESET} View Preservation Patterns")
        print(f"{Color.BOLD}{Color.GREEN}2.{Color.RESET} Scan for Custom Files")
        print(f"{Color.BOLD}{Color.GREEN}3.{Color.RESET} View Lessons with Custom Changes")
        print(f"{Color.BOLD}{Color.RED}0.{Color.RESET} {Icon.ARROW_LEFT} Back")

        print()
        return Terminal.prompt("Select an option", "0")

    def handle_choice(self, choice: str):
        """Handle custom files menu choice"""
        if choice == '1':
            self.view_preservation_patterns()
        elif choice == '2':
            self.scan_custom_files()
        elif choice == '3':
            self.view_lessons_with_custom()
        elif choice != '0':
            Terminal.print_error("Invalid option.")
            Terminal.pause()

    def view_preservation_patterns(self):
        """View preservation patterns"""
        Terminal.clear()
        Terminal.print_section(f"{Icon.LOCK} PRESERVATION PATTERNS")

        print("Files matching these patterns are preserved during syncs:\n")

        for pattern in self.manager.metadata.preservation_patterns:
            print(f"  {Icon.BULLET} {Color.CYAN}{pattern}{Color.RESET}")

        print(f"\n{Color.DIM}These patterns protect your custom work from being overwritten.{Color.RESET}")
        print()
        Terminal.pause()

    def scan_custom_files(self):
        """Scan all lessons for custom files"""
        Terminal.clear()
        Terminal.print_section(f"{Icon.SEARCH} SCANNING FOR CUSTOM FILES")

        print("Scanning all lessons...\n")

        found_custom = []

        for lesson in self.manager.get_all_lessons():
            custom_files = self.manager.check_custom_changes(lesson)
            if custom_files:
                found_custom.append((lesson, custom_files))
                Terminal.print_success(f"{lesson.folder}: {len(custom_files)} custom file(s)")

        print()

        if found_custom:
            print(f"{Color.BOLD}Found custom files in {len(found_custom)} lesson(s){Color.RESET}")
        else:
            Terminal.print_info("No custom files found")

        print()
        Terminal.pause()

    def view_lessons_with_custom(self):
        """View lessons that have custom changes"""
        Terminal.clear()
        Terminal.print_section(f"{Icon.LOCK} LESSONS WITH CUSTOM CHANGES")

        lessons_with_custom = [l for l in self.manager.get_all_lessons() if l.has_custom_changes]

        if not lessons_with_custom:
            Terminal.print_info("No lessons have custom changes marked")
            print()
            Terminal.pause()
            return

        for lesson in lessons_with_custom:
            print(f"{Icon.LOCK} {lesson.folder}")
            custom_files = self.manager.check_custom_changes(lesson)
            if custom_files:
                for file in custom_files[:3]:
                    print(f"    {Icon.FILE} {file}")
                if len(custom_files) > 3:
                    print(f"    {Color.DIM}...and {len(custom_files) - 3} more{Color.RESET}")
            print()

        Terminal.pause()


class SettingsMenu(Menu):
    """Settings menu"""

    def display(self) -> str:
        """Display settings menu"""
        Terminal.print_header(f"{Icon.GEAR} SETTINGS")

        print(f"{Color.BOLD}{Color.GREEN}1.{Color.RESET} View Metadata")
        print(f"{Color.BOLD}{Color.GREEN}2.{Color.RESET} Refresh Metadata")
        print(f"{Color.BOLD}{Color.GREEN}3.{Color.RESET} Check Git Status")
        print(f"{Color.BOLD}{Color.GREEN}4.{Color.RESET} About")
        print(f"{Color.BOLD}{Color.RED}0.{Color.RESET} {Icon.ARROW_LEFT} Back")

        print()
        return Terminal.prompt("Select an option", "0")

    def handle_choice(self, choice: str):
        """Handle settings menu choice"""
        if choice == '1':
            self.view_metadata()
        elif choice == '2':
            self.refresh_metadata()
        elif choice == '3':
            self.check_git_status()
        elif choice == '4':
            self.show_about()
        elif choice != '0':
            Terminal.print_error("Invalid option.")
            Terminal.pause()

    def view_metadata(self):
        """View metadata"""
        Terminal.clear()
        Terminal.print_section(f"{Icon.INFO} METADATA")

        print(f"{Color.BOLD}Version:{Color.RESET} {self.manager.metadata.version}")
        print(f"{Color.BOLD}Last Updated:{Color.RESET} {self.manager.metadata.last_updated}")
        print(f"{Color.BOLD}Total Lessons:{Color.RESET} {len(self.manager.metadata.lessons)}")
        print(f"{Color.BOLD}Preservation Patterns:{Color.RESET} {len(self.manager.metadata.preservation_patterns)}")

        print()
        Terminal.pause()

    def refresh_metadata(self):
        """Refresh metadata from disk"""
        Terminal.clear()
        Terminal.print_section(f"{Icon.SYNC} REFRESH METADATA")

        print("Reloading metadata from disk...\n")

        try:
            self.manager.metadata = LessonMetadata.load()
            Terminal.print_success("Metadata refreshed successfully")
        except Exception as e:
            Terminal.print_error(f"Failed to refresh metadata: {e}")

        print()
        Terminal.pause()

    def check_git_status(self):
        """Check git status"""
        Terminal.clear()
        Terminal.print_section(f"{Icon.INFO} GIT STATUS")

        success, stdout, stderr = CommandRunner.run("git status --short")

        if success:
            if stdout.strip():
                print(f"{Color.BOLD}Modified files:{Color.RESET}\n")
                print(stdout)
            else:
                Terminal.print_success("Working directory is clean")
        else:
            Terminal.print_error("Failed to check git status")
            print(stderr)

        print()
        Terminal.pause()

    def show_about(self):
        """Show about information"""
        Terminal.clear()
        Terminal.print_header(f"{Icon.INFO} ABOUT")

        about_text = """SCTP-DSAI Lessons Management System
Version: 1.0.0

A comprehensive management tool for the SCTP-DSAI course lessons repository.

Features:
  • Browse and search lessons
  • Sync lessons from upstream repositories
  • Preserve custom changes automatically
  • View repository statistics
  • Manage custom files

Created for SCTP-DSAI students to efficiently manage their course materials.
"""

        print(about_text)
        Terminal.pause()


# ============================================================================
# Main Application
# ============================================================================

class DSAIManagementApp:
    """Main application class"""

    def __init__(self):
        self.manager = LessonManager()

    def run(self):
        """Run the application"""
        try:
            # Show welcome screen
            self.show_welcome()

            # Run main menu
            main_menu = MainMenu(self.manager)
            main_menu.run()

            # Show goodbye
            self.show_goodbye()

        except KeyboardInterrupt:
            print(f"\n\n{Color.YELLOW}Interrupted by user{Color.RESET}")
            sys.exit(0)
        except Exception as e:
            Terminal.print_error(f"Unexpected error: {e}")
            sys.exit(1)

    def show_welcome(self):
        """Show welcome screen"""
        Terminal.clear()

        welcome_art = f"""{Color.BOLD}{Color.CYAN}
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║               {Icon.BOOK}  SCTP-DSAI LESSONS MANAGEMENT SYSTEM  {Icon.BOOK}               ║
║                                                                           ║
║                     Your Gateway to Data Science Success                  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
{Color.RESET}"""

        print(welcome_art)
        print(f"\n{Color.DIM}Version 1.0.0 | Created for SCTP-DSAI Students{Color.RESET}")
        print(f"\n{Color.GREEN}{Icon.CHECKMARK} Repository loaded: {len(self.manager.metadata.lessons)} lessons available{Color.RESET}")

        Terminal.pause("\nPress Enter to continue...")

    def show_goodbye(self):
        """Show goodbye message"""
        Terminal.clear()

        goodbye_text = f"""{Color.BOLD}{Color.CYAN}
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                      Thank you for using DSAI Manager!                    ║
║                                                                           ║
║                    Happy Learning and Coding! {Icon.ROCKET}                         ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
{Color.RESET}"""

        print(goodbye_text)
        print()


# ============================================================================
# Entry Point
# ============================================================================

def main():
    """Main entry point"""
    # Verify we're in the right directory
    if not Path("lessons").exists():
        print(f"{Color.RED}Error: 'lessons' directory not found.{Color.RESET}")
        print(f"{Color.YELLOW}Please run this script from the SCTP-DSAI repository root.{Color.RESET}")
        sys.exit(1)

    # Run the application
    app = DSAIManagementApp()
    app.run()


if __name__ == "__main__":
    main()
