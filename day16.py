#pip install fabric
#apt install python
#python get-pip.py


#pip install python-jenkins

import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='myuser', password='mypassword')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))


from fabric.api import *

def greeting(msg):
    print("Good %s" % msg)

def system_info():
    print("Disk Space")
    local("df-h")

    print("RAM size")
    local("free -m")

    print("System uptime")
    local("uptime")

def remote_exec():
    print("Get System Info")
    run("hostname")
    run("uptime")
    run("df-h")
    run("free -m")










