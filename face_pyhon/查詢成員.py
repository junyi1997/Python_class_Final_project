import requests

base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'    # 端點
gp_url = base + '/persongroups/gp01'                                    # 創建群組的請求路徑
key = '6f9af40fc8924f9fa3fe8795905a057b'                                # 你的 key
headers = {'Ocp-Apim-Subscription-Key': key}   # 請求標頭
response = requests.get(gp_url, 
                        headers = headers)       # HTTP GET
if response.status_code == 200:                       
    print(response.json())
else:
    print("查詢失敗", response.json())
