<<<<<<< HEAD
# -*- encoding=utf8 -*-
__author__ = "lei.z"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

import json,pika

auto_setup(__file__)

# 连接的认证信息
credentials = pika.PlainCredentials('lei.z', '123456')
parameters = pika.ConnectionParameters('10.88.41.231',
                                       5672,
                                       '/',
                                       credentials)
# 根据当前开关的状态，返回开启或关闭
def get_switch_status():
    '''
    由于开关按钮在元素中没有text选项
    使用次函数方便获取开启或关闭字段
    方便进行状态判断
    '''
    if exists(Template(r"tpl1585632339980.png", rgb=True, record_pos=(0.396, -0.53), resolution=(1080, 1920))):
        return '开启'
    elif exists(Template(r"tpl1585632400738.png", rgb=True, record_pos=(0.409, -0.588), resolution=(1080, 1920))):
        return '关闭'
    else:
        return '没有开关按钮'

# 封装一个断言函数，判断两个结果是否一致
def assert_result_equal(expectation,actuality,check_info):
    # 断言函数引用加入抓错，不会影响程序运行
    try:
        assert_equal(expectation,actuality,check_info)
        return True
    except Exception as e:
        return False
    snapshot(msg=check_info)

# 封装一个断言函数，判断一个结果在误差范围内
def assert_deviation_equal(expectation,actuality,deviation=2,check_info='判断APP上的结果和实际结果在误差内'):
    expect = '一致'
    
    # 计算实际结果和期望结果之间的差值
    deviation_value = abs(expectation-actuality)
    # 将差值和误差值作比较
    if deviation_value <= deviation:
        actual = '一致'
    else:
        actual = '不一致'
    try:
        assert_equal(expect,actual,check_info+'--实际值：'+str(expectation)+'--显示值：'+str(actuality))
        return True
    except Exception as e:
        return False
    snapshot(msg=check_info)
    
# 元素存在断言,元素作为一个参数，函数判断此元素存在情况是否符合预期   
def assert_exists_check(element,check_info="检查",expectation='存在'):
    # 如果元素存在，实际值actuality为存在，否则值为不存在
    if element.exists():
        actuality = '存在'
    else:
        actuality= '不存在'
    # 断言实际结果和预期结果进行比较
    try:
        assert_equal(expectation,actuality,check_info+expectation)
        return True
    except Exception as e:
        return False
    snapshot(msg=check_info)

# 弱提示存在断言     
def wait_assert_exists_check(expectation,pic,info="检查有弱提示--"):
    '''检查有弱提示
    pic参数为一个弱提示图像
    '''
    # wait函数没有等到要的结果会报错，影响函数运行
    try:
        wait(pic,timeout=5)
        actual = "存在"
    except Exception as e:
        actual = "不存在"
    check_info=info+expectation
    assert_result_equal(expectation,actual,check_info)

# 断言函数，判断两个值大小是否符合预期
def assert_comparison(value1,value2,expectation='greater',check_info="检查两值大小"):
    if value1 > value2:
        actuality = 'greater'
    else:
        actuality = 'less'
    ret = assert_equal(expectation,actuality,check_info)
    snapshot(msg=check_info)
# MQ消息传递函数
def publish_message2queue(queuename,body_text):

    # 格式转换字典转为字符串
    body_info = json.dumps(body_text)
    # 进行连接queue
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # 声明一个queue
    channel.queue_declare(queue=queuename)

    # 信息传递至queue
    channel.basic_publish(exchange='',
                      routing_key=queuename,
                      body=body_info)
    # print(" [x] Sent 'deebot run message'")
    connection.close()
    return " [x] Sent 'deebot run message'"

# 从任何页面返回主界面
def back_to_main(deebotname="DEEBOT T8 POWER"):
    if poco("com.eco.global.app:id/actionbar_image_title").exists():
        poco(text=deebotname).click(sleep_interval=1)
    else:
        while(bool(1-poco("com.eco.global.app:id/top_status_more").exists())):
            poco("com.eco.global.app:id/title_back").click(sleep_interval=1)
    snapshot(msg="显示主界面")

# 从任何页面返回设备列表页面
def back_to_devicelist():
    if poco("com.eco.global.app:id/actionbar_image_title").exists():
        pass
    else:
        back_to_main()
        poco("com.eco.global.app:id/top_status_back1").click(sleep_interval=1)
    snapshot(msg="显示设备列表界面") 
    snapshot(msg="显示设备列表界面")

# 每隔interval秒检查一次需要的元素
def wait_element_expected(element,func=snapshot(),interval=30):
    '''
    每隔interval检查一次页面，看是否有出现需要的结果
    出现，则调用响应的函数
    '''
    while True:
        if element.exists():
            func
            break
        else:
            sleep(interval)
# 每隔interval秒检查一次需要的图片
def wait_pic_expected(pic,func,interval=30):
    while True:
        if exists(pic):
            func
            break
        else:
            sleep(interval)

# 截图并保存到指定目录
def snapshot_and_save(filepath=r'D:\airtest_result'):
    name=time.strftime("%m%d-%H%M%S") + '.png'
    snapshot(filename = filepath + '\\' + name,msg='take a pic')



=======
# -*- encoding=utf8 -*-
__author__ = "lei.z"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

import json,pika

auto_setup(__file__)

# 连接的认证信息
credentials = pika.PlainCredentials('lei.z', '123456')
parameters = pika.ConnectionParameters('10.88.41.231',
                                       5672,
                                       '/',
                                       credentials)
# 根据当前开关的状态，返回开启或关闭
def get_switch_status():
    '''
    由于开关按钮在元素中没有text选项
    使用次函数方便获取开启或关闭字段
    方便进行状态判断
    '''
    if exists(Template(r"tpl1585632339980.png", rgb=True, record_pos=(0.396, -0.53), resolution=(1080, 1920))):
        return '开启'
    elif exists(Template(r"tpl1585632400738.png", rgb=True, record_pos=(0.409, -0.588), resolution=(1080, 1920))):
        return '关闭'
    else:
        return '没有开关按钮'

# 封装一个断言函数，判断两个结果是否一致
def assert_result_equal(expectation,actuality,check_info):
    # 断言函数引用加入抓错，不会影响程序运行
    try:
        assert_equal(expectation,actuality,check_info)
        return True
    except Exception as e:
        return False
    snapshot(msg=check_info)

# 封装一个断言函数，判断一个结果在误差范围内
def assert_deviation_equal(expectation,actuality,deviation=2,check_info='判断APP上的结果和实际结果在误差内'):
    expect = '一致'
    
    # 计算实际结果和期望结果之间的差值
    deviation_value = abs(expectation-actuality)
    # 将差值和误差值作比较
    if deviation_value <= deviation:
        actual = '一致'
    else:
        actual = '不一致'
    try:
        assert_equal(expect,actual,check_info+'--实际值：'+str(expectation)+'--显示值：'+str(actuality))
        return True
    except Exception as e:
        return False
    snapshot(msg=check_info)
    
# 元素存在断言,元素作为一个参数，函数判断此元素存在情况是否符合预期   
def assert_exists_check(element,check_info="检查",expectation='存在'):
    # 如果元素存在，实际值actuality为存在，否则值为不存在
    if element.exists():
        actuality = '存在'
    else:
        actuality= '不存在'
    # 断言实际结果和预期结果进行比较
    try:
        assert_equal(expectation,actuality,check_info+expectation)
        return True
    except Exception as e:
        return False
    snapshot(msg=check_info)

# 弱提示存在断言     
def wait_assert_exists_check(expectation,pic,info="检查有弱提示--"):
    '''检查有弱提示
    pic参数为一个弱提示图像
    '''
    # wait函数没有等到要的结果会报错，影响函数运行
    try:
        wait(pic,timeout=5)
        actual = "存在"
    except Exception as e:
        actual = "不存在"
    check_info=info+expectation
    assert_result_equal(expectation,actual,check_info)

# 断言函数，判断两个值大小是否符合预期
def assert_comparison(value1,value2,expectation='greater',check_info="检查两值大小"):
    if value1 > value2:
        actuality = 'greater'
    else:
        actuality = 'less'
    ret = assert_equal(expectation,actuality,check_info)
    snapshot(msg=check_info)
# MQ消息传递函数
def publish_message2queue(queuename,body_text):

    # 格式转换字典转为字符串
    body_info = json.dumps(body_text)
    # 进行连接queue
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # 声明一个queue
    channel.queue_declare(queue=queuename)

    # 信息传递至queue
    channel.basic_publish(exchange='',
                      routing_key=queuename,
                      body=body_info)
    # print(" [x] Sent 'deebot run message'")
    connection.close()
    return " [x] Sent 'deebot run message'"

# 从任何页面返回主界面
def back_to_main(deebotname="DEEBOT T8 POWER"):
    if poco("com.eco.global.app:id/actionbar_image_title").exists():
        poco(text=deebotname).click(sleep_interval=1)
    else:
        while(bool(1-poco("com.eco.global.app:id/top_status_more").exists())):
            poco("com.eco.global.app:id/title_back").click(sleep_interval=1)
    snapshot(msg="显示主界面")

# 从任何页面返回设备列表页面
def back_to_devicelist():
    if poco("com.eco.global.app:id/actionbar_image_title").exists():
        pass
    else:
        back_to_main()
        poco("com.eco.global.app:id/top_status_back1").click(sleep_interval=1)
    snapshot(msg="显示设备列表界面")
  
# 每隔interval秒检查一次需要的元素
def wait_element_expected(element,func=snapshot(),interval=30):
    '''
    每隔interval检查一次页面，看是否有出现需要的结果
    出现，则调用响应的函数
    '''
    while True:
        if element.exists():
            func
            break
        else:
            sleep(interval)
# 每隔interval秒检查一次需要的图片
def wait_pic_expected(pic,func,interval=30):
    while True:
        if exists(pic):
            func
            break
        else:
            sleep(interval)

# 截图并保存到指定目录
def snapshot_and_save(filepath=r'D:\airtest_result'):
    name=time.strftime("%m%d-%H%M%S") + '.png'
    snapshot(filename = filepath + '\\' + name,msg='take a pic')
    
# class telnet_to_device(host=HOST, username=USERNAME, password=PASSWORD):
#     """
#         function:
#             telnet到主机
#         args：
#             host：（obj:str）缺省值为HOST, 是deebot的ip地址
#             username:（obj:str）缺省值为USERNAME, 是deebot的用户名, 
#             password:（obj:str）缺省值为PASSWORD, 是deebot的密码
#         return:
#             返回telnet连接的对象
#     """
#     tn = telnetlib.Telnet(HOST)
#     tn.read_until('deboot login: '.encode("ascii"))
#     tn.write(USERNAME.encode("ascii") + b'\n')
#     time.sleep(1)
#     tn.read_until('Password: '.encode("ascii"))
#     tn.write(PASSWORD.encode("ascii") + b'\n')
#     time.sleep(1)
#     tn.read_until(FINISH.encode("ascii"))
#     log("登陆成功")
    
# if __name__ == 'airtest.cli.runner':
# # if __name__ == 'main':
# TN = telnet_to_device(host='192.168.1.58',username='root',password='eco_rd4!')
# echo_cmd = "echo > \tmp\log\11.txt"
# TN.write(echo_cmd)

    



>>>>>>> xiaomei.teng
