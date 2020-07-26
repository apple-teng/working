# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-571 验证对拖地禁区框进行拉伸，删除等操作"
__case_theme__ = "ZJ1921-571 验证对拖地禁区框进行拉伸，删除等操作"
"""
**前提条件**:1.主机有图  2.开始自动清扫  
**步骤ID 1**  
主界面点击
虚拟墙，切换至拖地禁区  
**期望结果**  
显示设置拖地禁区页面  
**步骤ID** 2  
点击矩形按钮  
**期望结果**  
页面下方有“请在地图范围内设定拖地禁区”的提示文字
手动画定拖地禁区矩形框，处于待确认状态，文字消失  
**步骤ID** 3  
查看矩形框  
**期望结果**  
矩形框有“x”“√”拖动节点    
**步骤ID** 9  
点击删除按钮  
**期望结果**  
矩形框会删除   
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
case_name = "571"

log('1.主机有图  2.开始自动清扫')
# 确保主机在充电座
try:
    Charge.check_lighting_icon(expectation='存在')
    logger.debug("主机在充电座")
except:
    logger.debug("主机当前不在充电座，使其回充")
    Charge.anyhow_go_charge()
    Main.click_any_popMsg_on_main()
log("#**前提条件**:1.主机有图  2.开始自动清扫")
log("导入地图-只有新环境地图")
cp_cmd = 'cp -r ' + NEW_PATH + DESTINATION_MAP_PATH                     
cmd = [cp_cmd, REBOOT_CMD]                        
app.telnet_to_deboot(cmd)
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)
# 开始自动清扫
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

log("步骤一：主界面点击,虚拟墙，切换至拖地禁区")
virtualWall.click_main_to_virtualWall()
sleep(5)
virtualWall.click_virtualWall_button('mop')
#**期望结果**  
# 显示设置拖地禁区页面
virtualWall.check_default_choose_of_virtualWall('mop')

log("步骤二：点击矩形按钮")
# **期望结果**  
# 页面下方有“请在地图范围内设定拖地禁区”的提示文字
# 手动画定拖地禁区矩形框，处于待确认状态，文字消失
virtualWall.click_rect_line_button('rect')
sleep(1)
virtualWall.check_draw_moppingWall_display()
virtualWall.draw_a_virtualwall()

log("步骤三：查看矩形框")
# **期望结果**  
# 矩形框有“x”“√”拖动节点
virtualWall.check_edit_virtualwall_display()

log("步骤四：点击删除按钮")
virtualWall.click_to_cancel_a_virtualwall()
# **期望结果**
# 矩形框会删除
snapshot('截图检查地图无拖地禁区.png',msg='删除拖地禁区成功，截图检查地图无拖地禁区')


