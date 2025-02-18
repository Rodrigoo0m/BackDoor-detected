import os

def check_persistence():
    """Check for persistence mechanisms like startup items."""
    suspicious_files = []
    
    # Check common persistence locations
    persistence_paths = [
        "/etc/rc.local",  # Linux
        "/etc/init.d/",  # Linux
        "C:\\Windows\\System32\\tasks",  # Windows
        "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"  # Windows
    ]
    
    for path in persistence_paths:
        if os.path.exists(path):
            suspicious_files.append(path)
    return suspicious_files
