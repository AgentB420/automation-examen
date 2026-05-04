from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException
from dotenv import dotenv_values
import os

env = dotenv_values()

switch_ips = [
  "10.0.0.100",
  "10.0.0.200",
]

backup_dir = os.path.join(os.path.dirname(__file__), "configbackups")
os.makedirs(backup_dir, exist_ok=True)

for ip in switch_ips:
  print(f"Connecting to {ip}")

  switches = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": env.get("USERNAME"),
    "password": env.get("PASSWORD"),
    "secret": env.get("SECRET"),
  }

  try:
    connection = ConnectHandler(**switches)
    connection.enable()

    connection.send_command("terminal length 0")

    prompt = connection.find_prompt()
    hostname = prompt.rstrip("#>").strip()
    if not hostname:
      hostname = ip.replace('.', '-')

    running_config = connection.send_command("show running-config")

    filename = f"{hostname}-backup.ios"
    path = os.path.join(backup_dir, filename)
    with open(path, "w") as fh:
      fh.write(running_config)

    print(f"Backup saved to {path}")
  except (NetMikoTimeoutException, NetMikoAuthenticationException) as exc:
    print(f"Fout bij verbinden met {ip}: {exc}")
  finally:
    if "connection" in locals():
      connection.disconnect()
  