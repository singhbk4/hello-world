import paramiko
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect("10.10.10.1", port=22, username="cisco", password="Cisco", look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('sh version')
output = stdout.read().decode()
print(output)

with open("Router_1.txt", "w") as f:
    f.write(output)
