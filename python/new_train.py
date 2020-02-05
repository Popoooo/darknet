import glob, os

#dir = 'C:/Users/377/Desktop/ogurano/2nd_ano'
#dir = 'C:/Users/377/Desktop/下見/results/ori'
dir = 'C:/Users/winte/Desktop/cheese/3rd'


# Create and/or truncate train.txt and test.txt
new_train = open('new_train_list_c.txt', 'w')  
 
 
for pathAndFilename in glob.iglob(os.path.join(dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    new_train.write(dir + "/" + title + '.jpg' + "\n")
