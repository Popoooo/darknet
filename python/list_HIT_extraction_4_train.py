import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = '../data/meitrain/1000_1999'

print(current_dir)

g_colab_full_path='/content/darknet/data/meitrain/1000_1999'

# Percentage of images to be used for the test set
percentage_test = 20;

# Create and/or truncate train.txt and test.txt
file_train = open('meigetsu-train.txt', 'w')  
file_test = open('meigetsu-test.txt', 'w')# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    f = open(current_dir + "/" + title + ".txt" , "r")
    line = f.readline()
    while line:
        if line.startswith("1") or line.startswith("2") or  line.startswith("3"):            
            if counter == index_test:
                counter = 1
                file_test.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
            else:
                file_train.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
                counter = counter + 1
            break
        line = f.readline()
    f.close()
    
