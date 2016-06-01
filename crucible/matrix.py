#https://gist.github.com/VikParuchuri/5994925
from copy import deepcopy

def invert(X):
    """
    Invert a matrix X according to gauss-jordan elimination
    In gauss-jordan elimination, we perform basic row operations to turn a matrix into
    row-echelon form.  If we concatenate an identity matrix to our input
    matrix during this process, we will turn the identity matrix into our inverse.
    X - input list of lists where each list is a matrix row
    output - inverse of X
    """
    #copy X to avoid altering input
    X = deepcopy(X)

    #Get dimensions of X
    rows = len(X)
    cols = len(X[0])

    #Get the identity matrix and append it to the right of X
    #This is done because our row operations will make the identity into the inverse
    identity = make_identity(rows,cols)
    for i in xrange(0,rows):
        X[i]+=identity[i]

    i = 0
    for j in xrange(0,cols):
        #print("On col {0} and row {1}".format(j,i))
        #Check to see if there are any nonzero values below the current row in the current column
        zero_sum, first_non_zero = check_for_all_zeros(X,i,j)
        #If everything is zero, increment the columns
        if zero_sum==0:
            if j==cols:
                return X
            raise Exception("Matrix is singular.")
        #If X[i][j] is 0, and there is a nonzero value below it, swap the two rows
        if first_non_zero != i:
            X = swap_row(X,i,first_non_zero)
        #Divide X[i] by X[i][j] to make X[i][j] equal 1
        X[i] = [m/X[i][j] for m in X[i]]

        #Rescale all other rows to make their values 0 below X[i][j]
        for q in xrange(0,rows):
            if q!=i:
                scaled_row = [X[q][j] * m for m in X[i]]
                X[q]= [X[q][m] - scaled_row[m] for m in xrange(0,len(scaled_row))]
        #If either of these is true, we have iterated through the matrix, and are done
        if i==rows or j==cols:
            break
        i+=1

    #Get just the right hand matrix, which is now our inverse
    for i in xrange(0,rows):
        X[i] = X[i][cols:len(X[i])]

    return X

def check_for_all_zeros(X,i,j):
    """
    Check matrix X to see if only zeros exist at or below row i in column j
    X - a list of lists
    i - row index
    j - column index
    returns -
        zero_sum - the count of non zero entries
        first_non_zero - index of the first non value
    """
    non_zeros = []
    first_non_zero = -1
    for m in xrange(i,len(X)):
        non_zero = X[m][j]!=0
        non_zeros.append(non_zero)
        if first_non_zero==-1 and non_zero:
            first_non_zero = m
    zero_sum = sum(non_zeros)
    return zero_sum, first_non_zero

def swap_row(X,i,p):
    """
    Swap row i and row p in a list of lists
    X - list of lists
    i - row index
    p - row index
    returns- modified matrix
    """
    X[p], X[i] = X[i], X[p]
    return X

def make_identity(r,c):
    """
    Make an identity matrix with dimensions rxc
    r - number of rows
    c - number of columns
    returns - list of lists corresponding to  the identity matrix
    """
    identity = []
    for i in xrange(0,r):
        row = []
        for j in xrange(0,c):
            elem = 0
            if i==j:
                elem = 1
            row.append(elem)
        identity.append(row)
    return identity

#https://stackoverflow.com/questions/32669855/dot-product-of-two-lists-in-python
def dot(K, L):
   if len(K) != len(L):
      return 0

   return sum(i[0] * i[1] for i in zip(K, L))

def mult(matrix, vector):
    a = [0 for n in range(len(vector))]
    for n in range(len(vector)):
        a[n] = dot(matrix[n], vector)
    return a
