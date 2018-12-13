import requests
import os

def getImage(path_in,path_out):
    imgList = open(path_in).readlines()
    List = []
    m = 0
    rot = os.getcwd()
    if not(os.path.exists(rot+path_out)):
        os.mkdir(rot+path_out)
    for line in imgList:
        m = m+1
        line = line.strip()
        res = requests.get(line)
        
        print("Downloading:%s\n" % line)
        with open(rot+path_out+str(m)+".png",'ab') as f:
            for chunk in res.iter_content(chunk_size = 1024):
                if chunk:
                    f.write(chunk)
        print("Saved as %s\n" % path_out.strip+str(m)+".png")


print(os.getcwd())
getImage('imgList.txt','\\download\\')
