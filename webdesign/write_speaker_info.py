import cPickle as pickle

talk_speaker=pickle.load(open('talk_speakerfull.pickle','rb'))
talk_speaker1=pickle.load(open('talk_speaker1.pickle','rb'))


for k in range(len(talk_speaker)):
    c1="<div class='topic'><div>"+talk_speaker.values()[k]+"</div><table>"
    name=talk_speaker1.values()[k]
    html1=open(name+'.html',"a")
    html1.write(c1)
    html1.close()