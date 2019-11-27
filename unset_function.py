import os.path
from os import path


#method for unsetting the proxy

def unset_proxy():
    if not path.exists('/etc/environment') or not path.exists('/etc/environment.bak'):
        print('ERROR: Backup file not present')
        return
    proxy_file = open('/etc/environment','w')
    backup_proxy = open('/etc/environment.bak','r')
    backup_proxy_content = backup_proxy.read()
    proxy_file.write(backup_proxy_content)
    proxy_file.close()
    backup_proxy.close()
    print('Proxy Unset!')