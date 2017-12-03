#1.之前的readCsv不能被其他测试用例调用，所以应该给这段代码封装在一个方法里
#2.每个测试用例的路径不同，所以path应该作为参数传入到这个方法中
#4.我们打开了一个文件，但是并没有关闭，最终可能会造成内存泄露
import csv
import os
def read (file_name):#path作为参数
    #所有的重复代码的出现，都是程序设计的不合理
    #重复的代码应该封装在一个方法里
    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4", "data/" + file_name)
   # file = open(path, 'r')
    #with 语句是一个代码块，代码块的内容都要缩进4个空格
    #with 代码块可以自动关闭with中声明的变量file
    #try ...finally.... 也可以保证程序中间发生异常时,文件最后也可以关闭,
    #但是finally语法的可读性比较差,写起来比较容易出错, 一般都用with语句代替finally
    #因为file文件一旦被关闭，里面的数据也随着消失，所以单独声明一个列表result来保存里面的数据
    result = []
    with open(path, 'r') as file :
        data_table = csv.reader(file)
        for row in data_table:
            result.append(row)
            #print(row)
    return result
        #如果在打开和关闭程序的代码中间发生了异常，导致后面的代码不能正常运行
        #这样file_close()也无法执行，这时，文件仍然不能关闭
        #应该用with...as...语句实现文件的关闭
        #file.close()
if __name__ == '__main__':
   # path = r"C:\Users\51Testing\PycharmProjects\1125\data\member_info.csv"
    #3.这个路径是一个绝对路径，我们工作中一个项目不止一个人编写
    #我们没法统一要求大家都把项目代码放在一个路径下，因为有的人会放在d盘
    #这个文件因为在项目中，它的路径也会随着项目变化
    #所以应该在代码中,通过当前文件代码文件的路径，根据相对位置自动找到相对路径
   #所以首先要找到当前文件的路径
   #os是操作系统,path是路径，dir是directory目录
   #__file__是python内置的变量，指的是当前文件
  # current_file_path=os.path.dirname(__file__)
   #print(current_file_path)
   #我们真正想要的路径是csv文件的路径
  # path = current_file_path.replace("day4", "data/member_info.csv")
   #print(path)
   #  找到一个csv文件自动找到相对路径
  # base_path=""
   member_info = read("member_info.csv")
   #member_info = read("goods_info.csv")
   #print(member_info)
   #使用for循环是为了将打印结果分行打印
   for row in member_info :
       #print（row）
       print(row[0])#row[0]只打印姓名

   #5.读出数据不是目的，目的是通过数据驱动测试，所以应该把数据作为方法的返回值方便进一步调用
       #使用return