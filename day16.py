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

sudo("yum install mariadb-server -y")
sudo("systemctl start mariadb")
sudo("systemctl enable mariadb -y")

def web_setup(WEBURL, DIRNAME):
    print("#######################################")
    local("apt install zip unzip -y")

    print("#######################################")
    print("Installing dependencies")
    sudo("yum install httpd wget unzip -y")


    print("#######################################")
    print("Start & enable service")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")

    print("#######################################")
    print("Start & enable service")
    local(("wget -O website.zip %S") %  WEBURL)
    local("unzip -o website.zip")

    with lcd(DIRNAME):
        local("zip -r tooplate.zip *")
        put("tooplate.zip", "/var/www/html", use_sudo=True)

    with cd("/var/www/html/"):
        sudo("unzip -o tooplate.zip")
    
    sudo("systemctl restart httpd")

    print("Website setup is done")















