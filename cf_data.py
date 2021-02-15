from datetime import datetime,date
from bs4 import BeautifulSoup
import requests

def count():
    today=date.today()
    cur_date=today.strftime("%b/%d/%Y")

    # insert your handle here
    user="" 
    base='http://codeforces.com/submissions/' + user + '/page/'
    page=1

    resp=requests.head(base+str(page))
    #print(resp.status_code)
    data=requests.get(base+str(page))
    html=data.content
    soup=BeautifulSoup(html,"html.parser")

    trs=soup.find_all('tr')
    s=0
    faced=[]

    for tr in trs:
        if tr.get("data-submission-id") == None: continue
        td=tr.find_all('td')
        day         = str(td[1])
        problem_url = td[3].a.get('href')
        verdict     = td[5].span.get('submissionverdict')
        #print(verdict)
        dt=(day.split(' ')[3]).split('>')[1]
        if((problem_url not in faced) and (cur_date==dt) and len(verdict)==2):
            s+=1
            faced.append(problem_url)
    return s