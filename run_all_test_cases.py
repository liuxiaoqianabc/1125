import unittest


if __name__ == '__main__':
    #defaultTestLoader默认测试用例加载器，用来寻找符合一定规则的测试用例
    #discover 发现,*表示通配符，任意文件
    # unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    # 定义一个变量名
    suite = unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    #执行suite中的所有的测试用例
    #TextTestRunner文本测试用例运行器，返回一段文本日志
    #TextTestRunner首字母大写，说明它是一个类，类不能直接调用方法，必须要实例化对象才能调用方法
    #python中实例化不需要new 关键字，直接在类后面加一个小括号就行
    unittest.TextTestRunner().run(suite)
