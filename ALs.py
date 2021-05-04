import requests
import json
import csv

token='1776016878:AAEJCHpS_N84FeBgQ8_B741xAGWEW12LnlM'
method='sendMessage'

def get_data(index_no):
    r=requests.get('https://www.doenets.lk/result/service/AlResult/'+str(index_no))
    jsondata = json.loads(r.text)
    if jsondata['year']==None:
        print(str(index_no)+' is not valid')
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

        print(year)
        print(name)
        print(indexNo)
        print(nic)
        print(districtRank)
        print(islandRank)
        print(zScore)
        print(stream)
        print(Sub1name)
        print(Sub1result)
        print(Sub2name)
        print(Sub2result)
        print(Sub3name)
        print(Sub3result)
    
        msg=year+'\n'+name+'\n'+indexNo+'\n'+nic+'\n'+districtRank+'\n'+islandRank+'\n'+zScore+'\n'+stream+'\n'+Sub1name+' '+Sub1result+'\n'+Sub2name+' '+Sub2result+'\n'+Sub3name+' '+Sub3result

        response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
        data={'chat_id':-1001448516010, 'text': msg}
        ).json() 


for i in range(1000000,9999999):
	get_data(i)
