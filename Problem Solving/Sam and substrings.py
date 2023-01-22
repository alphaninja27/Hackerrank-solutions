def substrings(n):
    # Write your code here
    leen=len(n)
    ans=0
    mod=10**9+7
    i=0
    for ltt in n[::-1]:
        i=(10*(i%mod)+1)%mod
        lt=int(ltt)
        ans+=(lt*i*leen)%mod
        leen-=1
    return ans%mod
