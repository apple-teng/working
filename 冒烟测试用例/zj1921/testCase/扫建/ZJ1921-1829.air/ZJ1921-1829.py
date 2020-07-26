# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-1829 验证主机不从充电座出发扫建清扫行走逻辑：先4.5x4.5m沿边，再弓字型清扫"
__case_theme__ = "ZJ1921-1829 验证主机不从充电座出发扫建清扫行走逻辑：先4.5x4.5m沿边，再弓字型清扫"
from airtest.core.api import *
"""
前提条件**:主机配网成功无图，非充电座待机，至少1个4.5*4.5m矩形区域  **

步骤ID 1**  
打开APP，进入主界面  
**期望结果**  
APP上方显示：“返回”“Deebot T8”“分享”“更多”“电量”，
示图
暂无地图；
“清扫建图注意事项”链接
可滑动选择“区域”“自动”“自定义”；
按钮显示“地图管理”“清扫”“回充”  
**步骤ID** 2  
先规划一个4.5*4.5m的矩形范围，
主机不在充电座上，点击主界面“清扫”按钮  
**期望结果**  
主机会走到边矩形边界处，按照矩形边界进行逆时针方向4.5*4.5m沿边清扫，沿边清扫完成后进行弓字型清扫，清扫过程中遇到障碍物进行顺时针沿边清扫。
APP显示 清扫页面：
APP显示“虚拟墙” “暂停”“结束”按钮；
状态显示“清扫”；
清扫面积和清扫时长随着实际清扫变化；
地图显示清扫轨迹，地宝位置。  
**步骤ID** 3  
主机扫建完成，开始回充  
**期望结果**  
主机自动回充。
APP页面弱提示“清扫已完成，返回充电”，3秒后消失；
状态显示“回充”；
显示“停止”按钮；
清扫面积和清扫时长显示无变化；
地图显示清扫轨迹，充电座位置，地宝位置。  
**步骤ID** 4  
主机回充成功  
**期望结果**  
主机充电座上待机。

APP显示待机页面：

清扫记录小卡片，显示地图轮廓，地宝位置，充电座位置，清扫轨迹；
可滑动选择“区域”“自动”“自定义”；
按钮显示“地图管理”“清扫”“回充”  
"""
import time,telnetlib
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'E:\airTest\冒烟测试用例\zj1921\base')
from import_package import *
import UniversalModule, Sweep, Charge, Main, More, MoreResetMaps
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)
auto_setup(__file__) 
# 执行脚本的前置操作（包括开启app，进入设备列表，进入主界面）
setup()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# MQ准备数据
case_name = "1829"

log("前提条件:主机配网成功无图，充电座待机，至少1个4.5*4.5m矩形区域")
# 确保主机在充电座
try:
    Charge.check_lighting_icon(expectation='不存在')
    log("主机不在充电座")
    logger.debug("主机不在充电座")
except:
    logger.debug("使主机在充电座外待机")
    log("使主机在充电座外待机")
    Charge.anyhow_standby_out_of_charger()
# 确保主机无图
log("导入地图-无图")
cp_cmd = 'cp -r ' + NO_MAP_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
app.telnet_to_deboot(cmd)

log("步骤一：打开APP，进入主界面") 
# 刷新地图-通过进出主界面
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)
# 预期结果
# APP上方显示：
# 1.存在返回”“Deebot T8”“更多”和不存在“电量”动态充电图标
Main.check_title_elements(charging=0)
# 2.检查建图事项
Main.check_no_map_cue()
# 3.可滑动选择“区域”“自动”“自定义”
Main.click_area_to_area_clean()
Main.click_custom_to_custom_clean()
# 4.按钮显示“地图管理”“清扫”“回充”
Main.check_bottom_elements
    
log('步骤二：先规划一个4.5*4.5m的矩形范围，点击主界面“清扫”按钮；主机不在充电座上，点击主界面“清扫”按钮')
Sweep.click_auto_btn()
main.click_any_popMsg_on_main()
#预期结果：
# 主机会走到边矩形边界处，按照矩形边界进行逆时针方向4.5*4.5m沿边清扫，沿边清扫完成后进行弓字型清扫，清扫过程中遇到障碍物进行顺时针沿边清扫。
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "start" # 开始清扫
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot start message'")    
# APP显示 清扫页面：
# APP显示“虚拟墙” “暂停”“结束”按钮；
    
# 状态显示“清扫”；
if Sweep.get_auto_btn_status() == '清扫':
    log("APP显示 清扫页面")
else:
    raise AssertionError("APP没有显示 清扫页面")    
# 清扫面积和清扫时长随着实际清扫变化；
sleep(60) # 等待主机清扫1min
area1 = Sweep.get_area()
clean_time1 = Sweep.get_clean_time()
logger.debug(area1 + ' - ' + clean_time1)
sleep(60) # 等待主机清扫1min
area2 = Sweep.get_area()
clean_time2 = Sweep.get_clean_time()
logger.debug(area2 + ' - ' + clean_time2)
if (area1 != area2) and (clean_time1 != clean_time2):
    log("清扫面积和清扫时长随着实际清扫变化")
else:
    log("80S前的清扫时间" + clean_time1 + ' , ', + "清扫面积" + area1)
    log("80S后的清扫时间" + clean_time2 + ' , ', + "清扫面积" + area2)
    raise AssertionError("清扫面积和清扫时长在主机清扫期间没有变化")

log("步骤三：主机扫建完成，开始回充")
# 主机自动回充，APP页面弱提示“清扫已完成，返回充电”，3秒后消失
sleep(300) # 等待主机清扫5min
Charge.check_tips_complete_clean_go_charge(expectation='存在')   
logger.debug("捕捉到“清扫已完成，返回充电”")
log("捕捉到“清扫已完成，返回充电”")
Charge.wait_finish_work_go_charge()
logger.debug("主机开始回充")
log("主机开始回充")

# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "recharge" # 返回充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot recharge message'")
# 预期结果：
# 主机自动回充，APP页面弱提示“清扫已完成，返回充电”，3秒后消失；
# log("步骤三：主机扫建完成，开始回充")中包含
# 状态显示“回充”；
Sweep.get_deebot_status() =='回充'
# 显示“停止”按钮；
Charge.check_stop_go_charge_icon(expectation='存在')
# 清扫面积和清扫时长显示无变化；
### 先取出当前主机的清扫时间和面积
area3 = Sweep.get_area()
clean_time3 = Sweep.get_clean_time()
# 地图显示，充电座位置，地宝位置
# Charge.check_deebot_on_charger()
log("步骤三：主机回充成功") 
Charge.anyhow_go_charge()
Main.click_any_popMsg_on_main()
# 上传清扫信息
log(time.strftime("%H:%M:%S"))
body["timestamp"] = int(time.time())
body["action"] = "stop" # 回到充电座
UniversalModule.publish_message2queue(body["sn"],body)
print(" [1] Sent 'deebot stop message'")
### 主机回充成功后，对比主机的清扫时间和面积
area4 = Sweep.get_cleanCard_area()
clean_time4 = Sweep.get_cleanCard_time()
if (area3 == area3) and (clean_time4 == clean_time4):
    log("清扫面积和清扫时长显示无变化")
else:
    log("回充时的清扫时间" + clean_time3 + ' , ', + "清扫面积" + area3)
    log("回充完成的清扫时间" + clean_time4 + ' , ', + "清扫面积" + area4)
    raise AssertionError("清扫面积和清扫时长在主机回充期间有变化")
# 预期结果：
# 清扫记录小卡片，显示地图轮廓，地宝位置，充电座位置，清扫轨迹；
Main.check_sweep_card_exists(expectation='存在')
Charge.check_deebot_on_charger()
# 按钮显示“地图管理”“清扫”“回充” 
if not Sweep.get_all_sweep_mode_name() == ['区域','自动','自定义']:    
    raise AssertionError('主页面的清扫模式缺失')
# 可滑动选择“区域”“自动”“自定义”； 
Sweep.check_map_manager_btn_exist(expectation='存在')
Sweep.check_auto_btn_exist(expectation='存在')
Sweep.check_go_charge_btn_exist(expectation='存在')