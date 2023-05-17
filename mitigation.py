import paramiko

# Define the list of servers with their SSH details
servers = [
    {
        'hostname': 'server1.example.com',
        'port': 22,
        'username': 'your-ssh-username',
        'password': 'your-ssh-password',
    },
    {
        'hostname': 'server2.example.com',
        'port': 22,
        'username': 'your-ssh-username',
        'password': 'your-ssh-password',
    },
    # Add more servers as needed
]

# Define the mitigation command to be executed on each server
command = 'echo -e "\\nlog4j2.formatMsgNoLookups=true\\n" >> log4j2.properties'

# Iterate over each server and execute the mitigation command
for server in servers:
    try:
        # Connect to the server using SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            server['hostname'],
            port=server['port'],
            username=server['username'],
            password=server['password']
        )
        
        # Execute the mitigation command
        stdin, stdout, stderr = ssh_client.exec_command(command)
        
        # Print the output
        print(f"Mitigation command executed on {server['hostname']}:\n{stdout.read().decode()}")
        
        # Close the SSH connection
        ssh_client.close()
        
    except paramiko.AuthenticationException as auth_error:
        print(f"Authentication failed for {server['hostname']}: {str(auth_error)}")
        
    except paramiko.SSHException as ssh_error:
        print(f"SSH connection error for {server['hostname']}: {str(ssh_error)}")
