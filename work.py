import ru_local

'''Mark'''
def mark_fun(x):
    if x == 5:
        return ru_local.ONE
    elif 0 < x < 15:
        return ru_local.TWO
    elif 0 < x < 20:
        return ru_local.TREE
    elif x == 25:
        return ru_local.FORE

def otziv_mne(y,p):
    if p == 0:
        return 0
    else:
        return y * p

'''Work of one file'''
file_in = open("one.txt", 'r')
line_1 = file_in.read().splitlines()
l_1 = line_1[0]
l_2 = line_1[1]
l_3 = line_1[2]
l_4 = line_1[3]
l_5 = line_1[4]
file_in.close()
'''Work of two file'''
file_in_2 = open("two.txt", 'r')
line_2 = file_in_2.read().splitlines()
li_1 = line_2[0]
li_2 = line_2[1]
li_3 = line_2[2]
li_4 = line_2[3]
li_5 = line_2[4]
file_in_2.close()

print(l_1, '\n', li_1)
print()
print(l_2, '\n', li_2)
print()
print(l_3, '\n', li_3)
print()
print(l_4, '\n', li_4)
print()
print(l_5, '\n', li_5)
print()


one = list(input(ru_local.MARK) for _ in range(5))
a, b, c, d, e = one
one = [a, b, c, d, e]
six = one.count('1')
two = one.count('2')
tree = one.count('3')
fore = one.count('4')
five = one.count('5')

six_1 = otziv_mne(1,six)
two_1 = otziv_mne(2, two)
tree_1 = otziv_mne(3, tree)
fore_1 = otziv_mne(4, fore)
five_1 = otziv_mne(5, five)
one = [six_1, two_1, tree_1, fore_1, five_1]
one = sum(one)
print(ru_local.FIVE, one)
print()
print(mark_fun(one))
