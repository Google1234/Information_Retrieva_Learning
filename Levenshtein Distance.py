#-*- coding: UTF-8 -*-
'''
编辑距离
    两个字符串s1和s2编辑距离是指从 s1 转换成s2所需要的最少的基本操作数目
    Levenshtein距离: 采用的基本操作是插入(insert)、删除(delete)和替换(replace)
    Levenshtein距离 dog-do: 1
    Levenshtein距离 cat-cart: 1
    Levenshtein距离 cat-cut: 1
    Levenshtein距离 cat-act: 2
'''
def levenshtein_distance(s1,s2):
    row=len(s1)+1
    colum=len(s2)+1
    m=[[0 for i in range(colum)] for j in range(row)]
    for i in range(row):
        m[i][0]=i
    for j in range(colum):
        m[0][j]=j
    for i in range(1,row):
        for j in range(1,colum):
            if s1[i-1]==s2[j-1]:
                m[i][j]=min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1])
            else :
                m[i][j]=min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1]+1)
    return m[row-1][colum-1]

'''
    Damerau-Levenshtein距离：除了上述三种基本操作外，还包括两个字符之间的交换（transposition）操作
    Damerau-Levenshtein距离 cat-act: 1
'''
def damerau_levenshtein_distance(s1,s2):
    row=len(s1)+1
    colum=len(s2)+1
    m=[[0 for i in range(colum)] for j in range(row)]
    for i in range(row):
        m[i][0]=i
    for j in range(colum):
        m[0][j]=j
    for i in range(1,row):
        j=1
        if s1[i-1]==s2[j-1]:
            m[i][j]=min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1])
        else :
            m[i][j]=min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1]+1)
    for j in range(1,colum):
        i=1
        if s1[i-1]==s2[j-1]:
            m[i][j]=min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1])
        else :
            m[i][j]=min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1]+1)
    for i in range(2,row):
        for j in range(2,colum):
            if s1[i-1]==s2[j-1]:
                if s1[i-1]==s2[j-2] and s1[i-2]==s2[j-1]:
                    m[i][j]=min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1],m[i-2][j-2]+1)
                else :
                    m[i][j]=min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1])
            else :
                if s1[i-1]==s2[j-2] and s1[i-2]==s2[j-1]:
                    m[i][j]=min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1]+1,m[i-2][j-2]+1)
                else:
                    m[i][j]=min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1]+1)
    return m[row-1][colum-1]


#示例
#print levenshtein_distance('cat','act')
#print damerau_levenshtein_distance('cat','act')