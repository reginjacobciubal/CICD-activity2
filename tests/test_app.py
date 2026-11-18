import unittest
from src.app import greet
class TestGreeting(unittest.TestCase):
def test_greeting(self):
self.assertEqual(
greet(),
"Hello! Welcome to Software Engineering."
)
if __name__ == "__main__":
unittest.main()
