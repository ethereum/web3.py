"""
parse_benchmark_output.py

Extracts per-function benchmark timings from pytest-benchmark's benchmark.json output.
Parses the JSON file, finds all test function results, and writes a JSON file
mapping submodules (e.g., Python submodules like faster_web3.abi) to groups and their test functions and results.

Usage:
    python parse_benchmark_output.py <benchmark.json> [output.json]
"""

import json
import sys
import re
from collections import defaultdict
from typing import Dict, Any


def get_submodule(bench: dict) -> str:
    # Extract Python submodule from fullname, e.g., "benchmarks/test_abi_benchmarks.py::test_abi_to_signature"
    fullname = bench.get("fullname", "")
    # Try to extract the submodule from the test file path
    m = re.search(r"benchmarks/test_([a-zA-Z0-9_]+)_benchmarks\.py", fullname)
    if m:
        return f"faster_web3.{m.group(1)}"
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
    grouped by submodule and group name.
    Returns a dict: {submodule: {group: {function_name: {...}}}}
    """
    results = defaultdict(lambda: defaultdict(dict))
    for bench in data.get("benchmarks", []):
        name = bench["name"]
        submodule = get_submodule(bench)
        group = get_group_name(name)
        stats = bench["stats"]
        results[submodule][group][name] = {
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
