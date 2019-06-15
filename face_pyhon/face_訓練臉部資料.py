import requests

base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'    # 端點
gId = 'gp01'    # 要訓練的群組
train_url = f'{base}/persongroups/{gId}/train' # 請求路徑
key = '6f9af40fc8924f9fa3fe8795905a057b'   # 你的金鑰
headers = {'Ocp-Apim-Subscription-Key': key}   # 請求標頭
response = requests.post(train_url,            # POST 請求
                         headers = headers)
if response.status_code == 202:     
    print("開始訓練...")
else:
    print("訓練失敗", response.json())

