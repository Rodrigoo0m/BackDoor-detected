from modules import monitor_processes, scan_network, check_persistence, check_integrity, monitor_user_activity, log_detection, send_alert_to_discord

def run_detection():
    # Monitor processes
    suspicious_processes = monitor_processes()
    if suspicious_processes:
        log_detection(f"Suspicious processes detected: {suspicious_processes}")
        send_alert_to_discord(f"Suspicious processes detected: {suspicious_processes}")
    
    # Scan network connections
    suspicious_connections = scan_network()
    if suspicious_connections:
        log_detection(f"Suspicious network connections detected: {suspicious_connections}")
        send_alert_to_discord(f"Suspicious network connections detected: {suspicious_connections}")
    
    # Check for persistence
    persistence_files = check_persistence()
    if persistence_files:
        log_detection(f"Persistence mechanisms found: {persistence_files}")
        send_alert_to_discord(f"Persistence mechanisms found: {persistence_files}")
    
    # Check file integrity
    for file_path in ["/etc/passwd", "/etc/shadow"]:
        result = check_integrity(file_path)
        if result:
            log_detection(result)
            send_alert_to_discord(result)
    
    # Monitor user activity
    suspicious_activity = monitor_user_activity()
    if suspicious_activity:
        log_detection(f"Suspicious user activity detected: {suspicious_activity}")
        send_alert_to_discord(f"Suspicious user activity detected: {suspicious_activity}")

if __name__ == "__main__":
    run_detection()
