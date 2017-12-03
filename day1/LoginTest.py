# 1.打开浏览器
from selenium import webdriver
# 从 selenium  导入  网络驱动, 用代码来操作浏览器的
# 第一个python语言不需要加分号
# 第二个Chrome后面一定要有括号
# 第三个字体的问题:
# 1.左上角File ---->settings---->Editor---->color and font---> font ---> 修改字体大小
driver = webdriver.Chrome()
# 2.打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
# 3.输入用户名, 首先寻找用户名的输入框
# 网页上所有可见的都属虎element, 比如, link, 按钮,下拉框....
# 在叫driver的浏览器上, 寻找一个网页元素, 如果它的id等于 "username"
# 并且向页面元素中发送键盘上常城这个几个按键
driver.find_element_by_id("username").send_keys("changcheng")
# 4.输入密码
driver.find_element_by_id("password").send_keys("123654")
# 5.点击登录按钮
# 如果我使用一个方法,这个方法没有提示信息,那么这个方法肯定是不存在的
driver.find_element_by_class_name("login_btn").click()