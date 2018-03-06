import os
import time

def listDir(fileDir):
    for eachFile in os.listdir(fileDir):
        if os.path.isfile(fileDir + "/" + eachFile) & eachFile.endswith(".pdf"):  # 如果是文件，判断最后修改时间，符合条件进行删除
            ft = os.stat(fileDir + "/" + eachFile);
            ltime = int(ft.st_mtime);  # 获取文件最后修改时间
            # print "文件"+path+"/"+eachFile+"的最后修改时间为"+str(ltime);
            ntime = int(time.time()) - 60;  # 获取现在时间减去1min
            if ltime <= ntime:
                print ("我要删除文件" + fileDir + "/" + eachFile);
                os.remove(fileDir + "/" + eachFile);  # 删除1min前的文件

        elif os.path.isdir(fileDir + "/" + eachFile):  # 如果是文件夹，继续递归
            listDir(fileDir + "/" + eachFile);


if __name__ == '__main__':
    path = r"C:\Users\jeafi\Desktop\1";  # 规定目录
    while True:  # 持续
        time.sleep(15);  # 减少资源利用率  600s秒一次
        print ("3600s  wake up");
        listDir(path);