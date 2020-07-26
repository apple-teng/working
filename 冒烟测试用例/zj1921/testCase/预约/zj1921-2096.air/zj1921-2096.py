# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
__case_theme__ = "ZJ1921-2096 验证新环境地图保存成地图1后，原来的预约上地图名称会改成地图1"
"""
**前提条件**:1.开启多楼层按钮； 2.主机新环境地图上有正常的预约 
**步骤ID 1**  
主机的新环境地图上存在正常的预约，失效的预约  
**期望结果**  
确认预约列表显示正常  
**步骤ID** 2  
进入地图管理，保存新环境地图为地图1  
**期望结果**  
确认可以保存正常  
**步骤ID** 3  
查看预约列表  
**期望结果**  
原来新环境地图的预约，地图名称全部改成地图1的预约 
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
case_name = "2096"

log("前提条件:开启多楼层按钮； 2.主机新环境地图上有正常的预约")
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
Main.click_any_popMsg_on_main()
# 返回主界面
mapmgr.click_mapmgr_to_main()
Main.click_any_popMsg_on_main()
log("导入地图-只有新环境地图")
cp_cmd = 'cp -r ' + NEW_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
app.telnet_to_deboot(cmd)

# 查看主机当前所在地图
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)
#查看主机当前所在地图
map_name = mapmgr.get_current_using_map_name()
if map_name == "新环境地图":
    logger.debug("当前所在地图为新环境地图")
    log("当前所在地图为新环境地图")
else:
    raise AssertionError("当前所在地图不为为新环境地图")
## 进入更多-工作预约
More.main_to_more()
Appoint.more_to_working_appointment()
## 点击“+”-进行区域预约,设置2min前的区域预约
try:
    Appoint.add_areaClean_appointment(-2)
finally:
    # 无论成功失败，返回更多页面
    poco(name='com.eco.global.app:id/title_back').click()
    logger.debug("返回更多")
    log("返回更多")
    poco(name='com.eco.global.app:id/titleContent').wait_for_appearance()
    if poco(name='com.eco.global.app:id/titleContent').get_text() == "更多":
        logger.debug("当前页面：更多")
        log("当前页面：更多")
        
log("步骤一：主机的新环境地图上存在正常的预约")
#进入工作预约
Appoint.more_to_working_appointment()
#点击区域清扫列表
Appoint.click_appointment_type_of_list('area')
#**期望结果**  
# 确认预约列表显示正常
if map_name in Appoint.get_appointment_list_map_name():
    logger.debug("区域预约显示正常-地图名称显示正确")
    log("区域预约显示正常-地图名称显示正确")
else:
    raise AssertionError("当前地图名称不在区域预约列表中，查看前提条件，区域预约是否设置成功")
# 返回更多
Appoint.working_appointment_to_more()

log("步骤二：进入地图管理，保存新环境地图为地图1")
# 返回主界面
More.more_to_main()
# j进入地图管理
mapmgr.click_main_to_mapmgr()
# 判断是否在多层地图页面
try:
    poco(text='地图管理').wait_for_appearance()
except:
    raise AssertionError("当前页面不在地图管理页面")
# 点击保存
save_as = mapmgr.click_to_save_newMap_as_map()
# **期望结果**  
# 确认可以保存正常
if "新环境地图" not in mapmgr.get_mapmgr_mapName():
    logger.debug("新环境地图可以保存正常，保存为" + save_as)
    log("新环境地图可以保存正常"+ save_as)

log("步骤三：查看预约列表")
# **期望结果**  
# 原来新环境地图的预约，地图名称全部改成地图1的预约
if "新环境地图" not in Appoint.get_appointment_list_map_name() and \
    save_as in Appoint.get_appointment_list_map_name():
        logger.debug("原来新环境地图的预约，地图名称全部改成地图1的预约")
        log("原来新环境地图的预约，地图名称全部改成地图1的预约")
        


