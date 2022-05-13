import math
from random import randint
from statistics import median, mean, variance, stdev


if __name__=='__main__':
    for _ in range(1, 21, 5):
        print('%d! = %d' % (_, math.factorial(_)))

    print()
    st=[80, 99, 77, 65, 92, 74, 82]
    print(st)
    print('중앙 값: %.2f' % median(st))
    print('평균: %.2f' % mean(st))
    print('분산: %.2f' % variance(st))
    print('표준편차: %.2f' % stdev(st))



    
