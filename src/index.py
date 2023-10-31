import requests

# 获取信息地址
apiGetUrl = "https://7qb-api.jd.com/mock/getList"
# 提交结果地址
apiPutUrl = "https://7qb-api.jd.com/mock/setItem"

# try
response = requests.get(url=apiGetUrl, timeout=18)

if response.status_code == 200:
    print(response.text)


session = {"key":"value"}
requests.post(url=apiPutUrl, data=session)
