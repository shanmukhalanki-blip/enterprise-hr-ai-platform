from datetime import datetime

def extract_dates(message: str):
    """
    Expects format: from YYYY-MM-DD to YYYY-MM-DD
    Example: Apply leave from 2026-01-20 to 2026-01-22
    """
    try:
        parts = message.lower().split("from")[1].split("to")
        start = datetime.strptime(parts[0].strip(), "%Y-%m-%d").date()
        end = datetime.strptime(parts[1].strip(), "%Y-%m-%d").date()
        return start, end
    except Exception:
        return None, None
