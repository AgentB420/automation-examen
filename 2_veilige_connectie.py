from sqlite3 import Connection

from netmiko import ConnectHandler
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")
secret = getpass("Secret: ")

switch_ip = ["10.0.0.100",
             "10.0.0.200"]

for ip in switch_ip:
    print(f"Connecting to {ip}")

    switch = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
        "secret": secret
    }
    
    connection = ConnectHandler(**switch)
    connection.enable()
    result = connection.send_command(
        "show running-config | include version")

    print(result)