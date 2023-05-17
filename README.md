# Log4j Vulnerability Mitigation Script

This Python script helps mitigate the Log4j vulnerability on multiple servers using SSH.

## Requirements

- Python 3.x
- `paramiko` library (can be installed via `pip install paramiko`)

## Usage

1. Update the `servers` list in the script with the details of the target servers (hostname, port, username, password).
2. Modify the `mitigation_command` variable if needed, based on your log4j mitigation requirements.
3. Run the script using the command `python log4j_mitigation.py`.
4. The script will establish an SSH connection to each server and execute the mitigation command.
5. The output of the execution will be displayed in the console, indicating the status on each server.

**Note:** Ensure you have the necessary permissions and legal rights to perform actions on the target servers.

## Customization

- You can modify the `mitigation_command` variable to match your specific log4j mitigation instructions.
- Adjust the `servers` list to include the SSH details of the target servers.
- Feel free to enhance the script further based on your specific requirements.

## Disclaimer

Use this script responsibly and ensure you comply with all legal and ethical guidelines. The script is provided as-is, without any warranties or guarantees.

## License
NA

