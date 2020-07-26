# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"

from airtest.core.api import *

auto_setup(__file__)# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"
__case_theme__ = "验证主机扫建多个区域，观察主机清扫行为逻辑"
"""
...  
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
case_name = "000"

auto_setup(__file__)
        
def multiAreaClean():
    # 确保主机在充电座
    Charge.anyhow_go_charge()
    Main.click_any_popMsg_on_main()
#     log("导入地图-无图")
#     cp_cmd = 'cp -r ' + NO_MAP_PATH + DESTINATION_MAP_PATH
#     cmd = [cp_cmd, REBOOT_CMD]
#     app.telnet_to_deboot(cmd)
#     Main.click_any_popMsg_on_main()
    log('步骤一：主机开始扫建，清扫时点击主机面板上的auto键')
    # 主机开始清扫
    Sweep.click_auto_btn()
    Main.click_any_popMsg_on_main()
    # 上传清扫信息
    log(time.strftime("%H:%M:%S"))
    body["timestamp"] = int(time.time())
    body["action"] = "start"
    UniversalModule.publish_message2queue(body["sn"],body)
    logger.debug(" [1] Sent 'deebot start message'")
    log(" [1] Sent 'deebot start message'")

    log("等待主机清扫完成，回充")
    Charge.check_tips_complete_clean_go_charge(expectation='存在')
    Charge.wait_finish_work_go_charge()
    # 上传清扫信息
    log(time.strftime("%H:%M:%S"))
    body["timestamp"] = int(time.time())
    body["action"] = "recharge" # 返回充电座
    UniversalModule.publish_message2queue(body["sn"],body)
    logger.debug(" [4] Sent 'deebot recharge message'")
    log(" [4] Sent 'deebot recharge message'")
            
    log("回充成功")
    Charge.anyhow_go_charge()
    Main.click_any_popMsg_on_main()
    
    log(time.strftime("%H:%M:%S"))
    body["timestamp"] = int(time.time())
    body["action"] = "stop"
    UniversalModule.publish_message2queue(body["sn"],body)
    logger.debug(" [5] Sent 'deebot stop message'")
    log(" [5] Sent 'deebot stop message'")
    
   
if __name__ == 'airtest.cli.runner':
    __i__ = 0
    while True:
        __i__ += 1
        logger.debug("清扫次数："+str(__i__))
        log("清扫次数："+str(__i__))
        # 检查到电量低
        if exists(Template(r"tpl1592554849106.png", rgb=True, record_pos=(0.419, -0.853), resolution=(1080, 2340))) or exists(Template(r"tpl1592961284078.png", record_pos=(0.419, -0.68), resolution=(1080, 1920))):
            logger.debug(u'主机当前处于低电状态')
            log('主机当前处于低电状态')
            # 低电时休息1H
            logger.debug(u'低电时休息1H')
            log('低电时休息1H')
            sleep(3600)
            # 结束清扫，作为下次清扫的setup.
            Charge.anyhow_go_charge()
            Main.click_any_popMsg_on_main()
        # 没低电，在主界面
        elif poco('com.eco.global.app:id/top_status_more').exists():
            # 开始清扫运行
            multiAreaClean()
            # 每次清扫间隔60S
            sleep(60)            
       # 设置清扫次数     
        elif __i__ >= 2:
            logger.debug('清扫次数达到{}次，结束清扫'.format(__i__))
            log('清扫次数达到%d次，结束清扫' % __i__)
            break
        # 其他未知情况
        else:
            snapshot("未知情况.png",msg="未知情况,退出循环")
            logger.debug("未知情况,退出循环")
            log("未知情况,退出循环")            
            break
            
        
    
 
