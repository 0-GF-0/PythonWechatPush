import requests

title = input("请输入内容：")
content = input("请输入内容：")

def get_page(url):
    page = requests.get(url)
    page = page.content
    page = page.decode('utf-8')
    return page

print(get_page('https://sctapi.ftqq.com/SCT35577TgqNbqFTRNh7Hf6OeHeSj3zxp.send?title='+title+'&desp='+content))