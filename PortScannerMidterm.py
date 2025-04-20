import socket
import sys

def scan_ports(target, start_port, end_port):
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                msg = f"[+] Port {port} is OPEN"
                print(msg)
                with open("scan_results.txt", "a") as f:
                    f.write(msg + "\n")
            sock.close()

        except KeyboardInterrupt:
            print("\n[!] Scan interrupted.")
            sys.exit()
        except socket.gaierror:
            print("[!] Hostname could not be resolved.")
            sys.exit()
        except socket.error:
            print("[!] Couldn't connect to server.")
            sys.exit()
    
    print("\n[✓] Scan complete.\nResults saved to 'scan_results.txt'.")

if __name__ == "__main__":
    # Test 1: Common ports on localhost
    scan_ports("127.0.0.1", 20, 100)

    # Test 2: Custom range
    scan_ports("127.0.0.1", 3000, 3010)

    # Test 3: scanme.nmap.org
    scan_ports("scanme.nmap.org", 20, 100)

    # Test 4: Invalid port
    scan_ports("127.0.0.1", -1, 80)

    # Test 5: Invalid host
    scan_ports("nohost.exists", 20, 80)

