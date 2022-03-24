def ins_exp_util(p, q, y, x) :
    return p * util(y - x + q - pi(p,q), theta) + (1 - p) * util(y - pi(p,q), theta)

def pi(p, q) :
    return p * q

def util(z, theta):
    return (z ** (1 + theta)) / (1 + theta)

