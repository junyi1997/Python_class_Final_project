
#推撥Code
#沒事不要執行Line會很吵
from urllib.request import urlopen
from urllib.parse import quote

from threading import Timer
import datetime
import w_test

#def printTime(inc,i,a,b):
def printTime(a,b):
    #i+=1
    #print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #c="第{:}次小提醒".format(i)
    a=quote(a,'utf-8')
    b=quote(b,'utf-8')
    html = urlopen("https://maker.ifttt.com/trigger/105103308/with/key/dqTARGjv_Q1zeS_-LY1TyV?value1={:}".format(a))
    html = urlopen("https://maker.ifttt.com/trigger/105103308/with/key/dqTARGjv_Q1zeS_-LY1TyV?value1={:}".format(b))
    #t = Timer(inc, printTime, (inc,i,a,b,))
    #t.start()

#def my_main(i):
#    printTime(5,i)
def morring():
    print("早上")
    [a,b,c]=w_test.my_weather()
    printTime(a,b)
def noon():
    print("中午") 
    [a,b,c]=w_test.my_weather()
    printTime(a,b)  
def night():
    print("晚上")   
    [a,b,c]=w_test.my_weather()
    printTime(a,b)

def weathertime(C):
    print(C)
    while True:
        [a,b,c]=w_test.my_weather()
        if C == c:
            #print("氣象未更新")
            pass
        else:    
            print("更新完成")
            print(c)
            C=c
            printTime(a,b)
'''            
def my_time():
    while True:
        a=str(datetime.datetime.now())
        #print(a)
        a.split(' ')
        myhr=a[11]+a[12]
        mymin=a[14]+a[15]
        if myhr=='06' and mymin=='08':
            morring()
        elif myhr=='11' and mymin=='30': 
            noon()
        elif myhr=='18' and mymin=='00': 
            night()
'''    
if __name__ == "__main__":
    #i=0
    #[a,b]=w_test.my_weather()
    #print("a=",a,"\nb=",b)
    #my_main(i)
    #my_time()
    #printTime(a,b)
    [a,b,c]=w_test.my_weather()
    weathertime(c)