def makingAnagrams(s1, s2):
    count = 0
    for i in list(set(s1)):
       if (i not in s2):
           count = count + s1.count(i)
           
    for i in list(set(s2)):
       if(i not in s1):
           count = count + s2.count(i)
           
    for i in list(set(s1)):
        if(i in s2):
            count = count + abs(s2.count(i) - s1.count(i))
           
    return count
