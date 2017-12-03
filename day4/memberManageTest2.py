import unittest
#1.导入ddt代码库
import ddt
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsv2 import read

#2.装饰这个类
@ddt.ddt
class MemberManagerTest2(unittest.TestCase):
    #3.调用之前写好的read()方法，获取配置文件中的数据
    member_info = read("member_info.csv")
   #数据读出来，附上一个变量
    # 在当前类只执行一次
    #装饰class方法
    @classmethod
    # def 定义一个方法
    def setUpClass(cls):
        print("在所有方法之前,只执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    def test_a_log_in(self):
        print("登录测试")
        driver = self.driver
        driver.get("http://localhost/admin.php")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(
            Keys.ENTER).perform()
        #python中集合前的星号，表示把集合中的所有元素拆开，一个一个写
        #list=["小红","小马"];
        #*list="小红","小马"
        #星号的作用就是把一个列表，拆成连个string
        #假如一个方法需要接收两个参数，那么肯定不能传一个list进去
        #但是如果list中正好也是两个元素，这时在列表前面加一个*
        #这时就不认为这是一个列表，而是两个参数
        #5.ddt.data()测试数据来源于read()方法，然后把数据表中的每一行传入方法
        # 在方法中增加一个参数row
    @ddt.data(*member_info)
    def test_b_add_member(self, row):
        # 每组测试数据就是一条测试用例，每条测试用例应该是独立的，不能因为上一条测试用例执行失败
        # 导致下一组数据不能被正常执行，所以这里不推荐用for循环
        #应该用ddt装饰器，去修饰这个方法，达到每条测试用例独立执行的目的
        #ddt是数据驱动测试，data driver test
        #4.注释掉for循环，改变代码的缩进，使方法中的代码比方法声明缩进4个空格，快捷键是shift+TAP
        #for row in read("member_info.csv"):
        #print("添加会员")
        driver = self.driver
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        # driver.switch_to_frame("mainFrame")
        iframe_css = "#mainFrame"
        # 如果frame没有name属性时，我们可以通过其他方式定位ifame标签，把定位好的页面元素传给driver.switch_to_frame(iframe_html)方法也可以实现frame切换
        iframe_html = driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        # '[value="' + row[2] + '"]'='[value="1"]'
        # format是初始化
        driver.find_element_by_css_selector('[value="{0}"]'.format(row[2])).click()
        # driver.find_element_by_css_selector('[value="'+row[2]+'"]').click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        # 之前的代码是能够自动运行，但是还不能自动判断程序运行是否正确
        # 我们自动化代码，不能找人一直盯着运行，检查是否执行正确
        # actual实际结果，执行测试用例后，页面上实际显示的结果
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        # 获取元素的文本
        #  #expected期望结果，来自于手动测试用例，或者是需求文档，配置文件
        expected = row[0]
        # 断言类似于if...else...，用来做判断的
        # if(actual == expected):#()可以不写
        #     print("测试通过")
        # else:
        #     print("测试失败")
        # 断言叫assert，断言是框架提供的，要想用断言，那么必须加上self
        # 因为测试用例类继承了框架中的TestCase类，也继承了这个类中的断言，所以我们直接用断言
        # 断言有几个特点：
        # 1.断言比较简洁
        # 2.断言关注于错误的测试用例，只有断言出错的时候，才会打印信息，正确时没有打印信息
        # 3.断言报错时，后面的代码将不会继续执行，前面的步骤失败，后面的步骤就不需要尝试执行了，浪费性能
        # for循环输入完用户名后就跳回去会员管理，所以需要切换到原来的输入用户名界面
        # 切换到父框架
        # driver.switch_to.parent_frame()
        # 切换到网页的根节点
        driver.switch_to.default_content()
        # driver.switch_to.active_element#切换到鼠标所在的元素
        self.assertEqual(actual, expected)  # 写在切换窗口后面
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()
    # 加入main方法是为了让所有的方法都执行，鼠标放在main方法后
