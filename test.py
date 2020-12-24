#소스 
#https://blessingdev.wordpress.com/2017/10/20/term-project-%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4%EB%A5%BC-%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%97%90-%EA%B4%80%ED%95%98%EC%97%AC/


from bs4 import BeautifulSoup
import urllib.request as req
import os 
import requests

def get_html(url):
    html =""
    resp = requests.get(url)

    if resp.status_code == 200:
        html = resp.text
    
    return html


target = "가지(채소)"
base_url = "https://namu.wiki/w/{}".format(target)
html = get_html(base_url)


soup = BeautifulSoup(html,"html.parser")
# print(soup)
# class="wiki-heading-content"

searchList = soup.select("div.wiki-heading-content > div.wiki-paragraph")
# print(len(searchList))
# print(searchList[0].text)

image_search = soup.find_all()


savePath = 'C:\\Users\\mis\\Desktop\\crawling\\image'

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

# images = soup.select("div.wiki-paragraph > img")
# images = soup.find_all('img',{'class':'wiki-image'})
images = soup.findAll('img')
# print(images)
for i, div in enumerate(images,1):
    fullfilename = os.path.join(savePath, "채소"+ str(i)+'.jpg')
    # print('{} : {}'.format(i, fullfilename))
    # print(fullfilename)
    address ="""
   https://ww.namu.la/s/7de74a7a044d4675c6794b5944ac4829cc8d18f7588fd81a685ddfd4065ca9f3dbaba4d54ebf8445271a422b682f9842b8e921cf9b5bf3cd3ec99952f4d85a1540e03b058b353a6a9432aac903b0c6e158aac869747d6f4d31195d5911ede9cf        """
    # print(type(requests.get(address)))
    # req.urlretrieve(address,fullfilename)


