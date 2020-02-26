import requests

cookies = '_zap=b8299cd3-24ab-44d6-a5c5-55ac40556bdc; _xsrf=c5982556-3a5d-408c-ae66-032911d3b012; d_c0="ACDZ5Ysj1xCPThmSrzplO47gG6JWYfXxAwY=|1582095631"; capsion_ticket="2|1:0|10:1582381362|14:capsion_ticket|44:NzY5NTkyOWZjZTU2NDVkMzhhZGI2NTdjN2I4OTBlODk=|0b1f285ec4b9ad444496851699bf961e41bfc16477d6d3e1ca57a96c613a9359"; z_c0="2|1:0|10:1582381398|4:z_c0|92:Mi4xX2NzRURRQUFBQUFBSU5ubGl5UFhFQ1lBQUFCZ0FsVk5Wb2MtWHdCX0JhNWVGVldoWnRRVU00RHJkNlU5dXE1NHJB|9c9a06570e49dc0a41afa8aae534033783b7da99c2fb89961007077b4d6eb1af"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1582360519,1582360926,1582362196,1582453237; BAIDU_SSP_lcr=https://cn.bing.com/; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1582466763; KLBRSID=975d56862ba86eb589d21e89c8d1e74e|1582466773|1582466147'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
print(r.text)