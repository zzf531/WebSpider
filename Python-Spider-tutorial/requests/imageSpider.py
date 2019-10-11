# 导入模块
import requests
# 下载图片地址
url = "https://pic3.zhimg.com/50/v2-f37e65e90750e994a719f427595cb7a7_hd.jpg"
# 发送请求获取响应
response = requests.get(url)
# 保存图片
with open('image.png','wb') as f:
    # 返回响应内容，
  f.write(response.content)

'''
保存图片时后缀名和请求的后缀名一致

保存必须使用 response.content 进行保存文件
'''
