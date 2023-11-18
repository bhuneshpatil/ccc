import socket

def dns_lookup(input_value):
    try:
        # Try to interpret the input as an IP address
        ip_address = socket.gethostbyname(input_value)
        print(f"IP Address: {ip_address}")
        
        # If successful, try to get the host name for the IP address
        host_name, _, _ = socket.gethostbyaddr(ip_address)
        print(f"Host Name: {host_name}")
        
    except socket.herror as e:
        # If an error occurs (e.g., invalid input), print an error message
        print(f"Error: {e}")

if __name__ == "__main__":
    user_input = input("Enter an IP address or a host name: ")
    dns_lookup(user_input)
