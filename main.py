import os#导入os模块，
import 爬虫模块库

name="goofish"
base_path=r"C:\Users\asus\Desktop\python工程\图片"#创建图片存储地址
urls=r"https://www.goofish.com/search"
goofish_path=base_path+'/goofish'
if not os.path.exists(goofish_path):#判断地址是否存在，如果不存在，使用os模块中的mkdir()函数创建地址
    os.mkdir(goofish_path)

response=爬虫模块库.get_html(urls)
爬虫模块库.parse_andz_download(response,goofish_path,name)
