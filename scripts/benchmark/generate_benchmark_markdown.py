import os
import json

def main():
    diff_path = "pytest_benchmark_diff.json"
    results_dir = os.path.join("benchmarks", "results")
    os.makedirs(results_dir, exist_ok=True)

    # Get repo and branch info from environment variables (for links)
    repo = os.environ.get("GITHUB_REPOSITORY", "unknown/unknown")
    branch = os.environ.get("GITHUB_HEAD_REF") or os.environ.get("GITHUB_REF", "main").replace("refs/heads/", "")

    with open(diff_path, "r", encoding="utf-8") as f:
        diff = json.load(f)

    for submodule, groupDiffs in diff.items():
        # Convert submodule name to submodule file path (e.g., faster_web3.abi -> faster_web3/abi.py)
        submoduleFile = "unknown"
        benchmarkFile = "unknown"
        m = None
        if submodule.startswith("faster_web3."):
            m = submodule[len("faster_web3."):]

        if m:
            submoduleFile = f"faster_web3/{m}.py"
            benchmarkFile = f"benchmarks/test_{m}_benchmarks.py"

        submoduleUrl = f"https://github.com/{repo}/blob/{branch}/{submoduleFile}"
        benchmarkUrl = f"https://github.com/{repo}/blob/{branch}/{benchmarkFile}"

        md_lines = []
        md_lines.append(f"#### [{submodule}]({submoduleUrl}) - [view benchmarks]({benchmarkUrl})\n")
        md_lines.append("| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |")
        md_lines.append("|----------|---------------|-------------|----------|-------------|----------|--------|")

        for group, data in sorted(groupDiffs.items()):
            if data.get("percent_change") is not None:
                emoji = "➖"
                if data["percent_change"] > 0:
                    emoji = "✅"
                elif data["percent_change"] < 0:
                    emoji = "❌"
                percentChange = f"{data['percent_change']:.2f}%" if data.get("percent_change") is not None else ""
                speedupPercent = f"{data['speedup_percent']:.2f}%" if data.get("speedup_percent") is not None else ""
                speedupX = f"{data['speedup_x']:.2f}x" if data.get("speedup_x") is not None and isinstance(data["speedup_x"], (int, float)) else ""
                md_lines.append(
                    f"| `{group}` | {data.get('reference_mean', '')} | {data.get('faster_mean', '')} | {percentChange} | {speedupPercent} | {speedupX} | {emoji} |"
                )
            elif data.get("note"):
                md_lines.append(f"| `{group}` |  |  |  |  |  | ➖ |")

        md_lines.append("")  # Blank line at end
        md_content = "\n".join(md_lines)

        # Write to file
        module_name = submodule.split(".")[-1]
        out_path = os.path.join(results_dir, f"{module_name}.md")
        with open(out_path, "w", encoding="utf-8") as outf:
            outf.write(md_content)

if __name__ == "__main__":
    main()
