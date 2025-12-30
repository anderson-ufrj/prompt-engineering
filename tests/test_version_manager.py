#!/usr/bin/env python3
"""
Tests for Version Manager
Author: Anderson Henrique da Silva
Location: Minas Gerais, Brazil
"""

import pytest
import json
import tempfile
from pathlib import Path
from datetime import datetime, timedelta
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from src.versioning.version_manager import (
    VersionChange,
    VersionManager
)

class TestVersionChange:
    """Test cases for VersionChange dataclass"""
    
    def test_version_change_creation(self):
        """Test basic creation of VersionChange"""
        change = VersionChange(
            type="major",
            description="Updated core identity",
            impact_score=0.9,
            files_affected=["anderson-skill/core/identity.md"],
            timestamp=datetime.now().isoformat()
        )
        
        assert change.type == "major"
        assert change.description == "Updated core identity"
        assert change.impact_score == 0.9
        assert len(change.files_affected) == 1

class TestVersionManager:
    """Test cases for VersionManager class"""
    
    @pytest.fixture
    def temp_base_path(self):
        """Create temporary base path for testing"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)
    
    @pytest.fixture
    def version_manager(self, temp_base_path):
        """Create VersionManager with temp paths"""
        return VersionManager(base_path=temp_base_path)
    
    def test_load_current_version_default(self, version_manager):
        """Test loading current version when no version file exists"""
        assert version_manager.current_version == "0.1.0"
    
    def test_load_current_version_existing(self, version_manager):
        """Test loading existing version"""
        # Create version file
        version_file = version_manager.base_path / "meta" / "current_version.json"
        version_file.parent.mkdir(exist_ok=True)
        
        with open(version_file, 'w') as f:
            json.dump({"version": "1.2.3"}, f)
        
        # Create new manager to load the version
        new_manager = VersionManager(base_path=version_manager.base_path)
        assert new_manager.current_version == "1.2.3"
    
    def test_bump_version_major(self, version_manager):
        """Test major version bumping"""
        version_manager.current_version = "1.2.3"
        new_version = version_manager._bump_version("1.2.3", "major")
        assert new_version == "2.0.0"
    
    def test_bump_version_minor(self, version_manager):
        """Test minor version bumping"""
        version_manager.current_version = "1.2.3"
        new_version = version_manager._bump_version("1.2.3", "minor")
        assert new_version == "1.3.0"
    
    def test_bump_version_patch(self, version_manager):
        """Test patch version bumping"""
        version_manager.current_version = "1.2.3"
        new_version = version_manager._bump_version("1.2.3", "patch")
        assert new_version == "1.2.4"
    
    def test_analyze_changes_empty(self, version_manager):
        """Test analyzing empty changes"""
        current_version = version_manager.current_version
        new_version = version_manager.analyze_changes([])
        assert new_version == current_version
    
    def test_analyze_changes_major(self, version_manager):
        """Test analyzing changes that should trigger major version"""
        changes = [
            {
                "type": "major",
                "description": "Core identity change",
                "impact_score": 0.9,
                "files_affected": ["anderson-skill/core/identity.md"],
                "timestamp": datetime.now().isoformat()
            }
        ]
        
        new_version = version_manager.analyze_changes(changes)
        assert new_version == "1.0.0"  # 0.1.0 -> 1.0.0
    
    def test_analyze_changes_multiple_high_impact(self, version_manager):
        """Test analyzing multiple high-impact changes"""
        changes = [
            {
                "type": "major",
                "description": "Core identity change",
                "impact_score": 0.85,
                "files_affected": ["anderson-skill/core/identity.md"],
                "timestamp": datetime.now().isoformat()
            },
            {
                "type": "major",
                "description": "Communication style change",
                "impact_score": 0.82,
                "files_affected": ["anderson-skill/core/communication-style.md"],
                "timestamp": datetime.now().isoformat()
            }
        ]
        
        new_version = version_manager.analyze_changes(changes)
        assert new_version == "1.0.0"  # Should still be major
    
    def test_analyze_changes_minor(self, version_manager):
        """Test analyzing changes that should trigger minor version"""
        changes = [
            {
                "type": "minor",
                "description": "Career status update",
                "impact_score": 0.5,
                "files_affected": ["anderson-skill/dynamic/career-status.md"],
                "timestamp": datetime.now().isoformat()
            }
        ]
        
        new_version = version_manager.analyze_changes(changes)
        assert new_version == "0.2.0"  # 0.1.0 -> 0.2.0
    
    def test_analyze_changes_patch(self, version_manager):
        """Test analyzing changes that should trigger patch version"""
        changes = [
            {
                "type": "patch",
                "description": "Interaction examples update",
                "impact_score": 0.2,
                "files_affected": ["anderson-skill/interactions/good/example.md"],
                "timestamp": datetime.now().isoformat()
            }
        ]
        
        new_version = version_manager.analyze_changes(changes)
        assert new_version == "0.1.1"  # 0.1.0 -> 0.1.1
    
    def test_detect_changes_from_files(self, version_manager):
        """Test detecting changes from file modifications"""
        file_changes = [
            {"file": "anderson-skill/core/identity.md", "type": "modified"},
            {"file": "anderson-skill/dynamic/goals.md", "type": "modified"},
            {"file": "anderson-skill/interactions/bad/example.md", "type": "added"}
        ]
        
        detected_changes = version_manager.detect_changes_from_files(file_changes)
        
        assert len(detected_changes) == 3
        
        # Check identity change (should be major)
        identity_change = next(c for c in detected_changes if "identity" in c["description"].lower())
        assert identity_change["type"] == "major"
        assert identity_change["impact_score"] == 0.9

        # Check goals change (should be minor)
        goals_change = next(c for c in detected_changes if "goals" in c["description"].lower())
        assert goals_change["type"] == "minor"
        assert goals_change["impact_score"] == 0.4

        # Check interactions change (should be patch)
        interactions_change = next(c for c in detected_changes if "calibration" in c["description"].lower())
        assert interactions_change["type"] == "patch"
        assert interactions_change["impact_score"] == 0.2
    
    def test_detect_changes_unmapped_file(self, version_manager):
        """Test detecting changes for unmapped files"""
        file_changes = [
            {"file": "random/unmapped/file.txt", "type": "modified"}
        ]
        
        detected_changes = version_manager.detect_changes_from_files(file_changes)
        
        assert len(detected_changes) == 1
        change = detected_changes[0]
        assert change["type"] == "patch"
        assert change["impact_score"] == 0.1
        assert "file.txt" in change["description"]
    
    def test_record_version_change(self, version_manager):
        """Test recording version change"""
        changes = [
            {
                "type": "minor",
                "description": "Test change",
                "impact_score": 0.6,
                "files_affected": ["test.md"],
                "timestamp": datetime.now().isoformat()
            }
        ]
        
        new_version = version_manager.analyze_changes(changes)
        assert new_version == "0.2.0"
        
        # Verify version file was created
        version_file = version_manager.versions_path / "v0_2_0.json"
        assert version_file.exists()
        
        # Verify content
        with open(version_file) as f:
            version_data = json.load(f)
            assert version_data["version"] == "0.2.0"
            assert version_data["previous_version"] == "0.1.0"
            assert version_data["change_type"] == "minor"
            assert len(version_data["changes"]) == 1
            assert version_data["summary"]["total_changes"] == 1
    
    def test_get_version_history(self, version_manager):
        """Test retrieving version history"""
        # Create multiple versions
        version_changes = [
            ([{"type": "patch", "description": "Patch 1", "impact_score": 0.1, "files_affected": ["file1.md"], "timestamp": datetime.now().isoformat()}], "0.1.1"),
            ([{"type": "minor", "description": "Minor 1", "impact_score": 0.5, "files_affected": ["file2.md"], "timestamp": datetime.now().isoformat()}], "0.2.0"),
            ([{"type": "patch", "description": "Patch 2", "impact_score": 0.1, "files_affected": ["file3.md"], "timestamp": datetime.now().isoformat()}], "0.2.1"),
        ]
        
        for changes, expected_version in version_changes:
            version_manager.analyze_changes(changes)
        
        history = version_manager.get_version_history(limit=10)
        
        assert len(history) == 3
        assert history[0]["version"] == "0.2.1"  # Most recent first
        assert history[1]["version"] == "0.2.0"
        assert history[2]["version"] == "0.1.1"
        
        # Test limit
        limited_history = version_manager.get_version_history(limit=2)
        assert len(limited_history) == 2
    
    def test_suggest_next_changes_empty_history(self, version_manager):
        """Test suggestions with empty history"""
        suggestions = version_manager.suggest_next_changes()
        
        assert len(suggestions) > 0
        assert any("baseline version 0.1.0" in s for s in suggestions)
    
    def test_suggest_next_changes_many_patches(self, version_manager):
        """Test suggestions when many patches have been made"""
        # Create multiple patch versions
        for i in range(4):
            changes = [{
                "type": "patch",
                "description": f"Patch {i}",
                "impact_score": 0.1,
                "files_affected": [f"file{i}.md"],
                "timestamp": datetime.now().isoformat()
            }]
            version_manager.analyze_changes(changes)
        
        suggestions = version_manager.suggest_next_changes()
        
        # Should suggest minor version to bundle patches
        assert any("minor version to bundle recent refinements" in s for s in suggestions)
    
    def test_suggest_next_changes_old_version(self, version_manager):
        """Test suggestions when version is old"""
        # Create an old version in the versions directory
        old_time = (datetime.now() - timedelta(days=35)).isoformat()
        version_file = version_manager.versions_path / "v0_1_0.json"
        version_file.parent.mkdir(parents=True, exist_ok=True)

        with open(version_file, 'w') as f:
            json.dump({
                "version": "0.1.0",
                "previous_version": "0.0.0",
                "change_type": "minor",
                "timestamp": old_time,
                "changes": [],
                "summary": {"total_changes": 0}
            }, f)

        suggestions = version_manager.suggest_next_changes()

        # Should suggest checking if system needs evolution
        assert any("No updates in" in s and "days" in s for s in suggestions)

class TestIntegration:
    """Integration tests for complete version management workflow"""
    
    def test_complete_workflow(self):
        """Test complete version management workflow"""
        with tempfile.TemporaryDirectory() as tmpdir:
            base_path = Path(tmpdir)
            manager = VersionManager(base_path=base_path)
            
            # Simulate file changes
            file_changes = [
                {"file": "anderson-skill/core/identity.md", "type": "modified"},
                {"file": "anderson-skill/dynamic/career-status.md", "type": "modified"},
                {"file": "anderson-skill/interactions/good/great-example.md", "type": "added"},
                {"file": "anderson-skill/contexts/debugging.md", "type": "modified"}
            ]
            
            # Detect changes
            detected_changes = manager.detect_changes_from_files(file_changes)
            assert len(detected_changes) == 4
            
            # Analyze and create new version
            new_version = manager.analyze_changes(detected_changes)
            
            # Should be major version due to identity change
            assert new_version == "1.0.0"
            
            # Verify current version was updated
            assert manager.current_version == "1.0.0"
            
            # Verify version file was created
            current_version_file = base_path / "meta" / "current_version.json"
            assert current_version_file.exists()
            
            with open(current_version_file) as f:
                current_data = json.load(f)
                assert current_data["version"] == "1.0.0"
                assert "updated_at" in current_data
            
            # Verify version history entry
            version_history_file = base_path / "meta" / "versions" / "v1_0_0.json"
            assert version_history_file.exists()

            with open(version_history_file) as f:
                history_data = json.load(f)
                assert history_data["version"] == "1.0.0"
                assert history_data["previous_version"] == "0.1.0"
                assert history_data["change_type"] == "major"
                assert len(history_data["changes"]) == 4
            
            # Get version history
            history = manager.get_version_history()
            assert len(history) == 1
            assert history[0]["version"] == "1.0.0"
            
            # Get suggestions
            suggestions = manager.suggest_next_changes()
            assert len(suggestions) > 0
            
            # Test version history with multiple versions
            # Add a minor version
            minor_changes = [{
                "type": "minor",
                "description": "Added new skill",
                "impact_score": 0.6,
                "files_affected": ["skills/new-skill/SKILL.md"],
                "timestamp": datetime.now().isoformat()
            }]
            
            new_version_2 = manager.analyze_changes(minor_changes)
            assert new_version_2 == "1.1.0"
            
            # History should now have 2 versions
            history = manager.get_version_history()
            assert len(history) == 2
            assert history[0]["version"] == "1.1.0"
            assert history[1]["version"] == "1.0.0"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])