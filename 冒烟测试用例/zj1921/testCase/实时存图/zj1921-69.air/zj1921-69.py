# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
__case_theme__ = "ZJ1921-69 无图时，自动、区域，自定义页面显示"
""" 
**前提条件**:主机无图，待机  
**步骤ID 1**  
主机无图待机，app进入主界面，查看主界面-自动页面显示  
**期望结果**  
自动页面：引导动图
页面显示文字：上方：建图成功后，可解锁区域清扫、自定义？清扫等高级功能  
**步骤ID** 2  
查看区域页面  
**期望结果**  
区域页面：可点击，显示文字：“暂无地图”  
**步骤ID** 3  
查看自定义页面  
**期望结果**  
自定义页面：可点击，显示文字：“暂无地图”  
**步骤ID** 4  
APP在“自动”页面，点击清扫  
**期望结果**  
主机开始扫建；
app开始显示扫建地图轮廓  
**步骤ID** 5  
APP在“区域”页面，点击清扫  
**期望结果**  
主机开始扫建；
app开始显示扫建地图轮廓  
**步骤ID** 6  
APP在“自定义”页面，点击清扫  
**期望结果**  
主机开始扫建
APP开始显示扫建地图轮廓 
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
case_name = "69"

log("前提条件:主机无图，待机")
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

log("步骤一：主机无图待机，app进入主界面，查看主界面-自动页面显示")
## 前提条件已完成
# **期望结果**  
# 自动页面：引导动图
# 页面显示文字：上方：建图成功后，可解锁区域清扫、自定义？清扫等高级功能
Sweep.check_main_while_no_map()
            
log("步骤二：查看区域页面")
Main.click_area_to_area_clean()
Main.click_I_know_popMsg()
# **期望结果**  
# 区域页面：可点击，显示文字：显示建图引导
poco(text='快速建图提示').exists()

log("步骤三：查看自定义页面")
Main.click_custom_to_custom_clean()
Main.click_I_know_popMsg()
# **期望结果**  
# 自定义页面：可点击，显示文字：显示建图引导
poco(text='快速建图提示').exists()

log("步骤四：APP在“自动”页面，点击清扫 ") 
Main.click_auto_to_auto_clean()
Sweep.click_auto_btn()
# **期望结果**  
# 主机开始扫建；
## 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "start" # 开始清扫
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot start message'")
## app开始显示扫建地图轮廓 
sleep(120)
snapshot('app开始显示扫建地图轮廓.png','app开始显示扫建地图轮廓')
             
log("步骤五：APP在“区域”页面，点击清扫")
# 结束自动清扫
Sweep.click_rightstop()
Sweep.click_stop_clean()
# 扫建中结束清扫的处理
Sweep.click_pop_windows_while_stop_building_map()
## 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "stop" # 回到充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [4] Sent 'deebot stop message'")

#APP在“区域”页面
Main.click_area_to_area_clean()
# 点击清扫
Sweep.click_auto_btn()
# **期望结果** 
# 无图，无法进行区域清扫，app弹出 “暂未生成区域地图，请先建立完整家居环境地图”
try:
    exists(Template(r"tpl1593673180393.png", rgb=True, record_pos=(0.007, 0.348), resolution=(1080, 1920)))
except Exception as e:
    raise e("无图区域清扫，app没有弹框")

log("步骤六：APP在“自定义”页面，点击清扫")
Main.click_custom_to_custom_clean()
# 点击清扫
Sweep.click_auto_btn()

# **期望结果** 
# 不划定区域，无法进行自定义清扫，app弹出“请框选清扫区域”
try :
    exists(Template(r"tpl1593674283521.png", record_pos=(-0.001, 0.358), resolution=(1080, 1920)))
except Exception as e:
    raise AssertionError("不划定区域进行自定义清扫，app没有弹框")
    

    
        

    
    
