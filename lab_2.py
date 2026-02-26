from sympy import Matrix, sqrt, Rational 


a = Matrix([5, 3])
b = Matrix([3, -4])

a_plus_b = a + b
a_minus_b = a - b
dot_ab = int(a.dot(b))          
dot_ab_sq = dot_ab**2           # (a·b)^2
norm_a_sq = int(a.dot(a))       # |a|^2
norm_b_sq = int(b.dot(b))       # |b|^2
norm_a = sqrt(norm_a_sq)        # |a|
norm_b = sqrt(norm_b_sq)        # |b|
inv_norm_b = Rational(1,1)/norm_b  # 1/|b|

print("a =", list(a))
print("b =", list(b))
print()
print("a + b =", list(a_plus_b))
print("a - b =", list(a_minus_b))
print("a · b =", dot_ab)
print("(a · b)^2 =", dot_ab_sq)
print("|a|^2 =", norm_a_sq)
print("|b|^2 =", norm_b_sq)
print("|a| =", norm_a)
print("|b| =", norm_b)
print("1/|b| =", inv_norm_b)
