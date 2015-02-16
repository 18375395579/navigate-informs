# create a HTML file with the full list of the talk names, followed by the appropriate speaker

import cPickle as pickle
import re
import codecs

import sys

reload(sys)
sys.setdefaultencoding('utf8')

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
string="""
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
"""

c1="""<meta http-equiv="content-type" content="text/html; charset=UTF-8" />

<div class='topic'>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
<div>Full List of Talks: Community 1</div><table>"""
for k1 in range(len(comm1)):

    name=talk_speaker[commOrig1[k1]]
    name=''.join(name)
    c1=c1+"""<tr><td><a href="../speaker_pages/comm1"""+str(k1)+""".html" onclick="javascript:void window.open("'../speaker_pages/comm1"""+str(k1)+""".html'",'1408393674039','width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0');return false;">"""
    c1=c1+comm1[k1]+", "+name+"</td></tr>"

c1=c1+"</table><div class='clearing'></div></div></html>"

html1=codecs.open("testpage.html","w",encoding='UTF-8',errors='replace')
c1.decode('iso-8859-1').encode('utf8')
html1.write(c1)
html1.close()


