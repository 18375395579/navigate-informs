# creates the main HTML page for the navigate informs website.

import cPickle as pickle
import re
import os

#os.chdir('/Users/john/Desktop/navigate-informs/webdesign') # change the working directory to the folder that contains your files


user_comm=pickle.load(open('doc_comm.pickle','rb')) # contains the names of the talks
#user_comm=pickle.load(open('user_comm_cutspeaker5.pickle','rb')) # contains the names of the speakers
talk_speaker=pickle.load(open('talk_speaker.pickle','rb')) # contains the names of
speaker_fixname=pickle.load(open('speaker_fixname.pickle','rb'))
talk_year=pickle.load(open('talk_year.pickle','rb'))
talk_details=pickle.load(open('talk_details.pickle','rb'))
# the talks and the speakers
print talk_details.keys()[0]

num_Comms= 5 # the number of communities that we have.     

# store the orginial communities to be used for keys later
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


#for i in range(num_Comms):
#for key in doc_comm:
#if doc_comm[key]==i: # look to see what community a talk belongs to
#eval("commOrig"+str(i+1)).append(key)
#key= key[6:] # remove initial characters in the string
#key= re.sub('"','',key)
#eval("comm"+str(i+1)).append(key)


# each c is a different community. We are going to write html code for each community

style="""<!DOCTYPE HTML>
    <html>
    <meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <style>
	body {
    background-color: #dddddd;
	}
    .topic {
    margin: 10px;
    padding: 10px;
	font-family: "Lucida Grande";
	background-color: #ffffff;
    }
    .clearing {
    clear: both;
    }
    </style>
    
    </head>
    
    <body>
    <h1>INFORMS Annual Meeting Abstract Clustering Result</h1>
    <h3>We took five-year's INFORMS Annual Meeting Abstract and applied the <a href="http://www.w3schools.com">Community-Content Custering model</a> on it. There are five speaker communities and five talk clusters. This page shows the a wordmap and 5 representative talks of each talk cluster. At the end, there is a bipartite graph showing the interrelationship between speaker communities and talk clusters.</h3>"""
c1="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus1.jpg" style="width:580px;height:360px;float:right">
    <div><A HREF="webdesign/talk_comm_subpage/ncomm1.html">Cluster 1</A></div>
    <table style="width:600px;float:left">"""
for k in range(5):
    print commOrig1[k]
    content= ""
    content= ''.join(talk_details[commOrig1[k]])
    html1=open('speaker_pages_main/comm1'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c1=c1+"""<tr><td><a href="webdesign/speaker_pages_main/comm1"""+str(k)+""".html" onclick="javascript:void window.open("'webdesign/speaker_pages_main/comm1"""+str(k)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""+comm1[k].strip()+", "+speaker_fixname[talk_speaker[commOrig1[k]]]+", "+talk_year[commOrig1[k]]+"""</td></tr>"""

c1=c1+"""</table>
<div class='clearing'></div></div>"""


c2="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus2.jpg" style="width:580px;height:360px;float:right">
    <div><A HREF="webdesign/talk_comm_subpage/ncomm2.html">Cluster 2</A></div>
    <table style="width:600px;float:left">"""
for k in range(5):
    content= ""
    content= ''.join(talk_details[commOrig2[k]])
    html1=open('speaker_pages_main/comm2'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c2=c2+"""<tr><td><a href="webdesign/speaker_pages_main/comm2"""+str(k)+""".html" onclick="javascript:void window.open("'webdesign/speaker_pages_main/comm2"""+str(k)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""+comm2[k].strip()+", "+speaker_fixname[talk_speaker[commOrig2[k]]]+", "+talk_year[commOrig1[k]]+"""</td></tr>"""
c2=c2+"""</table><div class='clearing'></div></div>"""

c3="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus3.jpg" style="width:580px;height:360px;float:right">
    <div><A HREF="webdesign/talk_comm_subpage/ncomm3.html">Cluster 3</A></div>
    <table style="width:600px;float:left">"""
for k in range(5):
    content= ""
    content= ''.join(talk_details[commOrig3[k]])
    html1=open('speaker_pages_main/comm3'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c3=c3+"""<tr><td><a href="webdesign/speaker_pages_main/comm3"""+str(k)+""".html" onclick="javascript:void window.open("'webdesign/speaker_pages_main/comm3"""+str(k)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""+comm3[k].strip()+", "+speaker_fixname[talk_speaker[commOrig3[k]]]+", "+talk_year[commOrig1[k]]+"""</td></tr>"""
c3=c3+"""</table><div class='clearing'></div></div>"""

c4="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus4.jpg" style="width:580px;height:360px;float:right">
    <div><A HREF="webdesign/talk_comm_subpage/ncomm4.html">Cluster 4</A></div>
    <table style="width:600px;float:left">"""
for k in range(5):
    content= ""
    content= ''.join(talk_details[commOrig4[k]])
    html1=open('speaker_pages_main/comm4'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c4=c4+"""<tr><td><a href="webdesign/speaker_pages_main/comm4"""+str(k)+""".html" onclick="javascript:void window.open("'webdesign/speaker_pages_main/comm4"""+str(k)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""+comm4[k].strip()+", "+speaker_fixname[talk_speaker[commOrig4[k]]]+", "+talk_year[commOrig1[k]]+"""</td></tr>"""
c4=c4+"""</table><div class='clearing'></div></div>"""

c5="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus5.jpg" style="width:580px;height:360px;float:right">
    <div><A HREF="webdesign/talk_comm_subpage/ncomm5.html">Cluster 5</A></div>
    <table style="width:600px;float:left">"""
for k in range(5):
    content= ""
    content= ''.join(talk_details[commOrig5[k]])
    html1=open('speaker_pages_main/comm5'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c5=c5+"""<tr><td><a href="/webdesign/speaker_pages_main/comm5"""+str(k)+""".html" onclick="javascript:void window.open("'webdesign/speaker_pages_main/comm5"""+str(k)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""+comm5[k].strip()+", "+speaker_fixname[talk_speaker[commOrig5[k]]]+", "+talk_year[commOrig1[k]]+"""</td></tr>"""
c5=c5+"""</table><div class='clearing'></div></div>"""


html=open("yujia9.html","w")
html.write(style+c1+c2+c3+c4+c5)
html.close()
