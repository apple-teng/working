# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-513 验证在主机清扫时从主界面进入虚拟墙和拖地禁区页，引导页显示"
__case_theme__ = "ZJ1921-513 验证在主机清扫时从主界面进入虚拟墙和拖地禁区页，引导页显示"
"""
前提条件**:主机配网成功，主机有图（或残图），在清扫中或者在拖地中  
**步骤ID 1**  
在主机清扫中，主界面首次点击“虚拟墙”  
**期望结果**  
主机继续清扫，app进入虚拟墙引导页  
**步骤ID** 2  
查看引导页  
**期望结果**  
进入到虚拟墙引导页：
虚拟墙有什么用？
设定虚拟墙后，地宝工作时会自动避开虚拟墙框定区域。
有“？”图标按钮显示在拖地禁区的右侧，且灰色显示（不高亮）  
**步骤ID** 3  
点击页面任意位置  
**期望结果**  
进入到拖地禁区引导页
页面文字提示：
拖地禁区有什么用？
设定拖地禁区后，地宝仅在拖地时会自动避开该拖地禁区。  
**步骤ID** 4  
点击页面任意位置  
**期望结果**  
进入下一引导页
如何绘制矩形虚拟墙与拖地禁区
1.选取矩形工具
2.在地图上滑动，设定范围
有小动图体现画线，调节大小，和拖拽移动的操作  
**步骤ID** 5  
点击页面任意位置  
**期望结果**  
进入下一引导页
如何绘制线形虚拟墙
1.选取线形工具
2.在地图上滑动，设定范围
知道了
有小动图体现画线，调节大小，和拖拽移动的操作  
**步骤ID** 6  
点击：知道了  
**期望结果**  
1.引导消失
2.如果主机在清扫状态，默认选中“虚拟墙”，
如果主机在拖地模式，默认选中“拖地禁区”，可以选择到“虚拟墙”
3.线性、矩形虚拟墙均可操作  
**步骤ID** 7  
查看虚拟墙和拖地禁区界面  
**期望结果**  
主机继续清扫
APP：地图上显示有充电座位置、地宝位置，不显示清扫轨迹  
**步骤ID** 8  
点击拖地禁区右侧的“？”  
**期望结果**  
APP：再次呼出虚拟墙引导页  
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
case_name = "513"

log("前提条件:主机配网成功，主机有图（或残图），在清扫中或者在拖地中")
# 确保app中功能首次打开--重新安装app
log("导入地图-只有新环境地图")
cp_cmd = 'cp -r ' + NEW_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
app.telnet_to_deboot(cmd)
# 开启app，进入设备列表，进入主界面
app.openApp()
sleep(5)
app.loginAPP_China()
# 刷新地图-通过进出主界面
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)

log("步骤一：在主机清扫中，主界面首次点击“虚拟墙”")
Main.click_auto_to_auto_clean()
Sweep.click_auto_btn()
Main.click_any_popMsg_on_main()
#**期望结果**  
# 主机继续清扫，app进入虚拟墙引导页
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "start" # 开始清扫
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot start message'")
# 清扫1min
sleep(60)
working_mode = Sweep.get_working_mode()
virtualWall.click_main_to_virtualWall()

log("步骤二：查看引导页")
# **期望结果**  
# 进入到虚拟墙引导页：
# 虚拟墙有什么用？
# 设定虚拟墙后，地宝工作时会自动避开虚拟墙框定区域。
# 有“？”图标按钮显示在拖地禁区的右侧，且灰色显示（不高亮）
virtualWall.check_virtalWall_popMsg()

log("步骤三：点击页面任意位置")
virtualWall.click_virtalWall_popMsg()
# **期望结果**  
# 进入到拖地禁区引导页
# 页面文字提示：
# 拖地禁区有什么用？
# 设定拖地禁区后，地宝仅在拖地时会自动避开该拖地禁区
virtualWall.check_mopping_popMsg()

log("步骤四：点击页面任意位置")
virtualWall.click_virtalWall_popMsg()
# **期望结果**
# 进入下一引导页
# 如何绘制矩形虚拟墙与拖地禁区
# 1.选取矩形工具
# 2.在地图上滑动，设定范围
# 有小动图体现画线，调节大小，和拖拽移动的操作
virtualWall.check_draw_virtalWall_direction()

log("步骤五：点击页面任意位置")
virtualWall.click_virtalWall_popMsg()
# **期望结果**
# 进入下一引导页
# 如何绘制线形虚拟墙
# 1.选取线形工具
# 2.在地图上滑动，设定范围
# 知道了
virtualWall.check_draw_line_virtallWall_dirction()

log("步骤六：点击：知道了")
virtualWall.click_Iknow_to_exit_virtualWall_dirction()
# **期望结果**
# 1.引导消失
# 2.如果主机在清扫状态，默认选中“虚拟墙”，
# 如果主机在拖地模式，默认选中“拖地禁区”，可以选择到“虚拟墙”
# 3.线性、矩形虚拟墙均可操作
logger.debug("主机工作状态：" + working_mode)
log("主机工作状态：" + working_mode)
virtualWall.check_default_choose_of_virtualWall(working_mode)
virtualWall.click_virtualWall_button(button_type='mop')
virtualWall.click_virtualWall_button(button_type='vwall')
virtualWall.click_rect_line_button("line")
virtualWall.click_rect_line_button("rect")
    
log("步骤七：查看虚拟墙和拖地禁区界面")
# **期望结果**
# 主机继续清扫
# APP：地图上显示有充电座位置、地宝位置，不显示清扫轨迹
snapshot(msg="截图检查虚拟墙和拖地禁区界面-地图上显示有充电座位置、地宝位置，不显示清扫轨迹")

log("步骤八：点击拖地禁区右侧的“？”")
virtualWall.click_virtualWall_quiz()
# **期望结果**
# APP：再次呼出虚拟墙引导页 
virtualWall.check_virtualWall_direction()



