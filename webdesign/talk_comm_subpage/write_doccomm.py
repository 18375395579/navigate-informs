# create a HTML file with the full list of the talk names, followed by the appropriate speaker

import cPickle as pickle
import re

glue=' '
user_comm=pickle.load(open('doc_comm_cut5.pickle','rb'))
#talk_speaker= pickle.load(open('/Users/john/Downloads/webdesign/talk_comm_subpage/talk_speaker1.pickle', 'rb'))
talk_speaker_full=pickle.load(open('talk_speakerfull.pickle','rb'))
talk_speaker=pickle.load(open('talk_speaker_fixname.pickle','rb'))
speaker_fixname=pickle.load(open('speaker_fixname.pickle','rb'))
talk_details=pickle.load(open('talk_details.pickle','rb'))

comm1=[] # different communities
comm2=[]
comm3=[]
comm4=[]
comm5=[]

# store the orginial communities to be used for keys later
commOrig1=[] # different communities
commOrig2=[]
commOrig3=[]
commOrig4=[]
commOrig5=[]
for key in user_comm:
    if user_comm[key]==0:
        commOrig1.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm1.append(key) 
        
    elif user_comm[key]==1:
        commOrig2.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm2.append(key)
        
    elif user_comm[key]==2:
        commOrig3.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm3.append(key)
        
    elif user_comm[key]==3:
        commOrig4.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm4.append(key)
        
    elif user_comm[key]==4:
        commOrig5.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm5.append(key)
string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""

c1="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div class='topic'><div>Full List of Talks: Community 1</div><table>"""
for k1 in range(len(comm1)):
    content= ""
    for i in talk_details[commOrig1[k1]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages/comm1'+str(k1)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig1[k1]]
    name=''.join(name)
    c1=c1+"""<tr><td><a href="../speaker_pages/comm1"""+str(k1)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm1"""+str(k1)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c1=c1+comm1[k1]+", "+name+"</td></tr>"

c1=c1+"</table><div class='clearing'></div></div></html>"

html1=open("ncomm1.html","w")
html1.write(c1)
html1.close()


c2="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div class='topic'><div>Full List of Talks: Community 2</div><table>"""
for k2 in range(len(comm2)):
    content= ""
    for i in talk_details[commOrig2[k2]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html2=open('../speaker_pages/comm2'+str(k2)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html2.write(string+content)
    html2.close()
    name=talk_speaker[commOrig2[k2]]
    name=''.join(name)
    c2=c2+"""<tr><td><a href="../speaker_pages/comm2"""+str(k2)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm2"""+str(k2)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c2=c2+comm2[k2]+", "+name+"</td></tr>"

c2=c2+"</table><div class='clearing'></div></div></html>"

html2=open("ncomm2.html","w")
html2.write(c2)
html2.close()


c3="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div class='topic'><div>Full List of Talks: Community 3</div><table>"""
for k3 in range(len(comm3)):
    content= ""
    for i in talk_details[commOrig3[k3]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages/comm3'+str(k3)+'.html',"w")
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig3[k3]]
    name=''.join(name)
    c3=c3+"""<tr><td><a href="../speaker_pages/comm3"""+str(k3)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm3"""+str(k3)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c3=c3+comm3[k3]+", "+name+"</td></tr>"

c3=c3+"</table><div class='clearing'></div></div></html>"

html3=open("ncomm3.html","w")
html3.write(c3)
html3.close()

c4="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div class='topic'><div>Full List of Talks: Community 4</div><table>"""
for k4 in range(len(comm4)):
    content= ""
    for i in talk_details[commOrig4[k4]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages/comm4'+str(k4)+'.html',"w")
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig4[k4]]
    name=''.join(name)
    c4=c4+"""<tr><td><a href="../speaker_pages/comm4"""+str(k4)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm4"""+str(k4)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c4=c4+comm4[k4]+", "+name+"</td></tr>"

c4=c4+"</table><div class='clearing'></div></div></html>"

html4=open("ncomm4.html","w")
html4.write(c4)
html4.close()

c5="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div class='topic'><div>Full List of Talks: Community 5</div><table>"""
for k5 in range(len(comm5)):
    content= ""
    for i in talk_details[commOrig5[k5]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages/comm5'+str(k5)+'.html',"w")
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig5[k5]]
    name=''.join(name)
    c5=c5+"""<tr><td><a href="../speaker_pages/comm5"""+str(k5)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm5"""+str(k5)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c5=c5+comm5[k5]+", "+name+"</td></tr>"

c5=c5+"</table><div class='clearing'></div></div></html>"

html5=open("ncomm5.html","w")
html5.write(c5)
html5.close()



