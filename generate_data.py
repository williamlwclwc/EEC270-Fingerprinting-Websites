import os
import csv

train_path = "./data/train.csv"
test_path = "./data/test.csv"
f1 = open(train_path, 'w')
writer1 = csv.writer(f1)
writer1.writerow([
    'cache-misses-1', 'node-loads-1', 'branch-misses-1', 'branch-load-misses-1',
    'cache-misses-2', 'node-loads-2', 'branch-misses-2', 'branch-load-misses-2',
    'cache-misses-3', 'node-loads-3', 'branch-misses-3', 'branch-load-misses-3',
    'cache-misses-4', 'node-loads-4', 'branch-misses-4', 'branch-load-misses-4',
    'cache-misses-5', 'node-loads-5', 'branch-misses-5', 'branch-load-misses-5',
    'label'
])
f2 = open(test_path, 'w')
writer2 = csv.writer(f2)
writer2.writerow([
    'cache-misses-1', 'node-loads-1', 'branch-misses-1', 'branch-load-misses-1',
    'cache-misses-2', 'node-loads-2', 'branch-misses-2', 'branch-load-misses-2',
    'cache-misses-3', 'node-loads-3', 'branch-misses-3', 'branch-load-misses-3',
    'cache-misses-4', 'node-loads-4', 'branch-misses-4', 'branch-load-misses-4',
    'cache-misses-5', 'node-loads-5', 'branch-misses-5', 'branch-load-misses-5',
    'label'
])
dir_path = "./sample_output"
files = os.listdir(dir_path)
for file in files:
    num_trace = int(file.split('_')[1].split('.')[0])
    if num_trace > 50:
        # test
        fw = writer2
    else:
        # train
        fw = writer1
    label = file.split('_')[0]
    with open(dir_path + '/' + file, 'r') as f:
        all_lines = f.readlines()
        # cache-misses:u node-loads:u branch-misses:u branch-load-misses:u
        row = []
        for i in range(3, len(all_lines)):
            trace = all_lines[i].split()
            row.append(trace[1])
        row.append(label)
        fw.writerow(row)

f1.close()
f2.close()