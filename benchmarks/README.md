# Benchmarks for faster-web3

This directory contains a comprehensive suite of benchmarks for both user-facing and internal APIs in `faster_web3`, designed for contributors and maintainers to:

- Compare performance between `web3.py` (reference) and `faster_web3` (optimized, C-accelerated)
- Catch regressions and measure improvements in core utilities, datastructures, and helpers
- Benchmark internals and helpers for advanced optimization

## Benchmark Files

- `test_datastructures_benchmarks.py`: Compares performance of key datastructures between `web3.py` and `faster_web3`.
- `_utils/test_*.py`: Benchmarks internal utility modules, always in pairs: one for the reference implementation (`web3._utils`) and one for the optimized version (`faster_web3._utils`).
- Additional files may benchmark other modules or helpers as needed.

## Running Benchmarks

Install all dev dependencies:

```
pip install .[dev]
```

Run all benchmarks with pytest-codspeed or pytest-benchmark:

```
pytest benchmarks/ --benchmark-only
pytest benchmarks/ --codspeed
```

## Contributing

- Add new benchmarks for any new public API or internal helper that could impact performance.
- Always provide paired benchmarks: one for the reference (`web3._utils.*`) and one for the optimized (`faster_web3._utils.*`) implementation, using the `test_xxx` (reference) and `test_faster_xxx` (optimized) naming pattern for easy comparison.
- If the reference implementation does not exist, include the paired structure and skip the reference test with a clear reason.
- Keep parameterizations broad to catch edge cases and stress-test the implementation.
- Do not benchmark error/exception cases—focus on valid, meaningful inputs and real computation.
