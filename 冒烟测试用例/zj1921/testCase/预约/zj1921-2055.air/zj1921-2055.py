# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
__case_theme__ = "ZJ1921-2055 验证有残图时，无法新增区域预约"
""" 
**描述**:主机配网成功，有一个残图
未开启多层地图  
**前提条件**:主机配网成功，有一个残图
未开启多层地图  
**步骤ID 1**  
主机有残图时，点击更多-清扫预约  
**期望结果**  
进入清扫预约页面  
**步骤ID** 2  
点击新增按钮  
**期望结果**  
出现预约自动清扫和预约区域清扫两个选项，其中区域清扫可以点击  
**步骤ID** 3  
点击预约区域清扫，  
**期望结果**  
页面显示“暂未生成区域地图，请先建立完整家具环境地图” 
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
case_name = "2055"

log("前提条件:主机配网成功，有一个残图")
# 确保主机在充电座
try:
    Charge.check_lighting_icon(expectation='存在')
    logger.debug("主机在充电座")
except:
    logger.debug("主机当前不在充电座，使其回充")
    Charge.anyhow_standby_out_of_charger()
# 确保主机无图
log("导入地图-无图")
cp_cmd = 'cp -r ' + NO_MAP_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
app.telnet_to_deboot(cmd)
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)

# 使主机出发清扫3min,构造残图
Sweep.click_auto_btn()
Main.click_any_popMsg_on_main()
sleep(180)
# 结束自动清扫
Sweep.click_rightstop()
Sweep.click_stop_clean()
# 扫建中结束清扫的处理
Sweep.click_pop_windows_while_stop_building_map()


log("步骤一：主机有残图时，点击更多-清扫预约")
More.main_to_more()
Appoint.more_to_working_appointment()
# **期望结果**  
# 进入清扫预约页面
## 步骤一已包含

log("步骤二：点击新增按钮")
Appoint.click_add_appointment()
# **期望结果**  
# 出现预约自动清扫和预约区域清扫两个选项，其中区域清扫可以点击
Appoint.check_type_of_adding_appointment()

log("步骤三：点击预约区域清扫")
Appoint.click_adding_appointment_type('area')
# **期望结果**  
# 页面显示“暂未生成区域地图，请先建立完整家具环境地图”
try:
    poco(name='com.eco.global.app:id/no_area_text').get_text == '暂未生成区域地图' + '\n' + '请先建立完整家居环境地图'
    logger.debug("页面显示“暂未生成区域地图，请先建立完整家具环境地图”")
    log("页面显示“暂未生成区域地图，请先建立完整家具环境地图”")
except Exception as e:
    raise AssertionError("无图进入区域预约，页面没有显示为生成区域地图",e)
    

        






