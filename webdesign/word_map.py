import cPickle as pickle

comm_aff=pickle.load(open('comm_affinities_cut5comm.pickle','rb'))
#user_comm=pickle.load(open('user_comm_cutspeaker5.pickle','rb'))
word_comm=pickle.load(open('word_comm.pickle','rb'))
word_count=pickle.load(open('word_count.pickle','rb'))
cluster_word=pickle.load(open('cluster_word.pickle','rb'))

wordcomm={}
wordrep={}
for k in cluster_word:
    wordcomm[k]={}
    for word in cluster_word[k]:
        if word in word_count:
            wordcomm[k][word]=word_count[word]
    wordrep[k]=sorted(wordcomm[k], key=wordcomm[k].get, reverse=True)[:5]     
    
#print max(wordcomm[0].values())

newA = sorted(wordcomm[0], key=wordcomm[0].get, reverse=True)[:5]
#print newA

comm_word_list={}
for k in word_comm:
    comm_word_list[k]=[]
    for comm in word_comm[k]:
        comm_word_list[k].append(wordrep[comm])

doc_comm_freq={}
for i in range(5):
    doc_comm_freq[i]=int(round(comm_aff[(i,0)]*2000))

print doc_comm_freq
f=open('/Users/yujialiu/Desktop/research/webdesign/wordmapu1.txt','w')
for k in range(5):
    for j in range(doc_comm_freq[k]):
        val=''
        for list in comm_word_list[k]:
            for w in list:
                val=val+' '+''.join(w)
        f.write(val)
f.close()