# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-1 验证无图时多层地图打开，首次出现残图，显示刷新地图引导"
__case_theme__ = "ZJ1921-1 验证无图时多层地图打开，首次出现残图，显示刷新地图引导"
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
import time, telnetlib
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
case_name = "1"

log("前提条件:主机配网成功无图，充电座待机，至少1个4.5*4.5m矩形区域")
# 确保主机在充电座
try:
    Charge.check_lighting_icon(expectation='存在')
    log("主机在充电座")
    logger.debug("主机在充电座")
except:
    logger.debug("使主机在充电座外待机")
    log("使主机在充电座外待机")
    Charge.anyhow_go_charge()
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
    
log("步骤一：在地图管理里打开多层地图开关")
mapmgr.click_main_to_mapmgr()
# 首次打开错层地图，会弹出“多层地图建图注意事项”
if poco(name='com.eco.global.app:id/checkbox').exists():
    mapmgr.check_and_click_turn_on_mapmgr_button_notice()
    mapmgr.click_autosave_map_popmsg()
mapmgr.click_mapmgr_switch(mapmgr_switch=1)
# 首次打开错层地图，会弹出“多层地图建图注意事项”
if poco(name='com.eco.global.app:id/checkbox').exists():
    mapmgr.check_and_click_turn_on_mapmgr_button_notice()
    mapmgr.click_autosave_map_popmsg()
#**期望结果**:地图管理里多层地图开关打开 
mapmgr.check_mapmgr_fun_swith() == 1
log("地图管理里多层地图开关打开")

log("步骤二：返回主界面，点击“清扫”按钮")
# 返回主界面
mapmgr.click_mapmgr_to_main()
# 若首次清扫，主界面会弹出开启多层地图
mapmgr.click_main_new_map_popmsg()
# 点击“清扫”按钮    
Sweep.click_auto_btn() 
Main.click_any_popMsg_on_main()
#预期结果：
## 主机开始扫建，
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "start" # 开始清扫
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot start message'") 
## app显示清扫状态，
if Sweep.get_deebot_status == "清扫" or Sweep.get_deebot_status == "拖地":
    log("app显示清扫状态")
## 清扫面积，
log("主机清扫面积为：" + Sweep.get_area())    
## 清扫时长 
log("主机清扫面积为：" + Sweep.get_clean_time())    
    
log("步骤三：待主机尚未清扫完成，手动点击“回充”")
sleep(180) # 清扫3min，在自动化场地中，就可以满足没有清扫完成
# 点击“回充”
Charge.set_finish_sweep_to_charge()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "recharge" # 返回充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot recharge message'")
# **期望结果**  
# 主机回充成功
Charge.anyhow_go_charge()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "stop" # 回到充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot stop message'")

log("步骤四：主机待机后，查看主界面显示")
## 步骤3的预期结果已经检查
# **期望结果**  
# 显示刷新地图引导：点击此处可定位地宝所在位置，建议在搬动后使用，弹出 "知道了"
if exists(Template(r"tpl1593395457840.png", record_pos=(-0.188, -0.169), resolution=(1080, 1920))):
    mapmgr.check_relocation_popmsg()

log("步骤五：点击知道了")
# **期望结果**  
# 引导消失，显示APP主界面
## 步骤四已包含




    
    


