# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng:ZJ1921-904 验证修改起始时间相同的勿扰模式"
__case_theme__ = "ZJ1921-904 验证修改起始时间相同的勿扰模式"
"""
## 概要:ZJ1921-904 验证修改起始时间相同的勿扰模式  
**描述**:主机配网成功，充电座待机，勿扰已开启  
**前提条件**:主机配网成功，充电座待机，勿扰已开启  
**步骤ID 1**  
在更多-工作设置界面上，选择勿扰模式  
**期望结果**  
进入勿扰模式页面，显示勿扰模式设置时间  
**步骤ID** 2  
修改勿扰模式禁用时间设定为开始与结束一致  
**期望结果**  
弹出提示，提示内容

“时间设定无效，请重新设定
知道了”  
**步骤ID** 3  
点击“知道了”  
**期望结果**  
弹框消失，APP停留在勿扰模式设置界面  
  
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule, Sweep,Main, More,disturb 
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "904"

auto_setup(__file__) 

log("前提条件:主机配网成功，充电座待机，勿扰已开启")
# 进入更多界面开启勿扰
More.main_to_more()

log('**步骤ID 1**:在更多-工作设置界面上，选择勿扰模式')
disturb.more_to_disturb()

'''
**期望结果**  
进入勿扰模式页面，显示勿扰模式设置时间
'''
disturb.change_disturb(switch = "开启")

log('**步骤ID** 2:修改勿扰模式禁用时间设定为开始与结束一致')
disturb.set_distrub_time(start_time="10:00", end_time="10:00")

'''
**期望结果**  
弹出提示，提示内容
“时间设定无效，请重新设定
知道了” 
'''
disturb.check_sametime_prompt()

log('**步骤ID** 3:点击“知道了”')
disturb.click_know()

"""
**期望结果**  
弹框消失，APP停留在勿扰模式设置界面  
  
"""





