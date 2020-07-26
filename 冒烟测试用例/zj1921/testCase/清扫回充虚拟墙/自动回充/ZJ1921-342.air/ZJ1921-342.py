# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-342 验证主机有图自动清扫行走逻辑为：按自动分区先沿边，后弓字型清扫"
__case_theme__ = "ZJ1921-342 验证主机有图自动清扫行走逻辑为：按自动分区先沿边，后弓字型清扫"
"""
前提：1.主机有图，有分区  
**前提条件**:1.主机有图，有分区  
**步骤ID 1**  
主机已存图
主机在充电座上，点击清扫  
**期望结果**  
主机按自动分区沿边清扫，再弓字型清扫。
APP显示 “虚拟墙”“暂停”“结束”按钮；
状态显示“清扫”；
清扫面积和清扫时长随着实际清扫变化。  
**步骤ID** 2  
主机清扫完成  
**期望结果**  
主机自动回充。
APP页面弱提示“清扫已完成，返回充电”，3秒后消失；
状态显示“回充”；
显示“停止”按钮；  
**步骤ID** 3  
回充成功  
**期望结果**  
主机在充电座上。
APP上显示动态充电图标；
有清扫记录生成
自动清扫完成的地图，清扫轨迹，地宝位置和充电座位置；
可滑动选择“区域”“自动”“自定义”；
按钮显示“地图管理”“清扫”“回充”   
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
case_name = "342"

# 确保主机在充电座
Charge.anyhow_go_charge()
Main.click_any_popMsg_on_main()
log("前提条件:1.主机有图，有分区")
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

log("步骤一：主机已存图,主机在充电座上，点击清扫")
Sweep.click_auto_btn()
Main.click_any_popMsg_on_main()
#**期望结果**  
# 主机按自动分区沿边清扫，再弓字型清扫。
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "start" # 开始清扫
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot start message'")

# APP显示 “虚拟墙”“暂停”“结束”按钮；
Sweep.check_virtual_wall_btn_exist(expectation='存在')
Sweep.check_auto_btn_status(expectation='清扫')
Sweep.check_stop_clean_btn_exist(expectation='存在')
# 状态显示“清扫
if Sweep.get_working_mode == 'clean':
    logger.debug("app状态显示“清扫")
    log("app状态显示“清扫")
# 清扫面积和清扫时长随着实际清扫变化
sleep(30)
area1 = Sweep.get_area()
clean_time1 = Sweep.get_clean_time()
sleep(120)
area2 = Sweep.get_area()
clean_time2 = Sweep.get_clean_time()
if (area1 < area2) and (clean_time1 < clean_time2):
    log("清扫面积和清扫时长随着实际清扫变化")
else:
    raise AssertError("清扫面积和清扫时长没有随着实际清扫变化")

log("步骤二：主机清扫完成")
# APP页面弱提示“清扫已完成，返回充电”，3秒后消失；
Charge.check_tips_complete_clean_go_charge(expectation='存在')
# 状态显示“回充”；
Charge.wait_finish_work_go_charge()
# **期望结果**  
# 主机自动回充。
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "recharge" # 返回充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot recharge message'")
# 显示“停止”按钮；
Charge.check_stop_go_charge_icon(expectation='存在')
    
log("步骤三：回充成功")
Charge.anyhow_go_charge()
Main.click_any_popMsg_on_main()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "stop" # 回到充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot stop message'")
# **期望结果**  
# 主机在充电座上,APP上显示动态充电图标；
Charge.check_deebot_on_charger()
# 有清扫记录生成
Main.check_sweep_card_exists("存在")
# 自动清扫完成的地图，清扫轨迹，地宝位置和充电座位置；
snapshot("自动清扫完成的地图.png",msg='截图检查：自动清扫完成的地图，清扫轨迹，地宝位置和充电座位置')
# 可滑动选择“区域”“自动”“自定义”；
Main.click_area_to_area_clean()
Main.click_custom_to_custom_clean()
Main.click_auto_to_auto_clean()
# 按钮显示“地图管理”“清扫”“回充”
Main.check_bottom_elements()
