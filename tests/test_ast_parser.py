import unittest
from analyzer.ast_parser import analyze_python_code

class TestASTParser(unittest.TestCase):
    def test_simple_function(self):
        code = '''
def foo(x):
    y = x + 1
    return y
'''
        result = analyze_python_code(code)
        self.assertIn("foo", result["functions"])
        self.assertIn("y", result["variables"])

if __name__ == "__main__":
    unittest.main()
