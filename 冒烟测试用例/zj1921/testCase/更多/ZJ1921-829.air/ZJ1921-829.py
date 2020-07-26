# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng:ZJ1921-829 验证地宝清扫过程中，可以复位边刷耗材"

from airtest.core.api import *

__case_theme__ = "ZJ1921-829 验证地宝清扫过程中，可以复位边刷耗材"
"""
## 概要:ZJ1921-829 验证地宝清扫过程中，可以复位边刷耗材  
**描述**:手机和地宝主机已连接

地宝主机正在执行清扫工作  
**前提条件**:1.手机和地宝主机已连接地宝    2.主机正在执行清扫工作  
**步骤ID 1**  
地宝在清扫过程中，打开更多->其他->点击耗材计时  
**期望结果**  
进入更多界面
进入其他页面
打开边刷耗材页面  
**步骤ID** 2  
点击边刷复位耗材按钮  
**期望结果**  
弹出弹框‘确认已更换边刷耗材？’  取消/确认  
**步骤ID** 3  
点击取消按钮  
**期望结果**  
耗材剩余百分比数值未被重置，地宝正常工作  
**步骤ID** 4  
重复步骤2，点击确认按钮  
**期望结果**  
耗材剩余百分比数值被重置为100%，地宝正常工作  
 
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule, Sweep,More,Accessories,Charge
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "829"

auto_setup(__file__) 

log("前提条件：1.手机和地宝主机已连接地宝    2.主机正在执行清扫工作")
"""确保主机正在清扫中"""
if Sweep.get_auto_btn_status() == '清扫':
    logger.debug("主机正在清扫中")
else:
    Sweep.click_auto_btn()

    
log('步骤ID 1**地宝在清扫过程中，打开更多->其他->点击耗材计时')
More.main_to_more()
More.more_to_additional()

'''
**期望结果**  
进入更多界面
进入其他页面
打开边刷耗材页面
'''
Accessories.more_to_accessories()
#获取当前边刷耗材剩余时间
side_residual_time = Accessories.get_remain_time(accessory_name = '边刷')
side_residual_percentage =Accessories.get_remain_percent(accessory_name = '边刷')


log('**步骤ID** 2:点击边刷复位耗材按钮')
Accessories.reset_sidebrush()
sleep(3)

'''
**期望结果**  
弹出弹框‘确认已更换边刷耗材？’  取消/确认  
'''
Accessories.check_reset_sidebrach()

log('**步骤ID** 3点击取消按钮')
Accessories.reset_or_cancel(choose = "取消")

'''
**期望结果**  
耗材剩余百分比数值未被重置，地宝正常工作  
'''
#当前边刷耗材所剩时间
side_time = Accessories.get_remain_time(accessory_name = '边刷')
#当前边刷所剩百分比
side_percentage = Accessories.get_remain_percent(accessory_name = '边刷')
if side_time == side_residual_time and side_percentage == side_residual_percentage:
    logger.debug("边刷耗材未复位")
else:
    raise AssertionError("未复位前所剩时间及百分比：",side_residual_time,side_residual_percentage,"取消复位后时间及百分比：",side_time,side_percentage)

#验证地宝仍正常工作中
Accessories.accessories_to_more()
More.more_to_main()
sleep(5)
if Sweep.get_auto_btn_status() == "清扫":
    logger.debug("主机仍在清扫")
else:
    raise AssertionError("主机未在清扫中")
    
log('**步骤ID** 4:重复步骤2，点击确认按钮')
'''
重读以上操作，选择复位
'''
log('打开更多->其他->点击耗材计时')
More.main_to_more()
More.more_to_additional()

'''
**期望结果**  
进入更多界面
进入其他页面
打开边刷耗材页面
'''
Accessories.more_to_accessories()
#获取当前边刷耗材剩余时间
side_residual_time = Accessories.get_remain_time(accessory_name = '边刷')
side_residual_percentage = Accessories.get_remain_percent(accessory_name = '边刷')


log('点击边刷复位耗材按钮')
Accessories.reset_sidebrush()
sleep(3)

'''
**期望结果**  
弹出弹框‘确认已更换边刷耗材？’  取消/确认  
'''
Accessories.check_reset_sidebrach()

log('点击确定按钮')
Accessories.reset_or_cancel(choose = "确定")

'''
**期望结果**  
耗材剩余百分比数值被重置，地宝正常工作  
'''
side_time = Accessories.get_remain_time(accessory_name = '边刷')
side_percentage = Accessories.get_remain_percent(accessory_name = '边刷')
if side_time == '150' and side_percentage == '100':
    logger.debug("边刷耗材已复位")
else:
    raise AssertionError("边刷耗材未复位成功:",side_time,side_percentage)

#验证地宝仍正常工作中
Accessories.accessories_to_more()
More.more_to_main()
sleep(5)
if Sweep.get_auto_btn_status() == "清扫":
    logger.debug("主机仍在清扫")
else:
    raise AssertionError("主机未在清扫中")


