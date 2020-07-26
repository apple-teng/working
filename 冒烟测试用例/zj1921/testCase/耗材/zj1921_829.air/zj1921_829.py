# -*- encoding=utf8 -*-
__author__ = "lei.z_验证地宝清扫过程中，可以复位边刷耗材"
__case_theme__ = "验证地宝清扫过程中，可以复位边刷耗材"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
using("base\Accessories.air")
import Accessories
using("base\Sweep.air")
import Sweep
using("base\\More.air")
import More
using(r"base\\UniversalModule.air")
import UniversalModule
using(r"base\\Charge.air")
import Charge


auto_setup(__file__)

#概要:ZJ1921-829验证地宝清扫过程中，可以复位边刷耗材
#测试用例集:软件功能-冒烟测试用例/更多/耗材
#描述:手机和地宝主机已连接
#
# 返回至主界面
UniversalModule.back_to_main()
#地宝主机正在执行清扫工作
Sweep.click_auto_btn()
sleep(10)
#步骤ID1 地宝在清扫过程中，打开更多->其他->点击耗材计时
assert_equal("", "", "步骤1 地宝在清扫过程中，打开更多->其他->点击耗材计时.")
#期望结果
#进入更多界面
More.main_to_more()
UniversalModule.assert_exists_check(poco("com.eco.global.app:id/titleContent"),check_info="检查进入更多页面")
#进入其他页面
More.more_to_additional()
UniversalModule.assert_exists_check(poco(text="耗材计时"),check_info="检查进入更多-其他页面")
#打开耗材页面
Accessories.more_to_accessories()
Accessories.check_accessories_exists(accessory_name = '边刷')
Accessories.check_accessories_exists(accessory_name = '滚刷')
Accessories.check_accessories_exists(accessory_name = '滤芯')


#步骤ID2 点击边刷复位耗材按钮
side_brush_remain_percent1 = Accessories.get_remain_percent(accessory_name = '边刷')
Accessories.reset_accessories(accessory_name = '边刷')
#期望结果
#弹出弹框‘确认已更换边刷耗材？’取消/确认
UniversalModule.assert_exists_check(poco("com.eco.global.app:id/tv_content"),check_info="检查进入更多页面")

#步骤ID3 点击取消按钮
poco("com.eco.global.app:id/tv_cancel").click(sleep_interval=1)
#期望结果
#耗材剩余百分比数值未被重置，地宝正常工作
side_brush_remain_percent2 = Accessories.get_remain_percent(accessory_name = '边刷')
UniversalModule.assert_result_equal(side_brush_remain_percent1,side_brush_remain_percent2,check_info="检查重置取消后剩余时间无变化")
snapshot("检查重置取消后剩余时间无变化")

#步骤ID4 重复步骤2，点击确认按钮
Accessories.reset_accessories(accessory_name = '边刷')
poco("com.eco.global.app:id/tv_positive").click(sleep_interval=1)
#期望结果
#耗材剩余百分比数值被重置为100%，地宝正常工作
side_brush_remain_percent3 = Accessories.get_remain_percent(accessory_name = '边刷')
UniversalModule.assert_result_equal(side_brush_remain_percent3,"100",check_info="检查重置后剩余时间为100")
snapshot("检查重置后剩余时间为100")
# 返回至主界面
UniversalModule.back_to_main()
sleep(5)
if Sweep.get_deebot_status() == '清扫':
    Charge.set_finish_sweep_to_charge()
elif Sweep.get_deebot_status() == '回充':
    UniversalModule.wait_element_expected(poco("com.eco.global.app:id/battery_charging_icon"),snapshot(msg="主机回充成功"),10)
else:
    pass
UniversalModule.wait_element_expected(poco("com.eco.global.app:id/battery_charging_icon"),snapshot(msg="主机回充成功"),10)
    
        
