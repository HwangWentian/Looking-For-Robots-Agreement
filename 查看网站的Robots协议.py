from re import findall as fa
from requests import get

if __name__ == "__main__":
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}
    while True:
        url = input("输入网址：")
        if url == "":
            print("错误的地址")
            continue
        if url[-1] != "/":
            url += "/"
        try:
            url = fa(pattern=r"http[s]?://.+?/", string=url)[0] + "robots.txt"
            text = get(url=url, headers=header)
            text.encoding = text.apparent_encoding
            text = text.text
            print(text)
        except:
            print("错误的地址")
