<<<<<<< HEAD
<<<<<<< HEAD
# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng:ZJ1921-898 验证重命名后，更多页面地宝命名与设备列表命名一致"
__case_theme__ = "ZJ1921-898 验证重命名后，更多页面地宝命名与设备列表命名一致 "
"""
## 概要:ZJ1921-898 验证重命名后，更多页面地宝命名与设备列表命名一致  
=======
# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng"
__case_theme__ = "ZJ1921-898 验证重命名后，更多页面地宝命名与设备列表命名一致"
"""
 ## 概要:ZJ1921-898 验证重命名后，更多页面地宝命名与设备列表命名一致  
>>>>>>> dd196aee2fce228a2934b23f7e00c9ea2d2e531d
**描述**:1.配网成功，2.APP点击设备列表，3.点击主机进入主界面4.主机处于待机状态  
**前提条件**:1.配网成功，2.APP点击设备列表，3.点击主机进入主界面4.主机处于待机状态  
**步骤ID 1**  
APP在主界面点击更多->其他，查看主机重命名  
**期望结果**  
主机显示默认命名：
重命名     Deebot T8>  
**步骤ID** 2  
点击“>”  
**期望结果**  
APP显示：左上角“取消”“重命名”右上角“保存”
输入框（Deebot T8）
最多输入32位字符  
**步骤ID** 3  
重命名页面，输入新名称“小白”，点击“保存”按钮  
**期望结果**  
可以重命名主机
命名成功后点击右上角保存
页面自动返回到更多 > 其他界面
地宝为修改之后的名字：小白  
**步骤ID** 4  
点击“返回”设备列表，查看地宝命名  
**期望结果**  
<<<<<<< HEAD
更多页面地宝命名与设备列表命名一致  
=======
更多页面地宝命名与设备列表命名一致 
>>>>>>> dd196aee2fce228a2934b23f7e00c9ea2d2e531d
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
<<<<<<< HEAD
import UniversalModule, Sweep, Charge, Main, More, Rename
=======
import UniversalModule, Sweep, Main, More, rename
>>>>>>> dd196aee2fce228a2934b23f7e00c9ea2d2e531d
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "898"

<<<<<<< HEAD
auto_setup(__file__) 

log(":1.配网成功，2.APP点击设备列表，3.点击主机进入主界面4.主机处于待机状态")
auto_setup(__file__)

log("步骤1:APP在主界面点击更多->其他，查看主机重命名") 
More.main_to_more()
More.more_to_additional()

'''期望结果:主机显示默认命名：DEEBOT T8 MAX ''' 
if Rename.check_default_name() == "DEEBOT T8 MAX":
    logger.debug("地宝默认名称显示正确")
else:
    raise AssertionError("地宝默认名称显示错误")

log("# 步骤2:点击'>'")
Rename.more_to_rename()

'''
# 期望结果
# APP显示：左上角“取消”“重命名”右上角“保存”
# 输入框（Deebot T8）
# 最多输入32位字符
'''
Rename.check_rename_show()

log('**步骤ID** 3 :重命名页面，输入新名称“小白”，点击“保存”按钮')  
Rename.clean_deboot_name()
Rename.set_deboot_name()
Rename.save_set()

'''**期望结果**  可以重命名主机
# 命名成功后点击右上角保存
# 页面自动返回到更多 > 其他界面
# 地宝为修改之后的名字：小白
'''
if Rename.get_more_rename() == "小白":
    logger.debug("重命名成功")
else:
    raise AssertionError("重命名失败")

=======
# -*- encoding=utf8 -*-
__author__ = "fangjiu.cheng"
__case_theme__ = "ZJ1921-898 验证重命名后，更多页面地宝命名与设备列表命名一致 "
"""
## 概要:ZJ1921-898 验证重命名后，更多页面地宝命名与设备列表命名一致  
**描述**:1.配网成功，2.APP点击设备列表，3.点击主机进入主界面4.主机处于待机状态  
**前提条件**:1.配网成功，2.APP点击设备列表，3.点击主机进入主界面4.主机处于待机状态  
**步骤ID 1**  
APP在主界面点击更多->其他，查看主机重命名  
**期望结果**  
主机显示默认命名：
重命名     Deebot T8>  
**步骤ID** 2  
点击“>”  
**期望结果**  
APP显示：左上角“取消”“重命名”右上角“保存”
输入框（Deebot T8）
最多输入32位字符  
**步骤ID** 3  
重命名页面，输入新名称“小白”，点击“保存”按钮  
**期望结果**  
可以重命名主机
命名成功后点击右上角保存
页面自动返回到更多 > 其他界面
地宝为修改之后的名字：小白  
**步骤ID** 4  
点击“返回”设备列表，查看地宝命名  
**期望结果**  
更多页面地宝命名与设备列表命名一致  
"""
import time
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'D:\airtest01\冒烟测试用例\zj1921\zj1921\base')
from import_package import *
import UniversalModule, Sweep, Charge, Main, More, Rename
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)

# setup()
# 从设备列表进入主界面		
# Main.deviceslist_to_main_with_first_device()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# MQ准备数据
case_name = "898"

auto_setup(__file__) 

log(":1.配网成功，2.APP点击设备列表，3.点击主机进入主界面4.主机处于待机状态")
auto_setup(__file__)

log("步骤1:APP在主界面点击更多->其他，查看主机重命名") 
More.main_to_more()
More.more_to_additional()

'''期望结果:主机显示默认命名：DEEBOT T8 MAX ''' 
if Rename.check_default_name() == "DEEBOT T8 MAX":
    logger.debug("地宝默认名称显示正确")
else:
    raise AssertionError("地宝默认名称显示错误")

log("# 步骤2:点击'>'")
Rename.more_to_rename()

'''
# 期望结果
# APP显示：左上角“取消”“重命名”右上角“保存”
# 输入框（Deebot T8）
# 最多输入32位字符
'''
Rename.check_rename_show()

log('**步骤ID** 3 :重命名页面，输入新名称“小白”，点击“保存”按钮')  
Rename.clean_deboot_name()
Rename.set_deboot_name()
Rename.save_set()

'''**期望结果**  可以重命名主机
# 命名成功后点击右上角保存
# 页面自动返回到更多 > 其他界面
# 地宝为修改之后的名字：小白
'''
if Rename.get_more_rename() == "小白":
    logger.debug("重命名成功")
else:
    raise AssertionError("重命名失败")

>>>>>>> 1309aaf9ff3f9e144f0563f0ae32c0e536ee398c
=======
auto_setup(__file__)

log('**步骤ID 1:APP在主界面点击更多->其他，查看主机重命名')
More.main_to_more()
More.more_to_additional()
sleep(5)

'''**期望结果**主机显示默认命名：重命名 Deebot T8 MAX>'''
if rename.check_default_name() == "DEEBOT T8 MAX":
    logger.debug("默认名称显示正确")
else:
    raise AssertionError("地宝默认名称显示有误")
'''
**步骤ID** 2  
点击“>”  
**期望结果**  
APP显示：左上角“取消”“重命名”右上角“保存”
输入框（Deebot T8）
最多输入32位字符  
**步骤ID** 3  
重命名页面，输入新名称“小白”，点击“保存”按钮  
**期望结果**  
可以重命名主机
命名成功后点击右上角保存
页面自动返回到更多 > 其他界面
地宝为修改之后的名字：小白  
**步骤ID** 4  
点击“返回”设备列表，查看地宝命名  
**期望结果**  
更多页面地宝命名与设备列表命名一致 
'''

>>>>>>> dd196aee2fce228a2934b23f7e00c9ea2d2e531d
