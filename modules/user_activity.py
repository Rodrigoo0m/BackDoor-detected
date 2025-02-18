import psutil

def monitor_user_activity():
    """Monitor user activity for suspicious commands."""
    suspicious_activity = []
    # Example: track all executed commands (Linux only)
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if "bash" in process.info['name']:  # Replace with heuristic for suspicious commands
                suspicious_activity.append(process.info['cmdline'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return suspicious_activity
