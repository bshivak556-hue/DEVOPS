import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class HelloTests(unittest.TestCase):
    def test_hello_world(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "exp07" / "hello.py")],
            capture_output=True, text=True, check=True,
        )
        self.assertEqual(result.stdout.strip(), "Hello World")

if __name__ == "__main__":
    unittest.main()
