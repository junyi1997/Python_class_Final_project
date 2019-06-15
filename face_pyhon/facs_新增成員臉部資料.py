import face_module as m   # 匯入自訂模組

base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0' # 端點
key = '6f9af40fc8924f9fa3fe8795905a057b'                             # 你的金鑰
gid = 'gp01'                                                         # 群組 Id
pid = 'a94b6139-d33e-4f03-b961-9fb37bba59dd'                         # 成員 Id

m.face_init(base, key)  # 初始化端點和金鋪
m.face_use(gid, pid)    # 指定要操作的 gid 和 pid
m.face_shot('add')      # 不斷進行拍照並上傳到Azuse新增成員人臉影像

