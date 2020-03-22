L = [6, 3, 9, 12, 15]
T = 21

L_sort = sorted(L, reverse=True)
L_out = []

def Lout(LL):
    L_ind = []
    for i1 in LL:
        L_ind.append(L.index(i1) + 1)
    print(sorted(L_ind))

def ListCount(L_list):
    L_count = []
    for ind in range(len(L_list)):
        L_count.append(L_list[ind])

        if sum(L_count) > T:
            L_count.pop()
            next

        if sum(L_count) == T:
            L_out.append(L_count.copy())
            L_count.pop()
            next
        
while sum(L_sort) > T:
    ListCount(L_sort)
    L_sort = L_sort[1:]

if sum(L_sort) == T:
    L_out.append(L_sort.copy())

L_out_new = []
for L_new in L_out:
    if L_new not in L_out_new:
        L_out_new.append(L_new)

if L_out_new:
    for i in L_out_new:
        Lout(i)
else: print('No Answer!')