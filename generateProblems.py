import os
import sys
import re

TEMPLATE_JAVA = """\
package {package_path};
{import_line}
class Solution {{
    public static void main(String[] args) {{
        System.out.println("Running {class_name}...");
    }}
}}
"""

TEMPLATE_PY = """\
from typing import Optional, List
import heapq
from collections import defaultdict
{import_line}

class Solution:
    pass

if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
"""

TEMPLATE_CPP = """\
// {filename}
//
// Compile locally with:
// clang++ {filename} -std=c++17 -Wall -Wextra -O2 -o run && ./run
//
// NOTE:
// - Remove main() before submitting to LeetCode.
// - Keep only the class Solution definition.
//

#include <algorithm>
#include <array>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

class Solution {{
public:
    // TODO: paste the LeetCode method signature here.
}};

int main() {{
    cout << "Running {filename}..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}}
"""


TEMPLATE_README = """\
# {title}

Your notes or the problem description here.
"""

LISTNODE_TEMPLATE = """\
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
"""

TREENODE_TEMPLATE = """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
null = None

def deserialize(treeList):
    if len(treeList) == 0:
        return None
    nodes = [ TreeNode(val) if val is not None else None for val in treeList ]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root
        
def printTree(root):
    print("Tree", end=" ")
    printTreeRecursive(root)
    print('\\n')
        
def printTreeRecursive(root):
    if root:
        printTreeRecursive(root.left)
        print(root.val, end=" ")
        printTreeRecursive(root.right)

if __name__ == "__main__":

    testList = [4,2,7,1,3,6,9]
    root = deserialize(testList)
    printTree(root)    

    print("testing treeNode")
"""

GRAPHNODE_TEMPLATE = """
# Definition for a Node.
class GraphNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
from collections import deque

def print_graph_bfs(start: 'GraphNode'):
    visited = set()
    queue = deque([start])
    print("Graph structure:")

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        neighbors_vals = [n.val for n in node.neighbors]
        print(f"Node {node.val}: Neighbors -> {neighbors_vals}")
        for neighbor in node.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

def build_graph(adjList: list[list[int]]) -> 'GraphNode':
    if not adjList:
        return None

    # Step 1: Create all nodes
    nodes = {}
    for i in range(len(adjList)):
        nodes[i + 1] = GraphNode(i + 1)

    # Step 2: Assign neighbors
    for i, neighbors in enumerate(adjList):
        node = nodes[i + 1]
        node.neighbors = [nodes[n] for n in neighbors]

    # Return the node with val = 1 (i.e., index 0), which is the root
    return nodes[1]
"""


def to_snake_case(name: str) -> str:
    return "".join(["_" + c.lower() if c.isupper() else c for c in name]).lstrip("_")


def safe_cpp_filename(folder_name: str) -> str:
    """
    Make a filename that won't cause quoting/escaping pain in shells.
    Keeps letters, digits, underscores. Converts other characters to underscores.
    """
    # Convert spaces to underscores first (common case)
    s = folder_name.replace(" ", "_")
    # Replace everything else non [A-Za-z0-9_] with underscore
    s = re.sub(r"[^A-Za-z0-9_]", "_", s)
    # Collapse multiple underscores
    s = re.sub(r"_+", "_", s).strip("_")
    # Fallback
    return s or "Solution"


def ensure_common_files(use_listnode, use_treenode, use_graphnode):
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

    if use_treenode:
        treenode_path = os.path.join(common_path, "treenode.py")
        if not os.path.exists(treenode_path):
            with open(treenode_path, "w") as f:
                f.write(TREENODE_TEMPLATE)

    if use_graphnode:
        graphnode_path = os.path.join(common_path, "graphnode.py")
        if not os.path.exists(graphnode_path):
            with open(graphnode_path, "w") as f:
                f.write(GRAPHNODE_TEMPLATE)


def generate_problem(
    category, problem_path, use_listnode=False, use_treenode=False, use_graphnode=False
):
    ensure_common_files(use_listnode, use_treenode, use_graphnode)

    base_path = os.path.join(".", category, problem_path)
    package_path = f"{category}.{problem_path.replace('/', '.')}"

    os.makedirs(base_path, exist_ok=True)

    # Only snake_case the *final folder name* for the Python file
    final_folder = os.path.basename(problem_path)
    function_name = to_snake_case(final_folder)

    java_import = "import common.ListNode;\n" if use_listnode else ""
    py_import = (
        "from common.listnode import ListNode, build_list, print_list"
        if use_listnode
        else ""
    )

    if use_treenode:
        java_import += "import common.TreeNode;\n"
        py_import += (
            "\nfrom common.treenode import TreeNode, deserialize, printTree, null"
        )

    if use_graphnode:
        java_import += "import common.Node;\n"
        py_import += "\nfrom common.graphnode import GraphNode as Node, print_graph_bfs, build_graph"

    java_path = os.path.join(base_path, "Solution.java")
    py_path = os.path.join(base_path, f"{function_name}.py")
    readme_path = os.path.join(base_path, "README.md")

    # NEW: C++ skeleton named after the folder
    cpp_base = safe_cpp_filename(final_folder)
    cpp_path = os.path.join(base_path, f"{cpp_base}.cpp")

    with open(java_path, "w") as f:
        f.write(
            TEMPLATE_JAVA.format(
                import_line=java_import,
                class_name=final_folder,
                package_path=package_path,
            )
        )

    with open(py_path, "w") as f:
        f.write(TEMPLATE_PY.format(import_line=py_import))

    with open(readme_path, "w") as f:
        f.write(TEMPLATE_README.format(title=final_folder))

    with open(cpp_path, "w") as f:
        f.write(TEMPLATE_CPP.format(filename=os.path.basename(cpp_path)))

    print(f"✅ Created files in: {base_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: python generateProblems.py <Category> <ProblemName> [--listnode] [--treenode] [--graphnode]"
        )
    else:
        category = sys.argv[1]
        problem_name = sys.argv[2]
        use_listnode = "--listnode" in sys.argv
        use_treenode = "--treenode" in sys.argv
        use_graphnode = "--graphnode" in sys.argv
        generate_problem(
            category, problem_name, use_listnode, use_treenode, use_graphnode
        )
