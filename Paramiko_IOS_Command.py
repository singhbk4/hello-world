import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("10.10.10.1", port=22, username="cisco", password="Cisco", look_for_keys=False, allow_agent=False)

remote_connection = ssh_client.invoke_shell()


remote_connection.send("enable\n")
remote_connection.send("Cisco\n")
remote_connection.send("Config terminal\n")
remote_connection.send("inter loopback 1\n")
remote_connection.send("ip address 1.1.1.1 255.255.255.255\n")
remote_connection.send("router ospf 10\n")
remote_connection.send("network 10.10.10.0 0.0.0.255 area 0\n")
remote_connection.send("network 1.1.1.1 0.0.0.0 area 0\n")
remote_connection.send("end\n")

import time
time.sleep(3)

output = remote_connection.recv(4096)
print(output.decode())





