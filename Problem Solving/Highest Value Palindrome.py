def highestValuePalindrome(s, n, k):
    # Write your code here
    list_s= list(s)
    list_s= list(map(int, list_s))
    p_flag= [0]*n

    for i in range(int(n/2)):
        if list_s[i]==list_s[n-1-i]:
            p_flag[i]=0
            p_flag[n-1-i]=0
        else:
            if list_s[i]> list_s[n-1-i]:
                p_flag[i]=1
            else:
                p_flag[n-1-i]=1
    if sum(p_flag)>k:
        return str(-1)

    for i in range(int(n/2)):
        if p_flag[i]==0 and p_flag[n-i-1]==0:
            continue
        elif p_flag[i]!=0:
            if list_s[i]==9:
                list_s[n-1-i]=9
                k=k-1
                p_flag[i]= 0
                p_flag[n-1-i]= 0
        elif p_flag[n-1-i]!=0:
            if list_s[n-1-i]==9:
                list_s[i]=9
                k=k-1
                p_flag[i]= 0
                p_flag[n-1-i]= 0

    for i in range(int(n/2)):
        if list_s[i]>list_s[n-1-i]:
            list_s[n-1-i]= list_s[i]
            k=k-1
        elif list_s[i]<list_s[n-1-i]:
            list_s[i]= list_s[n-1-i]
            k=k-1

    for i in range(int(n/2)):
        if p_flag[i]==0 and p_flag[n-i-1]==0:
            if list_s[i]==9 and list_s[n-i-1]==9:
                continue
            else:
                if k>=2:
                    list_s[i]=9
                    list_s[n-i-1]=9
                    k= k-2
        elif p_flag[i]==1:
            if k>=1:
                list_s[i]=9
                list_s[n-i-1]=9
                k= k-1
        elif p_flag[n-1-i]==1:
            if k>=1:
                list_s[i]=9
                list_s[n-i-1]=9
                k= k-1
    if k>=1 and n%2==1:
        list_s[int(n/2)]=9
    return ''.join(list(map(str, list_s)))
