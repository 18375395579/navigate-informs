import cPickle as pickle
import re

glue=' '
user_comm=pickle.load(open('user_comm_cutspeaker5.pickle','rb'))
#speaker_full=pickle.load(open('speaker_fullname.pickle','rb'))

comm1=[]
comm2=[]
comm3=[]
comm4=[]
comm5=[]
for key in user_comm:
    if user_comm[key]==0:
        #print key
        comm1.append(''.join(glue + x if x.isupper() else x for x in key))
        
    elif user_comm[key]==1:

        comm2.append(''.join(glue + x if x.isupper() else x for x in key))
    elif user_comm[key]==2:

        comm3.append(''.join(glue + x if x.isupper() else x for x in key))
    elif user_comm[key]==3:

        comm4.append(''.join(glue + x if x.isupper() else x for x in key))
    elif user_comm[key]==4:

        comm5.append(''.join(glue + x if x.isupper() else x for x in key))
        
        

c1="<div class='topic'><div>Full List of Speaker Community 1</div><table>"
for k1 in range(len(comm1)-1):
    c1=c1+"<tr><td>"+comm1[k1]+"</td></tr>"

c1=c1+"</table><div class='clearing'></div></div></html>"

html1=open("scomm1.html","w")
html1.write(c1)
html1.close()



c2="<div class='topic'><div>Full List of Speaker Community 2</div><table>"
for k2 in range(len(comm2)-1):
    c2=c2+"<tr><td>"+comm2[k2]+"</td></tr>"

c2=c2+"</table><div class='clearing'></div></div></html>"

html2=open("scomm2.html","w")
html2.write(c2)
html2.close()


c3="<div class='topic'><div>Full List of Speaker Community 3</div><table>"
for k3 in range(len(comm3)-1):
    c3=c3+"<tr><td>"+comm3[k3]+"</td></tr>"

c3=c3+"</table><div class='clearing'></div></div></html>"

html3=open("scomm3.html","w")
html3.write(c3)
html3.close()

c4="<div class='topic'><div>Full List of Speaker Community 4</div><table>"
for k4 in range(len(comm4)-1):
    c4=c4+"<tr><td>"+comm4[k4]+"</td></tr>"

c4=c4+"</table><div class='clearing'></div></div></html>"

html4=open("scomm4.html","w")
html4.write(c4)
html4.close()

c5="<div class='topic'><div>Full List of Speaker Community 5</div><table>"
for k5 in range(len(comm5)-1):
    c5=c5+"<tr><td>"+comm5[k5]+"</td></tr>"

c5=c5+"</table><div class='clearing'></div></div></html>"

html5=open("scomm5.html","w")
html5.write(c5)
html5.close()



c1="""<div class='topic'>
<div><A HREF="scomm1.html">Community 1</A></div>
<img src="./wordmap/wordmapu1.jpg" title="Doc Cluster 1 Word Map" style="width:580px;height:360px;float:right;">
<div class="row">
<table style="width:600px;float:left">"""
for k in range(10):
    c1=c1+"""<tr><td>"""+comm1[k]+"""</td></tr>"""

c1=c1+"""</table>
<div class='clearing'></div></div>"""


c2="""<div class='topic'><div><A HREF="scomm2.html">Community 2</A></div>
<img src="./wordmap/wordmapu2.jpg" title="Doc Cluster 1 Word Map" style="width:580px;height:360px;float:right;">
<div class="row">
<table style="width:600px;float:left">"""
for k in range(10):
    c2=c2+"""<tr><td>"""+comm2[k]+"""</td></tr>"""
c2=c2+"""</table><div class='clearing'></div></div>"""

c3="""<div class='topic'><div><A HREF="scomm3.html">Community 3</A></div>
<img src="./wordmap/wordmapu3.jpg" title="Doc Cluster 1 Word Map" style="width:580px;height:360px;float:right;">
<div class="row">
<table style="width:600px;float:left">"""
for k in range(10):
    c3=c3+"""<tr><td>"""+comm3[k]+"""</td></tr>"""
c3=c3+"""</table><div class='clearing'></div></div>"""

c4="""<div class='topic'><div><A HREF="scomm4.html">Community 4</A></div>
<img src="./wordmap/wordmapu4.jpg" title="Doc Cluster 1 Word Map" style="width:580px;height:360px;float:right;">
<div class="row">
<table style="width:600px;float:left">"""
for k in range(10):
    c4=c4+"""<tr><td>"""+comm4[k]+"""</td></tr>"""
c4=c4+"""</table><div class='clearing'></div></div>"""

c5="""<div class='topic'><div><A HREF="scomm5.html">Community 5</A></div>
<img src="./wordmap/wordmapu5.jpg" title="Doc Cluster 1 Word Map" style="width:580px;height:360px;float:right;">
<div class="row">
<table style="width:600px;float:left">"""
for k in range(10):
    c5=c5+"""<tr><td>"""+comm5[k]+"""</td></tr>"""
c5=c5+"""</table><div class='clearing'></div></div>"""


html=open("yujia_user.html","w")
html.write(c1+c2+c3+c4+c5)
html.close()