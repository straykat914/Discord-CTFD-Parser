

# This file was *autogenerated* from the file /mnt/d/Bureau/Arthur/github/Discord_CTFD/utils/Facto4CTF/modules/factoring/sage/qicheng.sage
from sage.all_cmdline import *   # import sage library

_sage_const_10000 = Integer(10000); _sage_const_50 = Integer(50); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_1728 = Integer(1728); _sage_const_5 = Integer(5); _sage_const_11 = Integer(11); _sage_const_6 = Integer(6); _sage_const_23 = Integer(23); _sage_const_29 = Integer(29)
import sys
sys.setrecursionlimit(_sage_const_10000 )

from sage.parallel.multiprocessing_sage import parallel_iter
from multiprocessing import cpu_count

def factor(n,attempts=_sage_const_50 ):
    Consts = {}
    Consts['0'] = _sage_const_0 
    Consts['1'] = _sage_const_1 
    Consts['2'] = _sage_const_2 
    Consts['3'] = _sage_const_3 
    Consts['1728'] = _sage_const_1728 
    js = [_sage_const_0 , (-_sage_const_2 **_sage_const_5 )**_sage_const_3 , (-_sage_const_2 **_sage_const_5 *_sage_const_3 )**_sage_const_3  ,(-_sage_const_2 **_sage_const_5 *_sage_const_3 *_sage_const_5 *_sage_const_11 )**_sage_const_3 , (-_sage_const_2 **_sage_const_6 *_sage_const_3 *_sage_const_5 *_sage_const_23 *_sage_const_29 )**_sage_const_3 ]


    def corefunc(n,js,Consts):
        R = Integers(int(n))
        
        for j in js:
            if j == Consts['0']:
                a = R.random_element()
                E = EllipticCurve([Consts['0'], a])

            else:
                a = R(j)/(R(Consts['1728'])-R(j))
                c = R.random_element()
                E = EllipticCurve([Consts['3']*a*c**Consts['2'], Consts['2']*a*c**Consts['3']])

            x = R.random_element()
            z = E.division_polynomial(n, x)
            g = gcd(z, n)
            if g > Consts['1']:return g

    cpus = cpu_count()
    if attempts > cpus:
        A = cpus
    else:
        A = attempts
    B = int(attempts/cpus)
    for i in range(_sage_const_0 ,B+_sage_const_1 ):
        inputs = [((n,js,Consts,),{})] * A
        for k, val in parallel_iter(A, corefunc,inputs):
            if val != None:
                return val

if __name__ == "__main__":
    print(factor(Integer(sys.argv[_sage_const_1 ])))

