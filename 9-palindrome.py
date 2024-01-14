class solution:
    def palindrome(self,x):
        if (x<0):
            return False
        s= 0
        i = x
        while(i>0):
            d= i % 10
            s=s * 10 + d
            i = i // 10
        if (x==s):
            return True
        else:
            return False

sol = solution()
num = 121
result = sol.palindrome(num)
print(result)

            
    
