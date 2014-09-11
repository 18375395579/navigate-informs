import cPickle as pickle

comm_aff=pickle.load(open('comm_affinities_cut5comm.pickle','rb'))
#user_comm=pickle.load(open('user_comm_cutspeaker5.pickle','rb'))
word_comm=pickle.load(open('word_comm.pickle','rb'))  #word_comm[0]=[53 31 13 15 77]
word_count=pickle.load(open('word_count.pickle','rb'))
cluster_word=pickle.load(open('cluster_word.pickle','rb'))

wordcomm={}
wordrep={}
for k in cluster_word:  #k=1:100
    wordcomm[k]={}
    for word in cluster_word[k]:
        if word in word_count:
            wordcomm[k][word]=word_count[word]
    wordrep[k]=sorted(wordcomm[k], key=wordcomm[k].get, reverse=True)[:5]     #top 5 most frequent words in word clsuter k
    
#print max(wordcomm[0].values())

#print word_comm[0]

comm_word_list={}
for k in word_comm:
    comm_word_list[k]=[]
    for comm in word_comm[k]:
        comm_word_list[k].append(wordrep[comm])
#print comm_word_list[0]
doc_comm_freq={}
for i in range(5):
    doc_comm_freq[i]=int(round(comm_aff[(i,4)]*1000))

c=''
f=open('wordmap_user5.txt','w')
for k in range(5):
    for i in range(doc_comm_freq[k]):
        for w in comm_word_list[k]:
            for word in w:
                c=c+''.join(word)+' '
            
f.write(c)
f.close()