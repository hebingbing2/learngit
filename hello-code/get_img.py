#-*- coding: utf-8 -*-
import requests
from lxml import etree
import os


def main():
    print("It will get some img from douban!")
    goon = input("want , enter Y, else enter N :\n")
    if goon == "Y" or goon == "y":
        filename = input("Enter the file name for save img ! \n")
        get_img(filename)
    elif goon == "N" or goon == "n":
        quit()

    

def get_img(fileName):
    print("Enter img address; \n")
    print("like (https://movie.douban.com/celebrity/1054449/photos/) , just for douban !!! ")
    img_add = input()
    if img_add:  
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
        response=requests.get(img_add, headers=header)
        selector=etree.HTML(response.content)
        img_douban = selector.xpath("//div[@class='cover']/a/img/@src")
        for img_item in img_douban:
            DIR_PATH = "E:\\Project\\Python\\img\\"+fileName   #图片保存路径
            try:
                img = requests.get(img_item, headers=header, timeout=10)
                with open( DIR_PATH+img_item[-10:], 'wb') as f:
                    f.write(img.content)
                    print("Downloading : " + img_item)
            except Exception as e:
                print(e)
        print("finish!")
    else:
        print ("Img add is null ! \n")
        print (img_add)
        go_on = input("try again? yes(Y), no(n) : ")
        if go_on == "Y" or go_on == "y":
            filename = input("Enter the file name for save img ! \n")
            get_img(filename)
        elif go_on == "N" or go_on == "n":
            quit()
        else:
            print ("error")
            main()



    

main()
 