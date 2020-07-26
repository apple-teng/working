# -*- encoding=utf8 -*-
__author__ = "lei.z_验证查看耗材计时页面"
__case_theme__ = "验证查看耗材计时页面"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

using("base\\More.air")
import More
using("base\\Accessories.air")
import Accessories,setaccessories
using(r"base\\UniversalModule.air")
import UniversalModule
import time
auto_setup(__file__)
host = "192.168.1.104"
# 文件修改内容,操作指令
cmd_str = '{"brush":220,"sidebrush":356,"hepa":235}'
# 耗材文件路径
file_path = "/data/save/lifespan.json"
# 概要:ZJ1921-821 验证查看耗材计时页面  
# 测试用例集:软件功能-冒烟测试用例/更多/耗材  
# 描述:手机和地宝主机已连接  
# 文件修改内容,操作指令
# cmd_str = '{"brush":7100,"sidebrush":550,"hepa":840}'
# setaccessories.set_accessories(host,cmd_str,file_path)
# sleep(20)

# 步骤ID 1  
# 主界面点击更多-其他-耗材计时
assert_equal("", "", "步骤1 主界面点击更多-其他-耗材计时.")

More.main_to_more()
More.more_to_additional()
snapshot('其他.png',msg="更多其他页面截图.")
# 进入耗材页面
Accessories.more_to_accessories()
snapshot('其他.png',msg="耗材页面截图.")
# 期望结果  
# 打开耗材计时页面，页面显示边刷，滚刷，滤芯状态，购买耗材，参照UI

Accessories.check_accessories_exists(accessory_name = '边刷')
Accessories.check_accessories_exists(accessory_name = '滚刷')
Accessories.check_accessories_exists(accessory_name = '滤芯')
# 购买耗材button在下方常驻  

Accessories.accessories_to_more()
# 步骤ID 2 查看边刷 
assert_equal("", "", "步骤2 查看边刷.")

# 期望结果  
# 耗材剩余百分比不同，进度条颜色不一样
# 6%-100%为蓝色进度条，0%-5%为红色进度条并有“告警”提示字样
# 文件修改内容,操作指令
# cmd_str = '{"brush":17100,"sidebrush":8550,"hepa":6840}'
# setaccessories.set_accessories(host,cmd_str,file_path)
sleep(20)
# 进入耗材页面
Accessories.more_to_accessories()
sleep(10)
poco("com.eco.global.app:id/tv_side_brush").wait_for_appearance()
# 查看耗材告警
snapshot(msg='查看耗材告警')

# 检查耗材告警标志存在
Accessories.check_accessories_warn_exists(accessory_name = '边刷')

# 进度条下方显示剩余小时数
# 边刷
# 获取进度条 y pos
pg_side_brush_ypos = poco("com.eco.global.app:id/pg_side_brush").get_position()[1]
# 获取小时数 y pos
side_brush_desc_ypos = poco("com.eco.global.app:id/tv_side_brush_desc").get_position()[1]
UniversalModule.assert_comparison(pg_side_brush_ypos,side_brush_desc_ypos,expectation='less',check_info='检查边刷进度条下方显示剩余小时')
# 查看耗材告警
snapshot(msg='查看耗材告警')
# 步骤ID 3 查看滚刷  
assert_equal("", "", "步骤3 查看滚刷.")
# 期望结果  
# 耗材剩余百分比不同， 进度条颜色不一样
# 6%-100%为蓝色进度条，0%-5%为红色进度条并有“告警”提示字样
Accessories.check_accessories_warn_exists(accessory_name = '滚刷')
# 进度条下方显示剩余小时数  
# 滚刷
# 获取进度条 y pos
pg_roll_brush_ypos = poco("com.eco.global.app:id/pg_side_brush").get_position()[1]
# 获取小时数 y pos
roll_brush_desc_ypos = poco("com.eco.global.app:id/tv_side_brush_desc").get_position()[1]
UniversalModule.assert_comparison(pg_roll_brush_ypos,roll_brush_desc_ypos,expectation='less',check_info='检查滚刷进度条下方显示剩余小时')
# 查看耗材告警
snapshot(msg='查看耗材告警')
# 步骤ID 4 查看滤芯  
assert_equal("", "", "步骤4 查看滤芯.")
# 期望结果  
# 耗材剩余百分比不同，进度条颜色不一样
# 6%-100%为蓝色进度条，0%-5%为红色进度条并有“告警”提示字样
Accessories.check_accessories_warn_exists(accessory_name = '滤芯')
# 进度条下方显示剩余小时数  
# 滤芯
# 获取进度条 y pos
pg_hepa_ypos = poco("com.eco.global.app:id/pg_side_brush").get_position()[1]
# 获取小时数 y pos
hepa_desc_ypos = poco("com.eco.global.app:id/tv_side_brush_desc").get_position()[1]
UniversalModule.assert_comparison(pg_hepa_ypos,hepa_desc_ypos,expectation='less',check_info='检查滤芯进度条下方显示剩余小时')
# 查看耗材告警
snapshot(msg='查看耗材告警')

# 步骤ID 5 点击购买耗材  
assert_equal("", "", "步骤5 点击购买耗材.")
# 期望结果  
# APP跳转至购买商场，当前型号的耗材在购买列表的最上方  


# 步骤ID 6 在耗材计时页面，点击左上角返回按钮 
assert_equal("", "", "步骤6 在耗材计时页面，点击左上角返回按钮.")
Accessories.accessories_to_more()
# 期望结果  
# 返回至更多-其他页面  
UniversalModule.assert_exists_check('检查返回更多-其他页面',poco(text="耗材计时"),expectation='存在')
snapshot(msg='检查返回更多-其他页面')

# 返回至主界面
UniversalModule.back_to_main()