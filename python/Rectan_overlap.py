##かぶっている矩形領域を判別してはじくスクリプト

import glob, os
from collections import namedtuple
import cv2

#dir = 'C:/Users/377/Desktop/ogurano/Sec/last_result/2nd'
#imgdir = 'C:/Users/377/Desktop/ogurano/Sec/last_result'
dir = 'C:/Users/winte/Desktop/cheese/2nd/cheese'
imgdir = 'C:/Users/winte/Desktop/cheese/2nd/cheese'
#vertex_list = open('vertex_list.txt', 'w')

#yolo形式を定義
yolo_rect = namedtuple('yolo_rect','c x y w h')

#矩形を定義
Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')

#yolo形式（中心点[x,y]と矩形の大きさ横縦[w,h]）から矩形の頂点(右上)と(左下）を求める関数
#* w,yは正確には画像の大きさに対する比率だが、領域の重なりが分かればいいのでこの際このままいきます。
def vertex(rec):
    
    hw = rec.w/2 #横辺の半分
    hh = rec.h/2 #縦辺の半分
    r = Rectangle(rec.x-hw, rec.y-hh, rec.x+hw, rec.y+hh) #(xmin ymin xmax ymax)
    return r

#重なっている部分の面積を求める関数
def area(ra, rb):  # returns None if rectangles don't intersect
    dx = min(ra.xmax, rb.xmax) - max(ra.xmin, rb.xmin)
    dy = min(ra.ymax, rb.ymax) - max(ra.ymin, rb.ymin)
    if (dx>=0) and (dy>=0):
        return dx*dy

#重なっている割合を求める関数 0が不一致、1が最大
def rectan_similar(yolo_a,yolo_b):
    iarea = area(vertex(yolo_a), vertex(yolo_b))
    if iarea != None:
        nab = (yolo_a.w * yolo_a.h) + (yolo_b.w * yolo_b.h) - iarea
        return iarea/nab

#画像を切り出す関数
def img_cut(imgdir, imgtitle, rect, count):
    filename = imgdir + '/' + imgtitle + '_re' + '.jpg'
    #filename = imgdir + '/' + imgtitle + '.jpg'
    # 画像読み込み
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    
    #画像のサイズを取得
    hw = rect.w/2 #横辺の半分
    hh = rect.h/2 #縦辺の半分
    height, width, channels = img.shape[:3]
    
    #yolo形式座標をcvピクセルに分解
    top = max(0, (rect.y - hh) * height)
    bottom = max(0, (rect.y + hh) * height)
    left = max(0, (rect.x - hw) * width)
    right = max(0, (rect.x + hw) * width)
    #画像の切り出し img[top : bottom, left : right]
    img1 = img[int(top) : int(bottom), int(left): int(right)]
    writename = imgdir + '/res/res_' + str(int(rect.c)) + '_' + str(count) + '.jpg'
    cv2.imwrite(writename, img1)


#test用
a = yolo_rect(1, 0.6387, 0.4101, 0.1934, 0.2220)
b = yolo_rect(1, 0.6567, 0.3774, 0.0315, 0.0253)

#print (rectan_similar(a, b))
classlist = 5
classcount = [0] * classlist
count = 0

#フォルダ内のファイルを順番に読み込み
for pathAndFilename in glob.iglob(os.path.join(dir, "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    list = []
    #ファイルを１行ずつ読み込み
    for line in open(dir + "/" + title + ".txt" , "r").readlines():
        lsp = line.rstrip().split(" ")
        lsp = [float(i) for i in lsp]
        a = yolo_rect(lsp[0],lsp[1],lsp[2],lsp[3],lsp[4])
        #print("現在の行")
        #print(title + ' => ' + str(a))
        #print(" ")

        #print("リスト")
        #print(list)
        #print(" ")
        
        
        vertex_count = 0
        similar = 0.0
        #Listの中身すべてと現在の行(Line)を比較する
        for i in list:
            isp = i.rstrip().split(" ")
            isp = [float(i) for i in isp]
            b = yolo_rect(isp[0], isp[1],isp[2],isp[3],isp[4])
            #print("重複率")
            similar = rectan_similar(a, b)
            #print (similar)
            #print(" ")
            
            if similar != None: #重複があればflagを立てる
                if similar > 0.6: #6割以上重複していたら
                    vertex_count = vertex_count + 1
        #重複がなかった場合、現在の行(line)をListに追加する
        if vertex_count == 0:
            list.append(line)
            img_cut(imgdir, title, a, classcount[int(a.c)])
            classcount[int(a.c)] = classcount[int(a.c)] + 1
            count = count + 1
    #print(title + "最終リスト")
    #print(list)

for i,classnum in enumerate(classcount):
    print('CLASS_' + str(i) + ' => ' + str(classnum))
print('All_CLASS => ' + str(count))