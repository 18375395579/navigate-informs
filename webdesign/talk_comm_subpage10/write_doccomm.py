# create a HTML file with the full list of the talk names, followed by the appropriate speaker

import cPickle as pickle
import re

glue=' '
user_comm=pickle.load(open('doc_comm_10.pickle','rb'))
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
comm6=[]
comm7=[]
comm8=[]
comm9=[]
comm0=[]

# store the orginial communities to be used for keys later
commOrig1=[] # different communities
commOrig2=[]
commOrig3=[]
commOrig4=[]
commOrig5=[]
commOrig6=[]
commOrig7=[]
commOrig8=[]
commOrig9=[]
commOrig0=[]


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
    elif user_comm[key]==5:
        commOrig6.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm6.append(key)
    elif user_comm[key]==6:
        commOrig7.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm7.append(key)

    elif user_comm[key]==7:
        commOrig8.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm8.append(key)
    elif user_comm[key]==8:
        commOrig9.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm9.append(key)

    elif user_comm[key]==9:
        commOrig0.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm0.append(key)


string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
"""

c1="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<div class='topic'>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<div>Full List of Talks: Community 1</div><table>"""
for k1 in range(len(comm1)):
    content= ""
    for i in talk_details[commOrig1[k1]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages10/comm1'+str(k1)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
"""
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig1[k1]]
    name=''.join(name)
    c1=c1+"""<tr><td><a href="../speaker_pages10/comm1"""+str(k1)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm1"""+str(k1)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c1=c1+comm1[k1]+", "+name+"</td></tr>"

c1=c1+"</table><div class='clearing'></div></div></html>"

html1=open("ncomm1.html","w")
html1.write(c1)
html1.close()


c2="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<div class='topic'>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<div>Full List of Talks: Community 2</div><table>"""
for k2 in range(len(comm2)):
    content= ""
    for i in talk_details[commOrig2[k2]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html2=open('../speaker_pages10/comm2'+str(k2)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
"""
    html2.write(string+content)
    html2.close()
    name=talk_speaker[commOrig2[k2]]
    name=''.join(name)
    c2=c2+"""<tr><td><a href="../speaker_pages10/comm2"""+str(k2)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm2"""+str(k2)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c2=c2+comm2[k2]+", "+name+"</td></tr>"

c2=c2+"</table><div class='clearing'></div></div></html>"

html2=open("ncomm2.html","w")
html2.write(c2)
html2.close()


c3="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<div class='topic'>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<div>Full List of Talks: Community 3</div><table>"""
for k3 in range(len(comm3)):
    content= ""
    for i in talk_details[commOrig3[k3]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages10/comm3'+str(k3)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
"""
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig3[k3]]
    name=''.join(name)
    c3=c3+"""<tr><td><a href="../speaker_pages10/comm3"""+str(k3)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm3"""+str(k3)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c3=c3+comm3[k3]+", "+name+"</td></tr>"

c3=c3+"</table><div class='clearing'></div></div></html>"

html3=open("ncomm3.html","w")
html3.write(c3)
html3.close()

c4="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<div class='topic'>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<div>Full List of Talks: Community 4</div><table>"""
for k4 in range(len(comm4)):
    content= ""
    for i in talk_details[commOrig4[k4]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages10/comm4'+str(k4)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
"""
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig4[k4]]
    name=''.join(name)
    c4=c4+"""<tr><td><a href="../speaker_pages10/comm4"""+str(k4)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm4"""+str(k4)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c4=c4+comm4[k4]+", "+name+"</td></tr>"

c4=c4+"</table><div class='clearing'></div></div></html>"

html4=open("ncomm4.html","w")
html4.write(c4)
html4.close()

c5="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<div class='topic'>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<div>Full List of Talks: Community 5</div><table>"""
for k5 in range(len(comm5)):
    content= ""
    for i in talk_details[commOrig5[k5]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages10/comm5'+str(k5)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
"""
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig5[k5]]
    name=''.join(name)
    c5=c5+"""<tr><td><a href="../speaker_pages10/comm5"""+str(k5)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm5"""+str(k5)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c5=c5+comm5[k5]+", "+name+"</td></tr>"

c5=c5+"</table><div class='clearing'></div></div></html>"

html5=open("ncomm5.html","w")
html5.write(c5)
html5.close()


c6="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div class='topic'>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div>Full List of Talks: Community 6</div><table>"""
for k6 in range(len(comm6)):
    content= ""
    for i in talk_details[commOrig6[k6]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages10/comm6'+str(k6)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
        """
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig6[k6]]
    name=''.join(name)
    c6=c6+"""<tr><td><a href="../speaker_pages10/comm6"""+str(k6)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm6"""+str(k6)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c6=c6+comm6[k6]+", "+name+"</td></tr>"

c6=c6+"</table><div class='clearing'></div></div></html>"

html6=open("ncomm6.html","w")
html6.write(c6)
html6.close()


c7="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div class='topic'>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div>Full List of Talks: Community 7</div><table>"""
for k7 in range(len(comm7)):
    content= ""
    for i in talk_details[commOrig7[k7]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages10/comm7'+str(k7)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
        """
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig7[k7]]
    name=''.join(name)
    c7=c7+"""<tr><td><a href="../speaker_pages10/comm7"""+str(k7)+""".html">"""
    c7=c7+comm7[k7]+", "+name+"</td></tr>"

c7=c7+"</table><div class='clearing'></div></div></html>"

html7=open("ncomm7.html","w")
html7.write(c7)
html7.close()

c8="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div class='topic'>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div>Full List of Talks: Community 8</div><table>"""
for k8 in range(len(comm8)):
    content= ""
    for i in talk_details[commOrig8[k8]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages10/comm8'+str(k8)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
        """
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig8[k8]]
    name=''.join(name)
    c8=c8+"""<tr><td><a href="../speaker_pages10/comm8"""+str(k8)+""".html">"""
    c8=c8+comm8[k8]+", "+name+"</td></tr>"

c8=c8+"</table><div class='clearing'></div></div></html>"

html8=open("ncomm8.html","w")
html8.write(c8)
html8.close()

c9="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div class='topic'>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div>Full List of Talks: Community 9</div><table>"""
for k9 in range(len(comm9)):
    content= ""
    for i in talk_details[commOrig9[k9]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages10/comm9'+str(k9)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
        """
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig9[k9]]
    name=''.join(name)
    c9=c9+"""<tr><td><a href="../speaker_pages10/comm9"""+str(k9)+""".html">"""
    c9=c9+comm9[k9]+", "+name+"</td></tr>"

c9=c9+"</table><div class='clearing'></div></div></html>"

html9=open("ncomm9.html","w")
html9.write(c9)
html9.close()

c0="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div class='topic'>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <div>Full List of Talks: Community 10</div><table>"""
for k0 in range(len(comm0)):
    content= ""
    for i in talk_details[commOrig0[k0]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('../speaker_pages10/comm0'+str(k0)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
        """
    html1.write(string+content)
    html1.close()
    name=talk_speaker[commOrig0[k0]]
    name=''.join(name)
    c0=c0+"""<tr><td><a href="../speaker_pages10/comm0"""+str(k0)+""".html">"""
    c0=c0+comm0[k0]+", "+name+"</td></tr>"

c0=c0+"</table><div class='clearing'></div></div></html>"

html0=open("ncomm0.html","w")
html0.write(c0)
html0.close()

