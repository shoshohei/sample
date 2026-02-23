N, Q = [int(i) for i in input().split(' ')]
X, Y = [0]*N, [0]*N
A, B = [0]*Q, [0]*Q
for i in range(N):
    X[i], Y[i] = [int(i) for i in input().split(' ')]
for i in range(Q):
    A[i], B[i] = [int(i) for i in input().split(' ')]
import math
thetas = [0]*N
for i in range(N):
    x, y = X[i], Y[i]
    theta = math.atan2(y, x)
    if theta < 0:
        theta += 2 * math.pi
    thetas[i] = theta
sorted_theta = sorted(thetas)
#print(thetas)
#print(sorted_theta)
import bisect
for i in range(Q):
    a, b = A[i], B[i]
    theta_a = thetas[a-1]
    theta_b = thetas[b-1]
    if  abs(X[a-1] * Y[b-1] - Y[a-1] * X[b-1]) < 1e-6:
        print(bisect.bisect_right(sorted_theta, theta_a)-bisect.bisect_left(sorted_theta, theta_a))
    elif theta_a > theta_b:
        pos_a = bisect.bisect_right(sorted_theta, theta_a)
        pos_b = bisect.bisect_left(sorted_theta, theta_b)
        print(pos_a-pos_b)#, pos_a, pos_b)

    else:
        pos_a = bisect.bisect_right(sorted_theta, theta_a)
        pos_b = bisect.bisect_left(sorted_theta, theta_b)
        print(pos_a+(N-pos_b))#, math.pi, pos_a, pos_b)
