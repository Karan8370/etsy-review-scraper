thonpython
from datetime import datetime

def normalize_date(date_str: str) -> str:
    try:
        return str(datetime.strptime(date_str, "%Y-%m-%d").date())
    except ValueError:
        try:
            return str(datetime.fromisoformat(date_str).date())
        except Exception:
            return str(datetime.utcnow().date())