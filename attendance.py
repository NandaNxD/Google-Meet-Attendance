from bs4 import BeautifulSoup
import re
import os
import datetime
import requests

#   Date in DD-MM-YYYY format 
today=str(datetime.datetime.date(datetime.datetime.now()))
today=today[8:10]+'-'+today[5:7]+'-'+today[0:4]

# Change directory to current directory
os.path.dirname(os.path.abspath(__file__))      
if os.path.dirname(os.path.abspath(__file__))!=os.getcwd():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Input Class name which is same as Html file
fname=input('Enter class name: ')

# Open html file of the google meet 
h=open(fname+'.html')

# Parse html file
data=BeautifulSoup(h,'lxml')
reqd=data.findAll('div',{'class':'XWGOtd'},{'role':'presentation'})

# Find the names of the attendees
name=re.findall('data-sort-key=\"(.*?) spaces',str(reqd))

# Dictionary which consists of names of students
nlist=dict()
for i in name:
    nlist[i]=1

# Open CSV file for the class

xl=fname+'.csv'
try:
    excel=open(xl,'r')
    edata=excel.readlines()
except:
    print('Empty Excel')
    #exit(0)
    #Create new Excel file 
    xname=fname+'.csv'
    excel=open(xname,'w')
    exit(0)

excel.close()

st=""
cnt=0
for line in edata:
    # print(line)
    line=line.replace(',,',',')
    cnt+=1
    if(cnt==1):
        #print(today)
        st+=line[:len(line)-1]+','+today+'\n'
    else:
        a=line.split(',')
        eles=a[0]
        eles=eles[0:len(eles)-1]
        print(eles)
        if(eles in nlist.keys() or a[0] in nlist.keys()):
            st += line[:len(line)-1]+','+'P\n'
        else:
            st += line[:len(line)-1]+','+'A\n'

print(st)

# Write to the excel file
excel=open(xl,'w')
excel.write(st)


