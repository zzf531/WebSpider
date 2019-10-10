import requests
url = "https://www.amazon.cn/dp/B0011F7WU4/ref=s9_acss_bw_cg_JAVA_1a1_w?m=A1AJ19PSB66TGU&pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-6&pf_rd_r=D9MK8AMFACZGHMFJGRXP&pf_rd_t=101&pf_rd_p=f411a6d2-b2c5-4105-abd9-69dbe8c05f1c&pf_rd_i=1899860071"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)
    print(r.text[1000:2000])
except:
    print('爬取错误')
