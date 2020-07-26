# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
__case_theme__ = "ZJ1921-355 验证主机无图&残图时，不可以选择区域清扫"
"""
前提条件**:1.主机配网成功  
**步骤ID 1**  
主机无图，进入主界面  
**期望结果**  
主机在充电座上。
APP上方显示：“返回”“Deebot T8”“分享”“更多”“电量”动态充电图标，
图示：
地宝往各个房间清扫，生成地图
建图成功后，可解锁区域清扫、自定义清扫等高级功能？
可滑动选择“区域”“自动”“自定义”；
按钮显示“地图管理”“开始”“回充”  
**步骤ID** 2  
点击“区域”按钮  
**期望结果**  
主机在充电座上。
APP上方显示：“返回”“Deebot T8”“分享”“更多”“电量”动态充电图标，
图示：
地宝往各个房间清扫，生成地图
建图成功后，可解锁区域清扫、自定义清扫等高级功能？
可滑动选择“区域”“自动”“自定义”；
按钮显示“地图管理”“开始”“回充”  
**步骤ID** 3  
主机扫建残图，点击区域按钮  
**期望结果**  
区域页面无地图显示，文字提示“暂未生成区域地图     请先建立完整家居环境地图
如何建立完整家居地图”  
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
case_name = "355"

log("前提条件：主机配网成功，在充电座充电")
try:
    Charge.check_lighting_icon(expectation='存在')
    log("主机在充电座")
    logger.debug("主机在充电座")
except:
    logger.debug("使主机在充电座待机")
    log("使主机在充电座待机")
    Charge.anyhow_go_charge()


log("步骤一：主机无图，进入主界面--导入地图-无图")
cp_cmd = 'cp -r ' + NO_MAP_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
app.telnet_to_deboot(cmd)
# 查看主机当前所在地图
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)
#**期望结果**  
# APP上方显示：“返回”“Deebot T8”“分享”“更多”“电量”动态充电图标，
Charge.check_deebot_on_charger()
# 图示：
# 地宝往各个房间清扫，生成地图
Main.check_title_elements()
# 检查建图事项
Main.check_no_map_cue()
# 可滑动选择“区域”“自动”“自定义”
Main.click_area_to_area_clean()
Main.click_custom_to_custom_clean()
# 按钮显示“地图管理”“清扫”“回充”
Main.check_bottom_elements()

log("步骤二：点击“区域”按钮")
Main.click_area_to_area_clean()
# **期望结果**  
# 主机在充电座上。
# APP上方显示：“返回”“Deebot T8”“分享”“更多”“电量”动态充电图标，
Charge.check_deebot_on_charger()
# 图示：
# 地宝往各个房间清扫，生成地图
Sweep.check_main_while_no_map()
# 建图成功后，可解锁区域清扫、自定义清扫等高级功能？
Main.check_no_map_cue()
# 按钮显示“地图管理”“开始”“回充”
Main.check_bottom_elements()


log("步骤三：主机扫建残图，点击区域按钮")
Main.click_auto_to_auto_clean()
Sweep.click_auto_btn()
Main.click_any_popMsg_on_main()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "start" # 开始清扫
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot start message'")
# 清扫2min的残图
sleep(120)
# 结束清扫
Charge.anyhow_go_charge()
# 点击区域按钮
Main.click_area_to_area_clean()
# **期望结果**  
# 区域页面无地图显示，文字提示“暂未生成区域地图     请先建立完整家居环境地图  如何建立完整家居地图”
Main.check_no_map_cue()

