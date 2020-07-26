# coding=utf-8
# Author: Cliff Zhang
# __date__='2020/4/24 4:41 下午'
import os,sys,telnetlib,time


# 耗材文件路径
file_path = "/data/save/lifespan.json"

def set_accessories(host = "192.168.1.3",
                    cmd_str = '{"brush":45,"sidebrush":9000,"hepa":235}',
                    file_path = "/data/save/lifespan.json"):
    username = "root"
    password = "eco_rd4!"
    finish = '~ #'
    tn = telnetlib.Telnet(host)
    tn.read_until('deboot login: '.encode("ascii"))
    tn.write(username.encode("ascii") + b'\n')
    time.sleep(1)
    tn.read_until('Password: '.encode("ascii"))
    tn.write(password.encode("ascii") + b'\n')
    time.sleep(1)
    tn.read_until(finish.encode("ascii"))

    # 耗材文件，写入内容
    echo_cmd = "echo '%s'>%s" %(cmd_str,file_path)
    tn.write(echo_cmd.encode("ascii") + b'\n')
    time.sleep(1)
    # 重启机器使其生效
    tn.read_until(finish.encode("ascii"))
    reboot_cmd = "reboot"
    tn.write(reboot_cmd.encode("ascii") + b'\n')
    time.sleep(1)
    tn.close()
set_accessories()