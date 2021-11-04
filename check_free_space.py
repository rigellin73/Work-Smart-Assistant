import os
import subprocess

server_conf = "configs/servers.conf"
path_conf= "configs/paths.conf"

def check_space(my_server, my_path):
    cmd = f'ssh {my_server} \'df -hi {my_path}\''
    os.system(cmd)
    #output = subprocess.check_output(['ssh', my_server, f'df -h {my_path}'])
    #print(output)

server_f = open(server_conf, "r")

for server in server_f:
    print(f"Check space in {server}")
    path_f = open(path_conf, "r")
    for path in path_f:
        check_space(server.rstrip('\n'), path.rstrip('\n'))
    path_f.close()
    print()

#output = subprocess.check_output(['программа', 'аргумент 1', '2'])
server_f.close()
