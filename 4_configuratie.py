from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException
from dotenv import dotenv_values

env = dotenv_values()

switch_ips = [
    "10.0.0.100",
    "10.0.0.200"
]

config_file = "4_configuratie.ios"

for ip in switch_ips:
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": env["USERNAME"],
        "password": env["PASSWORD"],
        "secret": env["SECRET"]
    }

    try:
        connection = ConnectHandler(**device)
        connection.enable()

        print("Configuratie opgeslagen.")

        output = connection.send_config_from_file(config_file)
        print(output)

        connection.save_config()
        print("Configuratie opgeslagen.")
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as exc:
        print(f"Fout bij verbinden met {ip}: {exc}")
    finally:
        if "connection" in locals():
            connection.disconnect()