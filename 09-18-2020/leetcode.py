def switcharoo(x):
    newnumber = 0
    if -1 < x < 1:
        if x  < 0:
            x = x * (-1)
            while x > 0:
                ones = x%10
                x = x//10
                newnumber = newnumber*10 + ones 
            return (newnumber*(-1))
        else: 
            while x > 0:
                ones = x%10
                x = x//10
                newnumber = newnumber*10 + ones 
            return (newnumber)
    else:
        return(0)

print(switcharoo(-8721))
print(2**31-1)

# print ("hello")

# def Helpme():
#     return "why does god hate me"

# print (Helpme())

#June's Solutions
class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        res = 0
        while x>0:
            res = res*10 +  x%10
            x //= 10
        max_val = (2**31-1) if not negative else 2**31
        if res > max_val:
            return 0
        return res if not negative else -res
def romanToInt(s):
    res = 0
    pre_val = None
    val_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    check_grammar = None
    for i in s:
        # i = "I", i = "I"
        if i not in val_dic.keys():
            return "There is somethign wrong with your input" 

        val = val_dic[i] # 1, 1

        if check_grammar and val > check_grammar:
            return "There is somethign wrong with your input"

        if pre_val and val > pre_val: # 1 > 0
            val = val - pre_val*2  # 1 - 0*2
            check_grammar = val
        res += val # 0 += 1
        pre_val = val_dic[i] # 1
    return res

def palindrome(x):
    newnumber = 0
    while x > 0:
        ones = x%10
        x = x//10
        newnumber = newnumber*10 + ones 
    if newnumber == x:
        return("true")
    else:
        return("false")

print(palindrome(1331))
