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

num_Comms= 10 # the number of communities that we have.

# store the orginial communities to be used for keys later
comm1=[] # different communities
comm2=[]
comm3=[]
comm4=[]
comm5=[]
comm6=[] # different communities
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
commOrig6=[] # different communities
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
    <meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <head>
    
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
    th, td {
    padding: 5px;
    }
    a.black:link {color:#000000; text-decoration: none;}
    a.black:visited {color:#000000; text-decoration: none;}
    a.black:hover {color:#0000ff; text-decoration: none;}
    </style>
    </head>
    <body>
    <h1>INFORMS Annual Meeting Abstract Clustering</h1>
    <h3>We took abstracts from five-years of the INFORMS Annual Meeting and used <a href="ContentAugmentedStochasticBlockModels.pdf">Content-Augmented Stochastic Blockmodels</a> to group speakers into communities and talks into clusters.  This page shows a word cloud and representative talks from each cluster. </h3>"""



c1="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus1.jpg" style="width:580px;height:360px;float:left">
    <table style="width:600px;float:left">
    <tr><td><div><strong>Example Talks from <A HREF="webdesign/talk_comm_subpage/ncomm1.html">Cluster 1</A></strong></div></tr></td>
    """
for k in range(5):
    content= ""
    for i in talk_details[commOrig1[k]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('speaker_pages_main/comm1'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />"""
    html1.write(string+content)
    html1.close()
    c1=c1+"""<tr><td><a href="webdesign/speaker_pages_main/comm1"""+str(k)+""".html" class="black">"""+comm1[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig1[k]]]+", "+talk_year[commOrig1[k]]+"""</i></td></tr>"""

c1=c1+"""</table>
<div class='clearing'></div></div>"""


c2="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus2.jpg" style="width:580px;height:360px;float:left">
    <table style="width:600px;float:left">
    <tr><td><div><strong>Example Talks from <A HREF="webdesign/talk_comm_subpage/ncomm2.html">Cluster 2</A></strong></div></tr></td>
    """
for k in range(5):
    content= ""
    for i in talk_details[commOrig2[k]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('speaker_pages_main/comm2'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />"""
    html1.write(string+content)
    html1.close()
    c2=c2+"""<tr><td><a href="webdesign/speaker_pages_main/comm2"""+str(k)+""".html" class="black">"""+comm2[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig2[k]]]+", "+talk_year[commOrig2[k]]+"""</i></td></tr>"""
c2=c2+"""</table><div class='clearing'></div></div>"""

c3="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus3.jpg" style="width:580px;height:360px;float:left">
    <table style="width:600px;float:left">
    <tr><td><div><strong>Example Talks from <A HREF="webdesign/talk_comm_subpage/ncomm3.html">Cluster 3</A></strong></div></tr></td>
    """
for k in range(5):
    content= ""
    for i in talk_details[commOrig3[k]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('speaker_pages_main/comm3'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />"""
    html1.write(string+content)
    html1.close()
    c3=c3+"""<tr><td><a href="webdesign/speaker_pages_main/comm3"""+str(k)+""".html" class="black">"""+comm3[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig3[k]]]+", "+talk_year[commOrig3[k]]+"""</i></td></tr>"""
c3=c3+"""</table><div class='clearing'></div></div>"""

c4="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus4.jpg" style="width:580px;height:360px;float:left">
    <table style="width:600px;float:left">
    <tr><td><div><strong>Example Talks from <A HREF="webdesign/talk_comm_subpage/ncomm4.html">Cluster 4</A></strong></div></td></tr>
    """
for k in range(5):
    content= ""
    for i in talk_details[commOrig4[k]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('speaker_pages_main/comm4'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />"""
    html1.write(string+content)
    html1.close()
    c4=c4+"""<tr><td><a href="webdesign/speaker_pages_main/comm4"""+str(k)+""".html" class="black">"""+comm4[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig4[k]]]+", "+talk_year[commOrig4[k]]+"""</td></tr>"""
c4=c4+"""</table><div class='clearing'></div></div>"""

c5="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus5.jpg" style="width:580px;height:360px;float:left">
    <table style="width:600px;float:left">
    <tr><td><div><strong>Example Talks from <A HREF="webdesign/talk_comm_subpage/ncomm5.html">Cluster 5</A></strong></div></td></tr>
    """
for k in range(5):
    content= ""
    for i in talk_details[commOrig5[k]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('speaker_pages_main/comm5'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />"""
    html1.write(string+content)
    html1.close()
    c5=c5+"""<tr><td><a href="/webdesign/speaker_pages_main/comm5"""+str(k)+""".html" class="black">"""+comm5[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig5[k]]]+", "+talk_year[commOrig5[k]]+"""</td></tr>"""
c5=c5+"""</table><div class='clearing'></div></div>"""


bottom="""
    <h3>This bipartite graph shows the interrelationship between speaker communities and talk clusters.
    The thickness of each bar shows how likely a speaker from each community is to be interested in a talk from that cluster.
    Click on a blue box to see speakers in that community.
    Click on a red box to see talks in that cluster.</h3>

    <body>
    <div id="imagemap">
    <img id="Map" src="webdesign/qxygraphs/qxy.png" width="400" height="500" usemap="#Map" border="0" />
    <map id="Map" name="Map">
    <area shape="circle" coords="55,53,45" href="webdesign/speaker_comm_subpage/scomm1.html" alt="Comm0" id="comm1" name="Comm1" onMouseOver="if(document.images) document.getElementById('Map').src= 'webdesign/qxygraphs/comm1.png';" onMouseOut="if(document.images) document.getElementById('Map').src= 'webdesign/qxygraphs/qxy.png';"/>
    <area shape="circle" coords="55,150,45" href="webdesign/speaker_comm_subpage/scomm2.html" alt="Comm1" id="comm2" name="Comm2" onMouseOver="if(document.images) document.getElementById('Map').src= 'webdesign/qxygraphs/comm2.png';" onMouseOut="if(document.images) document.getElementById('Map').src= 'webdesign/qxygraphs/qxy.png';"/>
    <area shape="circle" coords="55,250,45" href="webdesign/speaker_comm_subpage/scomm3.html" alt="Comm2" id="comm3" name="Comm3" onMouseOver="if(document.images) document.getElementById('Map').src= 'webdesign/qxygraphs/comm3.png';" onMouseOut="if(document.images) document.getElementById('Map').src= 'webdesign/qxygraphs/qxy.png';"/>
    <area shape="circle" coords="55,350,45" href="webdesign/speaker_comm_subpage/scomm4.html" alt="Comm3" id="comm4" name="Comm4" onMouseOver="if(document.images) document.getElementById('Map').src= 'webdesign/qxygraphs/comm4.png';" onMouseOut="if(document.images) document.getElementById('Map').src= 'webdesign/qxygraphs/qxy.png';"/>
    <area shape="circle" coords="55,450,45" href="webdesign/speaker_comm_subpage/scomm5.html" alt="Comm4" id="comm5" name="Comm5" onMouseOver="if(document.images) document.getElementById('Map').src= 'webdesign/qxygraphs/comm5.png';" onMouseOut="if(document.images) document.getElementById('Map').src= 'webdesign/qxygraphs/qxy.png';"/>
    <area shape="circle" coords="340,53,45" href="webdesign/talk_comm_subpage/ncomm1.html" alt="Clus0">
    <area shape="circle" coords="340,150,45" href="webdesign/talk_comm_subpage/ncomm2.html" alt="Clus1">
    <area shape="circle" coords="340,250,45" href="webdesign/talk_comm_subpage/ncomm3.html" alt="Clus2">
    <area shape="circle" coords="340,350,45" href="webdesign/talk_comm_subpage/ncomm4.html" alt="Clus3">
    <area shape="circle" coords="340,450,45" href="webdesign/talk_comm_subpage/ncomm5.html" alt="Clus4">
    </map>
    </body>
    </html>
    """
html=open("yujia10.html","w")
html.write(style+c1+c2+c3+c4+c5+bottom)
html.close()
