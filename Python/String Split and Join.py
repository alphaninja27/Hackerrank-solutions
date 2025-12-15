

def split_and_join(line):
    # write your code here
    arr = line.split(" ")
    ans = ""
    for i in range(len(arr) - 1):
        ans += arr[i] + "-"
    ans += arr[-1]
    return ans

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
