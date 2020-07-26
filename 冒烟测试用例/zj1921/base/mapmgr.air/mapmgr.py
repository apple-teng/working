# -*- encoding=utf8 -*-
__author__ = "xiaomei.teng"

from poco import exceptions
import sys
sys.path.append(r'../')
from import_package import *
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
# setup()
# poco 初始化要放在start_app（打开app）之后
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

import Charge,Main

"""
以下函数皆与 地图管理 有关
"""
auto_setup(__file__)
def click_mapmgr_notice():
    """
        function:
            点击首次进入多层地图的各种提示
            注意：该函数在做功能测试时最好与click_to_mapmgr()成对使用（做UI测试时可不搭配使用）
        args：
            none
        return:
            none
    """
    while True:
        if poco(text='已知晓').exists():
            poco(name='com.eco.global.app:id/checkbox').click()
            log('mapmgr_选择：已知晓')
            sleep(1)
            poco(name='com.eco.global.app:id/next_step').click()
            log('mapmgr_选择：下一步')
        elif poco(name='com.eco.global.app:id/tv_iknow').exists():
            poco(name='com.eco.global.app:id/tv_iknow').click()
            log("点击首次建图成功的地图保存引导")
        else:
            break
            log("多楼层地图建图注意事项 已点完或 不是第一次进入")

def click_main_to_mapmgr():
    """
        function:
            点击进入地图管理
        args：
            none
        return:
            none
    """
    poco(name='com.eco.global.app:id/iv_mapmgr_btn').click(sleep_interval=3)
    try:
        # 多层地图已经是开启状态下，app首次进入多层地图管理界面，会弹出：多层地图建图注意事项
        if poco(name="com.eco.global.app:id/tips_title").exists():
            click_mapmgr_notice()
        elif poco(text='地图管理').wait_for_appearance():
            log("进入地图管理")                    
    except Exception as e:
        raise AssertionError("进入地图管理失败", e)
        
        
def click_mapmgr_to_main():
    """
        function:
            地图管理返回主界面
        args：
            none
        return:
            none
    """
    poco(name='com.eco.global.app:id/title_back').click()
    sleep(2)
    try:
        poco(name='com.eco.global.app:id/deebot_battery_statues').exists()
        log("地图管理返回主界面")
    except:
        raise AssertionError("地图管理返回主界面失败")
        

def check_mapmgr_fun_swith():
    """
        function:
            检查多层地图的开关
        args：
            none
        return:
            mapmgr_switch:(obj: int) 多层地图的开关状态（0：关， 1：开）
    """
    mapmgr_switch = 0 # 默认开关为关
    if poco(text='地图管理').exists():
        if exists(Template(r"tpl1591867761217.png", threshold=0.7, rgb=True, record_pos=(0.391, -0.569), resolution=(1080, 1920))):
            mapmgr_switch = 1
#         elif exists(Template(r"tpl1591867887992.png", threshold=0.7, rgb=True, record_pos=(0.391, -0.574), resolution=(1080, 1920))):
# #             mapmgr_switch = 0 
#         else:
#             mapmgr_switch = 2
#             log("没有取到多层地图开关状态值")
    else:
        raise AssertionError("当前页面不在地图管理页面")
    return mapmgr_switch 

            
def mapmgr_map_num(mapmgr_switch):
    """
        function:
            检查多层地图的开关
        args：
            mapmgr_switch：多层地图的开关状态(obj: int)，包含参数：0 , 1。
            0：多层地图为关，1多层地图为开
        return:
            map_num: 地图的数量
    """
    map_num = 0
    __map_name_list__ = []
    try:
        poco(text='地图管理').exists()
        map_tag_path = poco("com.eco.global.app:id/map_container")\
            .child("com.eco.global.app:id/card_view").\
            offspring("com.eco.global.app:id/basic_map")
        if mapmgr_switch == 1:  
            if map_tag_path.exists():
                __map_name_list__.append(map_tag_path.attr('name'))
                
                map_num = len(__map_name_list__)
                # 点击地图中的一处向上划动出第三张图           
            poco(text='已存储的地图').swipe([0,-0.5])
            if map_tag_path.exists():
                __map_name_list__.append(map_tag_path.attr('name'))
                map_num += len(__map_name_list__)
            # 2次滑动都会有中间地图的存在，地图张数就会多算一次
            map_num -= 1
            print(__map_name_list__)
        # 多层地图关闭时
        else:
            # 有map_tag_path，说明有图
            if map_tag_path.exists():
                map_num = 1 
            # 无map_tag_path，说明无图
            else: 
                map_num = 0 
        return map_num               
    except:
        raise AssertionError("当前页面不在地图管理页面")
        
        
def get_current_using_map_name():
    """
        function:
            在主界面检查当前主机所在地图的地图名称
        args：
            none
        return:
            map_name:当前主机所在地图的地图名称（obj：str）
    """
    # 检查app当前是否停留在主页面（通过更多元素是否存在来判断）
    try:
        poco('com.eco.global.app:id/top_status_more').exists()
    except Exception as e:
        raise Exception("app当前不在主界面")
    # 刷新地图-通过进出主界面
    logger.debug("刷新地图-通过进出主界面")
    log("刷新地图-通过进出主界面")
    Main.main_to_deviceslist()
    Main.deviceslist_to_main_using_first_device()
    Main.click_any_popMsg_on_main()
    sleep(5)
    if poco(name='com.eco.global.app:id/map_name').exists():
        map_name = poco(name='com.eco.global.app:id/map_name').get_text()
        return map_name
    else:
        raise AssertionError("检查多层地图是否处于开启状态或当前地图是否为整图")
        

def get_mapmgr_mapName():
    """
        function:
            获取地图管理页面，已存在地图的全部地图名称
        args：
            none
        return:
            map_name:当前主机所在地图的地图名称（obj：set）
    """
    map_name = []
    element1 = []
    element2 = []
    mapmgr_switch = check_mapmgr_fun_swith()
    # 判断是否在多层地图页面
    try:
        poco(text='地图管理').wait_for_appearance()
    except:
        raise AssertionError("当前页面不在地图管理页面")    
    if mapmgr_switch == 1:  
        element1 = list(poco(name='com.eco.global.app:id/map_name'))
        for i in element1:
            map_name.append(i.get_text())
        # 点击地图中的一处向上划动出第三张图           
        poco(name='com.eco.global.app:id/map_container').swipe([0,-0.5])
        if poco(name='com.eco.global.app:id/map_name').exists():
            element2 = list(poco(name='com.eco.global.app:id/map_name'))
        for j in element2:
            map_name.append(j.get_text())    
        # 2次滑动都会有中间地图的存在，地图张名称会出现一次重复，用集合去重
        map_name = set(map_name)
        for i in map_name:
            print(i)
    # 多层地图关闭时
    else:
        logger.debug("多层地图关闭")
        map_name = None
    return map_name               
                                            

def click_mapmgr_switch(mapmgr_switch=1):
    """
        function:
            点击多层地图的开关，进行开/关多层地图
        args：
            mapmgr_switch(obj:int),传入整型的数值。
                0：关闭多层地图，1：开启多层地图
        return:
            none
    """
    __mapmgr_switch_status__ = {0:"关闭", 1:"开启"}
    # 当前状态与预期状态一致
    if mapmgr_switch == check_mapmgr_fun_swith():
        logger.debug("多层地图状态已经为 " + __mapmgr_switch_status__[mapmgr_switch])
        log("多层地图状态已经为 " + __mapmgr_switch_status__[mapmgr_switch])
    # 当前状态与预期状态不一致
    else:
        poco(name='com.eco.global.app:id/toggle_btn').click()
        sleep(2)
        logger.debug("多层地图成功 " + __mapmgr_switch_status__[mapmgr_switch])
        log("多层地图成功 " + __mapmgr_switch_status__[mapmgr_switch])
        
        
        
def check_question_mapmgr_build_notice():
    """
        function:
            检查点击“？”后弹出的多层地图的建图注意事项
        args：
           none
        return:
            none
    """    
    try:
        poco(text='地图管理').exists()
    except:
        raise AssertionError("当前页面不在地图管理页面")
    # 点击右上角的"?"
    touch(Template(r"tpl1592474186499.png", record_pos=(0.446, -0.944), resolution=(1080, 2340)))
    sleep(3)
    if exists(Template(r"tpl1592474212332.png", record_pos=(-0.006, 0.026), resolution=(1080, 2340))):
        logger.debug(u'建图注意事项首页正确')
        log('建图注意事项首页正确')
        poco('com.eco.global.app:id/tips_title').swipe([-0.9,0])
    else:
        logger.debug(u'建图注意事项首页不正确')
        raise AssertionError('建图注意事项首页不正确')
        
    if exists(Template(r"tpl1592474345948.png", record_pos=(-0.001, 0.028), resolution=(1080, 2340))):
        logger.debug(u'建图注意事项第二页正确')
        log('建图注意事项第二页正确')
        poco('com.eco.global.app:id/tips_title').swipe([-0.9,0])
    else:
        logger.debug(u'建图注意事项第二页不正确')
        raise AssertionError('建图注意事项第二页不正确')
        
    if exists(Template(r"tpl1592474400618.png", record_pos=(0.003, 0.029), resolution=(1080, 2340))):
        logger.debug(u'建图注意事项第三页正确')
        log('建图注意事项第三页正确')
        poco('com.eco.global.app:id/tips_title').swipe([-0.9,0])
    else:
        logger.debug(u'建图注意事项第三页不正确')
        raise AssertionError('建图注意事项第三页不正确')
        
    if exists(Template(r"tpl1592474447638.png", record_pos=(-0.001, 0.029), resolution=(1080, 2340))):
        logger.debug(u'建图注意事项第四页正确')
        log('建图注意事项第四页正确')
    else:
        logger.debug(u'建图注意事项第四页不正确')
        raise AssertionError('建图注意事项第四页不正确')
        
    # 点击知道了
    try:
        touch(Template(r"tpl1592474521330.png", record_pos=(0.001, 0.519), resolution=(1080, 2340)))
        sleep(3)
        logger.debug(u'点击知道了')
        log('点击知道了')
    except:
        raise AssertionError('点击知道了失败')
        

def check_and_click_turn_on_mapmgr_button_notice():
    """
        function:
            检查首次开启多层地图弹出的建图注意事项，并一一点掉
        args：
           none
        return:
            none
    """ 
    if exists(Template(r"tpl1592989721925.png", record_pos=(0.012, -0.019), resolution=(1080, 1920))):
        logger.debug(u'建图注意事项首页正确')
        log('建图注意事项首页正确')
        # 点击已知晓
        poco(name='com.eco.global.app:id/checkbox').click(sleep_interval=2)
        # 点击下一步
        poco(name='com.eco.global.app:id/next_step').click(sleep_interval=2)
        # 左滑到下一页
        poco('com.eco.global.app:id/tips_title').swipe([-0.9,0])
    else:
        logger.debug(u'建图注意事项首页不正确')
        raise AssertionError('建图注意事项首页不正确')
        
    if exists(Template(r"tpl1592989877207.png", record_pos=(-0.006, -0.02), resolution=(1080, 1920))):
        logger.debug(u'建图注意事项第二页正确')
        log('建图注意事项第二页正确')
        # 点击已知晓
        poco(name='com.eco.global.app:id/checkbox').click(sleep_interval=2)
        # 点击下一步
        poco(name='com.eco.global.app:id/next_step').click(sleep_interval=2)
        # 左滑到下一页
        poco('com.eco.global.app:id/tips_title').swipe([-0.9,0])
    else:
        logger.debug(u'建图注意事项第二页不正确')
        raise AssertionError('建图注意事项第二页不正确')
        
    if exists(Template(r"tpl1592989922410.png", record_pos=(-0.006, -0.027), resolution=(1080, 1920))):
        logger.debug(u'建图注意事项第三页正确')
        log('建图注意事项第三页正确')
        # 点击已知晓
        poco(name='com.eco.global.app:id/checkbox').click(sleep_interval=2)
        # 点击下一步
        poco(name='com.eco.global.app:id/next_step').click(sleep_interval=2)
        # 左滑到下一页
        poco('com.eco.global.app:id/tips_title').swipe([-0.9,0])
    else:
        logger.debug(u'建图注意事项第三页不正确')
        raise AssertionError('建图注意事项第三页不正确')
        
    if exists(Template(r"tpl1592990043163.png", record_pos=(-0.005, -0.017), resolution=(1080, 1920))):
        logger.debug(u'建图注意事项第四页正确')
        log('建图注意事项第四页正确')
         # 点击已知晓
        poco(name='com.eco.global.app:id/checkbox').click(sleep_interval=2)
    else:
        logger.debug(u'建图注意事项第四页不正确')
        raise AssertionError('建图注意事项第四页不正确')
        
    # 点击知道了
    try:
        touch(Template(r"tpl1592474521330.png", record_pos=(0.001, 0.519), resolution=(1080, 2340)))
        sleep(3)
        logger.debug(u'点击知道了')
        log('点击知道了')
    except:
        raise AssertionError('点击知道了失败')
    

def click_main_new_map_popmsg():
    """
        function:
           主机有整图，开启多层地图后，返回主界面，app界面会弹出引导消息：
           “”
        args：
            none
        return:
            none
    """    
    if exists(Template(r"tpl1592556625415.png", record_pos=(-0.173, 0.738), resolution=(1080, 2340))):
        touch(Template(r"tpl1592556625415.png", record_pos=(-0.173, 0.738), resolution=(1080, 2340))).click()
    elif poco(name='com.eco.global.app:id/tv_scroll_item').exists():        
        poco(name='com.eco.global.app:id/tv_scroll_item').click()
    if exists(Template(r"tpl1592990667338.png", record_pos=(-0.188, -0.168), resolution=(1080, 1920))):
        touch(Template(r"tpl1592990715879.png", record_pos=(-0.006, -0.113), resolution=(1080, 1920)))
    elif poco(name="com.eco.global.app:id/guide_tips").exists():
        poco(text="com.eco.global.app:id/i_know_tips").click()
                
#     if poco(text='已生成新环境地图，点击进入查看或保存').exists():
#         poco(text='知道了').click()
#     else:
#         raise AssertionError("新环境地图首次保存时，没有弹出引导")

        
def click_autosave_map_popmsg():
    """
        function:
            首次清扫出新环境地图，进入地图管理页面，点击弹出的新环境地图 保存引导框
            或者
            主机有图，首次开启多层地图，并点掉建图引导后，也会弹出该部分的引导消息
        args：
            none
        return:
            none
    """
    if exists(Template(r"tpl1592896712277.png", rgb=True, target_pos=7, record_pos=(-0.273, -0.364), resolution=(1080, 1920))) and not exists(Template(r"tpl1593582910812.png", rgb=True, target_pos=7, record_pos=(0.387, -0.362), resolution=(1080, 1920))):
        if exists(Template(r"tpl1592896924721.png", rgb=True, target_pos=7, record_pos=(0.065, -0.057), resolution=(1080, 1920))):
            poco(text='知道了').click()
        elif poco(text='点击此处保存新环境地图（仅支持保存完整的家居地图），若不保存，该地图会被其他新环境地图替代').exists() and poco(text='什么是完整家居地图').exists():
            poco(text='知道了').click()
        else:
            raise AssertionError("首次清扫出新环境地图，进入地图管理页面没有弹出引导存图弹框")
    else:
        log("非首次创建整图后进入多层地图")
        

def check_relocation_btn():
    """
        function:
            检查开启多层地图后，主界面有“寻找地宝位置”按钮
        args：
            none
        return:
            none
    """
    pass

def check_relocation_popmsg():
    """
        function:
            首次清扫出新环境地图，在主界面弹出“点击此处可定位地宝所在位置，建议在搬动后使用”
            或者
            开启多层地图，在主机清扫出整图后，重开安装app首次打开进入主界面，\
            在主界面弹出“点击此处可定位地宝所在位置，建议在搬动后使用” --》知道了
        args：
            none
        return:
            none
    """
    __popMsg__ = '点击此处可定位地宝所在位置，建议在搬动后使用'
    try:
        poco(name='com.eco.global.app:id/guide_tips').exists()
        if poco(name='com.eco.global.app:id/guide_tips').get_text() == __popMsg__:
            logger.debug(u'弹出“点击此处可定位地宝所在位置，建议在搬动后使用”的提示消息正确')
            log('弹出“点击此处可定位地宝所在位置，建议在搬动后使用”的提示消息正确')
            poco(text='知道了').click()
            logger.debug(u'点击“知道了”')
            log('点击“知道了”')
    except PocoTargetTimeout:
        raise PocoTargetTimeout("寻找地宝位置按钮在首次清扫完整图后，没有弹出引导消息[1]")
    except PocoNoSuchNodeException:
        raise PocoNoSuchNodeException("寻找地宝位置按钮在首次清扫完整图后，没有弹出引导消息[2]")

        
def click_to_save_newMap_as_map():
    """
        function:
            在地图管理页面，点击新环境地图的保存按钮，保存地图为地图1
        args：
            none
        return:
            save_as: 返回保存的地图名称（obj:str）
            eg. 返回值为：map1/map2
    """
    save_as = ''
    if  poco(name='com.eco.global.app:id/save_map_btn').exists():
        poco(name='com.eco.global.app:id/save_map_btn').click()
        # 只有新环境地图
        if "地图1" not in get_mapmgr_mapName() and "地图2" not in get_mapmgr_mapName():
            sleep(3)
            logger.debug("已保存为地图1")
            log("已保存为地图1")
            save_as = 'map1'
            return save_as
        # 有新环境地图 + 地图1
        elif "地图1" in get_mapmgr_mapName() and "地图2" not in get_mapmgr_mapName():
            sleep(3)
            logger.debug("已保存为地图2")
            log("已保存为地图2")
            save_as = 'map2'
            return save_as
        # 有新环境地图 +地图2
        elif "地图1" not in get_mapmgr_mapName() and "地图2" in get_mapmgr_mapName():
            sleep(3)
            logger.debug("已保存为地图1")
            log("已保存为地图1")
            save_as = 'map1'
            return save_as
        # 有新环境地图 +地图1 + 地图2
        elif "地图1" in get_mapmgr_mapName() and "地图2" in get_mapmgr_mapName():
            poco(text='地图已达上限，需要保存该地图，请选择已有地图进行替换').exists()
            poco(text='去替换').click(sleep_interval=2)
            # 默认选择第一个地图选择按钮
            poco(name='com.eco.global.app:id/map_selector').click(sleep_interval=1) 
            # 点击’替换‘
            poco(name='com.eco.global.app:id/right').click(sleep_interval=1)
            sleep(3)
            logger.debug("已保存为地图1")
            log("已保存为地图1")
            save_as = 'map1'
            return save_as
        else:
            raise AssertionError("出现异常，报错查看")                        
    else:
        raise AssertionError("没有新环境地图用来保存")
        
        
def click_rename_button():
    """
            function:
                在地图管理界面，点击重命名按钮
            args：
                none
            return:
                none
        """
    if poco(name='com.eco.global.app:id/text_right_btn').exists():
        poco(name='com.eco.global.app:id/text_right_btn').click()
        logger.debug(u'点击重命名按钮')                         
        log('点击重命名按钮')
    if poco(name='com.eco.global.app:id/dialog_title',text='地图重命名').exists():
        logger.debug(u'页面弹出重命名框')
        log('页面弹出重命名框')
    else:
        snapshot("页面没有弹出重命名框，截图检查")
        raise AssertionError("点击“重命名”没有页面没有弹出重命名框")


def click_to_enter_rename_text(rename_text):
    """
            function:
                在已打卡的重名名弹框界面，点击重命名输入框，并输入rename_text作为重命名字符串
            args：
                rename_text:重命名字符串(obj:str)
            return:
                none
    """
    poco(name='com.eco.global.app:id/name_edit_field').click()
    sleep(2)
    text(rename_text,enter=False)

def check_default_map_name(default_name):
    """
        function:
            在地图管理界面，点击重命名按钮，查看重命名窗口中的默认地图名称
        args：
            default_name:地图名称(obj:str),如，"地图1"            
        return:
            none 
    """
    click_rename_button()
    if poco(name='com.eco.global.app:id/name_edit_field').get_text() == default_name:
        logger.debug("默认地图名称为%s，正确" %default_name)
        log("默认地图名称为%s，正确" %default_name)
    else:
        snapshot("默认地图名称不正确，截图检查")
        raise AssertionError("默认地图名称不正确")
        
def modify_map_name(map_name):
    """
        function:
            主机有图，在地图管理界面，点击重命名按钮，给地图1/地图2重命名
        args：
            map_name:地图名称，长度为13位(obj:str)
            因为主机原本的地图名称占了3位，所以，该参数的长度最大为13位
        return:
            modified_name:重命名后主机的名称，(obj:str)
            格式为：“地图1”+map_name 
    """
    # 判断是否在多层地图页面
    try:
        poco(text='地图管理').wait_for_appearance()
    except:
        raise AssertionError("当前页面不在地图管理页面")
    # 判断输入字符长度
    if len(map_name) > 13:
        raise Exception("输入应该<=13位，请检查")
    else:
        # 点击重命名按钮
        if exists(Template(r"tpl1593845994151.png", record_pos=(-0.269, -0.266), resolution=(1080, 1920))):
            touch(Template(r"tpl1593845994151.png", record_pos=(-0.269, -0.266), resolution=(1080, 1920)))    
        elif poco(name='com.eco.global.app:id/text_right_btn').exists():
            poco(name='com.eco.global.app:id/text_right_btn').click(sleep_interval=1)
        logger.debug(u'点击重命名按钮')                         
        log('点击重命名按钮')
        ## 点击输入框    
        poco(name='com.eco.global.app:id/name_edit_field').click()
        logger.debug(u'点击输入框')                         
        log('点击输入框')
        log("尝试输入16位英文和数字字符")
        text(map_name,enter=False)
        sleep(1)
        # 点击确认
        poco(name='com.eco.global.app:id/tv_positive').click()
        sleep(2)
        modified_name = poco(name='com.eco.global.app:id/map_name').get_text()
        return modified_name
    

def get_map_name():
    """
            function:
                获取地图管理界面的地图名称
                或者
                获取主界面的地图名称
            args：
                none
            return:
                get_name: 获取到的地图名称
        """
    if poco(name='com.eco.global.app:id/map_name').exists():
        get_name = poco(name='com.eco.global.app:id/map_name').get_text()
        logger.debug("获取到的地图名称为：%s" % get_name)
        log("获取到的地图名称为：%s" % get_name)
        return get_name
    else:
        snapshot(msg="没有找到地图名称元素，截图检查")
        raise AssertionError("没有找到地图名称元素")


def click_to_mapmgr_setting():
    """
        function:
            主机有图，在地图管理界面，点击重地图名，进入地图管理的设置界面
        args：
            none
        return:
            mnone
    """
    # 判断是否在多层地图页面
    try:
        poco(text='地图管理').wait_for_appearance()
    except:
        raise AssertionError("当前页面不在地图管理页面")
    # 点击地图名称，进入地图管理的设置界面
    poco(name='com.eco.global.app:id/map_name').click()
    sleep(3)
    # 通过确认wifi地图元素是否存在，来判断是否成功进入
    try:
        poco(name='com.eco.global.app:id/iv_wifi_map').wait_for_appearance()
        logger.debug(u'进入地图管理的设置界面')                         
        log('进入地图管理的设置界面')
    except:
        raise AssertionError("进入地图管理的设置界面失败")

        
def click_map_catagory_button():
    """
        function:
            在地图管理的设置界面，点击“区域分类”
        args：
            none
        return:
            none
    """
    if poco(name='com.eco.global.app:id/area_map_tv').exists():
        poco(text='区域分类').click()
    try:
        poco(text='请点击区域编辑类型').wait_for_appearance()
    except:
        raise AssertionError("进入区域编辑类型失败")
       

def click_to_choose_map_catagory():
    """
        function:
            在点击“区域分类”后的地图管理的设置界面，点击“区域分类”,选择区域a/b/c为书房
        args：
            none
        return:
            none
    """
    # '请点击区域编辑类型' 对应的元素name
    if poco(name='com.eco.global.app:id/center_hint').exists():
        if exists(Template(r"tpl1593850901654.png", record_pos=(-0.001, 0.003), resolution=(1080, 1920))):
            touch(Template(r"tpl1593850901654.png", record_pos=(-0.001, 0.003), resolution=(1080, 1920)))
            logger.debug(u'选择区域A')                         
            log('选择区域A')
             
        elif exists(Template(r"tpl1593851176577.png", record_pos=(-0.245, -0.583), resolution=(1080, 1920))):
            touch(Template(r"tpl1593851176577.png", record_pos=(-0.245, -0.583), resolution=(1080, 1920)))
            logger.debug(u'选择区域b')                         
            log('选择区域B')
        elif exists(Template(r"tpl1593851290028.png", record_pos=(-0.177, -0.586), resolution=(1080, 1920))):
            touch(Template(r"tpl1593851290028.png", record_pos=(-0.177, -0.586), resolution=(1080, 1920)))
            logger.debug(u'选择区域C')                         
            log('选择区域C')
        else:
            snapshot("区域编辑类型页面没有显示区域截图.png","区域编辑类型页面没有显示区域截图")
            raise AssertionError("进入区域编辑类型失败")
    else:
        raise AssertionError("当前页面非区域编辑类型")
    # 进入请选择区域类型页面
    if poco(text='请选择区域类型').exists():
        poco(name='com.eco.global.app:id/title', text='客厅').click(sleep_interval=1)
        logger.debug(u'选择区域类型为书房')                         
        log('选择区域类型为书房')
    else:
        snapshot("在区域编辑类型页面点击区域，没有正确跳转页面.png","在区域编辑类型页面点击区域，没有正确跳转页面")
        raise AssertionError("在区域编辑类型页面点击区域，没有正确跳转页面")
    # 返回区域编辑类型
    poco(name='com.eco.global.app:id/title_back').click()
    try:
        wait(Template(r"tpl1594015672116.png", record_pos=(0.0, 0.0), resolution=(1080, 2340)))
        logger.debug(u'区域类型为书房成功选择[1]')                         
        log('区域类型为书房成功选择[1]')
    except Exception as e:
        snapshot("区域类型非书房，与选择不一致.png","区域类型非书房，与选择不一致")
        raise AssertionError("区域类型非书房，与选择不一致[1]",e)
    # 返回地图管理的设置页面
    poco(name='com.eco.global.app:id/title_back').click()
    try:
        wait(Template(r"tpl1594016215540.png", record_pos=(-0.002, -0.001), resolution=(1080, 2340)))
        logger.debug(u'区域类型为书房成功选择[2]')                         
        log('区域类型为书房成功选择[2]')
    except Exception as e:
        snapshot("区域类型非书房，与选择不一致.png","区域类型非书房，与选择不一致")
        raise AssertionError("区域类型非书房，与选择不一致[2]",e)
    # 返回地图管理界面
    poco(name='com.eco.global.app:id/title_back').click(sleep_interval=2)
    
            
def click_to_choose_living_room():
    """
        function:
            从地图管理界面开始，设置a/b/c为书房的一套流程
            步骤为：1.地图管理界面，点击地图
                    2.点击“区域分类”
                    3.选择a/b/c区域中的一个区域，
                    4.设置为书房
                    5.返回到地图管理界面
        args：
            none
        return:
            none
    """
    click_to_mapmgr_setting()
    click_map_catagory_button()
    click_to_choose_map_catagory()
    logger.debug(u'成功设置区域为客厅')                         
    log('成功设置区域为客厅')
    
    
        
       
       
       
       
    
# if __name__ == 'main':
if __name__ == 'airtest.cli.runner':
    if get_map_name() == '地图1一二三四五六七一二三四五六':
        logger.debug(u'地图管理界面上显示重命名成功')                         
        log('地图管理界面上显示重命名成功')
    ## 根据手机屏幕大小而定，小屏幕会显示出“...”
    elif  '...' in poco(name='com.eco.global.app:id/map_name').get_text():
        logger.debug(u'地图管理界面上显示不全的重命名用...代替')                         
        log('地图管理界面上显示不全的重命名用...代替')
    else:
        raise AssertionError('地图管理界面上显示重命名失败')
#     check_default_map_name("地图1")
#     click_to_choose_living_room()
#     click_to_choose_map_catagory()
#     click_to_mapmgr_setting()
#     print(modify_map_name('4567890abcdf'))
#     get_mapmgr_mapName()
#     click_main_to_mapmgr()
# #     click_to_mapmgr()
# #     sleep(5)
# #     mapmgr_to_main()
#     print(1111111111111111)
# #     mapmgr_switch = check_mapmgr_fun_swith()
# #     print(mapmgr_map_num(mapmgr_switch))
# #     click_mapmgr_switch(1)
#     check_mapmgr_build_notice()







