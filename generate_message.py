from random import randint
from cf_data import count
from select import good,bad

def get_sl():
    with open("sl.txt","r") as f:
        num=f.read()
        a,b=map(int,num.split(','))
    return a,b

def updt_sl(r,a,b):
    if r:
        a+=1
        with open("sl.txt","w") as f:
            s=str(a)+','+str(b)
            f.write(s)
    else:
        b+=1
        with open("sl.txt","w") as f:
            s=str(a)+','+str(b)
            f.write(s)

def generate_message():
    ls=[]
    cnt=0
    with open("Ps.txt","r") as f:
        words=f.readlines()
        for line in words:
            ls.append(line)
            cnt+=1
    num=randint(0,cnt-1)
    ps2="\nP.S. "+ls[num]
    return ps2

def message():
    n=int(count())
    ptg=(abs(n-2)/2)*100
    introduction="""My Qtpi,
Hope you are nice and cute by the grace of Almighty.\n"""
    cnt="\nYou have solved {} problem(s) today.".format(n)
    if(n<2):
        vrdc="That's {} % less than your daily goal.".format(ptg)
        opn="Look queen, I know you have a kingdom to run. But can't you solve 2 problems in 24 hours? 2 P R O B L E M S -_- . I want no excuses. Hope you won't disappoint from the next day. Keep that in mind -_-."
    elif(n==2):
        vrdc="All though you have completed your daily goal, my expectations from you, is much higher. You are on the edge. Hope you will solve more from the next day."
        opn=""
    else:
        vrdc="That's {} % more than your daily goal. ".format(ptg)
        opn="""Queen , o my queen, have you not set codeforces on flames ! Sad for Mike Mirzayanov tho. 
Take my heartiest of congratulations. I hope you will keep this up, always. """
    conc="\nI am fine. How's your enchanted mirror doing? \n"
    a,b=get_sl()
    if(n>=2):
        gift=good(a)
        ps1="\nP.S. Since you have completed your goal, here's a little gift : {}".format(gift)
        updt_sl(1,a,b)
    else:
        gift=bad(b)
        ps1="\nP.S. Punishment for not completing your goal : {}\n\n".format(gift)
        updt_sl(0,a,b)
    ps2=generate_message()
    sign="""\nYour's always,
    SAK"""
    msg=introduction+cnt+vrdc+opn+"\n"+conc+ps1+ps2+sign
    return msg