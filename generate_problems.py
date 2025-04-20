import os
import sys
from pathlib import Path

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
{import_line}

# def FUNCTION_NAME(...):
#     pass
'''

TEMPLATE_README = '''\
# {title}

Problem description goes here.
'''

LISTNODE_TEMPLATE = '''\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    head = ListNode(0)
    current = head
    for v in values:
        current.next = ListNode(v)
        current = current.next
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
    os.makedirs("common", exist_ok=True)
    listnode_path = os.path.join("common", "listnode.py")
    if use_listnode and not os.path.exists(listnode_path):
        with open(listnode_path, "w") as f:
            f.write(LISTNODE_TEMPLATE)
    init_path = os.path.join("common", "__init__.py")
    if not os.path.exists(init_path):
        with open(init_path, "w") as f:
            f.write("# init")

def generate_problem(category, problem_path, use_listnode=False):
    ensure_common_files(use_listnode)

    base_path = os.path.join(".", category, problem_path)
    os.makedirs(base_path, exist_ok=True)

    final_folder = os.path.basename(problem_path)
    function_name = to_snake_case(final_folder)
    package_path = f"{category}.{problem_path.replace('/', '.')}"

    java_import = "import common.ListNode;\n" if use_listnode else ""
    py_import = "from common.listnode import ListNode, build_list, print_list" if use_listnode else ""

    java_path = os.path.join(base_path, "Solution.java")
    py_path = os.path.join(base_path, f"{function_name}.py")
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
        print("Usage: python3 generate_problems.py <category> <problem_path> [--listnode]")
        sys.exit(1)

    category = sys.argv[1]
    problem_name = sys.argv[2]
    use_listnode = "--listnode" in sys.argv
    generate_problem(category, problem_name, use_listnode)
