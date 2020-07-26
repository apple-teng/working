# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng:ZJ1921-1220 验证更多中地毯增压界面显示，默认“开启”"

__case_theme__ = "ZJ1921-1220 验证更多中地毯增压界面显示，默认“开启”"
"""
**描述**:首次配网成功后，进入更多界面  
**前提条件**:首次配网成功后，进入更多界面  
**步骤ID 1**  
与主机完成配网后，进入更多--工作设置界面  
**期望结果**  
"地毯增压"功能右侧字段为"开启"  
**步骤ID** 2  
进入"地毯增压"查看页面显示  
**期望结果**  
界面显示：
“返回” 地毯增压
地毯增压 开关（默认绿色开启）
开启后，在清扫模式下，地宝识别到地毯时将自动开启强劲吸力

下方有相应说明：
1.请在非地毯区域启动清扫

2.滚刷缠绕毛发时可能在非地毯界面误启动强吸力模式，请及时清理滚刷  
**步骤ID** 3  
点击“返回”按钮  
**期望结果**  
返回更多-工作设置页面，地毯增压默认“开启”状态  
 
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule, Sweep, Main, More,carpet_func
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "1467"

auto_setup(__file__) 

log("前提条件:首次配网成功后，进入更多界面")

log('步骤ID1:与主机完成配网后，进入更多--工作设置界面')
More.main_to_more()

'''
**期望结果**  
"地毯增压"功能右侧字段为"开启"
'''
if carpet_func.carpet_close_or_open() == "开启":
    carpet_func.more_to_carpet_func()
    if carpet_func.get_status_of_carpet_func() == "开启":
        logger.debug("地毯增压默认显示开启")
    else:
        raise AssertionError("地毯增压界面开关显示错误")
else:
    raise AssertionError("地毯增压默认显示有误")


log('**步骤ID** 2:进入"地毯增压"查看页面显示')
'''
**期望结果**  
界面显示：
“返回” 地毯增压
地毯增压 开关（默认绿色开启）
开启后，在清扫模式下，地宝识别到地毯时将自动开启强劲吸力
下方有相应说明：
1.请在非地毯区域启动清扫
2.滚刷缠绕毛发时可能在非地毯界面误启动强吸力模式，请及时清理滚刷  
'''
carpet_func.check_carpet_func_introduce1()
carpet_func.check_carpet_func_introduce2()

log('**步骤ID** 3点击“返回”按钮')
carpet_func.carpet_func_to_more()
'''
**期望结果**  
返回更多-工作设置页面，地毯增压默认“开启”状态
'''
if carpet_func.carpet_close_or_open() == "开启":
    logger.debug("地毯增压默认显示开启")
else:
    raise AssertionError("地毯增压默认显示有误")