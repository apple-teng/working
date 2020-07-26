# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-380 验证自定义清扫未画框之前，地图操作"
__case_theme__ = "ZJ1921-380 验证自定义清扫未画框之前，地图操作"
"""
**前提条件**:1.主机地图扫建完成 2.主机状态为待机  
**步骤ID 1**  
左滑，切换到自定义清扫界面  
**期望结果**  
主机充电座上待机；
APP：跳转到自定义清扫设置页面
页面左侧出现“画框”“X1”次数选择按钮，画框按钮无填充色
未选择划框操作时，界面上无提示  
**步骤ID** 2  
单指操作地图  
**期望结果**  
APP：地图根据手势移动  
**步骤ID** 3  
双指操作地图  
**期望结果**  
APP：地图根据手势缩放  
"""

import time,telnetlib
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'E:\airTest\冒烟测试用例\zj1921\base')
from import_package import *
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)
auto_setup(__file__) 
# 执行脚本的前置操作（包括开启app，进入设备列表，进入主界面）
setup()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# MQ准备数据
case_name = "380"

log("前提条件:1.主机地图扫建完成 2.主机状态为待机")
# 确保主机在充电座
Charge.anyhow_go_charge()
Main.click_any_popMsg_on_main()
log("导入地图-只有地图1")
cp_cmd = 'cp -r ' + MAP1_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
app.telnet_to_deboot(cmd)
Main.click_any_popMsg_on_main()
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)
log("步骤一：左滑，切换到自定义清扫界面")
Main.click_custom_to_custom_clean()
# 点掉首次进入的pop消息
Main.click_any_popMsg_on_main()
#**期望结果**  
# 主机充电座上待机；
Charge.check_lighting_icon(expectation='存在')
# APP：跳转到自定义清扫设置页面
# 页面左侧出现“画框”“X1”次数选择按钮，画框按钮无填充色
customAndAreaClean.check_custom_clean_display()
# 未选择划框操作时，界面上无提示
customAndAreaClean.check_custom_clean_area_tips(expection='不存在')

log("步骤二：单指操作地图")
app.one_finger_drage_map()
# **期望结果**  
# APP：地图根据手势移动
## one_finger_drage_map中已截图检查

log("步骤三：双指操作地图")
log("双指操作地图-out")
app.two_fingers_drage_map("out")
log("双指操作地图-in")
app.two_fingers_drage_map("in")
# **期望结果**  
# APP：地图根据手势缩放 
## two_fingers_drage_map中已截图检查
