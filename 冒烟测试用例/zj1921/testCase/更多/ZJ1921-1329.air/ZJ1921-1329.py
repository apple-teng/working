# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng:ZJ1921-1329 验证主机清扫过程中手动回充生成工作日志状态显示"

__case_theme__ = "概要:ZJ1921-1329 验证主机清扫过程中手动回充生成工作日志状态显示"
"""
## 概要:ZJ1921-1329 验证主机清扫过程中手动回充生成工作日志状态显示  
**描述**:验证主机清扫过程中手动回充生成工作日志状态显示_x000D_
_x000D_
前提：APP为新版本，并已绑定主机且在设备在线，主机有图  
**前提条件**:APP为新版本，并已绑定主机且在设备在线，主机有图  
**步骤ID 1**  
点击主机进入APP主界面，点击清扫按钮  
**期望结果**  
主机开始自动清扫  
**步骤ID** 2  
主机清扫过程中点击返回充电按钮  
**期望结果**  
APP跳出弹框：                
返回充电   
结束清扫任务                
取消  
**步骤ID** 3  
点击返回充电  
**期望结果**  
主机语音播报：“返回充电”        
APP状态显示回充                
返回充电座后页面通知栏显示清扫记录小卡片：                      
自动清扫    
日期  
清扫开始时间                         
清扫面积    
清扫时长  
**步骤ID** 4  
点击清扫记录小卡片  
**期望结果**  
页面跳转到工作日志界面    
返回  
工作日志                      
累计面积  
工作次数   
累计时长                          
清扫记录列表（新生成的清扫日志显示在第一位，日期改显示为今天，左侧显示清扫结束状态图标）  
**步骤ID** 5  
点击第3步生成的清扫记录  
**期望结果**  
页面跳转到工作日志详情界面：
返回                        
清扫异常结束状态图标   
今天XX：XX自动清扫                   
清扫面积  清扫时长          
结束工作原因：清扫被人为结束  
清扫地图  
清扫轨迹                     
分享  
**步骤ID** 6  
点击左上角返回  
**期望结果**  
页面返回至工作日志界面，刚查看到清扫记录显示在第一位  
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule,Main, More,Sweep,SweepCard,Charge
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "1329"

auto_setup(__file__) 

log('前提条件：APP为新版本，并已绑定主机且在设备在线，主机有图')

log('**步骤ID 1**:点击主机进入APP主界面，点击清扫按钮')
Sweep.click_auto_btn()

'''
**期望结果**  
主机开始自动清扫
'''
Sweep.check_deebot_status(expectation='清扫')

log('**步骤ID** 2主机清扫过程中点击返回充电按钮')
Sweep.click_rightstop()

'''
**期望结果**  
APP跳出弹框：                
返回充电   
结束清扫任务                
取消
'''
Sweep.check_recharge_or_end()

log('**步骤ID** 3:点击返回充电')
Sweep.click_recharge()

'''
**期望结果**  
主机语音播报：“返回充电”        
APP状态显示回充                
返回充电座后页面通知栏显示清扫记录小卡片：                      
自动清扫    
日期  
清扫开始时间                         
清扫面积    
清扫时长  
'''
Sweep.check_deebot_status(expectation='回充')
sleep(10)
Charge.check_deebot_on_charger()
sleep(10)
Charge.check_sweep_card_exist(expectation='存在')
log('**步骤ID** 4:点击清扫记录小卡片')
SweepCard.sweepcard_to_worklog()

'''
**期望结果**  
页面跳转到工作日志界面    
返回  
工作日志                      
累计面积  
工作次数   
累计时长                          
清扫记录列表（新生成的清扫日志显示在第一位，日期改显示为今天，左侧显示清扫结束状态图标）  
'''




**步骤ID** 5  
点击第3步生成的清扫记录  
**期望结果**  
页面跳转到工作日志详情界面：
返回                        
清扫异常结束状态图标   
今天XX：XX自动清扫                   
清扫面积  清扫时长          
结束工作原因：清扫被人为结束  
清扫地图  
清扫轨迹                     
分享  
**步骤ID** 6  
点击左上角返回  
**期望结果**  
页面返回至工作日志界面，刚查看到清扫记录显示在第一位  
 
"""


