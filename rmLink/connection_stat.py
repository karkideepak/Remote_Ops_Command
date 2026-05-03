import subprocess
import platform
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# -------- CONFIG --------
SERVER_LIST_FILE = "servers.txt"   # one hostname/IP per line
MAX_THREADS = 100                  # adjust based on your network
CHECK_PORT = 3389                  # set None to skip port check
TIMEOUT = 2                        # seconds
# -----------------------

def ping(host):
    """Ping a host and return True if reachable."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=TIMEOUT
        )
        return result.returncode == 0
    except:
        return False


def check_port(host, port):
    """Check if a TCP port is open."""
    try:
        with socket.create_connection((host, port), timeout=TIMEOUT):
            return True
    except:
        return False


def check_server(host):
    """Check server status."""
    status = {
        "host": host,
        "ping": False,
        "port_open": None,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    status["ping"] = ping(host)

    if CHECK_PORT and status["ping"]:
        status["port_open"] = check_port(host, CHECK_PORT)

    return status


def main():
    with open(SERVER_LIST_FILE, "r") as f:
        servers = [line.strip() for line in f if line.strip()]

    results = []

    print(f"Checking {len(servers)} servers...")

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        future_to_host = {executor.submit(check_server, host): host for host in servers}

        for future in as_completed(future_to_host):
            result = future.result()
            results.append(result)

            print(f"{result['host']} | Ping: {result['ping']} | Port: {result['port_open']}")

    # Save results
    output_file = f"server_status_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(output_file, "w") as f:
        f.write("host,ping,port_open,timestamp\n")
        for r in results:
            f.write(f"{r['host']},{r['ping']},{r['port_open']},{r['timestamp']}\n")

    print(f"\nResults saved to {output_file}")


if __name__ == "__main__":
    main()
