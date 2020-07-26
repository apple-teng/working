# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-331验证主机扫建弓字型清扫时，点击结束按钮-操作主机，观察主机清扫行为逻辑"
__case_theme__ = "ZJ1921-331验证主机扫建弓字型清扫时，点击结束按钮-操作主机，观察主机清扫行为逻辑"
"""
**前提条件**:主机配网成功无图，充电座待机，至少1个4.5*4.5m矩形区域  
**步骤ID 1**  
主界面点击“清扫”，主机从充电座出发，开始扫建  
**期望结果**  
主机退出充电座，先按4.5*4.5m沿边后，再弓字型清扫  
**步骤ID** 2  
主机弓字型清扫时，APP点击“结束”按钮  
**期望结果**  
APP弹出：
返回充电座
结束当前工作
取消
三个选择框  
**步骤ID** 3  
点击“返回充电座”  
**期望结果**  
APP状态显示：回充；显示回充页面

主机回充，边刷慢转  
**步骤ID** 4  
主机回充成功  
**期望结果**  
主机充电座上待机。

APP显示待机页面：

清扫记录小卡片，显示地图轮廓，地宝位置，充电座位置，清扫轨迹；
可滑动选择“区域”“自动”“自定义”；
按钮显示“地图管理”“清扫”“回充”  
**步骤ID** 5  
重复步骤1-2，点击“结束当前工作”  
**期望结果**  
主机原地待机；

APP显示待机页面：
有清扫记录小卡片，显示地图轮廓，地宝位置，充电座位置，清扫轨迹；
可滑动选择“区域”“自动”“自定义”；
按钮显示“地图管理”“清扫”“回充”  
**步骤ID** 6  
重复步骤1-2，点击“取消”  
**期望结果**  
主机继续弓字型清扫，
扫建完成所有可清扫区域自动回充
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
# 从设备列表进入主界面		
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# MQ准备数据
case_name = "331"

log("前提条件:主机配网成功无图，充电座待机，至少1个4.5*4.5m矩形区域")
try:
    Charge.check_lighting_icon() 
except:
    Charge.anyhow_go_charge()
log("导入地图-无图")
cp_cmd = 'cp -r ' + NO_MAP_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
app.telnet_to_deboot(cmd)
# 刷新地图-通过进出主界面
Main.click_any_popMsg_on_main()
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)
    
log("步骤一：主界面点击“清扫”，主机从充电座出发，开始扫建") 
Sweep.click_auto_btn()
Main.click_any_popMsg_on_main()
if exists(Template(r"tpl1592793929556.png", record_pos=(0.001, -0.051), resolution=(1080, 1920))):
    Sweep.check_perpare_for_sweep_pic()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "start" # 开始清扫
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot start message'")

log('预期结果：主机退出充电座，先按4.5*4.5m沿边后，再弓字型清扫')
# 根据自动化场地面积计算，运行5min后，主机基本开始弓字
sleep(30)

log('步骤二：主机弓字型清扫时，APP点击“结束”按钮')
Sweep.click_rightstop()
# APP弹出：返回‘充电座、结束当前工作、取消’三个选择框
log("步骤三：点击“返回充电座")
Charge.click_go_charge_station()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "recharge" # 返回充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot recharge message'")
# 预期结果：APP状态显示：回充；显示回充页面,主机回充
if poco("com.eco.global.app:id/deebot_statues").get_text() == '回充':
    log("APP状态显示：回充")
    Charge.wait_finish_work_go_charge()
    
log('步骤四：主机回充成功')
Charge.anyhow_go_charge()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "stop" # 回到充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot stop message'")
sleep(2)
# 预期结果：
# 主机充电座上待机APP显示待机页面：
# Charge.check_lighting_icon(expectation='存在')已包含

# 清扫记录小卡片，显示地图轮廓，地宝位置，充电座位置，清扫轨迹；
Main.check_sweep_card_exists(expectation='存在')
# 可滑动选择“区域”“自动”“自定义”；
if Sweep.get_all_sweep_mode_name() == ['区域','自动','自定义']: 
    log("主界面显示“区域”“自动”“自定义”")
else:
    raise AssertionError('主页面的清扫模式缺失')
Main.click_area_to_area_clean()
Main.click_custom_to_custom_clean()
# 按钮显示“地图管理”“清扫”“回充” 
Sweep.check_map_manager_btn_exist(expectation='存在')
Sweep.check_auto_btn_exist(expectation='存在')
Sweep.check_go_charge_btn_exist(expectation='存在')
















