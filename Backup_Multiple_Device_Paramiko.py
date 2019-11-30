import myparamiko
import getpass

username = input('Please enter username: ')
password = getpass.getpass()
devices = ['10.10.10.1', '10.10.10.2', '10.10.10.3']
for device in devices:
    ssh_client = myparamiko.connect(device, 22, username, password)
    remote_connection = myparamiko.get_shell(ssh_client)
    myparamiko.send_command(remote_connection, 'enable')
    myparamiko.send_command(remote_connection, username)
    myparamiko.send_command(remote_connection, 'terminal length 0')
    output = myparamiko.send_command(remote_connection, 'show run')

    # Config decode bytes to text
    output_srt = output.decode()
    # output split
    backup = output_srt.split('\n')
    # output convert to list
    backup = backup[4:-1]
    # output join
    config = '\n'.join(backup)
    #print(config)

    import datetime
    now = datetime.datetime.now()
    today = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    file = device + '-' + today + '.txt'
    with open(file, 'w') as f:
        print('Saving configuration of ' + device)
        f.write(config)
        print('Ok')
    myparamiko.close(ssh_client)
