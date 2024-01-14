class solution:
    def twosum(self,nums: list[int], target:int) -> list[int]:
        #[2,11,15,7] target = 9
        comp_map = {}
        for i,n in enumerate(nums):
            comp = target - n
            if comp not in comp_map:
                comp_map[n] = i
            else:
             return [i,comp_map[comp]]
            
s = solution()
result = s.twosum([2, 11, 15, 7], 9)
print(result)
            



