# creates the main HTML page for the navigate informs website.

import cPickle as pickle
import re
import os

#os.chdir('/Users/john/Desktop/navigate-informs/webdesign') # change the working directory to the folder that contains your files


user_comm=pickle.load(open('doc_comm_10.pickle','rb')) # contains the names of the talks
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
    html1=open('speaker_pages_main_10/comm1'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c1=c1+"""<tr><td><a href="webdesign/speaker_pages_main_10/comm1"""+str(k)+""".html" class="black">"""+comm1[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig1[k]]]+", "+talk_year[commOrig1[k]]+"""</i></td></tr>"""

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
    html1=open('speaker_pages_main_10/comm2'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c2=c2+"""<tr><td><a href="webdesign/speaker_pages_main_10/comm2"""+str(k)+""".html" class="black">"""+comm2[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig2[k]]]+", "+talk_year[commOrig2[k]]+"""</i></td></tr>"""
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
    html1=open('speaker_pages_main_10/comm3'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c3=c3+"""<tr><td><a href="webdesign/speaker_pages_main_10/comm3"""+str(k)+""".html" class="black">"""+comm3[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig3[k]]]+", "+talk_year[commOrig3[k]]+"""</i></td></tr>"""
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
    html1=open('speaker_pages_main_10/comm4'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c4=c4+"""<tr><td><a href="webdesign/speaker_pages_main_10/comm4"""+str(k)+""".html" class="black">"""+comm4[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig4[k]]]+", "+talk_year[commOrig4[k]]+"""</td></tr>"""
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
    html1=open('speaker_pages_main_10/comm5'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c5=c5+"""<tr><td><a href="/webdesign/speaker_pages_main_10/comm5"""+str(k)+""".html" class="black">"""+comm5[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig5[k]]]+", "+talk_year[commOrig5[k]]+"""</td></tr>"""
c5=c5+"""</table><div class='clearing'></div></div>"""

c6="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus5.jpg" style="width:580px;height:360px;float:left">
    <table style="width:600px;float:left">
    <tr><td><div><strong>Example Talks from <A HREF="webdesign/talk_comm_subpage/ncomm5.html">Cluster 6</A></strong></div></td></tr>
    """
for k in range(5):
    content= ""
    for i in talk_details[commOrig6[k]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('speaker_pages_main_10/comm6'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c6=c6+"""<tr><td><a href="/webdesign/speaker_pages_main_10/comm6"""+str(k)+""".html" class="black">"""+comm6[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig6[k]]]+", "+talk_year[commOrig6[k]]+"""</td></tr>"""
c6=c6+"""</table><div class='clearing'></div></div>"""

c7="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus5.jpg" style="width:580px;height:360px;float:left">
    <table style="width:600px;float:left">
    <tr><td><div><strong>Example Talks from <A HREF="webdesign/talk_comm_subpage/ncomm5.html">Cluster 7</A></strong></div></td></tr>
    """
for k in range(5):
    content= ""
    for i in talk_details[commOrig7[k]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('speaker_pages_main_10/comm7'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c7=c7+"""<tr><td><a href="/webdesign/speaker_pages_main_10/comm7"""+str(k)+""".html" class="black">"""+comm7[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig7[k]]]+", "+talk_year[commOrig7[k]]+"""</td></tr>"""
c7=c7+"""</table><div class='clearing'></div></div>"""

c8="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus5.jpg" style="width:580px;height:360px;float:left">
    <table style="width:600px;float:left">
    <tr><td><div><strong>Example Talks from <A HREF="webdesign/talk_comm_subpage/ncomm5.html">Cluster 8</A></strong></div></td></tr>
    """
for k in range(5):
    content= ""
    for i in talk_details[commOrig8[k]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('speaker_pages_main_10/comm8'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c8=c8+"""<tr><td><a href="/webdesign/speaker_pages_main_10/comm8"""+str(k)+""".html" class="black">"""+comm8[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig8[k]]]+", "+talk_year[commOrig8[k]]+"""</td></tr>"""
c8=c8+"""</table><div class='clearing'></div></div>"""

c9="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus5.jpg" style="width:580px;height:360px;float:left">
    <table style="width:600px;float:left">
    <tr><td><div><strong>Example Talks from <A HREF="webdesign/talk_comm_subpage/ncomm5.html">Cluster 9</A></strong></div></td></tr>
    """
for k in range(5):
    content= ""
    for i in talk_details[commOrig9[k]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('speaker_pages_main_10/comm9'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c9=c9+"""<tr><td><a href="/webdesign/speaker_pages_main_10/comm9"""+str(k)+""".html" class="black">"""+comm9[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig9[k]]]+", "+talk_year[commOrig9[k]]+"""</td></tr>"""
c9=c9+"""</table><div class='clearing'></div></div>"""

c0="""<div class='topic'>
    <img src="webdesign/wordmap/doc_clus5.jpg" style="width:580px;height:360px;float:left">
    <table style="width:600px;float:left">
    <tr><td><div><strong>Example Talks from <A HREF="webdesign/talk_comm_subpage/ncomm5.html">Cluster 10</A></strong></div></td></tr>
    """
for k in range(5):
    content= ""
    for i in talk_details[commOrig0[k]]:
        content= content+"<br>"+''.join(i)+"</br>"
    html1=open('speaker_pages_main_10/comm0'+str(k)+'.html',"w")
    string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
    html1.write(content)
    html1.close()
    c0=c0+"""<tr><td><a href="/webdesign/speaker_pages_main_10/comm0"""+str(k)+""".html" class="black">"""+comm0[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[commOrig0[k]]]+", "+talk_year[commOrig0[k]]+"""</td></tr>"""
c0=c0+"""</table><div class='clearing'></div></div>"""

bottom="""
    <h3>This bipartite graph shows the interrelationship between speaker communities and talk clusters.
    The thickness of each bar shows how likely a speaker from each community is to be interested in a talk from that cluster.
    Click on a blue box to see speakers in that community.
    Click on a red box to see talks in that cluster.</h3>

    <body>
    <img src="webdesign/graph.jpg" width="650" height="400" alt="Planets" usemap="#planetmap">
    <map name="planetmap">
    <area shape="rect" coords="0,0,100,80" href="webdesign/speaker_comm_subpage/scomm1.html" alt="Comm0">
    <area shape="rect" coords="0,80,100,160" href="webdesign/speaker_comm_subpage/scomm2.html" alt="Comm1">
    <area shape="rect" coords="0,160,100,240" href="webdesign/speaker_comm_subpage/scomm3.html" alt="Comm2">
    <area shape="rect" coords="0,240,100,320" href="webdesign/speaker_comm_subpage/scomm4.html" alt="Comm3">
    <area shape="rect" coords="0,320,100,400" href="webdesign/speaker_comm_subpage/scomm5.html" alt="Comm4">
    <area shape="rect" coords="440,0,650,80" href="webdesign/talk_comm_subpage/ncomm1.html" alt="Comm0">
    <area shape="rect" coords="440,80,650,160" href="webdesign/talk_comm_subpage/ncomm2.html" alt="Comm1">
    <area shape="rect" coords="440,160,650,240" href="webdesign/talk_comm_subpage/ncomm3.html" alt="Comm2">
    <area shape="rect" coords="440,240,650,320" href="webdesign/talk_comm_subpage/ncomm4.html" alt="Comm3">
    <area shape="rect" coords="440,320,650,400" href="webdesign/talk_comm_subpage/ncomm5.html" alt="Comm4">
    </map>
    </body>
    </html>
    """
html=open("yujia10.html","w")
html.write(style+c1+c2+c3+c4+c5+c6+c7+c8+c9+c0+bottom)
html.close()
