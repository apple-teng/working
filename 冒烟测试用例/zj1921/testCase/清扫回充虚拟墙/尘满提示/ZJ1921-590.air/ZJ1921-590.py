# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-590 验证主机清扫模式，累计清扫超过300分钟，尘满提示界面"
__case_theme__ = "ZJ1921-590 验证主机清扫模式，累计清扫超过300分钟，尘满提示界面"
"""
**前提条件**:配网成功，主机清扫模式，累计清扫300分钟  
**步骤ID 1**  
主机清扫累计超过300min，自动清扫完成，开始回充，成功回到充电座  
**期望结果**  
主机回充成功，开始充电；
APP弹框提示：
为提升清扫效果
请及时清理尘盒和滤芯
 如何清理>
知道了  
**步骤ID** 2  
点击“知道了”  
**期望结果**  
提示消失，显示待机页面  
**步骤ID** 3  
步骤1，点击“如何清理>”链接  
**期望结果**  
跳转到告警详情页：
上方：“返回” 详情
如何清理尘盒滤芯？
1.请取出尘盒，拿出滤芯
图示
2 .请使用清理小工具清洁滤芯
图示  
**步骤ID** 4  
点击“返回”按钮  
**期望结果**  
显示待机页面  
**步骤ID** 5  
主机清扫累计超过300min，手动点击“回充”按钮，主机回充成功  
**期望结果**  
主机回充成功，开始充电；
APP弹框提示：
为提升清扫效果
请及时清理尘盒和滤芯
 如何清理>
知道了    
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
case_name = "590"

log('1.主机有图  2.开始自动清扫')
# 确保主机不在充电座
Charge.anyhow_standby_out_of_charger()
Main.click_any_popMsg_on_main()
cmd_str = '{"dusthepa":298}'   
file_path = '/data/config/medusa/dustfile.json'
dusty_cmd = "echo '%s' > %s" %(cmd_str,file_path)
logger.debug(dusty_cmd)
cmd = [dusty_cmd, REBOOT_CMD]
log("telnet修改配置，使累计清扫300分钟")                        
app.telnet_to_deboot(cmd)
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(5)

log("步骤一：主机清扫累计超过300min，自动清扫完成，开始回充，成功回到充电座")
# 开始自动清扫
Sweep.click_auto_btn()
# Main.click_any_popMsg_on_main()
#**期望结果**  
# 为提升清扫效果
# 请及时清理尘盒和滤芯
#  如何清理>
# 知道了
Main.check_dust_full_popmsg()
log("步骤二：点击“知道了”")
Main.click_any_popMsg_on_main()
# **期望结果**  
# 提示消失，显示待机页面
## 通过检查主机的清扫按钮来确认尘满的蒙层消失
Sweep.check_auto_btn_exist(expectation='存在')

log("步骤三：步骤1，点击“如何清理>”链接")
log("telnet修改配置，使累计清扫300分钟")  
cmd_str = '{"dusthepa":298}'   
file_path = '/data/config/medusa/dustfile.json'
dusty_cmd = "echo '%s' > %s" %(cmd_str,file_path)
app.telnet_to_deboot(cmd)
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(5)
# 开始自动清扫
Sweep.click_auto_btn()
Main.check_dust_full_popmsg()
Main.click_how_to_clean_dust()
# **期望结果**  
# 跳转到告警详情页：
# 上方：“返回” 详情
# 如何清理尘盒滤芯？
# 1.请取出尘盒，拿出滤芯
# 2 .请使用清理小工具清洁滤芯
Main.check_how_to_clean_link_content()

log("步骤四：点击“返回”按钮")
Main.click_fault_details_to_main()
# **期望结果**
# 显示待机页面
## 通过检查主机的清扫按钮来确认尘满的蒙层消失
Sweep.check_auto_btn_exist(expectation='存在')

log("步骤五：主机清扫累计超过300min，手动点击“回充”按钮，主机回充成功")
log("telnet修改配置，使累计清扫300分钟")
cmd_str = '{"dusthepa":299}'   
file_path = '/data/config/medusa/dustfile.json'
dusty_cmd = "echo '%s' > %s" %(cmd_str,file_path)
app.telnet_to_deboot(cmd)
# 刷新地图-通过进出主界面
Main.click_any_popMsg_on_main()
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(5)
# 使主机回充
Charge.click_go_charge()
# **期望结果**
# 主机回充成功，开始充电；
# APP弹框提示：
# 为提升清扫效果
# 请及时清理尘盒和滤芯
#  如何清理>
# 知道了
# 开始自动清扫
Sweep.click_auto_btn()
# 主机还有1min尘满，清扫2min来实现清扫超过300min
sleep(120)
Main.check_dust_full_popmsg()
Main.click_any_popMsg_on_main()
