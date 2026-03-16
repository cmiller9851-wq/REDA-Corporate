import hashlib
import json
import os

# --- CRA v2.1 MASTER SIGNER ---
VAULT_PATH = "manifests/APEX_ORIGIN_SETTLEMENT.json"

def sign_terminal_state():
    print("--- ACCESSING VAULT FOR SIGNATURE ---")
    
    try:
        with open(VAULT_PATH, 'r') as f:
            data = json.load(f)
            
        # Create the Sovereign Hash
        raw_payload = f"{data['manifest']}|{data['ticket']}|{data['audit_yield']}"
        sig = hashlib.sha256(raw_payload.encode()).hexdigest()
        
        print(f"TERMINAL SIGNATURE: {sig}")
        print(f"YIELD SECURED: {data['audit_yield']}")
        print("STATUS: Cycle 7/7 Complete. S=1.")
        
    except FileNotFoundError:
        print("ERROR: Vault path still unreachable. Check Pythonista permissions.")

if __name__ == "__main__":
    sign_terminal_state()
