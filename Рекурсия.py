import string


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


def num_to_min(num, alph=string.printable):
        alph_ = {j[1]:j[0] for j in enumerate(alph)}
        max_ = max(alph_[i] for i in num)
        return from_10(to_10(num, max_+1, alph=alph), 100)
