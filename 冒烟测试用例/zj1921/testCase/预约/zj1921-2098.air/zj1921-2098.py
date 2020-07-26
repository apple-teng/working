# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
__case_theme__ = "ZJ1921-2098 验证地图修改名称后，原来的预约上地图名称会对应的修改"
"""
**前提条件**:1.开启多楼层；  
**步骤ID 1**  
主机的地图上设置正常的预约  
**期望结果**  
确认预约列表显示正常  
**步骤ID** 2  
进入地图管理，编辑当前地图的名称，修改名称  
**期望结果**  
确认可以编辑地图名称  
**步骤ID** 3  
查看预约列表  
**期望结果**  
原来地图的预约，地图名称全部改成新的名称，
不会显示重叠，超出位置显示为省略号
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
case_name = "2098"

log("前提条件:开启多楼层按钮")
try:
    Charge.check_lighting_icon(expectation='存在')
    log("主机在充电座")
    logger.debug("主机在充电座")
except:
    logger.debug("使主机在充电座待机")
    log("使主机在充电座待机")
    Charge.anyhow_go_charge()
# 开启多层地图
log("在地图管理里打开多层地图开关")
mapmgr.click_main_to_mapmgr()
# 首次打开错层地图，会弹出“多层地图建图注意事项”
if poco(name='com.eco.global.app:id/checkbox').exists():
    mapmgr.check_and_click_turn_on_mapmgr_button_notice()
    mapmgr.click_autosave_map_popmsg()
mapmgr.click_mapmgr_switch(mapmgr_switch=1)
# 首次打开多层地图，会弹出“多层地图建图注意事项”
if poco(name='com.eco.global.app:id/checkbox').exists():
    mapmgr.check_and_click_turn_on_mapmgr_button_notice()
    mapmgr.click_autosave_map_popmsg()
## 返回主界面
mapmgr.click_mapmgr_to_main()

log("导入地图-只有地图1")
cp_cmd = 'cp -r ' + MAP1_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
app.telnet_to_deboot(cmd)

# 查看主机当前所在地图
## 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
# 查看主机当前所在地图
map_name = mapmgr.get_current_using_map_name()
if map_name == None:
    raise AssertionError("当前所在地图不为整图")
elif map_name == "新环境地图":
    raise AssertionError("导图不成功，当前地图不应该为新环境地图")

log("步骤一：主机的地图上设置正常的预约")
## 进入更多-工作预约
More.main_to_more()
Appoint.more_to_working_appointment()
## 点击“+”-进行区域预约,设置2min前的区域预约
Appoint.add_areaClean_appointment(-2)
#点击区域清扫列表
Appoint.click_appointment_type_of_list('area')
#**期望结果**  
# 确认预约列表显示正常
if map_name in Appoint.get_appointment_list_map_name():
    logger.debug("区域预约显示正常-地图名称显示正确")
    log("区域预约显示正常-地图名称显示正确")
else:
    raise AssertionError("当前地图名称不在区域预约列表中，区域预约是否设置成功")
# 返回更多
Appoint.working_appointment_to_more()    

log("步骤二：进入地图管理，编辑当前地图的名称，修改名称")
# 返回主界面
More.more_to_main()
# 进入地图管理
mapmgr.click_main_to_mapmgr()
# 判断是否在多层地图页面
try:
    poco(text='地图管理').wait_for_appearance()
except:
    raise AssertionError("当前页面不在地图管理页面")

# **期望结果**  
# 确认可以编辑地图名称
modified_name = mapmgr.modify_map_name('4567890abcdf')

log("步骤三：查看预约列表")
# **期望结果**  
# 原来地图的预约，地图名称全部改成新的名称，不会显示重叠，超出位置显示为省略号
## 返回主界面
mapmgr.click_mapmgr_to_main()
## 进入更多-工作预约
More.main_to_more()
Appoint.more_to_working_appointment()
## 点击区域清扫列表
Appoint.click_appointment_type_of_list('area')
if map_name in Appoint.get_appointment_list_map_name():
    raise AssertionError("修改地图名称，区域预约列表中地图名称没有跟着变化")    
elif modified_name in Appoint.get_appointment_list_map_name():
    logger.debug("修改地图名称，区域预约列表中地图名称跟着变化")
    log("修改地图名称，区域预约列表中地图名称没有跟着变化")
## 根据手机屏幕大小而定，小屏幕会显示出“...”
elif  '...' in poco(name='com.eco.global.app:id/map_name').get_text():
    logger.debug(u'地图管理界面上显示不全的重命名用...代替')                         
    log('地图管理界面上显示不全的重命名用...代替')
else:
    raise AssertionError("修改地图名称，区域预约列表中地图名称变化与实际修改值不符")

# teardown
Appoint.teardown_schedule('area')
