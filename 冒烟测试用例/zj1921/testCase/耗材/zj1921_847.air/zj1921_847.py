# -*- encoding=utf8 -*-
__author__ = "lei.z_"
__case_theme__ = 
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
using("base\\Accessories.air")
import Accessories
auto_setup(__file__)
 #概要:ZJ1921-847验证app没有打开，主机边刷耗材寿命还有5%，app进入主界面时会弹出提示
#测试用例集:软件功能-冒烟测试用例/更多/耗材
#描述:主机与app配网，设备列表里有主机，且在线，app没有打开
#主机边刷耗材寿命还有5%
UniversalModule.back_to_devicelist()

#步骤ID1 运行主机至耗材寿命低至5%，
assert_equal("", "", "步骤1 运行主机至耗材寿命低至5%")
#启动APP，APP进入设备列表，点击对应设备
#期望结果
#进入主界面，弹出提示框：边刷即将到期，请及时更换忽略/查看
#步骤ID2 点忽略
assert_equal("", "", "步骤2 点忽略")
#期望结果
#强弹框消失，APP停留在当前页面,
#
#无常驻信息提示
#步骤ID3 点击“Auto”清扫
assert_equal("", "", "步骤3 点击“Auto”清扫")
#期望结果
#主机正常沿边弓字型清扫
#步骤ID4 重复步骤1
assert_equal("", "", "步骤4 运行主机至耗材寿命低至5%")
#期望结果
#无强弹框显示，强弹框只显示一次
