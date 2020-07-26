# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-372 验证区域清扫完成自动回充成功"
__case_theme__ = "ZJ1921-372 验证区域清扫完成自动回充成功"
"""
## 概要:ZJ1921-372 验证区域清扫完成自动回充成功  

**前提条件**:1.主机有图  

**步骤ID 1**  
打开APP，进入主机页面  
**期望结果**  
主机在充电座上待机。
APP上显示动态充电图标；
有清扫记录小卡片，
显示地图轮廓，地宝位置，充电座位置，清扫轨迹；
按钮显示“地图管理”“清扫”“回充”
可滑动选择“区域”“自动”“自定义”；  
**步骤ID** 2  
选中“区域”，点击清扫  
**期望结果**  
主机开始区域清扫。 
APP显示 清扫页面： 
APP显示 “虚拟墙”“暂停”“结束”按钮； 状态显示“清扫”； 
清扫面积和清扫时长随着实际清扫变化； 
地图显示清扫轨迹，充电座位置，地宝位置； 选中的区域高亮显示，未选中的区域灰暗显示  
**步骤ID** 3  
等待主机区域清扫完成  
**期望结果**  
主机开始回充； APP清扫页面显示“清扫已完成，返回充电”3S 弱提示消失并显示回充页面； APP状态显示回充； “停止”按钮；  
**步骤ID** 4  
回充成功  
**期望结果**  
主机在充电座上待机。
APP上显示动态充电图标；
清扫记录小卡片显示：区域清扫 XX年XX月XX日   清扫时间 | 清扫面积；
app上呈现清扫轨迹，清扫的区域的编号以及名称  
**步骤ID** 5  
点击生成的清扫小卡片  
**期望结果**  
显示清扫日志界面  
**步骤ID** 6  
点击日志中的清扫的单条日志  
**期望结果**  
app显示清扫日期，清扫时间，清扫类型，清扫面积，清扫时长，结束原因，选中的区域显示清扫路径以及清扫编号和清扫区域的名称，未选中的区域灰色显示
分享按钮  
**步骤ID** 7  
点击分享按钮  
**期望结果**  
app弹出朋友圈，微信好友，QQ空间，新浪微博这四个分享当时
取消按钮  
**步骤ID** 8  
点击取消  
**期望结果**  
弹框消失，显示单条日志   
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

log("**前提条件**:1.主机有图，导入地图-只有地图1")

# 使主机在充电座待机
logger.debug("使主机在充电座待机")
log("使主机在充电座待机")
Charge.anyhow_go_charge()
log("导入地图-只有地图1")
cp_cmd = 'cp -r ' + MAP1_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
app.telnet_to_deboot(cmd)    
# MQ准备数据
case_name = "372"

log("步骤一：打开APP，进入主机页面")
# 上述步骤已开打app
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)
# **期望结果**  
# 主机在充电座上待机，PP上显示动态充电图标；
## 前提条件已经验证了
# 有清扫记录小卡片，
SweepCard.check_sweep_card_exist(expectation='存在')
# 显示地图轮廓，地宝位置，充电座位置，清扫轨迹；
# 按钮显示“地图管理”“清扫”“回充”,可滑动选择“区域”“自动”“自定义”；
Main.click_area_to_area_clean()
Main.click_any_popMsg_on_main()
Main.click_custom_to_custom_clean()
Main.click_any_popMsg_on_main()
Main.check_bottom_elements()

log("步骤二：选中“区域”，点击清扫")
Main.click_area_to_area_clean()
Main.click_any_popMsg_on_main()
try:
    wait(Template(r"tpl1594020710846.png", record_pos=(0.092, 0.443), resolution=(1080, 2340)))    
except:
    snapshot("区域界面没有区域A")
    raise AssertionError("区域界面没有区域A")
touch(Template(r"tpl1594020710846.png", record_pos=(0.092, 0.443), resolution=(1080, 2340)))
# 点击清扫按钮
Sweep.click_auto_btn()
Main.click_any_popMsg_on_main()   
# **期望结果**  
# 主机开始区域清扫
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "start" # 开始清扫
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot start message'") 
# APP显示 清扫页面： 
# APP显示 “虚拟墙”“暂停”“结束”按钮； 状态显示“清扫”； 
# 清扫面积和清扫时长随着实际清扫变化； 
## 先取出当前主机的清扫时间和面积
area1 = Sweep.get_area()
clean_time1 = Sweep.get_clean_time()
logger.debug("area1,clean_time1:" + area1+','+clean_time1)
log("area1,clean_time1:" + area1+','+clean_time1)
sleep(150)
area2 = Sweep.get_area()
clean_time2 = Sweep.get_clean_time()
logger.debug("area2,clean_time2:" + area2+','+clean_time2)
log("area2,clean_time2:" + area2+','+clean_time2)
if (area1 < area2) and (clean_time1 < clean_time2):
    log("清扫面积和清扫时长随着实际清扫变化")
else:
    raise AssertionError("清扫面积和清扫时长没有随着实际清扫变化")
# 地图显示清扫轨迹，充电座位置，地宝位置； 选中的区域高亮显示，未选中的区域灰暗显示
## 通过截图查看
snapshot(msg="查看:地图显示清扫轨迹，充电座位置，地宝位置； 选中的区域高亮显示，未选中的区域灰暗显示")

log("步骤三：等待主机区域清扫完成")
# 等待主机状态为回充
element = poco(name='com.eco.global.app:id/deebot_statues',text='回充')
UniversalModule.wait_element_expected(element,log('主机开始回充'))
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "recharge" # 开始回充
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot recharge message'") 
# **期望结果**  
# 主机开始回充； APP清扫页面显示“清扫已完成，返回充电”3S 弱提示消失并显示回充页面； APP状态显示回充； “停止”按钮；
## 通过截图查看
snapshot(msg="APP状态显示回充； “停止”按钮")

log("步骤四：回充成功")
# **期望结果**
# 主机在充电座上待机。APP上显示动态充电图标；
Charge.anyhow_go_charge()
Main.click_any_popMsg_on_main()
# 清扫记录小卡片显示：区域清扫 XX年XX月XX日   清扫时间 | 清扫面积；
SweepCard.check_sweep_card_exist(expectation='存在')
SweepCard.check_sweep_area_no_empty()
SweepCard.check_sweep_time_no_empty()
# app上呈现清扫轨迹
## 通过截图查看
snapshot(msg="app上呈现清扫轨迹")

log("步骤五：点击生成的清扫小卡片")
SweepCard.sweepcard_to_worklog()
# **期望结果**
# 显示清扫日志界面
cleaningLog.check_cleaning_log_display()
        
log("步骤六：点击日志中的清扫的单条日志")
cleaningLog.click_the_newest_cleaning_log()
# **期望结果**
# app显示清扫日期，清扫时间，清扫类型，清扫面积，清扫时长，结束原因，选中的区域显示清扫路径以及清扫编号和清扫区域的名称，未选中的区域灰色显示
snapshot('清扫日志详情页截图.png',msg="app显示清扫日期，清扫时间，清扫类型，清扫面积，清扫时长，结束原因，选中的区域显示清扫路径以及清扫编号和清扫区域的名称，未选中的区域灰色显示")
log("步骤七：点击分享按钮")
cleaningLog.click_cleaning_log_share_button()
# **期望结果** 
# app弹出朋友圈，微信好友，QQ空间，新浪微博这四个分享,取消按钮
## 首次分享，会弹出权限申请
cleaningLog.check_share_cleaning_log_display()

log("步骤八：点击取消")
# **期望结果**
# 弹框消失，显示单条日志
cleaningLog.click_to_cancel_share_cleaning_log()
