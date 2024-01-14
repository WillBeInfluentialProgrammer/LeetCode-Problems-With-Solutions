class Solution:
    def MedianOfTwoSortedSubArrays(self, num1: list[int], num2: list[int]) -> float:
        A, B = num1, num2
        total = len(num1) + len(num2)
        half = total / 2

        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # for odd list
                if total % 2:
                    return min(Aright, Bright)
                # for even list
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

sol = Solution()

# Example lists to test the code
num1 = [1, 3]
num2 = [2]
result = sol.MedianOfTwoSortedSubArrays(num1, num2)
print(result)
