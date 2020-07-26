# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng:ZJ1921-851 验证主机边刷耗材寿命还有0%，app进入主界面时会弹出提示"

__case_theme__ = "概要:ZJ1921-851 验证主机边刷耗材寿命还有0%，app进入主界面时会弹出提示"
"""
## 概要:ZJ1921-851 验证主机边刷耗材寿命还有0%，app进入主界面时会弹出提示  
**描述**:主机与app配网，设备列表里有主机，且在线

主机耗材寿命还有0%  
**前提条件**:主机与app配网，设备列表里有主机，且在线 主机耗材寿命还有0%  
**步骤ID 1**  
在手机APP不在线的情况下，运行主机至耗材寿命低至0%，

启动APP，APP进入设备列表，点击对应设备  
**期望结果**  
进入主界面，弹出提示框： 
边刷已到期，请及时更换
 忽略/查看  
**步骤ID** 2  
点忽略  
**期望结果**  
强弹框消失，APP停留在当前页面,

告警栏有常驻提示  
**步骤ID** 3  
点击“Auto”清扫  
**期望结果**  
主机正常 沿边弓字型清扫  
**步骤ID** 4  
APP操控页面有告警常驻信息  
**期望结果**  
告警栏有常驻提示“边刷已到期，请更换”  
**步骤ID** 5  
点击APP上告警栏  
**期望结果**  
APP 跳转到耗材详情页；  
**步骤ID** 6  
重复步骤1，点查看  
**期望结果**  
跳转到耗材到期页面  
**步骤ID** 7  
耗材计时中点击复位耗材  
**期望结果**  
返回APP主界面，告警栏提示消失  
**步骤ID** 8  
重复步骤1，切换APP至后台后再次打开APP  
**期望结果**  
APP仍停留在主界面，告警弹框存在并等待确认  

"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule,Main, More,Accessories,setaccessories,Sweep
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "851"

auto_setup(__file__) 

log('前提条件：主机与app配网，设备列表里有主机，且在线 主机耗材寿命还有0')
## 概要:ZJ1921-851 验证主机边刷耗材寿命还有0%，app进入主界面时会弹出提示  
log('**步骤ID 1**:在手机APP不在线的情况下，运行主机至耗材寿命低至0%，启动APP，APP进入设备列表，点击对应设备') 
setaccessories.set_accessories()
sleep(5)
Main.deviceslist_to_main()
sleep(3)
    
'''    
**期望结果**  
进入主界面，弹出提示框： 
边刷已到期，请及时更换
 忽略/查看  
'''
Accessories.check_sidebrach_exhaust_sp_window()

log('**步骤ID** 2:点忽略')
Accessories.choose_lgnore()    
'''    
**期望结果**  
强弹框消失，APP停留在当前页面,
告警栏有常驻提示  
'''
Accessories.check_sidebrach_esident_prompt()
      
log('**步骤ID**3:点击“Auto”清扫')
Sweep.click_auto_btn()
sleep(3)
    
'''
**期望结果**  
主机正常 沿边弓字型清扫
'''
if Sweep.get_auto_btn_status() == "清扫":
    logger.debug("主机正在清扫")
else:
    raise AssertionError("主机未开始清扫任务")
    
log('**步骤ID** 4:查看APP操控页面有告警常驻信息')
'''
**期望结果**  
告警栏有常驻提示“边刷已到期，请更换”
'''
Accessories.check_sidebrach_esident_prompt()

log('**步骤ID** 8:重复步骤1，切换APP至后台后再次打开APP')
Main.main_to_deviceslist()
sleep(3)
Main.deviceslist_to_main(DEEBOT T8 MAX)
'''
**期望结果**  
APP仍停留在主界面，告警弹框存在并等待确认
'''
Accessories.check_sidebrach_esident_prompt()
      
log('**步骤ID**5:点击APP上告警栏')
Accessories.into_sidebrach_esident_prompt()
''''    
**期望结果**  
APP 跳转到耗材详情页；
'''
Accessories.check_sidebrach_exhaust_show()
Accessories.reset_sidebrush()
Accessories.check_reset_sidebrach()
Accessories.reset_or_cancel(choose = "确定")
sleep(5)
    
log('**步骤ID** 6重复步骤1，点查看')
setaccessories.set_accessories()
sleep(5)
Main.deviceslist_to_main()
sleep(3)
Accessories.check_sidebrach_exhaust_sp_window()
Accessories.choose_examine()    

'''
**期望结果**  
跳转到耗材到期页面
'''
Accessories.check_sidebrach_exhaust_show()    
log('**步骤ID** 7:耗材计时中点击复位耗材')
Accessories.reset_sidebrush()    
Accessories.check_reset_sidebrach()
Accessories.reset_or_cancel(choose = "确定")
'''
**期望结果**  
返回APP主界面，告警栏提示消失
'''
if Accessories.check_sidebrach_esident_prompt() == "存在":
    raise AssertionError(snapshot(msg="常驻提示栏不应该仍显示"))
else:
    logger.debug("常驻提示栏消失")
 




