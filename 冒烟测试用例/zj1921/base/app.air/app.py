# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
import time,telnetlib
from airtest.core.api import *
from airtest.core.error import (AdbError, AdbShellError, AirtestError, DeviceConnectionError)
import sys
sys.path.append(r'../')
from import_package import *
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

""" 以下函数，均与操作app 和 telnet相关，
包含app安装/app卸载/app登陆
"""

# 检测是否已经安装app，并重新安装app方法 
def installApp():
    """
        function:
            安装app
            如果当前手机有ecovacs app，就卸载再安装；否则直接安装
        args：
            参数为app包名
            - apk_name：（obj:str)app包名，缺省值为PACKAGE_NAME = 'com.eco.global.app'           
        return:
            none
    """
    dev = device()
    try:
        dev.check_app(PACKAGE_NAME)
    except AirtestError:
        print('no app')
        install(APP_PATH)
        logger.debug("安装app[1]")
        log("安装app[1]")
    else:
        dev.uninstall_app(PACKAGE_NAME)
        logger.debug("uninstall_app")
        log("uninstall_app")
        sleep(1)
        install(APP_PATH)
        logger.debug("安装app[2]")
        log("安装app[2]")
    sleep(2)
    if poco(text='风险提示').exists():
        while True:
            if poco(text='继续安装').exists():                
                poco(text='继续安装').click()
            else:
                break
        
               
def openApp(apk_name=PACKAGE_NAME):    
    """
        function:
            打开app
        args：
            参数为app包名
            - apk_name：（obj:str)app包名，缺省值为PACKAGE_NAME = 'com.eco.global.app'           
        return:
            none
    """
    try:
        start_app(PACKAGE_NAME)
        logger.debug("打开app")
        log("打开app")
    except:
        raise AssertionError("打开app失败")
        
        
def closeApp(apk_name=PACKAGE_NAME):
    """
        function:
            关闭app
        args：
            参数为app包名
            - apk_name：（obj:str)app包名，缺省值为PACKAGE_NAME = 'com.eco.global.app'           
        return:
            none
    """
    try:
        stop_app(PACKAGE_NAME)
        logger.debug("关闭app")
        log("关闭app")
    except:
        raise AssertionError("关闭app失败")


def loginAPP_China(username=CHINA_USER_NAME, passwd=CHINA_PASSWPRD):
    """
        function:
            登陆国家为中国的前提下，使用手机号、密码登陆
        args：
            参数为登陆账号的手机号和密码
            - username：（obj：str）登陆账号的手机号，缺省为CHINA_USER_NAME = '18896719707'
            - passwd：（obj：str）登陆账号的密码，缺省为CHINA_PASSWPRD = '123456'
        return:
            none
    """
    if poco(text='下一步').exists():
        poco(text='下一步').click()
    # 用户协议
    if poco(name='com.eco.global.app:id/checkboxProtocol').exists():
        # 用户协议
        poco(name='com.eco.global.app:id/checkboxProtocol').click()
        sleep(1)
        # 隐私协议
        poco(name='com.eco.global.app:id/checkboxPrivacy').click()
        sleep(1)
        # 下一步
        poco(text='下一步').click()
    # 其他登录方式
    poco(name='com.eco.global.app:id/btn_change_login').click()
    sleep(3)
    # 选择手机号、密码登录
    poco(name='com.eco.global.app:id/method1Btn').click()
    logger.debug("选择手机号、密码登录")
    log('选择手机号、密码登录')
    sleep(2)
    # 请输入手机号
    poco(name='com.eco.global.app:id/edit_account').click()
    text(username,enter=False)
    logger.debug("请输入手机号")
    log('请输入手机号')
    sleep(2)
    # 请输入密码 
    poco(name='com.eco.global.app:id/edit_password').click()
    text(passwd,enter=False)
    logger.debug("请输入密码")
    log('请输入密码')
    sleep(2)
    # 登陆
    poco(name='com.eco.global.app:id/btn_login').click()
    try:
        poco(name='com.eco.global.app:id/actionbar_qr').wait_for_appearance()
        logger.debug("成功登陆，进入主界面")
        log('成功登陆，进入主界面')
    except:
        snapshot(msg='输入完用户名密码后没有进入主界面')
        raise AssertionError("输入完用户名密码后没有进入主界面")
    
def telnet_to_deboot(cmd):
    """
        function:
            telnet到主机，并执行相关命令
            主机命令顺序，比如重启的命令，就放在最后执行
        args：
            cmd:telnet到主机后执行的命令（obj:list）
            
        return:
            none
    """
    sleep_time = 10
    # telnet
    tn = telnetlib.Telnet(HOST)
    try:
        tn.read_until('deboot login: '.encode("ascii"))
        tn.write(USERNAME.encode("ascii") + b'\n')
        logger.debug('deboot login: ' + USERNAME)
        log('deboot login')
        time.sleep(1)
        tn.read_until('Password: '.encode("ascii"))
        tn.write(PASSWORD.encode("ascii") + b'\n')
        logger.debug('Password:' + PASSWORD)
        log('Password:'+ PASSWORD)
        time.sleep(1)
        tn.read_until(FINISH.encode("ascii"))
        logger.debug(FINISH)
        log(FINISH)
        if len(cmd) == 0:
            raise AssertionError("命令列表没有值，请检查")
        else:
            for i in cmd:               
                sleep_time = 5
                 
                logger.debug("命令 %s" % i)
                if "cp -r" in i and "map" in i:
                    logger.debug("进入cp命令处理")
                    sleep_time = 20
                    tn.write('rm -r /data/FILES/'.encode("ascii") + b'\n')
                    time.sleep(2)
                    tn.write(i.encode("ascii") + b'\n')
                elif "reboot" in i:  
                    logger.debug("进入reboot命令处理")
                    sleep_time = 25
                    tn.write(i.encode("ascii") + b'\n')
                    time.sleep(3)
                    # 第一次发送重启命令没有生效
#                     logger.debug(tn.read_until(FINISH.encode("ascii"),5))
                    if FINISH in str(tn.read_until(FINISH.encode("ascii"),8), encoding='utf-8'):
                        logger.debug("第一次发送重启命令没有生效")
                        # 第二次发送重启命令
                        tn.write(i.encode("ascii") + b'\n')
                        logger.debug("第二次发送重启命令")
                else:
                    logger.debug("进入非reboot,cp命令处理")
                    tn.write(i.encode("ascii") + b'\n')                    
                    tn.read_until(FINISH.encode("ascii")) 
                logger.debug("sleep:%d" % sleep_time)                 
                time.sleep(sleep_time) 
#                 logger.debug(i)
#                 log(i)

    # close telnet连接
    finally:
        tn.close()
        logger.debug('close')
        log('close')


def one_finger_drage_map():
    """
        function:
            单指操作拖拽地图
        args：
            none
        return:
    """
    x1, y1 = poco(name='android.widget.RelativeLayout').get_position()
    x2, y2 = x1 + 0.2, y1 + 0.2
    logger.debug("x1,y1: %s, %s" %(x1, y1))
    log("x1,y1: %s, %s" %(x1, y1))
    sleep(2)
    snapshot("拖动前截图.png",msg='拖动前截图')
    poco.swipe((x1, y1),(x2, y2))
    snapshot("拖动后截图.png",msg='拖动后截图')
#     if exists(Template(r"拖动前截图.png"),resolution=(1080, 1920)):
#         raise AssertionError("拖动前后，地图显示没有变化，拖动失败")
#     else:
#         logger.debug("拖动前后，地图显示有变化")
#         log("拖动前后，地图显示有变化") 
    


def two_fingers_drage_map(operation):
    """
        function:
            双指以设备中心为起点，操作缩放地图
        args：
            operation:双指的操作为收缩（in），或外扩（out)
            - in:向内捏合
            - out:向外捏合
        return:
    """
#     x1, y1 = poco(name='android.widget.RelativeLayout').get_position()
#     x2, y2 = x1 + 0.2, y1 + 0.2
#     x3, y3 = x1 -0.2, y1 - 0.2
#     logger.debug("x1,y1: %s, %s" %(x1, y1))
#     log("x1,y1: %s, %s" %(x1, y1))
    # 获取当前设备
    dev = device()
    snapshot("缩放前截图.png",msg='缩放前截图')
    dev.pinch(in_or_out=operation, center=None, percent=0.5)
    snapshot("缩放后截图.png",msg='缩放后截图') 
    
    
    
    
# if __name__ == "__main__":  
if __name__ == "airtest.cli.runner":
   # 替换地图
    cmd_str = '{"dusthepa":300}'   
    file_path = '/data/config/medusa/dustfile.json'
    dusty_cmd = "echo '%s' > %s" %(cmd_str,file_path)                   
    cmd = [dusty_cmd, REBOOT_CMD] 
#     for j in cmd:
#         print(j)
#         print(type(j))
                          
    telnet_to_deboot(cmd)
# #     installApp()
#     loginAPP_China()

 





