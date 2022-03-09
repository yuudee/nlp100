#1:文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ
import random

str = "stressed"
for s in reversed(str):
    print(s,end='')

print()

#2:「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
str1 = 'パトカー'
str2 = 'タクシー'
str = ''
for s1,s2 in zip(str1,str2):
    str += s1
    str += s2
print(str)

print()
#3:“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
str = str.split(' ')
str_len = []

for i in range(len(str)):
    str_len.append(len(str[i]))
print(str_len)


print()

#4:“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ
str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
str = str.split(' ')
str_map = {}
one_list = [1,5,6,7,8,9,15,16,19]
for i in range(len(str)):
    if i+1 in one_list:
        tmp = str[i][0]
        str_map[tmp] = i+1
    else:
        tmp = str[i][:2]
        str_map[tmp] = i+1
    
print(str_map)

print()

#5:与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ
def n_gram(str,n):
    n_gram_list = []
    for i in range(len(str)):
        if i+n > len(str):
            break
        n_gram_list.append(str[i:i+n])
    return n_gram_list
    
n_gram('I am an NLPer',4)

print()
        
#6:“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
str1 = 'paraparaparadise'
str2 = 'paragraph'

X = n_gram(str1,2)
Y = n_gram(str2,2)

sum_set = set(X) | set(Y)
inter_set = set(X) & set(Y)
dif_set = set(X) - set(Y)

if 'se' in X:
    print('Xに"se"が含まれるかどうか：True')
else:
    print('Xに"se"が含まれるかどうか：False')
    
if 'se' in Y:
    print('Yに"se"が含まれるかどうか：True')
else:
    print('Yに"se"が含まれるかどうか：False')
    
print('和集合:',sum_set)
print('積集合:',inter_set)
print('差集合：',dif_set)

print()

#7:引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
def x_y_z(x,y,z):
    str1 = '{}時の{}は{}'.format(x,y,z)
    return str1

str = x_y_z(12,'気温',22.4)
print(str)

print()

#8:与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力.この関数を用い，英語のメッセージを暗号化・復号化せよ．
def cipher(str):
    message = ''
    for i in range(len(str)):
        if str[i].islower():
            tmp = chr(219 - ord(str[i]))
            message += tmp
        elif str[i] == ' ':
            message += ' '
        else:
            message += str[i]
    return message

print('暗号化')            
message = cipher('the quick brown fox jumps over the lazy dog')
print(message)
print('複合化')
message = cipher(message)
print(message)

print()

#9:スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
# （例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，
# その実行結果を確認せよ．

def typoglycemia(str):
    message = ''
    str = str.split(' ')
    for i in range(len(str)):
        if len(str[i]) <= 4:
            message += str[i] + ' '
        else:
            tmp = ''
            tmp2 = ''
            tmp = str[i][1:-1]
            tmp1 = [x for x in tmp]
            random.shuffle(tmp1)
            for s in tmp1:
                tmp2 += s
            message += str[i][0] + tmp2 + str[i][-1] +' '
    return message

str = typoglycemia('I could believe that I could actually understand what I was reading : the phenomenal power of the human mind .')
print(str)
            
            