import cPickle as pickle
import re
doc_comm=pickle.load(open('doc_comm.pickle','rb'))
user_comm=pickle.load(open('_cutspeaker5.pickle','rb'))
talk_speaker=pickle.load(open('talk_speaker1.pickle','rb'))

comm1=[]
comm2=[]
comm3=[]
comm4=[]
comm5=[]
ncomm1=[]
ncomm2=[]
ncomm3=[]
ncomm4=[]
ncomm5=[]

for key in user_comm:
    if user_comm[key]==0:
        ncomm1.append(key)
    elif user_comm[key]==1:
        ncomm2.append(key)
    elif user_comm[key]==2:
        ncomm3.append(key)
    elif user_comm[key]==3:
        ncomm4.append(key)
    elif user_comm[key]==4:
        ncomm5.append(key)

for key in doc_comm:
    if doc_comm[key]==0:
        key=key[6:]
        key=re.sub('"','',key)
        comm1.append(key)
        
    elif doc_comm[key]==1:
        key=key[6:]
        key=re.sub('"','',key)
        comm2.append(key)
    elif doc_comm[key]==2:
        key=key[6:]
        key=re.sub('"','',key)
        comm3.append(key)
    elif doc_comm[key]==3:
        key=key[6:]
        key=re.sub('"','',key)
        comm4.append(key)
    elif doc_comm[key]==4:
        key=key[6:]
        key=re.sub('"','',key)
        comm5.append(key)
        
        
        
name='comm11'

c1="""<div class='topic'>
<div><A HREF="ncomm1.html">Community 1</A></div>
<div class="row">
<table style="width:50%">"""
for k in range(5):
    c1=c1+"""<tr><td><a href="file:///Users/yujialiu/Desktop/research/webdesign/speaker_info/comm1"""+str(k)+""".html" onclick="javascript:void window.open("'file:///Users/yujialiu/Desktop/research/webdesign/speaker_info/comm1"""+str(k)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""+comm1[k]+"""</td></tr>"""

c1=c1+"""</table>
<div class="col-g-2" style="float:right">
<img src="./wordmap/wordmapu1.jpg">
</div>
<div class='clearing'></div></div>"""


c2="""<div class='topic'><div><A HREF="ncomm2.html">Community 2</A></div><table>"""
for k in range(5):
    c2=c2+"""<tr><td><a href="file:///Users/yujialiu/Desktop/research/webdesign/speaker_info/comm2"""+str(k)+""".html" onclick="javascript:void window.open("'file:///Users/yujialiu/Desktop/research/webdesign/speaker_info/comm2"""+str(k)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""+comm2[k]+"""</td></tr>"""
c2=c2+"""</table><div class='clearing'></div></div>"""

c3="""<div class='topic'><div><A HREF="ncomm3.html">Community 3</A></div><table>"""
for k in range(5):
    c3=c3+"""<tr><td><a href="file:///Users/yujialiu/Desktop/research/webdesign/speaker_info/comm3"""+str(k)+""".html" onclick="javascript:void window.open("'file:///Users/yujialiu/Desktop/research/webdesign/speaker_info/comm3"""+str(k)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""+comm3[k]+"""</td></tr>"""
c3=c3+"""</table><div class='clearing'></div></div>"""

c4="""<div class='topic'><div><A HREF="ncomm4.html">Community 4</A></div><table>"""
for k in range(5):
    c4=c4+"""<tr><td><a href="file:///Users/yujialiu/Desktop/research/webdesign/speaker_info/comm4"""+str(k)+""".html" onclick="javascript:void window.open("'file:///Users/yujialiu/Desktop/research/webdesign/speaker_info/comm4"""+str(k)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""+comm4[k]+"""</td></tr>"""
c4=c4+"""</table><div class='clearing'></div></div>"""

c5="""<div class='topic'><div><A HREF="ncomm5.html">Community 5</A></div><table>"""
for k in range(5):
    c5=c5+"""<tr><td><a href="file:///Users/yujialiu/Desktop/research/webdesign/speaker_info/comm5"""+str(k)+""".html" onclick="javascript:void window.open("'file:///Users/yujialiu/Desktop/research/webdesign/speaker_info/comm5"""+str(k)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""+comm5[k]+"""</td></tr>"""
c5=c5+"""</table><div class='clearing'></div></div>"""


html=open("yujia7.html","w")
html.write(c1+c2+c3+c4+c5)
html.close()

