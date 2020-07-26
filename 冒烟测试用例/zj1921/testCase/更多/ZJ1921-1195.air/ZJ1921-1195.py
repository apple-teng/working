<<<<<<< HEAD
# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng:ZJ1921-1195 验证主机自动清扫过程中，点击寻找地宝"

__case_theme__ = "ZJ1921-1195 验证主机自动清扫过程中，点击寻找地宝"
"""
## 概要:ZJ1921-1195 验证主机自动清扫过程中，点击寻找地宝  
**描述**:主机正在自动清扫  
**前提条件**:主机正在自动清扫  
**步骤ID 1**  
点击“清扫”，使主机开始自动清扫  
**期望结果**  
主机开始自动清扫  
**步骤ID** 2  
更多页面，点寻找地宝  
**期望结果**  
主机播放语音，主机继续自动清扫
app更多页面：有寻找地宝的动效（播放时间与语音一致）
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule, Sweep,More,findDeebot
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "1195"

auto_setup(__file__) 

log("前提条件:主机正在自动清扫")

log('**步骤ID 1**:点击“清扫”，使主机开始自动清扫')
Sweep.click_auto_btn()
sleep(5)
'''
**期望结果**  
主机开始自动清扫
'''
if Sweep.get_auto_btn_status() == "清扫":
    logger.debug("主机正在清扫中")
else:
    raise AssertionError("主机未开始清扫任务")

log('**步骤ID** 2:更多页面，点寻找地宝')
More.main_to_more()

'''
**期望结果**  
主机播放语音，主机继续自动清扫
app更多页面：有寻找地宝的动效（播放时间与语音一致）
'''
findDeebot.check_deebot_icon()
findDeebot.find_deebot_response_icon()
=======
# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng"

__case_theme__ = "ZJ1921-1195 验证主机自动清扫过程中，点击寻找地宝"
"""
## 概要:ZJ1921-1195 验证主机自动清扫过程中，点击寻找地宝  
**描述**:主机正在自动清扫  
**前提条件**:主机正在自动清扫  
**步骤ID 1**  
点击“清扫”，使主机开始自动清扫  
**期望结果**  
主机开始自动清扫  
**步骤ID** 2  
更多页面，点寻找地宝  
**期望结果**  
主机播放语音，主机继续自动清扫
app更多页面：有寻找地宝的动效（播放时间与语音一致）
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule, Sweep,More,findDeebot
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# MQ准备数据
case_name = "1195"
auto_setup(__file__) 
log("前提条件:主机正在自动清扫")
log('**步骤ID 1**:点击“清扫”，使主机开始自动清扫')
Sweep.click_auto_btn()
sleep(5)
'''
**期望结果**  
主机开始自动清扫
'''
if Sweep.get_auto_btn_status() == "清扫":
    logger.debug("主机正在清扫中")
else:
    raise AssertionError("主机未开始清扫任务")
log('**步骤ID** 2:更多页面，点寻找地宝')
More.main_to_more()
'''
**期望结果**  
主机播放语音，主机继续自动清扫
app更多页面：有寻找地宝的动效（播放时间与语音一致）
'''
findDeebot.check_deebot_icon()
findDeebot.find_deebot_response_icon()
>>>>>>> 1309aaf9ff3f9e144f0563f0ae32c0e536ee398c
