import os.path
from os import path

env_content = 'PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"'+'\n'

# method for setting the proxy to environment file in root folder

def set_proxy(proxy,port):

    if path.exists('/etc/environment') and path.exists('/etc/environment.bak'):
        backup_proxy = open('/etc/environment.bak','r+')
        proxy_file = open('/etc/environment','w+')
        proxy_file.write(backup_proxy.read())
        proxy_file = open('/etc/environment','a')

    elif path.exists('/etc/environment') and not path.exists('/etc/environment.bak'):
        backup_proxy = open('/etc/environment.bak','w+')
        temp = open('/etc/environment','r')
        backup_proxy.write(temp.read())
        proxy_file = open('/etc/environment','a+')
    
    else:
        proxy_file = open('/etc/environment','a+')
        backup_proxy = open('/etc/environment.bak','w+')
        proxy_file.write(env_content)
        backup_proxy.write(env_content)
    
    change_proxy = []
    change_proxy.append("http_proxy={0}".format("http://{0}:{1}".format(proxy,port)))
    change_proxy.append("https_proxy={0}".format("http://{0}:{1}".format(proxy,port)))
    change_proxy.append("ftp_proxy={0}".format("http://{0}:{1}".format(proxy,port)))
    change_proxy.append("HTTP_PROXY={0}".format("http://{0}:{1}".format(proxy,port)))
    change_proxy.append("HTTPS_PROXY={0}".format("http://{0}:{1}".format(proxy,port)))
    change_proxy.append("FTP_PROXY={0}".format("http://{0}:{1}".format(proxy,port)))
    change_proxy.append("no_proxy=localhost,127.0.0.0/8,::1,10.0.0.0/8,127.0.0.1/8\n")

    new_proxy = '\n'.join(change_proxy)
    proxy_file.write(new_proxy)
    proxy_file.close()
    backup_proxy.close()
    print('Proxy Set!')
