#!/usr/bin/python3

import os
import sys

# First part

if len(os.listdir('/home/administrator/Desktop/00010-GCS-u_R_0_IW/ft_reference')) == 0:
    print("Directory missing: ft_reference")
    sys.exit()

if len(os.listdir('/home/administrator/Desktop/00010-GCS-u_R_0_IW/ft_run')) == 0:
    print("Directory missing: ft_run")
    sys.exit()

# Second part

dir1 = os.listdir('/home/administrator/Desktop/00010-GCS-u_R_0_IW/ft_reference/1')
dir2 = os.listdir('/home/administrator/Desktop/00010-GCS-u_R_0_IW/ft_run/1')

duplicates = set(dir1) & set(dir2)

orig_stdout = sys.stdout
f = open('report.txt', 'w')
sys.stdout = f

for file in dir1:
    if file not in duplicates:
        print("In ft_run there are missing files present in ft_reference: " + file)
   

for file in dir2:
    if file not in duplicates:
        print("In ft_reference there are missing files present in ft_run: " + file)

sys.stdout = orig_stdout

f.close()

# Third part

file_path = "/home/administrator/Desktop/00010-GCS-u_R_0_IW/ft_run/1/1.stdout"

word0 = 'error'
word1 = 'Error' 
word2 = 'ERROR'

with open(file_path) as file:
    for num_line, line in enumerate(file):
        if word0 in line:
            print("Error in line:" , num_line)
            print(line)
        if word1 in line:
            print("Number of line is:" , num_line)
            print(line)
        if word2 in line:
            print("Number of line is:" , num_line)
            print(line)

with open(file_path) as file:
    contents = file.read()
    search_word = 'Solver finished at'
    for search_word in contents:
        break
    else:
        print ("In 00010-GCS-u_R_0_IW/ft_run/1/1.stdout: missing'Solver finished at'")

# Four part

word = 'Memory Working Set'  
 
inp = open('/home/administrator/Desktop/00010-GCS-u_R_0_IW/ft_run/1/1.stdout').readlines()

orig_stdout = sys.stdout 
f = open('report1.txt', 'w')
sys.stdout = f


for i in iter(inp):
    if word in i:
        print(i)

sys.stdout = orig_stdout

f.close()


with open('/home/administrator/Desktop/report1.txt', 'r') as f1:
    lines = f1.readlines()
lines = [line.replace(' ', '') for line in lines]
with open('/home/administrator/Desktop/report1.txt', 'w') as f1:
    f1.writelines(lines)

with open('/home/administrator/Desktop/report1.txt') as f2:
    n = []
    for line in f2:
        line = line.replace(",", ".")   
        found = line.find('SetPeak=')
        if found !=1:
            a = line[found+len('SetPeak='):len(line)-len('Mb')-1]
            if (len(a))>1:
                n.append(float(a))
    #print(max(n))

###----------------------------------------------

word = 'Memory Working Set'  

inn = open('/home/administrator/Desktop/00010-GCS-u_R_0_IW/ft_reference/1/1.stdout').readlines()

orig_stdout = sys.stdout 
f3 = open('report2.txt', 'w')
sys.stdout = f3


for i in iter(inn):
    if word in i:
        print(i)

sys.stdout = orig_stdout

f3.close()


with open('/home/administrator/Desktop/report2.txt', 'r') as f4:
    lines = f4.readlines()
lines = [line.replace(' ', '') for line in lines]
with open('/home/administrator/Desktop/report2.txt', 'w') as f5:
    f5.writelines(lines)

with open('/home/administrator/Desktop/report2.txt') as f6:
    m = []
    for line in f6:
        line = line.replace(",", ".")   
        found = line.find('SetPeak=')
        if found !=1:
            c = line[found+len('SetPeak='):len(line)-len('Mb')-1]
            if (len(c))>1:
                m.append(float(c))
    #print(max(m))

x = ((max(m)/max(n))*100)
if x < 50:
    print("/home/administrator/Desktop/00010-GCS-u_R_0_IW/ft_run different: Memory Working Set Peak" + " ft_run = " + str(max(n)) + " ft_reference= " + str(max(m)) + " rel.diff= " + str(round(x,2)))

# Four part (2)

word1 = 'MESH::Bricks:'  
 
ink = open('/home/administrator/Desktop/00010-GCS-u_R_0_IW/ft_run/1/1.stdout').readlines()

orig_stdout = sys.stdout 
f8 = open('report3.txt', 'w')
sys.stdout = f8


for i in iter(ink):
    if word1 in i:
        print(i)

sys.stdout = orig_stdout

f8.close()


with open('/home/administrator/Desktop/report3.txt', 'r') as f10:
    lines = f10.readlines()
lines = [line.replace(' ', '') for line in lines]
with open('/home/administrator/Desktop/report3.txt', 'w') as f10:
    f10.writelines(lines)

with open('/home/administrator/Desktop/report3.txt') as f20:
    y = []
    for line in f20:
        line = line.replace(",", ".")   
        found = line.find('Total=')
        f = line.find('Gas=')
        if found !=1:
            b = line[f:]
            a = line[found+len('Total='):f]
            if (len(a))>1:
                y.append(float(a))
    #print(y[len(y)-1])


inz = open('/home/administrator/Desktop/00010-GCS-u_R_0_IW/ft_reference/1/1.stdout').readlines()

orig_stdout = sys.stdout 
f9 = open('report4.txt', 'w')
sys.stdout = f9


for i in iter(inz):
    if word1 in i:
        print(i)

sys.stdout = orig_stdout

f9.close()


with open('/home/administrator/Desktop/report4.txt', 'r') as f11:
    lines = f11.readlines()
lines = [line.replace(' ', '') for line in lines]
with open('/home/administrator/Desktop/report4.txt', 'w') as f11:
    f11.writelines(lines)

with open('/home/administrator/Desktop/report4.txt') as f21:
    w = []
    for line in f21:
        line = line.replace(",", ".")   
        found = line.find('Total=')
        f = line.find('Gas=')
        if found !=1:
            b = line[f:]
            a = line[found+len('Total='):f]
            if (len(a))>1:
                w.append(float(a))
    #print(w[len(w)-1])

x = (y[len(y)-1]/w[len(w)-1])*100
if x < 90:
    print("/home/administrator/Desktop/00010-GCS-u_R_0_IW different: Total of bricks" + " ft_run = " + str(max(n)) + " ft_reference= " + str(max(m)) + " rel.diff= " + str(round(x,2)))
