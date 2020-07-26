# airtest 必须的引用文件
from airtest.core.api import *

# poco 必须的引用文件
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco import exceptions
# 图像识别文件cv2
# 如果出现'cv2.cv2' has no attribute 'xfeatures2d'的报错，执行下面的命令
# pip install opencv_python==3.4.2.16 
# pip install opencv-contrib-python==3.4.2.16
import cv2, sys

# log输出等级为：error
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

# 标记公共字段
basepath = r'E:\airTest\冒烟测试用例\zj1921\base'

# 常量
######################******安装app相关常量********####################
## ecovacsHome包名
global PACKAGE_NAME
PACKAGE_NAME = 'com.eco.global.app'

global APP_PATH
APP_PATH = '/tmp/udisk-sda1/app/20200703211150878.apk'

global CHINA_USER_NAME
CHINA_USER_NAME = '18896719707'

global CHINA_PASSWPRD
CHINA_PASSWPRD = '123456'

global GLOBAL_USER_NAME
GLOBAL_USER_NAME = 'xiaomei.teng@ecovacs.com'

global GLOBAL_PASSWPRD
GLOBAL_PASSWPRD = '123456'

######################******telnet相关常量********####################
## telnet的主机地址
global HOST
HOST = "192.168.13.47"
## telnet登录主机的用户名
global USERNAME
USERNAME = "root"
## telnet登录主机的密码
global PASSWORD
PASSWORD = "eco_rd4!"
## telent进入主机的命令结束符finish
FINISH = '~ #'
## 重启主机的命令
global REBOOT_CMD
REBOOT_CMD = 'reboot -f'

######################******导入地图目录********####################
## telnet要传输的地图的文件路径
global SOURCE_MAP_PATH
SOURCE_MAP_PATH = '/tmp/udisk-sda1/map'
global DESTINATION_MAP_PATH
DESTINATION_MAP_PATH = ' /data/'

## 主机有3张图，当前在新环境地图上
global NEW_MAP1_MAP2_PATH
NEW_MAP1_MAP2_PATH = SOURCE_MAP_PATH + '/new_map1_map2' + '/FILES/'

## 主机有3张图，当前在地图1上
global MAP1_NEW_MAP2_PATH
MAP1_NEW_MAP2_PATH = SOURCE_MAP_PATH + '/map1_new_map2' + '/FILES/'

## 主机有3张图，当前在地图2上
global MAP2_NEW_MAP1_PATH
MAP2_NEW_MAP1_PATH = SOURCE_MAP_PATH + '/map2_new_map1' + '/FILES/'

## 主机有1张图，当前在新环境地图上
global NEW_PATH
NEW_PATH = SOURCE_MAP_PATH + '/new' + '/FILES/'

## 主机有1张图，当前在地图1上
global MAP1_PATH
MAP1_PATH = SOURCE_MAP_PATH + '/map1' + '/FILES/'

## 主机有1张图，当前在地图2上
global MAP2_PATH
MAP2_PATH = SOURCE_MAP_PATH + '/map2' + '/FILES/'

## 主机有2张图(地图1和新环境地图)，当前在新环境地图上
global NEW_MAP1_PATH
NEW_MAP1_PATH = SOURCE_MAP_PATH + '/new_map1' + '/FILES/'

## 主机有2张图(地图1和地图2)，当前在地图1上
global MAP1_MAP2_PATH
MAP1_MAP2_PATH = SOURCE_MAP_PATH + '/map1_map2' + '/FILES/'

## 主机无图
global NO_MAP_PATH
NO_MAP_PATH = SOURCE_MAP_PATH + '/no_map' + '/FILES/'

# MQ相关信息
global machine_name
machine_name = 'A3楼'
global case_name
case_name = "602"
global queuename
queuename = "E0001234518250530010"
# 传递的内容字典格式(json)
global body
body = {
"timestamp":int(time.time()),
"project":"zj1921",
"caseName":case_name,
"sn":queuename,
"action":"start",
"workFromCharger":False,
"workType":"sweep",
"sweepMode":"auto",
"advanceMode":True
}

# import yaml,sys
# # 导入yaml配置文件
# with open(r'E:\airTest\冒烟测试用例\zj1921\common.yaml','r', encoding='utf-8') as f: 
    # comm = yaml.load(f.read())

# basepath = comm['basepath']
# global body
# body = comm['body_text']

# 引入基础模块，需要使用的模块，直接import
sys.path.append(os.path.join(basepath,'UniversalModule.air'))
using('UniversalModule.air')
import UniversalModule

sys.path.append(os.path.join(basepath,'Main.air'))
using('Main.air')
import Main

sys.path.append(os.path.join(basepath,'Sweep.air'))
using('Sweep.air')
import Sweep

sys.path.append(os.path.join(basepath,'Charge.air'))
using('Charge.air')
import Charge

sys.path.append(os.path.join(basepath,'More.air'))
using('More.air')
import More

sys.path.append(os.path.join(basepath,'MoreResetMaps.air'))
using('MoreResetMaps.air')
import MoreResetMaps

sys.path.append(os.path.join(basepath,'Accessories.air'))
using('Accessories.air')
import Accessories

sys.path.append(os.path.join(basepath,'break_point.air'))
using('break_point.air')
import break_point

sys.path.append(os.path.join(basepath,'carpet_func.air'))
using('carpet_func.air')
import carpet_func

sys.path.append(os.path.join(basepath,'CheckStatus.air'))
using('CheckStatus.air')
import CheckStatus

sys.path.append(os.path.join(basepath,'disturb.air'))
using('disturb.air')
import disturb

sys.path.append(os.path.join(basepath,'findDeebot.air'))
using('findDeebot.air')
import findDeebot

sys.path.append(os.path.join(basepath,'MoreChangeMopCloth.air'))
using('MoreChangeMopCloth.air')
import MoreChangeMopCloth

sys.path.append(os.path.join(basepath,'MoreResetMaps.air'))
using('MoreResetMaps.air')
import MoreResetMaps

sys.path.append(os.path.join(basepath,'MoreSuction.air'))
using('MoreSuction.air')
import MoreSuction

sys.path.append(os.path.join(basepath,'regulate_water_flow.air'))
using('regulate_water_flow.air')
import regulate_water_flow

sys.path.append(os.path.join(basepath,'rename.air'))
using('rename.air')
# import rename

sys.path.append(os.path.join(basepath,'SweepCard.air'))
using('SweepCard.air')
import SweepCard

sys.path.append(os.path.join(basepath,'mapmgr.air'))
using('mapmgr.air')
import mapmgr

sys.path.append(os.path.join(basepath,'WorkingAppointment.air'))
using('WorkingAppointment.air')
import WorkingAppointment as Appoint

sys.path.append(os.path.join(basepath,'cleaningLog.air'))
using('cleaningLog.air')
import cleaningLog 

sys.path.append(os.path.join(basepath,'app.air'))
using('app.air')
import app

sys.path.append(os.path.join(basepath,'virtualWall.air'))
using('virtualWall.air')
import virtualWall

"""
正确顺序：
先连接设备（auto_setup）--> 打开应用app（start_app）--> 等应用开启完毕，初始化poco
不然，可能出现错误：远程主机强迫关闭了一个现有连接，或 socket connection broken
"""
def setup():
	# 打开app			
    try:
        stop_app(PACKAGE_NAME)
        sleep(2)
        log("打开ecovacsHome app")
        start_app(PACKAGE_NAME)
        sleep(3)
        # poco 初始化要放在start_app（打开app）之后
        # poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)          
    except Exception as e:
        raise AssertionError("app打开失败")
        
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
	# 从设备列表进入主界面		
    Main.deviceslist_to_main_using_first_device()
    Main.click_any_popMsg_on_main()
	
	
def teardown():
    stop_app(PACKAGE_NAME)
    sleep(3)			

	
# 检测是否已经安装app，并重新安装app方法 
def installapp():
    dev = device()
    try:
        # 因为check_app（）成功返回true，失败抛出异常，所以在检测没有的情况下，需要捕获异常，直接安装
        dev.check_app(PACKAGE_NAME)
        dev.uninstall_app(PACKAGE_NAME)
    except Exception as e:
        logger.debug(e)
        install(APP_PATH)
        logger.debug("安装app")
        log("安装app")
