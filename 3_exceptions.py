from  netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException
from dotenv import dotenv_values

env = dotenv_values()

switch_ips = [
    "10.0.0.100",
    "10.0.0.200"
]

for ip in switch_ips:
  print(f"Connecting to {ip}") 

  switch = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": env["USERNAME"],
    "password": env["PASSWORD"],
    "secret": env["SECRET"]
    }
  
  try:
    connection = ConnectHandler(**switch)
    connection.enable()
    result = connection.send_command(
      "show running-config | include version")
    print(result)

  except NetMikoTimeoutException:
    print(f"{switch['host']} is niet bereikbaar")
    