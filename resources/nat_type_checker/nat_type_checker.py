import socket
import requests
import stun

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json()['ip']
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None

def check_cone_nat():
    try:
        nat_type, external_ip, external_port = stun.get_ip_info()
        public_ip = get_public_ip()

        if public_ip is None:
            print("Could not determine public IP.")
            return

        print(f"Public IP: {public_ip}")
        print(f"STUN server IP: {external_ip}")

        if public_ip == external_ip:
            print("You have a Cone NAT.")
        else:
            print("You do not have a Cone NAT.")
    except Exception as e:
        print(f"Error checking NAT type: {e}")

if __name__ == "__main__":
    check_cone_nat()