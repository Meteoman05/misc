import string
import sys
sys.setrecursionlimit(1030)


def fac_r(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)


def fac_i(n):
    if n == 0 or n == 1:
        return 1
    else:
        fac = 1
        for i in range(1, n + 1):
            fac *= i
        return fac


def from_10(num, to_base, alph=string.printable):
    if num // to_base < to_base:
        if num // to_base == 0:
            return alph[num % to_base]
        else:
            return alph[num // to_base] + alph[num % to_base]   
    else:
        return from_10(num // to_base, to_base) + alph[num % to_base]


def to_10(num, from_base, alph=string.printable, i=0):
    alph_ = {j[1]:j[0] for j in enumerate(alph)}
    if i == len(num)-1:
        return int(alph_[num[i]])
    else:
        return (int(alph_[num[i]])*from_base**(len(num)-1-i) +
    to_10(num,
          from_base,
          alph=string.printable,
          i = i + 1))


def sn_conv(num, from_base, to_base, alph=string.printable):
    num = int(to_10(num, from_base, alph=alph))
    return from_10(num, to_base)


def num_to_min(num, alph=string.printable):
        alph_ = {j[1]:j[0] for j in enumerate(alph)}
        max_ = max(alph_[i] for i in num)
        return from_10(to_10(num, max_+1, alph=alph), 100)


def invert_b(num, alph=string.printable):
    num = list(num)
    if len(num) == 1:
        if num.pop() == '1':
            return '0'
        else:
            return '1'
    else:
        if num.pop() == '1':
            return invert_b(''.join(num)) + '0'
        else:
            return invert_b(''.join(num)) + '1'


def invert_bin(num):
        num = num.zfill(1024)
        num = invert_b(num)
        return num


def invert(num, base, alph=string.printable):
    num = sn_conv(num, base, 2)
    return sn_conv(invert_bin(num), 2, base)


def rec(func, val, _max, i = 1):
    if i == _max:
        return func(val)
    else:
        return func(rec(func, val, _max, i + 1))


a = invert('1101', 13)
b = invert('1101', 8)

#while True: exec(input('>>>'))
