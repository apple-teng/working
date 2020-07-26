# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
__case_theme__ = "验证主机扫建弓字型清扫时操作主机暂停（点击面板auto键、app键、故障），观察主机清扫行为逻辑"
"""
**前提条件**:主机配网成功无图，充电座待机，至少1个4.5*4.5m矩形区域  
**步骤ID 1**  
主机开始扫建，弓字型清扫时点击主机面板上的auto键  
**期望结果**  
主机原地停止清扫
app显示主机状态为暂停  
**步骤ID** 2  
再次主机面板的auto键  
**期望结果**  
主机继续弓型扫建，
APP状态转换为清扫，之前的清扫轨迹都还在  
**步骤ID** 3  
APP上点击“暂停”  
**期望结果**  
主机原地停止清扫
app显示主机状态为暂停  
**步骤ID** 4  
APP上点击“继续”  
**期望结果**  
主机继续弓型扫建，
APP状态转换为清扫，之前的清扫轨迹都还在   
"""

import time
from airtest.core.api import *
sys.path.append(r'E:\airTest\冒烟测试用例\zj1921\base')
from import_package import *
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)
# 执行脚本的前置操作（包括开启app，进入设备列表，进入主界面）
setup()
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# MQ准备数据
case_name = "329"

auto_setup(__file__)
        
def ZJ1921_329():
    # 确保主机在充电座
    try:
        Charge.check_lighting_icon(expectation='存在')
        logger.debug("主机在充电座")
    except:
        logger.debug("主机当前不在充电座，使其回充")
        Charge.anyhow_go_charge()
        Main.click_any_popMsg_on_main()
    log("导入地图-无图")
    cp_cmd = 'cp -r ' + NO_MAP_PATH + DESTINATION_MAP_PATH
    cmd = [cp_cmd, REBOOT_CMD]
    app.telnet_to_deboot(cmd)
    Main.click_any_popMsg_on_main()
    log('步骤一：主机开始扫建，清扫时点击主机面板上的auto键')
    # 主机开始清扫
    Sweep.click_auto_btn()
    Main.click_any_popMsg_on_main()
    # 上传清扫信息
    log(time.strftime("%H:%M:%S"))
    body["timestamp"] = int(time.time())
    body["action"] = "start"
    UniversalModule.publish_message2queue(body["sn"],body)
    print(" [1] Sent 'deebot run message'")

    # 等待主机清扫4min
    sleep(240)
    # 鉴于对自动化清扫环境的预估，清扫4min后基本已经进入弓字阶段
    # 步骤一：弓字型清扫时点击主机面板上的auto键
    log("再次点击使主机暂停")
    Sweep.click_auto_btn()
    # 上传清扫信息
    log(time.strftime("%H:%M:%S"))
    body["timestamp"] = int(time.time())
    body["action"] = "pause"
    UniversalModule.publish_message2queue(body["sn"],body)
    print(" [2] Sent 'deebot run message'")
    # 暂停清扫5S
    sleep(30)
            
    log("步骤二：再次主机面板的auto键")
    Sweep.click_auto_btn()
    # 上传清扫信息
    log(time.strftime("%H:%M:%S"))
    body["timestamp"] = int(time.time())
    body["action"] = "resume"
    UniversalModule.publish_message2queue(body["sn"],body)
    print(" [3] Sent 'deebot run message'")
            
    log("回充成功")
    elem = poco(name='com.eco.global.app:id/battery_charging_icon')
    UniversalModule.wait_element_expected(elem)
    log(time.strftime("%H:%M:%S"))
    body["timestamp"] = int(time.time())
    body["action"] = "stop"
    UniversalModule.publish_message2queue(body["sn"],body)
    print(" [4] Sent 'deebot run message'")
   
if __name__ == 'airtest.cli.runner':
    __i__ = 0
    while True:
        __i__ += 1
        log("清扫次数："+str(__i__))
        # 检查到电量低
        if exists(Template(r"tpl1592554849106.png", rgb=True, record_pos=(0.419, -0.853), resolution=(1080, 2340))) or exists(Template(r"tpl1592961284078.png", record_pos=(0.419, -0.68), resolution=(1080, 1920))):
            logger.debug(u'主机当前处于低电状态')
            log('主机当前处于低电状态')
            # 低电时休息1H
            logger.debug(u'低电时休息1H')
            log('低电时休息1H')
            sleep(3600)
#             break
            # 结束清扫，作为下次清扫的setup
            if Sweep.get_auto_btn_status() == '暂停':
                # 点击右下角按钮呼出停止清扫按钮
                Sweep.click_rightstop()
                logger.debug('点击右下角按钮呼出停止清扫按钮')
                log('点击右下角按钮呼出停止清扫按钮')
                # 点击停止清扫按钮
                Sweep.click_stop_clean()
                logger.debug('点击停止清扫按钮')
                log('点击停止清扫按钮')
        elif __i__ == 2:
            logger.debug('清扫次数达到50次，结束清扫')
            log('清扫次数达到50次，结束清扫')
            break
        
    try:
        poco('com.eco.global.app:id/top_status_more').exists()                
    except:
        touch(Template(r"tpl1592474521330.png", record_pos=(0.001, 0.519), resolution=(1080, 2340)))
        sleep(3)
        logger.debug(u'点击知道了')
        log('点击知道了')
    # 开始清扫运行
    ZJ1921_329()
    # 等待下次清扫
    sleep(60)

 
