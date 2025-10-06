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

    for module_path, groupDiffs in diff.items():
        # module_path is like "ens/base_ens" or "web3/foo"
        # Build output path and ensure subdirectories exist
        out_path = os.path.join(results_dir, f"{module_path}.md")
        out_dir = os.path.dirname(out_path)
        os.makedirs(out_dir, exist_ok=True)

        # Build links to source and benchmark files (best effort)
        # Try to infer package and file names for links
        parts = module_path.split("/")
        if len(parts) >= 2:
            package = parts[0]
            base = parts[1]
            submoduleFile = f"{package}/{base}.py"
            benchmarkFile = f"benchmarks/{package}/test_{base}_benchmarks.py"
        elif len(parts) == 1:
            package = ""
            base = parts[0]
            submoduleFile = f"{base}.py"
            benchmarkFile = f"benchmarks/test_{base}_benchmarks.py"
        else:
            submoduleFile = "unknown"
            benchmarkFile = "unknown"

        submoduleUrl = f"https://github.com/{repo}/blob/{branch}/{submoduleFile}"
        benchmarkUrl = f"https://github.com/{repo}/blob/{branch}/{benchmarkFile}"

        md_lines = []
        # Collapsible section for the whole benchmark table
        md_lines.append(f"<details>")
        md_lines.append(f"<summary>Benchmarks for [{module_path}]({submoduleUrl}) ([view benchmarks]({benchmarkUrl}))</summary>\n")
        md_lines.append("")
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

        md_lines.append("</details>")
        md_lines.append("")  # Blank line at end
        md_content = "\n".join(md_lines)

        # Write to file
        with open(out_path, "w", encoding="utf-8") as outf:
            outf.write(md_content)

if __name__ == "__main__":
    main()
