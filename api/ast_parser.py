import ast
from typing import List, Dict

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.functions: List[str] = []
        self.variables: List[str] = []

    def visit_FunctionDef(self, node):
        self.functions.append(node.name)
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.variables.append(target.id)
        self.generic_visit(node)

def analyze_python_code(source_code: str) -> Dict:
    """
    Parses Python source code and extracts functions and variables.
    """
    tree = ast.parse(source_code)
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)
    return {
        "functions": analyzer.functions,
        "variables": analyzer.variables
    }
