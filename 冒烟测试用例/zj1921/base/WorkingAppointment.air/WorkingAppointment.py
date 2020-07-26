# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"

from airtest.core.api import *
from poco import exceptions
import sys
sys.path.append(r'../')
from import_package import *
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

"""
以下函数均与 工作预约 有关
"""

auto_setup(__file__)
# setup()
# poco 初始化要放在start_app（打开app）之后

def more_to_working_appointment():
    """
        function:
            更多进入工作预约
        args：
            none
        return:
            none
    """
    try:
        poco(name='com.eco.global.app:id/title', text='工作预约').click()
    except Exception as e:
        raise AssertionError("更多进入工作预约出错",e)
    try:
        poco(name='com.eco.global.app:id/tv_tab_title', text='自动清扫').wait_for_appearance()
        logger.debug("成功从更多进入工作预约")
        log("成功从更多进入工作预约")
    except Exception as e:
        raise AssertionError("点击工作预约按钮，没有进入工作预约",e)
        
        
def working_appointment_to_more():
    """
        function:
            工作预约返回更多
        args：
            none
        return:
            none
    """
    try:
        poco(name='com.eco.global.app:id/title_back').click()
    except Exception as e:
        raise AssertionError("工作预约返回更多出错",e)
    try:
        poco(name='com.eco.global.app:id/tv_tab_title', text='工作设置').wait_for_appearance()
        logger.debug("成功从工作预约返回更多")
        log("成功从工作预约返回更多")
    except Exception as e:
        raise AssertionError("点击退出工作预约按钮，没有进入更对页面",e) 
        
        
def click_AddAppointment_back_to_AppointmentList():
    """
        function:
            添加工作预约设置界面返回到工作预约列表页面
        args：
            none
        return:
            none
    """
    if poco('com.eco.global.app:id/title_back').exists():
        poco('com.eco.global.app:id/title_back').click()
        logger.debug("在自动预约界面点击返回")
        log("在自动预约界面点击返回")        
    elif poco('com.eco.global.app:id/back_to').exists():
        poco('com.eco.global.app:id/back_to').click()
        logger.debug("在区域预约界面点击返回")
        log("在区域预约界面点击返回")
    else:
        raise AssertionError("当前页面没有返回按钮")
        
        
def click_appointment_type_of_list(appoint_type='auto'):
    """
        function:
            点击进入工作预约界面的自动清扫的预约列表，或，区域清扫预约的列表
        args：
            appoint_type：选择预约列表的类型（obj：str），
            可选值为：'auto' 、 'area'。'auto'为自动清扫的预约列表，'area'为区域清扫预约的列表
            缺省值为：'auto'            
        return:
            none
    """
    # 自动清扫的预约列表
    if appoint_type == 'auto':
        poco(name='com.eco.global.app:id/tv_tab_title', text='自动清扫').click(sleep_interval=2)
    # 点击区域预约列表    
    elif appoint_type == 'area':
        poco(name='com.eco.global.app:id/tv_tab_title', text='区域清扫').click(sleep_interval=2)
    else:
        raise AssertionError("appoint_type值写错")
        
                        
def click_add_appointment():
    """
        function:
            点击右上角的“+”
        args：
            none
        return:
            none
    """
    try:
        poco('com.eco.global.app:id/right').click()
        logger.debug("点击右上角的“+”")
        log("点击右上角的“+”")
    except Exception as e:
        raise AssertionError("点击右上角的“+”出错",e)
        

def check_type_of_adding_appointment():
    """
        function:
            检查点击右上角的“+”后，弹出的新增预约类型
        args：
            none
        return:
            none
    """
    if exists(Template(r"tpl1593679850317.png", record_pos=(0.3, -0.556), resolution=(1080, 1920))):
        logger.debug("出现预约自动清扫和预约区域清扫两个选项[1]")
        log("出现预约自动清扫和预约区域清扫两个选项[1]")
    elif poco('com.eco.global.app:id/auto_add').exists() and poco('com.eco.global.app:id/area_add').exists():
        logger.debug("出现预约自动清扫和预约区域清扫两个选项[2]")
        log("出现预约自动清扫和预约区域清扫两个选项[2]")
    else:
        raise AssertionError("点击右上角的“+”后，弹出的新增预约类型有错")
        

def click_adding_appointment_type(clean_type):
    """
        function:
            选择新增的清扫预约类型
        args：
            clean_type:预约类型（obj:str)
            包括：'auto'，'area'。 auto为点击自动清扫预约，area为点击区域清扫预约
        return:
            none
    """
    if clean_type == 'auto':
        poco('com.eco.global.app:id/auto_add').click()
        logger.debug("点击新增自动清扫预约")
        log("点击新增自动清扫预约")
    elif clean_type == 'area':
        poco('com.eco.global.app:id/area_add').click()
        logger.debug("点击新增区域清扫预约")
        log("点击新增区域清扫预约")
    else:
        raise AssertionError("clean_type参数值不对，请检查。。。")
        
          
def add_autoClean_appointment(booking_time=2):
    """
        function:
            在工作预约界面，操作，添加2min后的自动清扫预约
            booking_time：预约的相对时间，即相对于设置预约的当前时间的 分钟 往后延时booking_time（obj：int.注意，是有符号整型）
            default值为2，即延时2min的预约
            如：设置预约时间为10:03，那么，当booking_time=-2时，设置的预约时间为10:01
            设置预约时间为10:01，那么，当booking_time=2时，设置的预约时间为10:03
        args：
            none
        return:
            none
    """
    # 点击右上角的“+”
    click_add_appointment()
    # 选择自动清扫预约
    poco('com.eco.global.app:id/auto_add').click()
    if poco('com.eco.global.app:id/titleContent', text='新增预约').exists():
        booking_time = -(float(booking_time/10))
        poco(name='android.widget.NumberPicker').child(name='android:id/numberpicker_input')[1].swipe([0, booking_time])
        logger.debug("")
        log("设置2min后的预约")
        sleep(2)
        poco(text="保存").click(sleep_interval=3)
        logger.debug("保存预约")
        log("保存预约")
        # 在勿扰模式下，提交保存时会有弹框
        if poco(name='com.eco.global.app:id/tv_content').exists():
            # 有弹窗，点击"仍然设定"
            poco(text="仍然设定").click()
            logger.debug("勿扰时间内，也仍然设定")
            log("勿扰时间内，也仍然设定")
            sleep(5)
    else:
        raise AssertionError("当前页面不在新增预约")



def add_areaClean_appointment(booking_time=2):
    """
        function:
            在工作预约界面，操作添加2min后的区域清扫预约
        args：
            booking_time：预约的相对时间，即相对于设置预约的当前时间的 分钟 往后延时booking_time（obj：int.注意，是有符号整型），
            default值为2，即延时2min的预约
            如：设置预约时间为10:03，那么，当booking_time=-2时，设置的预约时间为10:01
            设置预约时间为10:01，那么，当booking_time=2时，设置的预约时间为10:03
        return:
            none
    """
    # 点击右上角的“+”
    poco('com.eco.global.app:id/right').click()
    sleep(2)
    # 选择区域清扫预约
    poco('com.eco.global.app:id/area_add').click()
    sleep(5)
    if poco(name='com.eco.global.app:id/tv_appoint_area').exists():
        logger.debug("进入新增区域预约设置界面")
        log("进入新增区域预约设置界面")
    # 主机无图：暂未生成区域地图，请先建立完整家居环境地图
    elif poco(name='com.eco.global.app:id/no_area_text').exists():
        snapshot("点击区域清扫预约，没进入设置页面截图.png",'点击区域清扫预约，没有进入新增区域预约设置界面')
        raise AssertionError("主机当前所在地图非整图，不可设置区域清扫")
    else:
        snapshot("点击区域清扫预约，没进入设置页面截图.png",'点击区域清扫预约，没有进入新增区域预约设置界面,请检查')
        raise AssertionError("没有进入新增区域预约设置界面,请检查")
    # 点击“清扫区域”，选择清扫区域
    if poco(text="未选择").exists():
        poco(name='com.eco.global.app:id/tv_appoint_area_value', text="未选择").click('center', 3)
        logger.debug("进入地图，选择区域")
        log("进入地图，选择区域")
        sleep(5)    
    else:
        raise AssertionError("点击选择清扫区域出错")
    try:
        poco(name='com.eco.global.app:id/tip').wait_for_appearance()
    except:
        snapshot(msg='进入地图，没有显示区域，截图检查')
        raise AssertionError("进入地图，没有显示区域")
    try:
        # 选中区域A
        touch(Template(r"tpl1593740153147.png", record_pos=(-0.297, -0.077), resolution=(1080, 1920)))
    except:
        snapshot(msg='区域预约选中区域A出错，截图检查')
        raise AssertionError("区域预约选中区域A出错")
    sleep(2)
    # 点击返回，回到设置页面
    poco(name='com.eco.global.app:id/back_to').click()
    logger.debug("点击返回，回到设置页面")
    log("点击返回，回到设置页面")
    booking_time = -(float(booking_time/10))
    # 设置预约时间
    poco(name='android.widget.NumberPicker').child(name='android:id/numberpicker_input')[1].swipe([0, booking_time])
    logger.debug("设置"+str(booking_time)+"后的预约")
    log("设置"+str(booking_time)+"后的预约")
    sleep(2)
    # 保存预约设置    
    # pop_message = "请避开这一时间段并预留充足时间"
    poco(text="保存").click(sleep_interval=3)
    logger.debug("保存预约")
    log("保存预约")
    # 在勿扰模式下，提交保存时会有弹框
    if poco(name='com.eco.global.app:id/tv_content').exists():
        # 有弹窗，点击"仍然设定"
        poco(text="仍然设定").click()
        logger.debug("勿扰时间内，也仍然设定")
        log("勿扰时间内，也仍然设定")
        # 修改全局变量disturb_mode，改为在勿扰时间内
        global disturb_mode
        disturb_mode = 1
        sleep(5)
    
    
def click_appointment_switch(swith_status):
    """
        function:
            点击清扫预约的开关，来开启或关闭清扫预约
        args：
            none
        return:
            none
    """
    pass
    
        
def get_appointment_time_list():
    """
        function:
            获取预约列表中各预约的时间
        args：
            none
        return:
            time_list:返回预约列表中各预约的时间组成的列表(obj:list)
            eg.['9:44','10:37','10:37','10:38']
    """
    time_list = []
    element = poco(name='android.view.ViewGroup').offspring(name='com.eco.global.app:id/tv_time')
    for i in element:
        time_list.append(i.get_text())
    return time_list

    
def get_appointment_list_map_name():  
    """
        function:
            获取区域预约列表中各预约的地图名称
        args：
            none
        return:
            map_name_list:返回预约列表中各预约的地图名称组成的列表(obj:set)
            eg.('地图1','地图2')
    """
    map_name_list = []
    if poco(name='com.eco.global.app:id/map_name').exists():
        element = list(poco(name='com.eco.global.app:id/map_name'))
        for i in element:
            logger.debug(i)
            map_name_list.append(i.get_text())
        map_name_list = set(map_name_list)   
    else:
        map_name_list = []
    return map_name_list
    

def teardown_schedule(clean_type):
    """
        function:
            删除预约列表中的预约
        args：
            clean_type:选择要删除的预约列表(obj:str)
            -auto：自动清扫列表
            -area：区域清扫列表
        return:
            none
    """
    clean_text = {'auto': '自动清扫', 'area': '区域清扫'}
    schdule_item = 'com.eco.global.app:id/tv_appoint_type'
    log("进入teardown_schedule...删除的预约类型为：" + clean_type)       
    poco(name='com.eco.global.app:id/tv_tab_title', text=clean_text[clean_type]).wait_for_appearance()
    # 点击自动清扫的title
    poco(name='com.eco.global.app:id/tv_tab_title', text=clean_text[clean_type]).click()
    log("进入自动清扫栏下删除预约")
    if poco(name=schdule_item, text=clean_text[clean_type]).exists():
        # 左滑，滑出删除按钮
        poco(name=schdule_item, text=clean_text[clean_type]).swipe([-0.5, 0])
        log("删除预约--左滑")
        sleep(2)
        if poco(text="删除").exists:
            # 点击删除
            poco(text="删除").click()
            sleep(8)    
            log(clean_text[clean_type] + " 预约删除成功")
    else:
        log(clean_text[clean_type] + " 没有预约")
        
        
def check_effect_of_schedule(disturb_mode=0): 
    """
        function:
            在工作预约界面，检查预约是否生效的弱消息提示
            在主界面，通过auto图标，检查主机的行为与弱消息是否一致
            检查完成过后，使主机返回充电座，界面最终停留在主界面
        args：
           disturb_mode：主机当前是否在勿扰时间段内
            - 0：不在勿扰时间段内（缺省值）
            - 1：在勿扰时间段内
        returns:
            - popmsg_flag (0：ok  1:没有弱消息)
            - deboot_flag (0：ok  1:主机状态不正确)
        raises:
            - PocoTargetTimeout: when timeout
    """
    log("进入check_effect_of_schedule...")    
    # 默认没有弹框，主机状态不对
    __popmsg_flag__ = 0
    __deboot_flag__ = 0
    # 在勿扰时间内
    if disturb_mode:
        # 勿扰的设置使当前时间的2min后，所以在3min内捕获 弱消息
        try:
            wait(Template(r"tpl1587001264275.png", rgb=True, record_pos=(-0.007, 0.567), resolution=(1080, 2160)), 180)
            __popmsg_flag__ = 1
            logger.debug("等待勿扰时间内的弱消息")
            log("等待勿扰时间内的弱消息")
        except TargetNotFoundError:
            raise AssertionError("勿扰时间段内没弹出 预约任务无法执行 的弱消息")
            
        # 主界面检查勿扰时间内，主机状态为待机
        # 进入主界面
        try:
            # 工作预约界面返回更多
            poco(name='com.eco.global.app:id/title_back').click()
            # 更多返回主界面
            poco(name='com.eco.global.app:id/title_back').click()
            Main.click_any_popMsg_on_main()
            logger.debug("从更多返回主界面")
            log("从更多返回主界面")
            try:
                wait(Template(r"tpl1587009679616.png", record_pos=(0.006, 0.849), resolution=(1080, 2160)), 180)
                __deboot_flag__ = 1
                logger.debug("回到主界面后，查看主机状态为待机")
                log("回到主界面后，查看主机状态为待机")
            except TargetNotFoundError:
                snapshot(msg="勿扰时间段内主机没有保持 待机 状态")
                raise AssertionError("勿扰时间段内主机没有保持 待机 状态")
        finally:
            if poco(name='com.eco.global.app:id/top_status_more').exists():
                # 最终都要返回更多页面
                poco(name='com.eco.global.app:id/top_status_more').click()
                logger.debug("进入更多界面")
                log("进入更多界面")
            elif poco(text="知道了").exists():
                poco(text="知道了").click()

    # 勿扰关闭或者在勿扰时间外
    else:
        try:
            wait(Template(r"tpl1594286103642.png", record_pos=(0.028, 0.534), resolution=(1080, 2340)), 180)
            __popmsg_flag__ = 1
            logger.debug("3min内等到了 预约任务已启动 的弱消息")
            log("3min内等到了 预约任务已启动 的弱消息")
        except TargetNotFoundError:
            snapshot(msg="勿扰时间段外，主机响应预约，没有弹出弱消息")
#             raise AssertionError("勿扰时间段外，主机响应预约，没有弹出弱消息")
        try:
            # 工作预约界面返回更多
            poco(name='com.eco.global.app:id/title_back').click()
            # 更多返回主界面
            poco(name='com.eco.global.app:id/title_back').click()
            logger.debug("返回主界面")
            log("返回主界面")
            try:
                wait(Template(r"tpl1585822379315.png", record_pos=(0.003, 0.753), resolution=(720, 1440)),180)
                __deboot_flag__ = 1
                logger.debug("查看到主机状态为运行")
                log("查看到主机状态为运行")
                ################## teardown操作 ########################
                # 结束清扫状态
                poco(name='com.eco.global.app:id/iv_rightstop_btn').wait_for_appearance()
                sleep(5)
                logger.debug("点击电池按钮")
                log("点击电池按钮")
                poco(name='com.eco.global.app:id/iv_rightstop_btn').click()
                sleep(2)
                poco(text="结束当前工作").click()
                sleep(5)  
                logger.debug("点击结束当前工作，停止主机运行状态")
                log("点击结束当前工作，停止主机运行状态")
            except TargetNotFoundError:
                snapshot(msg="勿扰时间段外主机没有运行")
#                 raise AssertionError("勿扰时间段外主机没有运行")
        except Exception as e:
            snapshot("返回主界面失败的实时截图.png","返回主界面失败的实时截图")
            raise e("返回主界面失败")
    return __popmsg_flag__, __deboot_flag__

        
        
        
# if __name__ == 'main':
if __name__ == 'airtest.cli.runner':
    ll = get_appointment_list_map_name()
    print(ll)
#     for i in l:
#         print(i)
#     more_to_working_appointment()
#     click_appointment_type_of_list('area')
#     popmsg_flag,deboot_flag = check_effect_of_schedule()
#     if popmsg_flag == 1 and deboot_flag ==1:
#         logger.debug("主机响应预约，去往对应的区域清扫")
#         log("主机响应预约，去往对应的区域清扫")
#     else:
#         raise AssertionError("主机响应预约出错，popmsg_flag,deboot_flag的状态值分别为 %d，%d")%(popmsg_flag,deboot_flag)

    
#     teardown_schedule('auto')
#     get_appointment_list_map_name()
#     get_appointment_time_list()
#     add_areaClean_appointment(-2)
#     more_to_working_appointment()









