def ngrams(inputT, n):
 m = {}
 hist = dict()
 occr = dict()
 resdict = dict()



 for l in inputT:
     for i in range(len(l)-n+1):
         ser = tuple(l[i:i+n])

         if ser in occr.keys():
             occr[ser]+=1
         else:
             occr.update({ser:1})

     for j in range(len(l)-n+2):
         kh = tuple(l[j:j+n-1])

         if kh in hist.keys():
             hist[kh]+=1
         else:
             hist.update({kh:1})
 for key, value in occr.items():
     if n==2:
         if key not in resdict:
             keyden = key[0],
             wordn = hist[keyden]

             fin = value/wordn
             resdict.update({key:fin})

     else:
         wordn=' '.join(key)
         wordn = str(wordn).split()[0:n-1]
         wordnn = tuple(wordn)
         if wordnn in hist:
             if key not in resdict:
                 denom = hist[wordnn]
                 fin = value/denom
                 resdict.update({key:fin})

 return resdict




input1 =  [['A', 'B', 'C', 'D', 'E'],
     ['D', 'E', 'C', 'D', 'E'],
     ['A', 'C', 'D', 'D']
    ]
input2 = [['<s>', 'I', 'am', 'Sam', '</s>'],
          ['<s>','Sam', 'I', 'am','</s>'],
          ['<s>', 'I', 'do', 'not', 'like', 'green', 'eggs', 'and', 'ham', '</s>']]
print(ngrams(input1,3))


#question2(smoothing)


def smothing(inputT,n):

 def get_vocab(inputT):
    return set([word for sentence in inputT for word in sentence])
 hist = dict()
 occr = dict()
 resdict = dict()
 import itertools
 from itertools import product
 word =set(product(get_vocab(inputT),repeat=n))
 word = tuple(word)

 for l in inputT:

     for i in range(len(l)-n+1):
         ser = tuple(l[i:i+n])

         if ser in occr.keys():
             occr[ser]+=1
         else:
             occr.update({ser:1})


     for j in range(len(l)-n+2):
         kh = tuple(l[j:j+n-1])

         if kh in hist.keys():
             hist[kh]+=1
         else:
             hist.update({kh:1})

 for i in range(len(word)):
     if word[i] not in occr.keys():
         occr.update({word[i]:0})

 for key, value in occr.items():
    if n==2:
      if key not in resdict:
          #print(ngramdenom)
          keyden = key[0],
          denom = hist[keyden]+ len(get_vocab(inputT))
          fin = (value+1)/denom
          resdict.update({key:fin})
    else:

        nword = ' '.join(key)
        nword = str(nword).split()[0:n-1]
        nwordd = tuple(nword)
        if nwordd in hist:
            if key not in resdict:
                denom = hist[nwordd]+ len(get_vocab(inputT))
                fin = (value+1)/denom
                resdict.update({key:fin})
        else:
            if key not in resdict:
                denom = len(get_vocab(inputT))
                fin = (value+1)/denom
                resdict.update({key:fin})





 return resdict
print(smothing(input1,3))

#example3
def prob_ngram(model, a, n):
 kh = []
 total = 1
 for i in range(len(a)-n+1):
     sert = tuple(a[i:i+n])

 if sert in model.keys():
         kh.append(model[sert])

 else:
         kh.append(0)

 for i in range(len(kh)):
    total *= kh[i]
 return total
sen = ['like', 'green', 'eggs']
print(prob_ngram(smothing(input2,2),sen,2))
