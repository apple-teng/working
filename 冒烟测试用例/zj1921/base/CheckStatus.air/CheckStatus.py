# -*- encoding=utf8 -*-
__author__ = "lei.z"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
using('Charge.air')
import Charge

auto_setup(__file__)



# 主机运行模式检查
def device_mode_check():
    """
    function:
        检查主机状态
    args：
        none
    return:
        mode_name：主机当前状态 
    """
    mode_name = ''
    if poco(name='com.eco.global.app:id/deebot_statues').exists() \
        and not poco(name='com.eco.global.app:id/battery_charging_icon').exists():
            mode_name = poco(name='com.eco.global.app:id/deebot_statues').get_text()

    elif poco(name='com.eco.global.app:id/rd_clean_type').exists() \
        and poco(name='com.eco.global.app:id/battery_charging_icon').exists():
            mode_name = "充电座上待机"

    elif poco(name='com.eco.global.app:id/rd_clean_type').exists() \
        and not poco(name='com.eco.global.app:id/battery_charging_icon').exists():
            mode_name = "充电座外待机"
    else:
        raise AssertionError("APP上显示主机当前状态有错误")
            
    return mode_name

# 地图状态检查
def map_check():
    """
    function:
        检查主机地图情况
    args：
        none
    return:
        mode_name：主机当前状态 
    """
    
# 清扫中的信息检查
# 检查清扫状态显示
def cleaning_status_check():
    '''
    主机清扫状态检查
    检查状态文字是否为清扫     
    '''
    pass

# 检查清扫标志显示
def cleaning_icon_check():
    '''
    主机清扫状态检查
    检查页面底部清扫标志
    '''
    pass

# 检查虚拟墙标志显示
def cleaning_virtualwall_check():
    '''
    主机清扫状态检查
    检查页面底部虚拟墙标志
    '''
    pass

# 检查右下角标志显示
def cleaning_right_bottom_icon_check():
    '''
    主机清扫状态检查
    检查页面底部右下角标志
    '''
    pass
# 暂停中
def pause_check():
    pass




# 待机页面检查
def idle_check():
    pass

if __name__ == 'airtest.cli.runner':
    print(device_mode_check())