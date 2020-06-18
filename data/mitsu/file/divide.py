import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)
f_name = 'mitsu'


#current_dir = '../pic/'
#g_colab_full_path='/content/darknet/data/' + f_name + '/pic'
current_dir'/content/gdrive/My Drive/Colab Notebooks/Dataset/train/' + f_name
g_colab_full_path='/content/gdrive/My Drive/Colab Notebooks/Dataset/train/' + f_name
#train_pass = f_name + '-train.txt'
#test_pass = f_name + '-test.txt'
train_pass = 'cfg-train.txt'
test_pass = 'cfg-test.txt'

# Percentage of images to be used for the test set
percentage_test = 20

# Create and/or truncate train.txt and test.txt
file_train = open(train_pass, 'w')  
file_test = open(test_pass, 'w')# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
        counter = counter + 1
