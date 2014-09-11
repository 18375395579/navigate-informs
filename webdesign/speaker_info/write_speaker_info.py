import cPickle as pickle
import re


doc_comm=pickle.load(open('doc_comm.pickle','rb'))
user_comm=pickle.load(open('user_comm_cutspeaker5.pickle','rb'))
talk_speaker=pickle.load(open('talk_speakerfull.pickle','rb'))
talk_speaker1=pickle.load(open('talk_speaker1.pickle','rb'))

print user_comm.keys()[0]

comm1=[]
comm2=[]
comm3=[]
comm4=[]
comm5=[]
for key in doc_comm:
    if doc_comm[key]==0:
        comm1.append(key)
        
    elif doc_comm[key]==1:

        
        comm2.append(key)
    elif doc_comm[key]==2:
       
        
        comm3.append(key)
    elif doc_comm[key]==3:

        comm4.append(key)
    elif doc_comm[key]==4:
     
        comm5.append(key)




for k in range(5):
    speaker=re.sub('"','',talk_speaker[comm1[k]])
    if talk_speaker1[comm1[k]] in user_comm:
        c1="<div class='topic'><table><tr><td>"+speaker+"</tr></td><tr><td>"+"User community"+str(user_comm[talk_speaker1[comm1[k]]])+"</tr></td></table>"
    else:
        c1="<div class='topic'><table><tr><td>"+speaker+"</tr></td></table>"
    name=talk_speaker1[comm1[k]]
    html1=open('comm1'+str(k)+'.html',"a")
    html1.write(c1)
    html1.close()

for k in range(5):
    speaker=re.sub('"','',talk_speaker[comm2[k]])
    if talk_speaker1[comm2[k]] in user_comm:
        c1="<div class='topic'><table><tr><td>"+speaker+"</tr></td><tr><td>"+"User community"+str(user_comm[talk_speaker1[comm2[k]]])+"</tr></td></table>"
    else:
        c1="<div class='topic'><table><tr><td>"+speaker+"</tr></td></table>"
    name=talk_speaker1[comm2[k]]
    html1=open('comm2'+str(k)+'.html',"a")
    html1.write(c1)
    html1.close()
    
for k in range(5):
    speaker=re.sub('"','',talk_speaker[comm3[k]])
    if talk_speaker1[comm3[k]] in user_comm:
        c1="<div class='topic'><table><tr><td>"+speaker+"</tr></td><tr><td>"+"User community"+str(user_comm[talk_speaker1[comm3[k]]])+"</tr></td></table>"
    else:
        c1="<div class='topic'><table><tr><td>"+speaker+"</tr></td></table>"
    name=talk_speaker1[comm3[k]]
    html1=open('comm3'+str(k)+'.html',"a")
    html1.write(c1)
    html1.close()
    
for k in range(5):
    speaker=re.sub('"','',talk_speaker[comm4[k]])
    if talk_speaker1[comm4[k]] in user_comm:
        c1="<div class='topic'><table><tr><td>"+speaker+"</tr></td><tr><td>"+"User community"+str(user_comm[talk_speaker1[comm4[k]]])+"</tr></td></table>"
    else:
        c1="<div class='topic'><table><tr><td>"+speaker+"</tr></td></table>"
    name=talk_speaker1[comm4[k]]
    html1=open('comm4'+str(k)+'.html',"a")
    html1.write(c1)
    html1.close()
    
for k in range(5):
    speaker=re.sub('"','',talk_speaker[comm5[k]])
    if talk_speaker1[comm5[k]] in user_comm:
        c1="<div class='topic'><table><tr><td>"+speaker+"</tr></td><tr><td>"+"User community"+str(user_comm[talk_speaker1[comm5[k]]])+"</tr></td></table>"
    else:
        c1="<div class='topic'><table><tr><td>"+speaker+"</tr></td></table>"
    name=talk_speaker1[comm5[k]]
    html1=open('comm5'+str(k)+'.html',"a")
    html1.write(c1)
    html1.close()