<<<<<<< HEAD
# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng:ZJ1921-753 验证主机待机情况下，切换风力"

__case_theme__ = "ZJ1921-753 验证主机待机情况下，切换风力"
"""
## 概要:ZJ1921-753 验证主机待机情况下，切换风力  
**描述**:主机待机，未安装抹布支架  
**前提条件**:主机待机，未安装抹布支架  
**步骤ID 1**  
进入主界面，点击更多->工作设置->清扫吸力，选择强劲，点击保存  
**期望结果**  
APP上切换成功，主机“叮”一声  
**步骤ID** 2  
再次进入清扫吸力页面，选择标准，点击保存  
**期望结果**  
APP上切换成功，主机“叮”一声  
**步骤ID** 3  
再次进入清扫吸力页面，选择静音，点击保存  
**期望结果**  
APP上切换成功，主机“叮”一声  
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule,Main, More,MoreSuction,Sweep  
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "753"

auto_setup(__file__) 

log("前提条件：主机待机，未安装抹布支架")

#确保主机在待机状态下
if Sweep.get_auto_btn_status() == "清扫" or Sweep.get_auto_btn_status() == "暂停":
    Sweep.cancel_sweep()
    logger.debug("当前主机工作中，停止清扫")    
else:
    logger.debug("当前主机待机")
sleep(3)
    
log("步骤ID1:进入主界面，点击更多->工作设置->清扫吸力，选择强劲，点击保存")
More.main_to_more()
sleep(5)
MoreSuction.more_to_suction()
MoreSuction.set_suction_level(suction_level='强劲')
'''**期望结果**APP上切换成功，主机“叮”一声'''
# 检测清扫吸力是否设置成功
if MoreSuction.more_suction() == '强劲':
    logger.debug("强劲吸力设置成功")
else:
    raise AssertionError("清扫吸力设置失败")

log('步骤ID2:再次进入清扫吸力页面，选择标准，点击保存')
MoreSuction.more_to_suction()
# 检测清扫吸力界面显示正确
# if MoreSuction.get_suction_level() == "强劲":
#      logger.debug("强劲吸力设置成功")
# else:
#     raise AssertionError("清扫吸力设置失败")
# 切换吸力为标准 
MoreSuction.set_suction_level(suction_level='标准')
'''**期望结果**APP上切换成功，主机“叮”一声'''

# 检测清扫吸力设置成功
if MoreSuction.more_suction() == '标准':
    logger.debug("标准吸力设置成功")
else:
    raise AssertionError("清扫吸力设置失败")

log('步骤ID3:再次进入清扫吸力页面，选择静音，点击保存')
MoreSuction.more_to_suction()
# 检测清扫吸力界面显示正确
# if MoreSuction.get_suction_level() == "标准":
#      logger.debug("标准吸力设置成功")
# else:
#     raise AssertionError("清扫吸力设置失败")
# 切换吸力为静音 
MoreSuction.set_suction_level(suction_level='静音')
'''**期望结果**APP上切换成功，主机“叮”一声'''

# 检测清扫吸力设置成功
if MoreSuction.more_suction() == '静音':
    logger.debug("静音吸力设置成功")
else:
    raise AssertionError("清扫吸力设置失败")
    
log('步骤ID4:再次进入清扫吸力页面，选择超强，点击保存')
MoreSuction.more_to_suction()

# 检测清扫吸力界面显示正确
# if MoreSuction.get_suction_level() == "静音":
#      logger.debug("静音吸力设置成功")
# else:
#     raise AssertionError("清扫吸力设置失败")
# 切换吸力为超强 
MoreSuction.set_suction_level(suction_level='超强')
'''**期望结果**APP上切换成功，主机“叮”一声'''

# 检测清扫吸力设置成功
if MoreSuction.more_suction() == '超强':
    logger.debug("超强吸力设置成功")
else:
    raise AssertionError("清扫吸力设置失败")

# 检测清扫吸力界面显示正确
# MoreSuction.more_to_suction()
# if MoreSuction.get_suction_level() == "超强":
#      logger.debug("超强吸力设置成功")
# else:
#     raise AssertionError("清扫吸力设置失败")
<<<<<<< HEAD
=======
# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng"

__case_theme__ = "ZJ1921-753 验证主机待机情况下，切换风力"
"""
## 概要:ZJ1921-753 验证主机待机情况下，切换风力  
**描述**:主机待机，未安装抹布支架  
**前提条件**:主机待机，未安装抹布支架  
**步骤ID 1**  
进入主界面，点击更多->工作设置->清扫吸力，选择强劲，点击保存  
**期望结果**  
APP上切换成功，主机“叮”一声  
**步骤ID** 2  
再次进入清扫吸力页面，选择标准，点击保存  
**期望结果**  
APP上切换成功，主机“叮”一声  
**步骤ID** 3  
再次进入清扫吸力页面，选择静音，点击保存  
**期望结果**  
APP上切换成功，主机“叮”一声  
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule,Main, More,MoreSuction,Sweep  
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "753"

auto_setup(__file__) 

log("前提条件：主机待机，未安装抹布支架")

#确保主机在待机状态下
if Sweep.get_auto_btn_status() == "清扫" or Sweep.get_auto_btn_status() == "暂停":
    Sweep.cancel_sweep()
    logger.debug("当前主机工作中，停止清扫")    
else:
    logger.debug("当前主机待机")
sleep(3)
    
log("步骤ID1:进入主界面，点击更多->工作设置->清扫吸力，选择强劲，点击保存")
More.main_to_more()
sleep(5)
MoreSuction.more_to_suction()
MoreSuction.set_suction_level(suction_level='强劲')
'''**期望结果**APP上切换成功，主机“叮”一声'''
# 检测清扫吸力是否设置成功
if MoreSuction.more_suction() == '强劲':
    logger.debug("强劲吸力设置成功")
else:
    raise AssertionError("清扫吸力设置失败")

log('步骤ID2:再次进入清扫吸力页面，选择标准，点击保存')
MoreSuction.more_to_suction()
# 检测清扫吸力界面显示正确
# if MoreSuction.get_suction_level() == "强劲":
#      logger.debug("强劲吸力设置成功")
# else:
#     raise AssertionError("清扫吸力设置失败")
# 切换吸力为标准 
MoreSuction.set_suction_level(suction_level='标准')
'''**期望结果**APP上切换成功，主机“叮”一声'''

# 检测清扫吸力设置成功
if MoreSuction.more_suction() == '标准':
    logger.debug("标准吸力设置成功")
else:
    raise AssertionError("清扫吸力设置失败")

log('步骤ID3:再次进入清扫吸力页面，选择静音，点击保存')
MoreSuction.more_to_suction()
# 检测清扫吸力界面显示正确
# if MoreSuction.get_suction_level() == "标准":
#      logger.debug("标准吸力设置成功")
# else:
#     raise AssertionError("清扫吸力设置失败")
# 切换吸力为静音 
MoreSuction.set_suction_level(suction_level='静音')
'''**期望结果**APP上切换成功，主机“叮”一声'''

# 检测清扫吸力设置成功
if MoreSuction.more_suction() == '静音':
    logger.debug("静音吸力设置成功")
else:
    raise AssertionError("清扫吸力设置失败")
    
log('步骤ID4:再次进入清扫吸力页面，选择超强，点击保存')
MoreSuction.more_to_suction()

# 检测清扫吸力界面显示正确
# if MoreSuction.get_suction_level() == "静音":
#      logger.debug("静音吸力设置成功")
# else:
#     raise AssertionError("清扫吸力设置失败")
# 切换吸力为超强 
MoreSuction.set_suction_level(suction_level='超强')
'''**期望结果**APP上切换成功，主机“叮”一声'''

# 检测清扫吸力设置成功
if MoreSuction.more_suction() == '超强':
    logger.debug("超强吸力设置成功")
else:
    raise AssertionError("清扫吸力设置失败")

# 检测清扫吸力界面显示正确
# MoreSuction.more_to_suction()
# if MoreSuction.get_suction_level() == "超强":
#      logger.debug("超强吸力设置成功")
# else:
#     raise AssertionError("清扫吸力设置失败")

