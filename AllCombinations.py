# The following code finds of the combinations of a given word and prints them

import copy
def print_matrix(matrix,s):

    string_list=list(s)
    final_str=""
    for i in range(0,len(matrix)):
        if matrix[i]==1:
            final_str=final_str+string_list[i]
    print final_str

def all_combination(matrix,k,n,s):
    mat=copy.copy(matrix)
    if k==n:
        mat[n]==0
        print_matrix(mat,s)
        mat[n]=1
        print_matrix(mat,s)
    else:
        mat[k]=0
        all_combination(mat,k+1,n,s)
        mat[k]=1
        all_combination(mat,k+1,n,s)


def buildSubsequences(s):
    ln=len(s)
    sub_string=list(s)
    matrix=[0]*ln
    all_val=[]  
    all_combination(matrix,0,ln-1,s)

res = buildSubsequences("abc");
