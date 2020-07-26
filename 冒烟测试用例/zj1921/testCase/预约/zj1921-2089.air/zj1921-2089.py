# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
__case_theme__ = "ZJ1921-2089 验证开启多层地图，主机在当前环境上上，重置当前地图后，该环境的区域清扫预约会被删除"
""" 
**前提条件**:1.开启多层地图； 2.主机所在地图上有区域预约； 3.主机已存3张地图，地图1 ，地图2，新环境地图  
**步骤ID 1**  
主机已存3张地图，地图1 ，地图2，新环境地图，主机在新环境地图上；进入更多-清扫预约  
**期望结果**  
进入清扫预约列表  
**步骤ID** 2  
查看区域清扫列表  
**期望结果**  
新环境地图的区域预约显示正常 
**步骤ID** 3  
进入更多-重置当前地图  
**期望结果**  
跳出弹窗：
删除的是正在使用的地图
确认删除该地图并清空相关的预约？
取消  删除  
**步骤ID** 4  
点击删除  
**期望结果**  
确认当前界面不显示新环境地图，刷新成地图1  
**步骤ID** 5  
进入更多-清扫预约  
**期望结果**  
查看地图1的预约显示打开，地图2的预约显示失效
新环境地图的区域预约消失不显示  
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
case_name = "2089"

log("前提条件:1.开启多层地图； 2.主机所在地图上有区域预约； 3.主机已存3张地图，地图1 ，地图2，新环境地图")
# 确保主机在充电座
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
# 首次打开错层地图，会弹出“多层地图建图注意事项”
if poco(name='com.eco.global.app:id/checkbox').exists():
    mapmgr.check_and_click_turn_on_mapmgr_button_notice()
    mapmgr.click_autosave_map_popmsg()
# 返回主界面
mapmgr.click_mapmgr_to_main()

log("导入地图-导入3张地图，主机当前在新环境地图")
cp_cmd = 'cp -r ' + NEW_MAP1_MAP2_PATH + DESTINATION_MAP_PATH
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
# 在当前地图上设置区域预约
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

log("步骤一：主机已存3张地图，地图1 ，地图2，新环境地图；进入更多-清扫预约")
Appoint.more_to_working_appointment()
# **期望结果**  
# 进入清扫预约列表
## 步骤一已覆盖


log("步骤二：查看区域清扫列表")
Appoint.click_appointment_type_of_list('area')
sleep(2)
# **期望结果**  
# 区域预约显示正常
if map_name in Appoint.get_appointment_list_map_name():
    logger.debug("区域预约显示正常-地图名称显示正确")
    log("区域预约显示正常-地图名称显示正确")
else:
    snapshot(msg='当前地图名称不在区域预约列表中,截图检查')
    raise AssertionError("当前地图名称不在区域预约列表中")
# # 退出清扫预约列表，返回更多页面
# poco(name='com.eco.global.app:id/title_back').click()
    
log("步骤三：进入更多-重置当前地图")
# 退出工作预约->更多
Appoint.working_appointment_to_more()
# 删除的是正在使用的地图
MoreResetMaps.click_reset_map_button()
# **期望结果**  
# 跳出弹窗：
# 确认删除该地图并清空相关的预约？
MoreResetMaps.check_reset_map_popMsg()
# 取消  删除

log("步骤四：点击删除")
poco(name='com.eco.global.app:id/tv_neutral', text='删除').click()
try:
    poco(name='com.eco.global.app:id/top_status_more').wait_for_appearance()
except Exception as e:
    raise e("重置地图后没有回到主界面")
# **期望结果**  
# 确认当前界面不显示之前地图名称
## 重置成功后，自动从更多返回主界面
# 可能会有pop消息弹出，点击popmsg
Main.click_any_popMsg_on_main()
# 可能会有，点击准备建图的下一步
if poco(text="准备建图").exists():
    Sweep.check_perpare_for_sweep_pic()
## 检查主界面的地图名称与之前的不同
if mapmgr.get_current_using_map_name() != map_name:
    logger.debug("重置地图后，主界面地图正确切换")
    log("重置地图后，主界面地图正确切换")
else:
    logger.debug("重置后地图名称：" + mapmgr.get_current_using_map_name())
    logger.debug("重置前地图名称：" + map_name)
    log("重置后地图名称：" + mapmgr.get_current_using_map_name())
    log("重置前地图名称：" + map_name)
    snapshot("重置地图后，主界面地图切换失败,截图检查")
    raise AssertionError("重置地图后，主界面地图切换失败")

log("步骤五：进入更多-清扫预约")
## 进入更多-工作预约
More.main_to_more()
Appoint.more_to_working_appointment()
# **期望结果**  
# 原地图的区域预约消失不显示
## 点击区域预约列表
Appoint.click_appointment_type_of_list('area')
## 区域预约列表中的地图名称没有之前地图名
if Appoint.get_appointment_list_map_name() == None:
    logger.debug("区域预约列表中的地图名称没有之前地图名[1]")
    log("区域预约列表中的地图名称没有之前地图名[1]")
elif map_name not in Appoint.get_appointment_list_map_name():
    logger.debug("区域预约列表中的地图名称没有之前地图名[2]")
    log("区域预约列表中的地图名称没有之前地图名[2]")
else:
    raise AssertionError("原地图的区域预约没有消失")
    
# 恢复设置
# teardown()