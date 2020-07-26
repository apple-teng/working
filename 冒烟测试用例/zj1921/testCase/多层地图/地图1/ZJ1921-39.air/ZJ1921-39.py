# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng ZJ1921-39 验证地图重命名文本框格式及功能验证(字符或长度)"
__case_theme__ = "ZJ1921-39 验证地图重命名文本框格式及功能验证(字符或长度)"
"""
前提条件**:多楼层地图功能打开，主机有一张地图已经保存  **

步骤ID 1**  
在地图管理界面，点击“地图重命名”按钮  
**期望结果**  
页面弹出重命名框
默认名称为当前命名
取消  确认  
**步骤ID** 2  
点击输入框  
**期望结果**  
弹出输入键盘  
**步骤ID** 3  
尝试输入16位英文和数字字符  
**期望结果**  
输入超出16字符时，输入框下方显示红色提示文字“最多输入16字符”，且无法点击确人  
**步骤ID** 4  
输入16位中文字符，点确认  
**期望结果**  
重命名成功，页面自动返回更多页面，在更多界面上显示不全的重命名用...代替  
**步骤ID** 5  
返回主界面查看地图名称  
**期望结果**  
主界面的地图名称显示保存后的名字，

显示不全的重命名用...代替 
"""
import time,telnetlib
from airtest.core.api import *
from poco import exceptions
sys.path.append(r'E:\airTest\冒烟测试用例\zj1921\base')
from import_package import *
import UniversalModule, Sweep, Charge, Main, More, MoreResetMaps, mapmgr
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)
auto_setup(__file__) 
# 执行脚本的前置操作（包括开启app，进入设备列表，进入主界面）
setup()	
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# MQ准备数据
case_name = "39"

log("前提条件:多楼层地图功能打开，主机有一张地图已经保存")
# 确保主机在充电座
try:
    Charge.check_lighting_icon(expectation='存在')
    logger.debug("主机在充电座")
except:
    logger.debug("主机当前不在充电座，使其回充")
    Charge.anyhow_go_charge()
    Main.click_any_popMsg_on_main()
log("导入地图-只有地图1")
cp_cmd = 'cp -r ' + MAP1_PATH + DESTINATION_MAP_PATH
cmd = [cp_cmd, REBOOT_CMD]
app.telnet_to_deboot(cmd)
# 刷新地图-通过进出主界面
Main.click_any_popMsg_on_main()
Main.main_to_deviceslist()
Main.deviceslist_to_main_using_first_device()
Main.click_any_popMsg_on_main()
sleep(10)
# 打开多层地图
mapmgr.click_main_to_mapmgr()
# 如果主机有新环境整图，首次打开多层地图，会弹出地图保存的引导框
mapmgr.click_autosave_map_popmsg()
# 如果已经开启了多层地图，app重新安装后首次打开错层地图，会弹出“多层地图建图注意事项”
if poco(name='com.eco.global.app:id/checkbox').exists():
    mapmgr.check_and_click_turn_on_mapmgr_button_notice()
    mapmgr.click_autosave_map_popmsg()
mapmgr.click_mapmgr_switch(mapmgr_switch=1)
# 如果多层地图由关闭->开启，会弹出“多层地图建图注意事项”
if poco(text='多楼层地图建图注意事项').exists():
    mapmgr.check_and_click_turn_on_mapmgr_button_notice()
if poco(text='什么是完整家居地图').exists():
    mapmgr.click_autosave_map_popmsg()

log("步骤一：在地图管理界面，点击“地图重命名”按钮")
try:
    exists(Template(r"tpl1593566122644.png", record_pos=(-0.331, -0.272), resolution=(1080, 1920)))
except Exception as e:
    assert_not_exists('多层地图-地图1的界面没有“地图1”或者编辑图标.png',msg='多层地图-地图1的界面没有“地图1”或者编辑图标')
# **期望结果**  
# 页面弹出重命名框,# 默认名称为当前命名
mapmgr.check_default_map_name("地图1")
   
# 取消  确认
if poco(text='取消') and poco(text='确认'):
    logger.debug(u'地图重命名弹框有取消和确认按钮')                         
    log('地图重命名弹框有取消和确认按钮')   
else:                          
    snapshot('地图重命名弹框缺少取消和确认按钮.png','地图重命名弹框缺少取消和确认按钮，请确认')
    raise AssertionError("地图重命名弹框缺少取消和确认按钮，请确认")
             
log("步骤二：点击输入框")
poco(name='com.eco.global.app:id/name_edit_field').click()
# **期望结果**  
# 弹出输入键盘
## 手机键盘被Yosemite控制，不会显示键盘

log("步骤三：尝试输入16位英文和数字字符")
INT_CHAR = '4567890abcdf'
text(INT_CHAR,enter=False) #此时正好16位
if not poco(name='com.eco.global.app:id/error_tips', text='最多输入16位字符').exists():
    logger.debug(u'输入16位英文和数字字符,没有报错信息')                         
    log('输入16位英文和数字字符,没有报错信息')
else:
    raise Exception("输入<=16位英文和数字字符,不应该报错信息，请检查")
# **期望结果**  
# 输入超出16字符时，输入框下方显示红色提示文字“最多输入16字符”，且无法点击确人  
text('12345',enter=False)
if poco(name='com.eco.global.app:id/error_tips', text='最多输入16位字符').exists():
    logger.debug(u'输入>16位英文和数字字符,有报错信息')                         
    log('输入>16位英文和数字字符,有报错信息')
else:
    raise Exception("输入>16位英文和数字字符,没有报错信息，请检查")
# 点击确认
poco(text='确认').click()
if poco(text='地图重命名').exists() and poco(text='最多输入16位字符').exists():
    logger.debug(u'无法点击确认')                         
    log('无法点击确认')
else:
    raise Exception("输入>16位字符,点击确认有响应，请检查")

# log("步骤四：输入16位中文字符，点确认") 
## 点击取消，删除步骤三填入的数据
poco(text='取消').click()
## 再次点击重命名
mapmgr.click_rename_button()
mapmgr.click_to_enter_rename_text("一二三四五六七一二三四五六")
# 点击确认
poco(text='确认').click()
sleep(2)

# **期望结果**  
# 重命名成功，页面自动返回地图管理页面，在地图管理界面上显示不全的重命名用...代替
## 地图管理界面上可以显示的全，没有...，所以检查地图管理界面有重命名
if mapmgr.get_map_name() == '地图1一二三四五六七一二三四五六':
    logger.debug(u'地图管理界面上显示重命名成功')                         
    log('地图管理界面上显示重命名成功')
## 根据手机屏幕大小而定，小屏幕会显示出“...”
elif  '...' in poco(name='com.eco.global.app:id/map_name').get_text():
    logger.debug(u'地图管理界面上显示不全的重命名用...代替')                         
    log('地图管理界面上显示不全的重命名用...代替')
else:
    raise AssertionError('地图管理界面上显示重命名失败')
             
log("步骤五：返回主界面查看地图名称")
# **期望结果** 
# 主界面的地图名称显示保存后的名字，显示不全的重命名用...代替
## 从地图管理界面 返回 主界面
mapmgr.click_mapmgr_to_main()
sleep(2)
# 查看主界面地图名称
if mapmgr.get_map_name() == '地图1一二三四五六七一二三四五六':
    logger.debug(u'地图管理界面上显示重命名成功')                         
    log('地图管理界面上显示重命名成功')
## 根据手机屏幕大小而定，小屏幕会显示出“...”
elif  '...' in poco(name='com.eco.global.app:id/map_name').get_text():
    logger.debug(u'地图管理界面上显示不全的重命名用...代替')                         
    log('地图管理界面上显示不全的重命名用...代替')
else:
    raise AssertionError('地图管理界面上显示重命名失败')
