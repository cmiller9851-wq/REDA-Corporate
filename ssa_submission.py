import time

def build_submission(income, cola, esign_protocol):
    # SGA Compliance: 1689.0 < 1690.0
    sga_threshold = 1690.0
    status = "FINAL_SUBMISSION" if income < sga_threshold else "MANUAL_REVIEW"
    
    manifest = {
        "form": "SSA-16-BK",
        "status": status,
        "logic_parameters": {
            "monthly_income": float(income),
            "cola_adjustment": float(cola),
            "esign_protocol": esign_protocol
        }
    }
    
    from ledger_engine import get_canonical_hash
    manifest["signature_hash"] = get_canonical_hash(manifest)
    return manifest
