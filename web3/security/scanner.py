
import subprocess
import json
import os
from web3 import Web3

class SecurityScanner:
    def __init__(self, rpc_url=None):
        if rpc_url:
            self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        else:
            self.web3 = None

    def is_slither_installed(self):
        try:
            subprocess.run(["slither", "--version"], capture_output=True, check=True)
            return True
        except FileNotFoundError:
            return False

    def analyze_contract_file(self, contract_path):
        if not self.is_slither_installed():
            return "❌ Slither is not installed. Install it using `pip install slither-analyzer`"

        if not os.path.exists(contract_path):
            return "❌ Contract file not found!"

        try:
            subprocess.run(["slither", contract_path, "--json", "report.json"], check=True)
            with open("report.json", "r") as file:
                report = json.load(file)

            issues = report.get("results", {}).get("detectors", [])
            if not issues:
                return "✅ No vulnerabilities found!"

            report_summary = "\n🔍 **Security Report**\n"
            for issue in issues:
                report_summary += f"\n🚨 {issue['check']} \n📌 {issue['description']}\n"

            return report_summary

        except subprocess.CalledProcessError:
            return "❌ Error running Slither analysis!"

    def analyze_deployed_contract(self, contract_address):
        if not self.web3:
            return "❌ Web3 provider not initialized!"

        bytecode = self.web3.eth.get_code(contract_address).hex()
        if bytecode == "0x":
            return "❌ Invalid contract address!"

        return f"🔍 Retrieved bytecode for {contract_address}. Security analysis pending integration."

if __name__ == "__main__":
    scanner = SecurityScanner(rpc_url="https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY")
    print(scanner.analyze_contract_file("example_contract.sol"))
    print(scanner.analyze_deployed_contract("0xDeployedContractAddress"))
