def solve(x,n):
    if n==0:
        return 1
    if n<0:
        return 1/solve(x,-n)
    half=solve(x,n//2)
    if n%2==0:
        return half*half
    return x*half*half
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return solve(x,n)