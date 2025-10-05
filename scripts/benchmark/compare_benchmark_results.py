"""
compare_benchmark_results.py

Compares the two implementations in each benchmark group from a pytest-benchmark parsed results JSON file,
grouped by submodule.
For each submodule and group (e.g., "abi_to_signature"), finds both implementations
(e.g., "test_abi_to_signature" and "test_faster_abi_to_signature"), computes the percent change
in mean execution time, speedup percent, and x factor, and writes a diff JSON file summarizing the results.

Usage:
    python compare_benchmark_results.py <results.json> [output.json]
"""

import json
import sys
import re
from typing import Any, Dict


def get_group_name(test_name: str) -> str:
    # Extract group from test name, e.g., test_foo, test_faster_foo -> group: foo
    m = re.match(r"test_faster_(.+)", test_name)
    if m:
        return m.group(1)
    m = re.match(r"test_(.+)", test_name)
    if m:
        return m.group(1)
    return test_name


def compare_group(group_results: Dict[str, Any]) -> Dict[str, Any]:
    # Find reference and faster implementations in the group
    ref = None
    fast = None
    ref_name = None
    fast_name = None
    for func_name, data in group_results.items():
        if func_name.startswith("test_faster_"):
            fast = data
            fast_name = func_name
        elif func_name.startswith("test_"):
            ref = data
            ref_name = func_name

    if ref and fast:
        mean_ref = ref["mean"]
        mean_fast = fast["mean"]
        percent_change = (
            ((mean_ref - mean_fast) / mean_ref) * 100 if mean_ref != 0 else 0.0
        )
        speedup_x = mean_ref / mean_fast if mean_fast != 0 else float("inf")
        speedup_percent = (
            (speedup_x - 1) * 100 if speedup_x != float("inf") else float("inf")
        )
        return {
            "reference_mean": mean_ref,
            "faster_mean": mean_fast,
            "percent_change": percent_change,
            "speedup_percent": speedup_percent,
            "speedup_x": speedup_x,
            "reference": ref_name,
            "faster": fast_name,
        }
    else:
        missing = []
        if not ref:
            missing.append("reference")
        if not fast:
            missing.append("faster")
        return {"note": f"Missing implementation(s): {missing}"}


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python compare_benchmark_results.py <results.json> [output.json]")
        sys.exit(1)
    results_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "benchmark_diff.json"

    with open(results_path, "r") as f:
        results = json.load(f)

    # results: {submodule: {group: {function_name: {...}}}}
    diff_by_submodule = {
        submodule: {
            group: compare_group(group_results)
            for group, group_results in groups.items()
        }
        for submodule, groups in results.items()
    }

    with open(output_path, "w") as f:
        json.dump(diff_by_submodule, f, indent=2)
    print(f"Diff written to {output_path}")


if __name__ == "__main__":
    main()
