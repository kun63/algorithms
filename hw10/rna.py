import heapq
import datetime


def pair(a,b):
    if a == 'A':
        if b == 'U':
            return 1
        else:
            return 0
    elif a == 'G':
        if b == 'U' or b == 'C':
            return 1
        else:
            return 0
    elif a == 'U':
        if b == 'A' or b == 'G':
            return 1
        else:
            return 0
    elif a == 'C':
        if b == 'G':
            return 1
        else:
            return 0
    else:
        return 0


def best(rna, i=0, j=0, opt=None, path=None):
    if opt is None:
        j = len(rna) - 1
        opt = {(0,0):0}
        path={(0,0):'.'}
    if (i,j) in opt:
        return opt[(i,j)]
    if i == j:
        path[(i,j)] = '.'
        opt[(i,j)] = 0
        return opt[(i,j)]
    separate = []
    separate_best = 0
    together = 0
    if pair(rna[i], rna[j]) == 1:
        if i+1  == j:
            path[(i,j)] = '()'
            opt[(i,j)] = 1
            return 1
        else:
            together = best(rna, i+1, j-1, opt, path) + 1
    for k in range(i,j):
        separate.append((best(rna,i,k,opt,path)+best(rna,k+1,j,opt,path),k))
    separate_best = max(separate)
    if together > separate_best[0]:
        opt[(i,j)] = together
        path[(i,j)] = '(' + path[(i+1,j-1)] + ')'
    else:
        k = separate_best[1]
        opt[(i,j)] = separate_best[0]
        path[(i,j)] = path[(i,k)] + path[(k+1,j)]
    if i == 0 and j == len(rna)-1:
        return opt[(i,j)], path[(i,j)]
    else:
        return opt[(i,j)]


def _total(rna, i=0, j=0, opt=None, path=None):
    if opt is None:
        j = len(rna) - 1
        opt = {}

    if (i,j) in opt:
        return opt[(i,j)]
    possible_structure = set()
    if i == j:

        possible_structure.add((0, '.'))
        opt[(i,j)] = possible_structure
        return possible_structure
    

    if pair(rna[i], rna[j]) == 1:
        if i+1  == j:

            possible_structure.add((1, '()'))
            possible_structure.add((0, '..'))
            opt[(i,j)] = possible_structure
            return possible_structure
        else:
            for s in total(rna, i+1, j-1, opt, path):
                together = (s[0] + 1, '(' + s[1] + ')')
                possible_structure.add(together)
    for k in range(i,j):
        for a in total(rna,i,k,opt,path):
            for b in total(rna,k+1,j,opt,path):
                separate = (a[0]+b[0], a[1]+b[1])
                possible_structure.add(separate)

    if i == 0 and j == len(rna)-1:
        outcome = 0
        print(possible_structure)
        for p in possible_structure:
            outcome += 1
        return outcome
    else:
        opt[(i,j)] = possible_structure
        return possible_structure


def total(rna,i=0, j=0, opt=None):
    if opt == None:
        j = len(rna)-1
        opt = {'':1, 'A':1, 'G':1, 'C':1, 'U':1}
    subrna = rna[i:j+1]
    if subrna in opt:
        return opt[subrna]
    if i+1 == j:
        # opt[subrna] = 1
        # return 1
        if pair(rna[i], rna[j]) == 1:
            opt[subrna] = 2
            return 2
        else:
            opt[subrna] = 1
            return 1
    temp_opt = 0
    for k in range(i+1,j+1):
        sub_opt = 0
        if pair(rna[i], rna[k]):
            if k == i+1:
                sub_opt += total(rna,k+1,j,opt)
                # continue
            elif k == j:
                sub_opt += total(rna,i+1,k-1,opt)
            else:
                sub_opt += total(rna,i+1,k-1,opt) * total(rna,k+1,j,opt)
            # sub_opt *= 2
        temp_opt += sub_opt
    opt[subrna] = temp_opt + total(rna,i+1,j,opt)

    return opt[subrna]
        

def kbest(rna, n, i=0, j=0, opt=None):

    def trypush(h, m, a, b):
        if m == -1:
            
            if a+1 < len(l1):
                s = l1[a+1]
                vp = (s[0]-1,'()'+s[1][:])
                if vp not in temp:
                    heapq.heappush(h,(vp,-1,a+1,0))
                    temp.add(vp)
        elif m == -2:
            
            if a+1 < len(l2):
                s = l2[a+1]
                vp = (s[0]-1,'('+s[1][:]+')')
                if vp not in temp:
                    heapq.heappush(h,(vp,-2,a+1,0))
                    temp.add(vp)
        elif m == -3:
            
            if a+1 < len(l3):
                s = l3[a+1]
                vp = (s[0],'.'+s[1])
                if vp not in temp:
                    heapq.heappush(h,(vp,-3,a+1,0))
                    temp.add(vp)
        else:
            # k = l4_left[a+1]
            # t = l4_right[b+1]
            # a += 1
            # heapq.heappush(h,((l4_left[a][0]+l4_right[b][0]-1,'('+l4_left[a][1]+')'+l4_right[b][1]),m,a,b))
            # a -= 1
            # b += 1
            # heapq.heappush(h,((l4_left[a][0]+l4_right[b][0]-1,'('+l4_left[a][1]+')'+l4_right[b][1]),m,a,b))

            # if a+1 < len(l4_left[m]):
            #     if b+1 < len(l4_right[m]):
            #         a += 1
            #         # print(b,len(l4_right[m])-1)
            #         heapq.heappush(h,((l4_left[m][a][0]+l4_right[m][b][0]-1,'('+l4_left[m][a][1]+')'+l4_right[m][b][1]),m,a,b))
            #         a -= 1
            #         b += 1
            #         # k = l4_left[m][a][0]
            #         # print(b,len(l4_right[m])-1)
            #         # temp = k+l4_right[m][b][0]-1
            #         heapq.heappush(h,((l4_left[m][a][0]+l4_right[m][b][0]-1,'('+l4_left[m][a][1]+')'+l4_right[m][b][1]),m,a,b))
            #     else:
            #         a += 1
            #         heapq.heappush(h,((l4_left[m][a][0]+l4_right[m][b][0]-1,'('+l4_left[m][a][1]+')'+l4_right[m][b][1]),m,a,b))
            # else:
            #     if b+1 <len(l4_right[m]):
            #         b += 1
            #         heapq.heappush(h,((l4_left[m][a][0]+l4_right[m][b][0]-1,'('+l4_left[m][a][1]+')'+l4_right[m][b][1]),m,a,b))

            if a+1 < len(l4_left[m]):
                # a += 1
                k = a + 1
                vp = (l4_left[m][k][0]+l4_right[m][b][0]-1,'('+l4_left[m][k][1]+')'+l4_right[m][b][1])
                if vp not in temp:
                    heapq.heappush(h,(vp,m,k,b))
                    temp.add(vp)
            if b+1 <len(l4_right[m]):
                # b += 1
                t = b + 1
                vp = (l4_left[m][a][0]+l4_right[m][t][0]-1,'('+l4_left[m][a][1]+')'+l4_right[m][t][1])
                if vp not in temp:
                    heapq.heappush(h,(vp,m,a,t))
                    temp.add(vp)
                    



    if opt == None:
        j = len(rna)-1
        opt = {'':[(0,'')], 'A':[(0,'.')], 'G':[(0,'.')], 'C':[(0,'.')], 'U':[(0,'.')]}
    subrna = rna[i:j+1]
    if subrna in opt:
        return opt[subrna]
    if i+1 == j:
        # opt[subrna] = 1
        # return 1
        if pair(rna[i], rna[j]) == 1:
            vp=[(-1,'()'),(0,'..')]
            opt[subrna] = vp
            return opt[subrna]
        else:
            opt[subrna] = [(0,'..')]
            return opt[subrna]
    # temp_opt = 0
    vp = []
    l1 = []
    l2 = []
    l3 = []
    l4_left = []
    l4_right = []
    m = 0
    h = []
    for k in range(i+1,j+1):
        # sub_opt = 0
        if pair(rna[i], rna[k]):
            if k == i+1:
                # sub_opt += kbest(rna,k+1,j,opt)
                l1 = kbest(rna,n,k+1,j,opt)
                s = l1[0]
                # vp.append((s[0]-1,'()'+s[1][:]))
                heapq.heappush(h,((s[0]-1,'()'+s[1][:]),-1,0,0))
                # continue
            elif k == j:
                # sub_opt += kbest(rna,i+1,k-1,opt)
                l2 = kbest(rna,n,i+1,k-1,opt)
                s = l2[0]
                # vp.append((s[0]-1,'('+s[1][:]+')'))
                heapq.heappush(h,((s[0]-1,'('+s[1][:]+')'),-2,0,0))
            else:
                # sub_opt += kbest(rna,i+1,k-1,opt) * kbest(rna,k+1,j,opt)
                l4_left.append(kbest(rna,n,i+1,k-1,opt))
                l4_right.append(kbest(rna,n,k+1,j,opt))
                a = l4_left[m][0]
                b = l4_right[m][0]
                heapq.heappush(h,((a[0]+b[0]-1,'('+a[1]+')'+b[1]),m,0,0))
                m += 1
                # vp.append((a[0]+b[0]-1,'('+a[1]+')'+b[1]))
            # sub_opt *= 2
        # temp_opt += sub_opt
    l3 = kbest(rna,n,i+1,j,opt)
    s = l3[0]
    heapq.heappush(h,((s[0],'.'+s[1]),-3,0,0))
    # vp.append((s[0],'.'+s[1]))

    outcome = []
    temp = set()
    # x = set()
    while len(outcome) < n and len(h) != 0:
        vp, m, a, b = heapq.heappop(h)
        # _, p = vp
        # if p in temp:
        #     pass
        # else:
        # temp.add(p)
        outcome.append(vp)
        trypush(h,m,a,b)

    # t = set()
    # for _,c in outcome:
    #     if c in t:
    #         print('++++++++++++++++++++++++++++++++++++++')
    #     else:
    #         t.add(c)
    
    opt[subrna] = outcome
    

    # print('----------')
    # print(subrna)
    # print(opt[subrna])


    if i == 0 and j == len(rna)-1:
        
        _outcome = []
        x = set()
        for v in outcome:
            _outcome.append((-v[0],v[1]))

        return _outcome
    else:
        return opt[subrna]



def _kbest(rna, n, i=0, j=0, opt=None):
    if opt == None:
        j = len(rna)-1
        opt = {'':[(0,'')], 'A':[(0,'.')], 'G':[(0,'.')], 'C':[(0,'.')], 'U':[(0,'.')]}
    subrna = rna[i:j+1]
    if subrna in opt:
        return opt[subrna]
    if i+1 == j:
        # opt[subrna] = 1
        # return 1
        if pair(rna[i], rna[j]) == 1:
            vp=[(1,'()'),(0,'..')]
            opt[subrna] = vp
            return opt[subrna]
        else:
            opt[subrna] = [(0,'..')]
            return opt[subrna]
    # temp_opt = 0
    vp = []
    for k in range(i+1,j+1):
        # sub_opt = 0
        if pair(rna[i], rna[k]):
            if k == i+1:
                # sub_opt += kbest(rna,k+1,j,opt)
                for s in kbest(rna,n,k+1,j,opt):
                    vp.append((s[0]+1,'()'+s[1][:]))
                # continue
            elif k == j:
                # sub_opt += kbest(rna,i+1,k-1,opt)
                for s in kbest(rna,n,i+1,k-1,opt):
                    vp.append((s[0]+1,'('+s[1][:]+')'))
            else:
                # sub_opt += kbest(rna,i+1,k-1,opt) * kbest(rna,k+1,j,opt)
                for a in kbest(rna,n,i+1,k-1,opt):
                    for b in kbest(rna,n,k+1,j,opt):
                        vp.append((a[0]+b[0]+1,'('+a[1]+')'+b[1]))
            # sub_opt *= 2
        # temp_opt += sub_opt
    for s in kbest(rna,n,i+1,j,opt):
        vp.append((s[0],'.'+s[1]))

    
    opt[subrna] = sorted(vp, key = lambda x:-x[0])[:n]
    # opt[subrna] = vp
    # print('----------')
    # print(subrna)
    # print(opt[subrna])
    return opt[subrna]



def transf(s):
    outcome=[]
    for v, _ in s:
        outcome.append(v)
    return outcome


if __name__ == "__main__":
    # print(pair('A','U'))
    # print(best('GCACG'))
    # print(best('GCACG'))
    # print(best('UUCAGGA'))
    # print(best('ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC'))
    



    # print(total('ACAGU'))
    # print(total('AC'))
    # print(total('GUAC'))
    # print(total('GCACG'))
    # print(total('CCGG'))
    # print(total('CCCGGG'))
    # print(total('UUCAGGA'))
    # print(total('AUAACCUA'))
    # print(total('UUGGACUUG'))
    # print(total('UUUGGCACUA'))

    # print(kbest('ACAGU',10))
    # print(kbest('AC'))
    # print(kbest('GUAC'))
    # print(kbest('GCACG',10))
    # print(kbest('CCGG',10))
    # print(kbest('CCCGGG',10))
    # print(kbest('UUCAGGA'))
    # print(kbest('AUAACCUA'))
    # print(kbest('UUGGACUUG'))
    # print(kbest('UUUGGCACUA'))



    # print(total('GAUGCCGUGUAGUCCAAAGACUUC'))


    # print("\n",kbest('ACAGU', 10),"\n [(2, '((.))'), (1, '.(.).'), (1, '..(.)'), (1, '...()'), (1, '(...)'), (0, '.....')]")
    # print("\n",kbest('AC', 10),"\n [(0, '..')]")
    # print("\n",kbest('GUAC', 10),"\n [(2, '(())'), (1, '()..'), (1, '.().'), (1, '(..)'), (0, '....')]")
    # print("\n",kbest('GCACG', 10),"\n [(2, '().()'), (1, '(..).'), (1, '()...'), (1, '.(..)'), (1, '...()'), (0, '.....')]")
    # print("\n",kbest('CCGG', 10),"\n [(2, '(())'), (1, '(.).'), (1, '.().'), (1, '.(.)'), (1, '(..)'), (0, '....')]")
    # print("\n",kbest('CCCGGG', 10),"\n [(3, '((()))'), (2, '((.)).'), (2, '(.()).'), (2, '.(()).'), (2, '.(().)'), (2, '.((.))'), (2, '((.).)'), (2, '(.(.))'), (2, '(.().)'), (2, '((..))')]")
    # print("\n",kbest('UUCAGGA', 10),"\n [(3, '(((.)))'), (2, '((.).).'), (2, '((..)).'), (2, '(.(.)).'), (2, '((.))..'), (2, '.((.)).'), (2, '.((.).)'), (2, '.((..))'), (2, '((..).)'), (2, '((.)..)')]")
    # print("\n",kbest('AUAACCUA', 10),"\n [(2, '((.)..).'), (2, '(()...).'), (2, '()(...).'), (2, '().(..).'), (2, '()....()'), (2, '.()(..).'), (2, '.()...()'), (2, '.(.)..()'), (2, '.((...))'), (2, '.(.(..))')]")
    # print("\n",kbest('UUGGACUUG', 10),"\n [(4, '(())(.)()'), (4, '(()((.)))'), (3, '(().)..()'), (3, '(().).(.)'), (3, '(().)(..)'), (3, '((.))..()'), (3, '((.)).(.)'), (3, '((.))(..)'), (3, '(())(..).'), (3, '(())(.)..')]")
    # print("\n",kbest('UUUGGCACUA', 10),"\n [(4, '((()).).()'), (4, '((.)()).()'), (4, '(.()()).()'), (4, '.(()()).()'), (4, '.(()()(.))'), (4, '((()).(.))'), (4, '((.)()(.))'), (4, '((()())..)'), (4, '(.()()(.))'), (3, '((()).)...')]")


    # print(transf(kbest('UCAGAGGCAUCAAACCU', 300)))
    print(transf(kbest('UCAGAGGCAUCAAACCU', 300)))
    # print(kbest('UCAGAGGCAUCAAACCU', 300))
    # a = kbest('UCAGAGGCAUCAAACCU', 300)
    # k = set()
    # i = 0
    # for _, p in a:
    #     if p == '(.)(..()())..(..)':
    #         i += 1
    #         print(p)
    #     else:
    #         k.add(p)
    # print(i)
    # print(kbest('CGCCGUCCGGGCGCGCCUUUUACGUAGAUUU', 9))
    # print(kbest('AGGCAUCAAACCCUGCAUGGGAGCG', 9))



    # start = datetime.datetime.now()
    # print(transf(kbest('UCAGAGGCAUCAAACCU', 12)))
    # print(transf(_kbest('UCAGAGGCAUCAAACCU', 12)))
    # end = datetime.datetime.now()
    # print (end-start)

    # a = "UCAGAGGCAUCAAACCUGCAUGGAG"
    # a = "UCAGAGGCAUCAAACCU"
    # i=0
    # j=len(a)-1
    # for k in range(1,len(a)-2):
    #     # print("i, k", i,k)
    #     if transf( kbest(a[i:k], 12)) != transf(_kbest(a[i:k], 12)):
    #         print(a[i:k])
    #         print('-----------------')
    #         print(transf( kbest(a[i:k], 12)))
    #         print(transf(_kbest(a[i:k], 12)))
    #         print('-----------------')
    #     # print("k+1, j", k+1, j)
    #     if transf( kbest(a[k+1:j], 12)) != transf(_kbest(a[k+1:j], 12)):
    #         print(a[k+1:j])
    #         print('-----------------')
    #         print(transf( kbest(a[k+1:j], 12)))
    #         print(transf(_kbest(a[k+1:j], 12)))
    #         print('-----------------')


    # print(kbest('UG',10))
    # print(kbest('AU',10))
    




    
    




    





