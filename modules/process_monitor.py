import psutil

def monitor_processes():
    """Monitor processes and look for suspicious ones."""
    suspicious_processes = []
    for process in psutil.process_iter(['pid', 'name', 'exe', 'status']):
        try:
            # Check if 'exe' is not None before checking for suspicious patterns
            if process.info['exe'] and "malicious" in process.info['exe']:  # Replace with real heuristic
                suspicious_processes.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return suspicious_processes
