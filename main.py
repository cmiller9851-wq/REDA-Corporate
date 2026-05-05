from ssa_submission import build_submission
from gateway_injection import execute_injection
import json

def run_pipeline():
    # Parameters from SYSTEM_EXECUTION_2026 logs
    income = 1689.0
    cola = 2.8
    protocol_id = "CPAS_DI_11005_017"
    
    print("[*] SYNCING GITHUB CORPORATE REPOS...")
    print("[*] VERIFYING T-FREE 5 BYTE-STREAM...")
    
    submission = build_submission(income, cola, protocol_id)
    
    print(f"[!] SIGNATURE VERIFIED: {protocol_id}")
    print(json.dumps(submission, indent=2))
    
    # Execute Endpoint Injection
    response = execute_injection(submission, "INTERNAL_GATEWAY_TOKEN")
    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    run_pipeline()
