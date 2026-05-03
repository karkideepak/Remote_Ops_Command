"""
Server Status Checker Script
----------------------------

This script checks whether a list of servers is online or offline.

Think of it like this:
- You have a list of computers (servers)
- You try to "knock on the door" (connect to them)
- If they respond → they are ONLINE
- If they don’t respond → they are OFFLINE

At the end, the script creates a simple report.
"""

# This module lets us try connecting to servers over a network
import socket

# This module helps us get the current date and time
from datetime import datetime


# --------------------------------------------------
# STEP 1: DEFINE YOUR SERVER LIST
# --------------------------------------------------
# This is where you list all the servers you want to check.
# In real life, this could come from a file or database.

servers = [
    "google.com",      # Example public server (should be online)
    "example.com",     # Another example
    "192.168.1.10",    # Internal server (example)
    "192.168.1.20"     # Internal server (example)
]


# --------------------------------------------------
# STEP 2: CONFIGURATION
# --------------------------------------------------

# PORT:
# This is like a "door" on the server.
# Different services use different ports.
# Port 22 is commonly used for SSH (remote login).
PORT = 22

# TIMEOUT:
# How long we wait (in seconds) before deciding
# the server is not responding.
TIMEOUT = 2


# --------------------------------------------------
# STEP 3: FUNCTION TO CHECK ONE SERVER
# --------------------------------------------------

def check_server(host, port):
    """
    This function tries to connect to ONE server.

    Input:
    - host: the server name or IP address
    - port: the port number (the "door")

    Output:
    - True  → server is online
    - False → server is offline
    """

    try:
        # Try to open a connection to the server
        # If it works, the server is reachable
        with socket.create_connection((host, port), timeout=TIMEOUT):
            return True

    except Exception:
        # If anything goes wrong (timeout, no response, etc.)
        # we assume the server is offline
        return False


# --------------------------------------------------
# STEP 4: CHECK ALL SERVERS
# --------------------------------------------------

def generate_report(server_list):
    """
    This function checks all servers and separates them
    into two groups: ONLINE and OFFLINE.
    """

    online = []   # list to store online servers
    offline = []  # list to store offline servers

    # Loop through each server in the list
    for server in server_list:

        # Check if the server is reachable
        if check_server(server, PORT):
            online.append(server)   # add to online list
        else:
            offline.append(server)  # add to offline list

    return online, offline


# --------------------------------------------------
# STEP 5: SAVE RESULTS TO A FILE
# --------------------------------------------------

def save_report(online, offline):
    """
    This function writes the results into a text file
    so the team can review it later.
    """

    # Get current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Name of the output file
    filename = "server_status_report.txt"

    # Open the file in write mode ("w" means overwrite)
    with open(filename, "w") as file:

        # Write a header
        file.write(f"Server Status Report - {timestamp}\n")
        file.write("=" * 50 + "\n\n")

        # Write online servers
        file.write("ONLINE SERVERS:\n")
        for server in online:
            file.write(f" - {server}\n")

        # Write offline servers
        file.write("\nOFFLINE SERVERS:\n")
        for server in offline:
            file.write(f" - {server}\n")

    print(f"Report saved to {filename}")


# --------------------------------------------------
# STEP 6: MAIN PROGRAM (WHERE EVERYTHING RUNS)
# --------------------------------------------------

if __name__ == "__main__":
    """
    This is the starting point of the script.
    It runs all the steps in order.
    """

    print("Checking server status...\n")

    # Check all servers
    online, offline = generate_report(servers)

    # Show results on screen
    print("Online servers:")
    for s in online:
        print(f" - {s}")

    print("\nOffline servers:")
    for s in offline:
        print(f" - {s}")

    # Save results to a file
    save_report(online, offline)
