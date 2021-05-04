import requests
import json
import csv

def get_data(index_no):
    try:
        r=requests.get('https://www.doenets.lk/result/service/AlResult/'+str(index_no))
        jsondata = json.loads(r.text)

        if jsondata['year']==None:
            print(index_no+' is not valid')
            
        else:

            year=str(jsondata['year'])
            name=jsondata['name']
            indexNo=str(jsondata['indexNo'])
            nic=str(jsondata['nic'])
            districtRank=str(jsondata['districtRank'])
            islandRank=str(jsondata['islandRank'])
            zScore=str(jsondata['zScore'])
            stream=jsondata['stream']
            Sub1name=jsondata['subjectResults'][0]['subjectName']
            Sub1result=jsondata['subjectResults'][0]['subjectResult']
            Sub2name=jsondata['subjectResults'][1]['subjectName']
            Sub2result=jsondata['subjectResults'][1]['subjectResult']
            Sub3name=jsondata['subjectResults'][2]['subjectName']
            Sub3result=jsondata['subjectResults'][2]['subjectResult']

            arr=[year,name,indexNo,nic,districtRank,islandRank,zScore,stream,Sub1name,Sub1result,Sub2name,Sub2result,Sub3name,Sub3result]
            print(indexNo)
            
            
            with open('results.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(arr)
                csvFile.close()
        
    except:
        print('err')

fromm=1000000  
to   =9999999

for i in range(fromm,to):
	get_data(i)

