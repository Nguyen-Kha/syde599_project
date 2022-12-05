import pandas as pd
import glob, os

raw_path = 'C:\\Users\\Kha\\Documents\\Waterloo\\4A\\SYDE 599\\Project\cleaned_data\\without_header'

def add_task_to_data(path, file_name, task_number):
    old_labels = ['index', 'timestamp', 'LTA', 'RTA', 'IO', 'ECG', 'RGS', 'accel_x1', 'accel_y1', 'accel_z1', 'gyro_x1', 'gyro_y1', 'gyro_z1', 'NC1', 'accel_x2', 'accel_y2', 'accel_z2', 'gyro_x2', 'gyro_y2', 'gyro_z2', 'NC2', 'accel_x3', 'accel_y3', 'accel_z3', 'gyro_x3', 'gyro_y3', 'gyro_z3', 'NC3', 'accel_x4', 'accel_y4', 'accel_z4', 'gyro_x4', 'gyro_y4', 'gyro_z4', 'SC', 'label']
    ordered_labels = ['task', 'timestamp', 'LTA', 'RTA', 'IO', 'ECG', 'RGS', 'accel_x1', 'accel_y1', 'accel_z1', 'gyro_x1', 'gyro_y1', 'gyro_z1', 'NC1', 'accel_x2', 'accel_y2', 'accel_z2', 'gyro_x2', 'gyro_y2', 'gyro_z2', 'NC2', 'accel_x3', 'accel_y3', 'accel_z3', 'gyro_x3', 'gyro_y3', 'gyro_z3', 'NC3', 'accel_x4', 'accel_y4', 'accel_z4', 'gyro_x4', 'gyro_y4', 'gyro_z4', 'SC', 'label']
    output_path =  'C:\\Users\\Kha\\Documents\\Waterloo\\4A\\SYDE 599\\Project\\cleaned_data\\without_header_task\\'
    
    df = pd.read_csv(path, header=None)
    df.columns = old_labels
    df = df.drop(labels=['index'], axis=1)
    
    df['task'] = task_number
    df = df[ordered_labels]
    
    df.index.name = 'index'
    
    output_file_name = output_path + file_name
    df.to_csv(output_file_name, header=False, index=False)
    
    pass

def rename_patient_8():
    path = 'C:\\Users\\Kha\\Documents\\Waterloo\\4A\\SYDE 599\\Project\\cleaned_data\\without_header_task'
    os.chdir(path)
    os.rename('0081_task_1.txt', '008_task_1.txt')
    os.rename('0081_task_2.txt', '008_task_2.txt')
    os.rename('0081_task_3.txt', '008_task_3.txt')
    os.rename('0081_task_4.txt', '008_task_4.txt')
    os.remove('0082_task_1.txt')
    os.remove('0082_task_2.txt')
    os.remove('0082_task_3.txt')
    os.remove('0082_task_4.txt')
    pass

def main():
    os.chdir(raw_path)
    for file in glob.glob('*.txt'):
        task_number = (str(file).split('_')[2]).split('.')[0]
        
        path= raw_path + '\\' + str(file)
        add_task_to_data(path=path, file_name=file, task_number = task_number)

        pass
    
    rename_patient_8()


if __name__ == '__main__':
    main()
