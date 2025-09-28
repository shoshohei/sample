a, b, c = [int(i) for i in input().split(' ')]
mod = 10**9+7
print(int((((a%mod*b%mod)%mod)*(c%mod))%mod))