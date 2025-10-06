"""
parse_benchmark_output.py

Extracts per-function benchmark timings from pytest-benchmark's benchmark.json output.
Parses the JSON file, finds all test function results, and writes a JSON file
mapping modules (e.g., ens/base_ens) to groups and their test functions and results.

Usage:
    python parse_benchmark_output.py <benchmark.json> [output.json]
"""

import json
import sys
import re
from collections import defaultdict
from typing import Dict, Any

def get_module_path(bench: dict) -> str:
    # Extracts the relative module path from the test file path.
    # E.g., benchmarks/ens/test_base_ens_benchmarks.py -> ens/base_ens
    fullname = bench.get("fullname", "")
    m = re.search(r"benchmarks/(.+)/test_([a-zA-Z0-9_]+)_benchmarks\.py", fullname)
    if m:
        subdir = m.group(1)
        base = m.group(2)
        return f"{subdir}/{base}"
    # Try for top-level: benchmarks/test_foo_benchmarks.py -> foo
    m2 = re.search(r"benchmarks/test_([a-zA-Z0-9_]+)_benchmarks\.py", fullname)
    if m2:
        return m2.group(1)
    return "unknown"

def get_group_name(test_name: str) -> str:
    # Extract group from test name, e.g., test_foo, test_faster_foo -> group: foo
    m = re.match(r"test_faster_(.+)", test_name)
    if m:
        return m.group(1)
    m = re.match(r"test_(.+)", test_name)
    if m:
        return m.group(1)
    return test_name

def parse_pytest_benchmark_json(data: dict) -> Dict[str, Dict[str, Dict[str, Any]]]:
    """
    Parses pytest-benchmark's benchmark.json and extracts per-function timings,
    grouped by module path and group name.
    Returns a dict: {module_path: {group: {function_name: {...}}}}
    """
    results = defaultdict(lambda: defaultdict(dict))
    for bench in data.get("benchmarks", []):
        name = bench["name"]
        module_path = get_module_path(bench)
        group = get_group_name(name)
        stats = bench["stats"]
        results[module_path][group][name] = {
            "mean": stats.get("mean"),
            "stddev": stats.get("stddev", None),
            "iqr": stats.get("iqr", None),
            "min": stats.get("min", None),
            "max": stats.get("max", None),
            "rounds": stats.get("rounds", None),
        }
    return results

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python parse_benchmark_output.py <benchmark.json> [output.json]")
        sys.exit(1)
    infile = sys.argv[1]
    outfile = sys.argv[2] if len(sys.argv) > 2 else "benchmark_results.json"
    with open(infile, "r") as f:
        data = json.load(f)
    results = parse_pytest_benchmark_json(data)
    with open(outfile, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Parsed results written to {outfile}")

if __name__ == "__main__":
    main()
