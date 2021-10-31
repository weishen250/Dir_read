import os
import requests
import re

from main import url

file_dir = r"F://demo.vhsop//"
host = r"https://demo.vshop.kuaidiantong.cn/"

a = os.walk(file_dir)

ufp = open('./surl.txt',mode='a+',encoding='utf-8')
dfp = open('./sdir.txt',mode='a+',encoding='utf-8')
for root, dirs, files in os.walk(file_dir):

    # print(root) #当前目录路径
    # print(dirs) #当前路径下所有子目录
    # for cc in files:
    #     print(cc) #当前路径下所有非目录子文件

    home = root.replace(file_dir,'')
    # print(dir)

    for bb in files:
        name,ext = os.path.splitext(bb)
        ps = ('.ico','.css','.js','.png','.jpg','.gif','.cs','.dll')
        dir0 = home + '/' + bb
        if ext not in ps:
            dir = dir0.replace('\\','/').replace('//','/')
            print(dir)
            dfp.write(dir+'\n')

            url = host +dir

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
                      }
            resp = requests.get(url = url,headers=headers)

            code = resp.status_code
            lenge = resp.headers

            if code == 200:

                if 'content-length' in lenge.keys():  # if Flase  执行
                    content_length = lenge['content-length']

                    ufp.write(url  + '  ||  ' + content_length + '\n')
                    print(url+ '  ||  ' + content_length)




    # for son_dir in root :
    #     print(son_dir)
    #     for root2, dir2, file2 in os.walk(son_dir):
    #         for name in files:
    #             print(file2)