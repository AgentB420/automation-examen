from netmiko import ConnectHandler

switch_ip = ["10.0.0.100", "10.0.0.200"]

for ip in switch_ip:
    print(f"Connecting to {ip}")

    sw_acc_1 = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "admin",
        "password": "cisco",
        "secret": "cisco"
}

connection = ConnectHandler(**sw_acc_1)
connection.enable()
result = connection.send_command(
    "show running-config | include Version"
    )

print(result)