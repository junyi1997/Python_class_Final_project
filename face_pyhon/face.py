import face_pyhon.face_module as m   # 匯入自訂模組
#import face_module as m   # 匯入自訂模組
def my_main():
    print("開始進行臉部辨識")
    base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0' # 端點
    key = '16b209ef30ca4f56a355332e2ed69df1'                             # 你的金鑰
    gid = 'gp01'                                                         # 群組 Id
    pid = ''                                                             # 成員 Id
    
    #pid for 106111123 ： 5e21fd0d-8444-4bf3-9b5f-67891e826dc4
    #pid for 105103308 ： 17d646da-05b4-45b0-8cbb-14055f742534
    
    
    m.face_init(base, key)  # 初始化端點和金鋪
    m.face_use(gid, '')    # 指定要操作的 gid 和 pid
    Account=m.face_shot('who')      # 呼叫拍照函式來拍照並上傳到Azuse新增成員人臉影像
    return Account
#    print("Account",Account)


#----------------------------------------------------------------------
if __name__ == "__main__":
    my_main() 