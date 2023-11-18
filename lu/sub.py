def get_ip_class(ip_address):
    first_octet = int(ip_address.split('.')[0])

    if 1 <= first_octet <= 126:
        return 'Class A'
    elif 128 <= first_octet <= 191:
        return 'Class B'
    elif 192 <= first_octet <= 223:
        return 'Class C'
    elif 224 <= first_octet <= 239:
        return 'Class D (Multicast)'
    elif 240 <= first_octet <= 255:
        return 'Class E (Reserved)'
    else:
        return 'Invalid IP Address'

def ip_to_binary(ip_address):
    binary_parts = [bin(int(part))[2:].zfill(8) for part in ip_address.split('.')]
    return '.'.join(binary_parts)

def calculate_subnet(ip_address, subnet_mask):
    ip_binary_parts = ip_address.split('.')
    subnet_mask_parts = subnet_mask.split('.')

    subnet_parts = [str(int(ip_part, 2) & int(mask_part, 2)) for ip_part, mask_part in zip(ip_binary_parts, subnet_mask_parts)]

    return '.'.join(subnet_parts)

def main():
    # Input IP address
    ip_address = input("Enter the IP address: ")

    # Display IP class
    ip_class = get_ip_class(ip_address)
    print(f"IP Class: {ip_class}")

    # Display IP address in binary
    ip_binary = ip_to_binary(ip_address)
    print(f"IP Address (Binary): {ip_binary}")

    # Input subnet mask
    subnet_mask = input("Enter the subnet mask in dotted-decimal format (e.g., 255.255.255.0): ")

    # Validate subnet mask
    try:
        # Convert subnet mask to binary
        subnet_mask_binary = ip_to_binary(subnet_mask)
        print(f"Subnet Mask (Binary): {subnet_mask_binary}")
    except ValueError:
        print("Invalid subnet mask format. Please use dotted-decimal format.")

if __name__ == "__main__":
    main()
