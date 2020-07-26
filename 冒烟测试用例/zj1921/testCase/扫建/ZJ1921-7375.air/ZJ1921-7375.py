# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
__case_theme__ = "ZJ1921-7375验证主机在扫建时遇到房间门槛高度大于2cm的房间，不会进入该房间扫建"
"""
**前提条件**:1.主机无图 2.多楼层地图开关打开3.主机待机  
**步骤ID 1**  
在地图管理里打开多层地图开关  
**期望结果**  
地图管理里多层地图开关打开  
**步骤ID** 2  
返回主界面，点击“清扫”按钮  
**期望结果**  
主机开始扫建，app主界面地图实时更新，显示清扫状态，清扫面积，清扫时长  
**步骤ID** 3  
待主机沿边完成，手动点击“回充”  
**期望结果**  
主机回充成功，保存残图  
**步骤ID** 4  
主机待机后，查看主界面显示  
**期望结果**  
显示刷新地图引导：
点击此处可定位地宝所在位置，建议在搬动后使用
知道了  
**步骤ID** 5  
点击知道了  
**期望结果**  
引导消失，显示APP主界面 
"""

import time
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
case_name = "7375"

log("前提条件**:测试场景中有房间门槛高度大于2cm；2.将主机放在房间外")
# 前提条件为环境准备，但是需要主机外待机状态
Charge.anyhow_standby_out_of_charger()
log("导入地图-新环境地图")
cp_cmd = 'cp -r ' + NEW_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
app.telnet_to_deboot(cmd)
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)
log("步骤一：点击清扫按钮")
Sweep.click_auto_btn()
Main.click_any_popMsg_on_main()
# 点击准备建图的下一步
if poco(text="准备建图").exists():
    Sweep.check_perpare_for_sweep_pic()
# **期望结果**:主机开始在走廊扫建沿边
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "start" # 开始清扫
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot start message'") 

log("步骤二：沿边过程中遇到该房间")
sleep(120)
# **期望结果**:主机检测到门槛高度，不会进入该房间沿边
log(time.strftime("%H:%M:%S"))

log("步骤三：待主机清扫完房间外区域")
Charge.wait_finish_work_go_charge()

# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "recharge" # 返回充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot recharge message'")

# **期望结果**:主机开始回充，自始至终不会进入该房间清扫 
snapshot("回充时没有清扫门栏高于2cm的区域截图.jpg", msg="回充时没有清扫门栏高于2cm的区域截图")
logger.debug("进入teardown-主机回到充电座待机")
## 回充成功
Charge.anyhow_go_charge()
Main.click_any_popMsg_on_main()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "stop" # 回到充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot stop message'")
snapshot("回充成功后截图-没有清扫门栏高于2cm的区域.jpg", msg="回充成功后截图-没有清扫门栏高于2cm的区域")



