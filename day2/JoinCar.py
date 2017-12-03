import time
from selenium import webdriver

# 45版本以下的firefox浏览器, 不需要驱动文件
# 从46版本以上的firefox浏览器,也需要把driver.exe文件放到环境变量下面
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# 隐式等待, 一经设置,对后面的所有语句都有效果,所以在创建浏览器时设置一次就可以了
# implicitly 含蓄的,委婉的意思
driver.implicitly_wait(30)
# driver.maximize_window()

driver.get("http://localhost/")
# 在点击登录按钮之前,我们需要先删除target属性
# 但是javascript定位方式比selenium麻烦
# 可不可以用selenium的定位方式来替换javascript的定位方式呢?
# 用arguments关键字, 可以把元素定位作为一个参数,替换到javascript语句中
login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')", login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("changcheng")
driver.find_element_by_id("password").send_keys("123654")
driver.find_element_by_id("username").submit()
# submit()用于提交form表单, form是html中的一个元素
# form表单的任何子孙节点都可以调用submit()方法提交表单
# Alt+ enter 可以自动导包
# time.sleep(5)
# time.sleep到底设成几秒好.几秒都不好,
# 应该使用隐式等待,会自动判断网页是否加载完毕, 当加载完毕立刻开始执行后续的操作
# 我们需要设一个最大时间, 不能让程序无限等待, 一般这个时间是30秒
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
# iphone_img = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div:nth-child(2) > div.shop_01-imgbox > a > img"
iphone_link= "div:nth-child(2) > div.shop_01-imgbox > a"

# iphone_link2="body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div:nth-child(3) > div.shop_01-imgbox > a"
# img是标签名, >标签前面的是父节点, 后面的是子节点
# 如果想在css中写class属性, 那么前面需要加上小数点
# :nth-child(2), 表示当前节点在家中排行老二, 是它父亲的第二个儿子
# 为什么我们要把css selector中的内容改的越短越好?
# 涉及到越多的节点, 那么代码的健壮性和可维护性就越差
# 因为开发一旦修改页面时,修改了这些节点, 那么元素就会定位失败
# 因为我们copy的是selector,所以要用css selector的方式定位
iphone = driver.find_element_by_css_selector(iphone_link)
driver.execute_script("arguments[0].removeAttribute('target')", iphone)
iphone.click()

# 点击加入购物车按钮
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
#点击添加新地址
driver.find_element_by_class_name("add-address").click()

# 填写收货人
driver.find_element_by_css_selector("#add-new-address > div:nth-child(1) > input").send_keys("张三")
# 填写手机好
driver.find_element_by_name("address[mobile]").send_keys("13998023684")
# 选择下拉框
#
# driver.find_element_by_css_selector("[value='230000']").click()
sheng = driver.find_element_by_id("add-new-area-select")
# print(type(sheng))
# 下拉框是一种比较特殊的网页元素, selenium专门为下拉框提供了一种定位方式
# 需要把这个元素从WebElement类型转换成 Select 类型
# Select是selenium专门为我们创建的一个类, 用于操作下拉框的
# Select这个类中封装了很多操作下拉框的方法
Select(sheng).select_by_value('230000')

# 定位第二个下拉框
shi = driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_index(2)

# 定位第二个下拉框
xian = driver.find_elements_by_tag_name("select")[2]
Select(xian).select_by_visible_text("碾子山区")

#add-new-area-select
# driver.find_element_by_css_selector("#add-new-area-select")
# //*[@id="add-new-area-select"]
# driver.find_element_by_xpath('//*[@id="add-new-area-select"]')
driver.find_element_by_name("address[address]").send_keys("龙泽站")

driver.find_element_by_name("address[zipcode]").send_keys("110000")

driver.find_element_by_id("add-new-area-select").click()


