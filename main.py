from SshToServer import SshToServer


def executeProgram(ssh_obj: SshToServer, file_name: str, timeout_value: int) -> str:
    stdout, stderr = ssh_obj.runRemoteCommand(f"./bash_final.sh {file_name} {timeout_value}")
    return stdout


key_pair = input("Input key-pair path: ")
public_ip = input("Input public ip: ")
user_name = input("Input user name: ")
server_side_script_path = input("Input path of server script (from ~): ")

my_ssh = SshToServer(key_pair, public_ip, user_name)

file = input("Please enter the name of the file: ")
timeout = input("How many seconds to wait? ")

result = executeProgram(my_ssh, file, timeout)
print(result)
