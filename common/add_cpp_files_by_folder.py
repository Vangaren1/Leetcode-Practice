#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

CPP_TEMPLATE = """\
// {filename}
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
"""


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Create <FolderName>.cpp skeleton in every folder containing Solution.java"
    )
    ap.add_argument(
        "--root",
        default=".",
        help="Repo root to scan (default: current directory)",
    )
    ap.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing .cpp file if present",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing files",
    )
    args = ap.parse_args()

    root = Path(args.root).expanduser().resolve()
    created = 0
    skipped = 0
    matched = 0

    # Find every Solution.java and operate on its parent folder
    for sol_java in root.rglob("Solution.java"):
        folder = sol_java.parent
        matched += 1

        cpp_name = f"{folder.name}.cpp"
        cpp_path = folder / cpp_name

        if cpp_path.exists() and not args.overwrite:
            skipped += 1
            continue

        rel = cpp_path.relative_to(root)
        print(("WOULD WRITE" if args.dry_run else "WRITING") + f": {rel}")

        if not args.dry_run:
            cpp_path.write_text(
                CPP_TEMPLATE.format(filename=cpp_name), encoding="utf-8"
            )
            created += 1

    print(f"\nScanned root: {root}")
    print(f"Problem folders found (Solution.java): {matched}")
    print(f"Created/overwritten: {created}")
    print(f"Skipped (already existed): {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
