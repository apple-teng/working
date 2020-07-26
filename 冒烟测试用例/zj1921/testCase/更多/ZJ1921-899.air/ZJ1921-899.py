# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng:ZJ1921-899 验证使用帮助功能完善，且有对应机型配置内容"

__case_theme__ = "ZJ1921-899 验证使用帮助功能完善，且有对应机型配置内容"
"""
## 概要:ZJ1921-899 验证使用帮助功能完善，且有对应机型配置内容  
**描述**:1.配网成功，2.主机处于待机状态  
**前提条件**:1.配网成功，2.主机处于待机状态  
**步骤ID 1**  
APP在主界面右上角点击更多  
**期望结果**  
APP显示：左上角“返回按钮”右上角“寻找地宝”
工作设置，其他
（当前界面显示为工作设置界面）  
**步骤ID** 2  
点击其他，点击使用帮助  
**期望结果**  
APP显示：左上角“返回”“使用帮助”右上角“意见反馈”
常见问题、使用说明书、使用视频
搜索框
常见问题配置内容  
**步骤ID** 3  
查看常见问题内容配置  
**期望结果**  
显示产品部配置列表（对比Android和IOS一致）  
**步骤ID** 4  
点击使用说明书  
**期望结果**  
显示快速操作指南
快速操作指南配置内容
下载完整版说明书（可点击下载完整版说明书）  
**步骤ID** 5  
点击下载完整版说明书  
**期望结果**  
页面下方有下载进度条，直到完整版说明书下载完成  
**步骤ID** 6  
点击查看完整版说明书  
**期望结果**  
显示地面清洁机器人说明书  
**步骤ID** 7  
点击返回  
**期望结果**  
返回使用帮助页  
**步骤ID** 8  
点击使用视频  
**期望结果**  
显示使用视频页面  
**步骤ID** 9  
查看使用视频  
**期望结果**  
可以播放使用视频  
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule, Sweep, Main, More, MoreResetMaps,Help
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "899"

auto_setup(__file__) 

    
log('**步骤ID 1:APP在主界面右上角点击更多')
More.main_to_more()

'''
**期望结果**  
APP显示：左上角“返回按钮”右上角“寻找地宝”
工作设置，其他
（当前界面显示为工作设置界面）
'''
More.check_more()

log('**步骤ID**2:点击其他，点击使用帮助')
More.more_to_additional()
Help.more_to_help()

'''
**期望结果**  
APP显示：左上角“返回”“使用帮助”右上角“意见反馈”
常见问题、使用说明书、使用视频
搜索框
常见问题配置内容
'''
Help.check_help_show()

'''
**步骤ID** 3  
查看常见问题内容配置

**期望结果**  
显示产品部配置列表（对比Android和IOS一致）  
'''

log('**步骤ID**4:点击使用说明书')
Help.into_operation_instruction()

'''
**期望结果**  
显示快速操作指南
快速操作指南配置内容
下载完整版说明书（可点击下载完整版说明书）  
'''
Help.check_operation_instruction_preview()

log('**步骤ID** 5:点击下载完整版说明书')
Help.install_operation_instruction()

'''
**期望结果**  
页面下方有下载进度条，直到完整版说明书下载完成
'''
Help.check_install_operation_instruction()
for i in range(1,10):
    if Help.check_examine_operation_instruction() == '下载成功':
        continue
    else:
        sleep(5)
        i += 1
    
log('**步骤ID** 6:点击查看完整版说明书')
Help.examine_operation_instruction()

'''
**期望结果**  
显示地面清洁机器人说明书
'''
log('**步骤ID** 7点击返回')
Help.operation_instruction_back_help()
'''
**期望结果**  
返回使用帮助页
'''
Help.check_help_start()
log('**步骤ID** 8:点击查看使用视频')
Help.examine_help_video()
sleep(3)

'''
**期望结果**  
可以播放使用视频
'''
Help.check_help_video_ok()
video_back_help()