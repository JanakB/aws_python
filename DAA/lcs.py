import time

def lcs_length(X, Y):
    # LCS algorithm
    m = len(X)
    n = len(Y)
    # Initialize the LCS table
    L = [[0] * (n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    return L[m][n]

# Test the time complexity of LCS
X = "AGGTAB"
Y = "GXTXAYB"

start = time.time()
lcs_length(X, Y)
end = time.time()
print("LCS time:", end - start, "seconds")