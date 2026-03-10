import logging

audit_logger = logging.getLogger("audit")

def log_audit(action: str, user: str, details: str = ""):
    audit_logger.info(
        f"User={user} | Action={action} | Details={details}"
    )
