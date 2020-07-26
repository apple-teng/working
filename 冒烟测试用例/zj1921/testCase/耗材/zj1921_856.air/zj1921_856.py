# -*- encoding=utf8 -*-
__author__ = "lei.z_"
__case_theme__ = 
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
using("base\\Accessories.air")
import Accessories
auto_setup(__file__)
 #概要:ZJ1921-856验证地宝深度reset后，边刷耗材不复位
#测试用例集:软件功能-冒烟测试用例/更多/耗材
#描述:手机和地宝主机已连接
#步骤ID1
#打开APP，在主机列表选择测试地宝，打开主页面
#期望结果
#页面显示正常
#步骤ID2
#点击右上角的“更多->其他”按钮
#期望结果
#打开更多页面
#进入其他页面
#步骤ID3
#点击耗材计时
#期望结果
#打开边刷耗材页面，当前耗材值为X%
#预计剩余时间xx小时
#步骤ID4
#地宝长按reset键后重新配网，点击更多->点击耗材计时
#期望结果
#边刷耗材的剩余小时数和百分比和深度reset之前一致
#概要:ZJ1921-856验证地宝深度reset后，边刷耗材不复位
#测试用例集:软件功能-冒烟测试用例/更多/耗材
#描述:手机和地宝主机已连接
#步骤ID1
#打开APP，在主机列表选择测试地宝，打开主页面
#期望结果
#页面显示正常
#步骤ID2
#点击右上角的“更多->其他”按钮
#期望结果
#打开更多页面
#进入其他页面
#步骤ID3
#点击耗材计时
#期望结果
#打开边刷耗材页面，当前耗材值为X%
#预计剩余时间xx小时
#步骤ID4
#地宝长按reset键后重新配网，点击更多->点击耗材计时
#期望结果
#边刷耗材的剩余小时数和百分比和深度reset之前一致
