import nltk
  
def init_wfst(tokens, grammar):
    numtokens = len(tokens)
    wfst = [[None for i in range(numtokens+1)] for j in range(numtokens+1)]
    for i in range(numtokens):
        productions = grammar.productions(rhs=tokens[i])
        wfst[i][i+1] = productions[0].lhs()
    return wfst

def complete_wfst(wfst, tokens, grammar, trace=False):
    index = dict((p.rhs(), p.lhs()) for p in grammar.productions())
    numtokens = len(tokens)
    for span in range(2, numtokens+1):
        for start in range(numtokens+1-span):
            end = start + span
            for mid in range(start+1, end):
                nt1, nt2 = wfst[start][mid], wfst[mid][end]
                if nt1 and nt2 and (nt1,nt2) in index:
                    wfst[start][end] = index[(nt1,nt2)]
                    if trace:
                        print "[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" % \
                        (start, nt1, mid, nt2, end, start, index[(nt1,nt2)], end)
    return wfst

def display(wfst, tokens,chart):
    print '\nWFST ' + ' '.join([("%-4d" % i) for i in range(1, len(wfst))])
    chart.append("WFST")
    for i in range(1,len(wfst)):
        chart.append(i)
    for i in range(len(wfst)-1):
        print "%d   " % i,
        chart.append(i)
        for j in range(1, len(wfst)):
            print "%-4s" % (wfst[i][j] or '.'),
            chart.append(wfst[i][j] or '.')
        print


def validate(sentence,chart):
    sent = nltk.word_tokenize(sentence)
    tagged_text = nltk.pos_tag(sent)
    pos_tags = [pos for (token,pos) in nltk.pos_tag(sent)]

    var_s="S -> NP VP"
    var_pp="PP -> P NP | P VP"
    var_np="NP -> N | Det N | Det N P"
    var_vp="VP -> V N |V NP | VP PP | V PP | V"
    var_n=""
    var_v=""
    var_p=""
    var_det=""
    var_others=""

    k=-1
    for j in pos_tags:
       k=k+1
       i=sent[k]
       print(j)
       if j=='DT' or j=='PRP$':
         if(len(var_det)==0):
            var_det = var_det+'Det -> \''+i+'\''
         else:
            var_det = var_det+' | \''+i+'\''
       elif j=='NNP' or j=='PRP' or j=='NNS':
            var_np = var_np+' | \''+i+'\''
       elif j=='JJ' or j=='NN' or j=='JJR':
         if(len(var_n)==0):
            var_n = var_n+'N -> \''+i+'\''
         else:
            var_n = var_n+' | \''+i+'\''
       elif j=='VBZ' or j=='VBP' or j=='VBD' or j=='VB':
         if(len(var_v)==0):
            var_v = var_v+'V -> \''+i+'\''
         else:
            var_v = var_v+' | \''+i+'\''
       elif j=='PP' or j=='IN' or j=='TO':
         if(len(var_p)==0):
            var_p = var_p+'P -> \''+i+'\''
         else:
            var_p = var_p+' | \''+i+'\''

    if(len(var_n)==0):
       var_n='N -> \'aaa\''
    if(len(var_v)==0):
       var_v='V -> \'aaa\''
    if(len(var_p)==0):
       var_p='P -> \'aaa\''
    if(len(var_det)==0):
       var_det='Det -> \'aaa\''


    with open("my_grammar.cfg", "w") as myfile:
        myfile.write(var_s)
        myfile.write('\n')
        myfile.write(var_pp)
        myfile.write('\n')
        myfile.write(var_np)
        myfile.write('\n')
        myfile.write(var_vp)
        myfile.write('\n')
        myfile.write(var_n) 
        myfile.write('\n')
        myfile.write(var_v) 
        myfile.write('\n')
        myfile.write(var_det) 
        myfile.write('\n')
        myfile.write(var_p) 
        
    simple_grammar = nltk.data.load('file:my_grammar.cfg')

    wfst0 = init_wfst(sent, simple_grammar)
    wfst1 = complete_wfst(wfst0, sent, simple_grammar)
    print
    display(wfst1,sent,chart)
    print
    str= '%r' % (wfst1[0][len(sent)])
    if (str=='S'):
     return "valid sentence"
    else:
     return "invalid sentence"

inp=raw_input("enter sentence:",)
chart=[]
print(validate(inp,chart))