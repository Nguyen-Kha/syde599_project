import glob, os

import time
from datetime import datetime

path = 'C:\\Users\\Kha\\Documents\\Waterloo\\4A\\SYDE 599\\Project\\cleaned_data\\without_header_task'
train = []
test = []
val = []
os.chdir(path)
for file in glob.glob('*.txt'):
    task_number = int((str(file).split('_')[2]).split('.')[0])
    if(task_number > 4):
        os.remove(file)
        continue
        
    patient_number = str(file.split('_')[0])
    
    while patient_number[0] == '0':
        patient_number = patient_number[1:]
        
    patient_number = int(patient_number)
    
    if(patient_number < 10):
        train.append(file)
    elif(patient_number == 10 or patient_number == 11):
        test.append(file)
    else:
        val.append(file)

path_train_test_val = 'C:\\Users\\Kha\\Documents\\Waterloo\\4A\\SYDE 599\\Project\\cleaned_data\\without_header_train_test_val'
train_file = os.path.join(path_train_test_val,'train.txt')
test_file = os.path.join(path_train_test_val,'test.txt')
val_file = os.path.join(path_train_test_val,'val.txt')
# os.mkdir('C:\\Users\\Kha\\Documents\\Waterloo\\4A\\SYDE 599\\Project\\cleaned_data\\without_header_train_test_val')

start = datetime.now()
with open(train_file, 'w+') as outfile:
    for fname in train:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

with open(test_file, 'w+') as outfile:
    for fname in test:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

with open(val_file, 'w+') as outfile:
    for fname in val:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
                
end = datetime.now()
print(end - start)
