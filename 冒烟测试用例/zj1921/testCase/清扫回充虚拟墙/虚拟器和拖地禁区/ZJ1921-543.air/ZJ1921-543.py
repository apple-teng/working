# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-543 验证编辑虚拟墙页面"
__case_theme__ = "ZJ1921-543 验证编辑虚拟墙页面"
"""
**前提条件**:主机有图，正在自动清扫  
**步骤ID 1**  
主机清扫过程中，点击虚拟墙，点击或滑动切换至拖地禁区  
**期望结果**  
进入拖地禁区设置界面  
**步骤ID** 2  
点击矩形按钮在地图上添加拖地禁区，点击确认/√按钮  
**期望结果**  
主机：
继续清扫，能够清扫到拖地禁区位置
APP：
1.完成拖地禁区设置回到主界面时，APP上弱提示：
"清扫过程中不显示拖地禁区"
2.设置的拖地禁区也不会显示在地图上  
**步骤ID** 3  
完成完整清扫  
**期望结果**  
主机完成整张地图清扫包括拖地禁区
主机结束任务回到充电座后，APP上能够显示拖地禁区位置    
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
case_name = "543"

log('1.主机有图  2.开始自动清扫')
# 确保主机在充电座
try:
    Charge.check_lighting_icon(expectation='存在')
    logger.debug("主机在充电座")
except:
    logger.debug("主机当前不在充电座，使其回充")
    Charge.anyhow_go_charge()
    Main.click_any_popMsg_on_main()
log("导入地图-只有新环境地图")
cp_cmd = 'cp -r ' + NEW_PATH + DESTINATION_MAP_PATH                     
cmd = [cp_cmd, REBOOT_CMD]                        
app.telnet_to_deboot(cmd)
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)

log("步骤一：主机清扫过程中，点击虚拟墙，点击或滑动切换至拖地禁区")
# 使主机出发清扫
Sweep.click_auto_btn()
Main.click_any_popMsg_on_main()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "start" # 开始清扫
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot start message'")
# 清扫15S
sleep(15)
virtualWall.click_main_to_virtualWall()
sleep(5)
virtualWall.click_virtualWall_button('mop')
#**期望结果**  
# 进入拖地禁区设置界面
virtualWall.check_default_choose_of_virtualWall('mop')

log("步骤二：点击矩形按钮在地图上添加拖地禁区，点击确认/√按钮")
virtualWall.click_rect_line_button('rect')
sleep(1)
virtualWall.draw_a_virtualwall()
virtualWall.click_to_submit_a_virtualwall()
# **期望结果**   
# APP：
# 1.完成拖地禁区设置回到主界面时，APP上弱提示： "清扫过程中不显示拖地禁区"
virtualWall.click_virtualWall_to_main()
virtualWall.check_popmsg_by_mopping_vwall()
# 2.设置的拖地禁区也不会显示在地图上
snapshot("检查拖地禁区不会显示在地图上.png",msg="检查拖地禁区不会显示在地图上")
# # 主机：继续清扫，能够清扫到拖地禁区位置
if Sweep.get_deebot_status() == "清扫":
    logger.debug("退出虚拟墙界面，主机恢复运行")
    log("退出虚拟墙界面，主机恢复运行")
else:
    snapshot(msg='退出虚拟墙界面，主机没有恢复运行，截图检查')
    raise AssertionError("退出虚拟墙界面，主机没有恢复运行")

log("步骤三：完成完整清扫 ")
# 清扫完成开始回充
Charge.wait_finish_work_go_charge()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "recharge" # 返回充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot recharge message'")

# 回充成功
Charge.anyhow_go_charge()
Main.click_any_popMsg_on_main()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "stop" # 回到充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot stop message'")
# **期望结果** 
# 主机完成整张地图清扫包括拖地禁区,主机结束任务回到充电座后，APP上能够显示拖地禁区位置  
snapshot("主机完成整张地图清扫包括拖地禁区.png",msg="截图检查：主机完成整张地图清扫包括拖地禁区,主机结束任务回到充电座后，APP上能够显示拖地禁区位置")


