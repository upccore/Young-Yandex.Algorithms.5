p, v = map(int, input().split())
q, m = map(int, input().split())
minv, maxv = p - v, p + v
minm, maxm = q - m, q + m
if max(minv, minm) <= min(maxv, maxm):
    print(max(maxv, maxm) - min(minv, minm) + 1)
else:
    print((maxv - minv + 1) + (maxm - minm + 1))