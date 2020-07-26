# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng:ZJ1921-821 验证查看耗材计时页面"

from airtest.core.api import *
__case_theme__ = "ZJ1921-821 验证查看耗材计时页面"
"""
## 概要:ZJ1921-821 验证查看耗材计时页面  
**描述**:手机和地宝主机已连接  
**前提条件**:手机和地宝主机已连接  
**步骤ID 1**  
主界面点击更多-其他-耗材计时  
**期望结果**  
打开耗材计时页面，页面显示边刷，滚刷，滤芯状态，购买耗材，参照UI

购买耗材button在下方常驻  
**步骤ID** 2  
查看边刷  
**期望结果**  
耗材剩余百分比不同，进度条颜色不一样

6%-100%为蓝色进度条，0%-5%为红色进度条并有“告警”提示字样

进度条下方显示剩余小时数  
**步骤ID** 3  
查看滚刷  
**期望结果**  
耗材剩余百分比不同， 进度条颜色不一样
6%-100%为蓝色进度条，0%-5%为红色进度条并有“告警”提示字样
进度条下方显示剩余小时数  
**步骤ID** 4  
查看滤芯  
**期望结果**  
耗材剩余百分比不同，进度条颜色不一样
6%-100%为蓝色进度条，0%-5%为红色进度条并有“告警”提示字样
进度条下方显示剩余小时数  
**步骤ID** 5  
点击购买耗材  
**期望结果**  
APP跳转至购买商场，当前型号的耗材在购买列表的最上方  
**步骤ID** 6  
在耗材计时页面，点击左上角返回按钮  
**期望结果**  
返回至更多-其他页面  
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule, Main, More,Accessories
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "821"

auto_setup(__file__) 

log("**前提条件**:手机和地宝主机已连接")
  
log('**步骤ID 1**:主界面点击更多-其他-耗材计时')
More.main_to_more()
More.more_to_additional()

'''
**期望结果**  
打开耗材计时页面，页面显示边刷，滚刷，滤芯状态，购买耗材，参照UI
购买耗材button在下方常驻
'''
Accessories.check_accessories_exists(accessory_name = '边刷')
Accessories.check_accessories_percent_exists(accessory_name = '边刷')
Accessories.check_accessories_remain_exists(accessory_name = '边刷')
Accessories.check_accessories_exists(accessory_name = '滚刷')
Accessories.check_accessories_percent_exists(accessory_name = '滚刷')
Accessories.check_accessories_remain_exists(accessory_name = '滚刷')
Accessories.check_accessories_exists(accessory_name = '滤芯')
Accessories.check_accessories_percent_exists(accessory_name = '滤芯')
Accessories.check_accessories_remain_exists(accessory_name = '滤芯')
if Accessories.check_buy_acc()  == "存在":
    logger.debug("购买耗材显示正确")
else:
    raise AssertionError("app未显示购买耗材按钮")

log('**步骤ID** 2:查看边刷')

'''
**期望结果**  
耗材剩余百分比不同，进度条颜色不一样
6%-100%为蓝色进度条，0%-5%为红色进度条并有“告警”提示字样
进度条下方显示剩余小时数
'''




**步骤ID** 3  
查看滚刷  
**期望结果**  
耗材剩余百分比不同， 进度条颜色不一样
6%-100%为蓝色进度条，0%-5%为红色进度条并有“告警”提示字样
进度条下方显示剩余小时数  
**步骤ID** 4  
查看滤芯  
**期望结果**  
耗材剩余百分比不同，进度条颜色不一样
6%-100%为蓝色进度条，0%-5%为红色进度条并有“告警”提示字样
进度条下方显示剩余小时数  
**步骤ID** 5  
点击购买耗材  
**期望结果**  
APP跳转至购买商场，当前型号的耗材在购买列表的最上方  
**步骤ID** 6  
在耗材计时页面，点击左上角返回按钮  
**期望结果**  
返回至更多-其他页面  


