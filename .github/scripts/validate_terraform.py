import re
import subprocess
from pathlib import Path


root = Path(__file__).resolve().parents[2]
directories = sorted(
    path.parent for folder in ("examples", "modules")
    for path in (root / folder).glob("*/main.tf")
)
if not directories:
    raise SystemExit("No Terraform learning configurations found.")
failures = []
for directory in directories:
    relative = directory.relative_to(root)
    test_files = sorted((directory / "tests").glob("*.tftest.hcl"))
    if not test_files:
        raise SystemExit(f"Missing plan-only tests: {relative}")
    for test_file in test_files:
        text = test_file.read_text(encoding="utf-8")
        runs = len(re.findall(r'^run\s+"[^"]+"\s*\{', text, re.MULTILINE))
        plans = len(re.findall(r"^\s*command\s*=\s*plan\s*$", text, re.MULTILINE))
        if not runs or runs != plans:
            raise SystemExit(f"Every test run must explicitly use command = plan: {test_file}")
        if "azurerm" in (directory / "main.tf").read_text(encoding="utf-8"):
            if not re.search(r'^mock_provider\s+"azurerm"', text, re.MULTILINE):
                raise SystemExit(f"Azure tests must mock the provider: {test_file}")
    for arguments in (
        ["init", "-backend=false", "-input=false", "-lockfile=readonly"],
        ["validate", "-no-color"],
        ["test", "-no-color"],
    ):
        command = ["terraform", f"-chdir={directory}", *arguments]
        print(f"Running {' '.join(command)}", flush=True)
        result = subprocess.run(command, cwd=root, timeout=300)
        if result.returncode:
            failures.append(f"{relative}: {arguments[0]}")
            break
if failures:
    raise SystemExit("\n".join(failures))
print(f"Verified {len(directories)} configurations with plan-only tests; no Azure deployment performed.")
