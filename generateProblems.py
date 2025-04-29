import os
import sys

TEMPLATE_JAVA = '''\
package {package_path};
{import_line}
class Solution {{
    public static void main(String[] args) {{
        System.out.println("Running {class_name}...");
    }}
}}
'''


TEMPLATE_PY = '''\
from typing import Optional, List
{import_line}

class Solution:
    pass

if __name__ == "__main__":
    print("Running Solution...")
'''

TEMPLATE_README = '''\
# {title}

Your notes or the problem description here.
'''

LISTNODE_TEMPLATE = '''\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    head = ListNode(0)
    curr = head
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return head.next

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
'''


def to_snake_case(name):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in name]).lstrip('_')

def ensure_common_files(use_listnode):
    common_path = os.path.join("leetcode", "common")
    os.makedirs(common_path, exist_ok=True)

    init_path = os.path.join(common_path, "__init__.py")
    if not os.path.exists(init_path):
        with open(init_path, "w") as f:
            f.write("")

    if use_listnode:
        listnode_path = os.path.join(common_path, "listnode.py")
        if not os.path.exists(listnode_path):
            with open(listnode_path, "w") as f:
                f.write(LISTNODE_TEMPLATE)
def generate_problem(category, problem_path, use_listnode=False, use_treenode=False):
    ensure_common_files(use_listnode)
    
    base_path = os.path.join(".", category, problem_path)
    package_path = f"{category}.{problem_path.replace('/', '.')}"


    os.makedirs(base_path, exist_ok=True)

    # Fix here: only snake_case the *final folder name*
    final_folder = os.path.basename(problem_path)
    function_name = to_snake_case(final_folder)

    java_import = "import common.ListNode;\n" if use_listnode else ""
    py_import = "from common.listnode import ListNode, build_list, print_list" if use_listnode else ""

    if use_treenode:
        py_import += "\nfrom common.treenode import TreeNode, deserialize, printTree"

    java_path = os.path.join(base_path, "Solution.java")
    py_path = os.path.join(base_path, f"{function_name}.py")  # Only one folder level, correct now
    readme_path = os.path.join(base_path, "README.md")

    with open(java_path, "w") as f:
        f.write(TEMPLATE_JAVA.format(
            import_line=java_import,
            class_name=final_folder,
            package_path=package_path
        ))


    with open(py_path, "w") as f:
        f.write(TEMPLATE_PY.format(import_line=py_import))

    with open(readme_path, "w") as f:
        f.write(TEMPLATE_README.format(title=final_folder))

    print(f"✅ Created files in: {base_path}")
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_problem.py <Category> <ProblemName> [--listnode]")
    else:
        category = sys.argv[1]
        problem_name = sys.argv[2]
        use_listnode = "--listnode" in sys.argv
        use_treenode = "--treenode" in sys.argv
        generate_problem(category, problem_name, use_listnode, use_treenode)
        
