n = int(input())
matrix =[[1,1],[1,0]]

def power_mat(mat1, mat2):
    res=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for z in range(2):
                res[i][j] += mat1[i][z]*mat2[z][j] %1000000007
    return res

def power(a,b):
    if b ==1:
        return a
    else:
        tmp = power(a,b//2)
        if b%2 == 0:
            return power_mat(tmp,tmp)
        else:
            return power_mat(power_mat(tmp,tmp),a)


result= power(matrix,n)
print(result[0][1]%1000000007)

