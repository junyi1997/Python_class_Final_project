import face_module as m   # 匯入自訂模組

base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0' # 端點
key = '16b209ef30ca4f56a355332e2ed69df1'                             # 你的金鑰
gid = 'gp01'                                                         # 群組 Id
pid = '5e21fd0d-8444-4bf3-9b5f-67891e826dc4'                         # 成員 Id

m.face_init(base, key)  # 初始化端點和金鋪
m.face_use(gid, pid)    # 指定要操作的 gid 和 pid
m.face_shot('add')      # 不斷進行拍照並上傳到Azuse新增成員人臉影像

