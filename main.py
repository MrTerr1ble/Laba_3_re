import re
def check_ip(ip):
    pattern = re.compile(r"^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$")

    if not pattern.match(ip):
        print(f"The IP address {ip} is not valid")
        return False

    bytes = ip.split(".")

    for ip_byte in bytes:
        if int(ip_byte) < 0 or int(ip_byte) > 255:
            print(f"The IP address {ip} is not valid")
            return False
    print(f"The IP address {ip} is valid")
    return True

def main():
    while True:
        print("Enter an IP address: ", end='')
        user_answer = input()
        if user_answer == "stop":
            exit(0)
        print(check_ip(user_answer))

if __name__ == "__main__":
    main()
