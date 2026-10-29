import unittest
from pathlib import Path
class OverlayTests(unittest.TestCase):
    def test_rule_exists(self):
        self.assertTrue(Path("enhancements/research-and-writing.md").exists())
    def test_entry_exists(self):
        self.assertTrue(Path("SKILL.md").exists())
