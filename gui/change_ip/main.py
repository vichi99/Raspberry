from lib import *


data =  {
        "static ip_address": "static ip_address=192.168.0.100/24"
        }

bash_dhcpcd = [
    "sudo ifconfig wlan0 down",
    "sudo ifconfig wlan0 up",
    "sudo ifconfig eth0 down",
    "sudo ifconfig eth0 up",
    "sudo ifconfig br0 down",
    "sudo ifconfig br0 up",
    ]

dhcpcd = ChangeConf("path to /dhcpcd.conf","bash_password")
dhcpcd.load_data(data)
dhcpcd.load_file()
dhcpcd.save_file()
dhcpcd.bash(bash_dhcpcd)
