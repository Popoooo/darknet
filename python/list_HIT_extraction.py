import glob, os
#dir = 'C:/Users/winte/Desktop/mei0_999'
dir = 'C:/Users/377/Desktop/ogurano/Sec/2_2rd_ano/image_1000_1999_manual'

extraction_list = open('extraction_list1.txt', 'w')

for pathAndFilename in glob.iglob(os.path.join(dir, "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    f = open(dir + "/" + title + ".txt" , "r")
    line = f.readline()
    while line:
        if line.startswith("1") or line.startswith("2") or  line.startswith("3"):
            extraction_list.write(dir + "/" + title + ".jpg" + "\n")
            break
        line = f.readline()
    f.close()
    
