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
comm0=[] # different communities
comm1=[]
comm2=[]
comm3=[]
comm4=[]
comm5=[]
comm6=[] # different communities
comm7=[]
comm8=[]
comm9=[]

# store the orginial communities to be used for keys later
commOrig0=[]
commOrig1=[] # different communities
commOrig2=[]
commOrig3=[]
commOrig4=[]
commOrig5=[]
commOrig6=[] # different communities
commOrig7=[]
commOrig8=[]
commOrig9=[]



for key in user_comm:
    if user_comm[key]==0:
        commOrig0.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm0.append(key)
    
    elif user_comm[key]==1:
        commOrig1.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm1.append(key)
    
    elif user_comm[key]==2:
        commOrig2.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm2.append(key)
    
    elif user_comm[key]==3:
        commOrig3.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm3.append(key)
    
    elif user_comm[key]==4:
        commOrig4.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm4.append(key)
    elif user_comm[key]==5:
        commOrig5.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm5.append(key)
    elif user_comm[key]==6:
        commOrig6.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm6.append(key)
    elif user_comm[key]==7:
        commOrig7.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm7.append(key)
    elif user_comm[key]==8:
        commOrig8.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm8.append(key)
    elif user_comm[key]==9:
        commOrig9.append(key)
        key= key[6:]
        key= re.sub('"','', key)
        key= re.sub(r'\*[^)]*\*', '', key) # gets rid of ***_content_***
        key= re.sub(r'\<[^)]*\>', '', key) # gets rid of <=_content_=>
        comm9.append(key)


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

body=""
for i in range(10):
    c1="""<div class='topic'>
        <img src="webdesign/wordmap/doc_clus1.jpg" style="width:580px;height:360px;float:left">
        <table style="width:600px;float:left">
        <tr><td><div><strong>Example Talks from <A HREF="webdesign/talk_comm_subpage/ncomm1.html">Cluster """+str(i)+"""</A></strong></div></tr></td>
        """
    x1="commOrig"+str(i)
    x2="comm"+str(i)
    for k in range(5):
        content= ""
        for i in talk_details[x1[k]]:
            content = content+"<br>"+''.join(i)+"</br>"
        html1=open('speaker_pages_main_10/comm'+str(i)+str(k)+'.html',"w")
        string="""<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" />"""
        html1.write(content)
        html1.close()
        c1=c1+"""<tr><td><a href="webdesign/speaker_pages_main_10/comm"""+str(i)+str(k)+""".html" class="black">"""+x2[k].strip()+" -- <i>"+speaker_fixname[talk_speaker[x1[k]]]+", "+talk_year[x1[k]]+"""</i></td></tr>"""

        c1=c1+"""</table><div class='clearing'></div></div>"""
    body=body+c1
