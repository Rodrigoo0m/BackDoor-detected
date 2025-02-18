import psutil

def scan_network():
    """Scan network connections and look for suspicious activity."""
    suspicious_connections = []
    for conn in psutil.net_connections(kind='inet'):
        try:
            if conn.raddr:
                # Check if raddr is a tuple (ip, port) and access conn.raddr[0] for the IP
                ip = conn.raddr[0] if isinstance(conn.raddr, tuple) else conn.raddr.ip
                if "malicious_ip" in ip:  # Replace with real heuristic
                    suspicious_connections.append(conn)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return suspicious_connections
