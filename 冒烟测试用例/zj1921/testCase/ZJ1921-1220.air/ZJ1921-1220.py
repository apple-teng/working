# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"

from airtest.core.api import *
using(r'E:\airTest\automater\carpet_func.air')
import carpet_func

using(r'E:\airTest\automater\Main.air')
import Main

using(r'E:\airTest\automater\More.air')
import More


auto_setup(__file__)
""""
## 概要:ZJ1921-1220 验证更多中地毯增压界面显示，默认“开启”  
**测试用例集**:软件功能-冒烟测试用例/更多/地毯增压  
**描述**:首次配网成功后，进入更多界面  
**步骤ID 1**  
与主机完成配网后，进入更多--工作设置界面  
**期望结果**  
"地毯增压"功能右侧字段为"开启"  
**步骤ID** 2  
进入"地毯增压"查看页面显示  
**期望结果**  
界面显示：
“返回” 地毯增压
地毯增压 开关（默认绿色开启）
开启后，在清扫模式下，地宝识别到地毯时将自动开启强劲吸力

下方有相应说明：
1.请在非地毯区域启动清扫
2.滚刷缠绕毛发时可能在非地毯界面误启动强吸力模式，请及时清理滚刷  
**步骤ID** 3  
点击“返回”按钮  
**期望结果**  
返回更多-工作设置页面，地毯增压默认“开启”状态 
""""



# 步骤1：与主机完成配网后，进入更多--工作设置界面  
machine_name = 'T8'
log("设备列表进入主页面")
Main.deviceslist_to_main(machine_name)
log("主页面进入更多页面")
More.main_to_more()
#检查地毯增压状态
cappet_status1 = carpet_func.get_status_of_carpet_func()
if cappet_status1 == "开启":
    log("'地毯增压'功能右侧字段为'开启'")
else:
    raise AssertionError("步骤1：'地毯增压'功能右侧字段不为'开启'")

# 步骤2：进入"地毯增压"查看页面显示  
carpet_func.more_to_carpet_func()
# 设置地毯增压开关为 开
carpet_func.click_carpet_func_switch("open")
# 检查在清扫模式下，地宝识别到地毯时将自动开启强劲吸力 --》该步不好做

# 检查地毯增压使用说明文字
carpet_func.check_carpet_func_introduce()

# 步骤3：点击“返回”按钮
carpet_func.carpet_func_to_more()
# 检查地毯增压状态
cappet_status2 = carpet_func.get_status_of_carpet_func()
if cappet_status2 == "开启":
    log("'地毯增压'功能右侧字段为'开启'")
else:
    raise AssertionError("步骤3：'地毯增压'功能右侧字段不为'开启'")



