# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-2115 验证主机新增区域预约后，更新区域分类，区域预约能够响应"
__case_theme__ = "ZJ1921-2115 验证主机新增区域预约后，更新区域分类，区域预约能够响应"
"""
**前提条件**:主机配网成功，有整图  
**步骤ID 1**  
进入更多-清扫预约  
**期望结果**  
进入预约列表  
**步骤ID** 2  
新增区域预约，保存  
**期望结果**  
确认列表界面会显示所区域的地图名称，和区域名称  
**步骤ID** 3  
进入地图管理，选择地图重新进行区域分类  
**期望结果**  
确认地图分类成功，设成成房间，客厅，卫生间等类别  
**步骤ID** 4  
进入更多-清扫预约  
**期望结果**  
确认列表中区域预约的区域名称变成对应的类别:房间，客厅等  
**步骤ID** 5  
到达预约的时间点  
**期望结果**  
确认主机响应预约，去往对应的区域清扫 
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
case_name = "2115"

log("主机配网成功，有整图")
try:
    Charge.check_lighting_icon(expectation='存在')
    log("主机在充电座")
    logger.debug("主机在充电座")
except:
    logger.debug("使主机在充电座待机")
    log("使主机在充电座待机")
    Charge.anyhow_go_charge()
    
log("导入地图-只有新环境")
cp_cmd = 'cp -r ' + NEW_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)
# 查看主机当前所在地图
map_name = mapmgr.get_current_using_map_name()
if map_name == None:
    raise AssertionError("当前所在地图不为整图") 
else:
    logger.debug("主机有整图")
    log("主机有整图，前提条件准备完成")
    
log("步骤一：进入更多-清扫预约")
More.main_to_more()
Appoint.more_to_working_appointment()
#**期望结果**  
# 进入预约列表
##步骤已已涵盖

log("步骤二：新增区域预约，保存")
## 点击“+”-进行区域预约,设置2min后的区域预约
Appoint.add_areaClean_appointment(2)
#点击区域清扫列表
Appoint.click_appointment_type_of_list('area')
# **期望结果**  
# 确认列表界面会显示所区域的地图名称，和区域名称
if map_name in Appoint.get_appointment_list_map_name():
    logger.debug("区域预约显示正常-地图名称显示正确")
    log("区域预约显示正常-地图名称显示正确")
else:
    raise AssertionError("当前地图名称不在区域预约列表中，区域预约没设置成功")

log("步骤三：进入地图管理，选择地图重新进行区域分类")
# 返回更多
Appoint.working_appointment_to_more()
# 返回主界面
More.more_to_main()
# j进入地图管理
mapmgr.click_main_to_mapmgr()
# 判断是否在多层地图页面
try:
    poco(text='地图管理').wait_for_appearance()
except:
    raise AssertionError("当前页面不在地图管理页面")
# 在地图管理，选择地图重新进行区域分类
mapmgr.click_to_choose_living_room()
# **期望结果**  
# 确认地图分类成功，设成成房间，客厅，卫生间等类别
## mapmgr.click_to_choose_living_room()中已做检查

log("步骤四：进入更多-清扫预约")
# 从地图管理 返回主界面
mapmgr.click_mapmgr_to_main()
## 主界面进入更多-工作预约
More.main_to_more()
Appoint.more_to_working_appointment()
sleep(5)
## 点击区域清扫列表
Appoint.click_appointment_type_of_list('area')
#**期望结果**  
# 确认列表中区域预约的区域名称变成对应的类别:房间，客厅等
if exists(Template(r"tpl1594015235441.png", record_pos=(-0.002, 0.0), resolution=(1080, 2340))):
    logger.debug("列表中区域预约的区域名称变成对应的类别")
    log("列表中区域预约的区域名称变成对应的类别")
else:
    raise AssertionError("列表中区域预约的区域名称没有变成对应的类别")

log("步骤五：到达预约的时间点")
#**期望结果**  
# 确认主机响应预约，去往对应的区域清扫
popmsg_flag,deboot_flag = Appoint.check_effect_of_schedule()
if popmsg_flag == 1 and deboot_flag ==1:
    logger.debug("主机响应预约，去往对应的区域清扫")
    log("主机响应预约，去往对应的区域清扫") 
else:
    raise AssertionError("主机响应预约出错，popmsg_flag,deboot_flag的状态值分别为 %d，%d")%(popmsg_flag,deboot_flag)