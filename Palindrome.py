import sys

with open(sys.argv[1]) as f:
    string = f.readline().strip()

n = len(string)
table = [[None for a in range(n)] for b in range(n)]
for i in range(n):
    table[i][i] = (1, string[i])


for d in range(1, n):
    for i in range(n-d):
        j = i + d
        substring = string[i:j+1]
        if substring[0] == substring[-1]:
            if table[i+1][j-1] is not None:
                table[i][j] = (2 + (table[i+1][j-1])[0], substring[0] + (table[i+1][j-1])[1] + substring[0])
            else:
                table[i][j] = (2, substring[0] + substring[0])
        else:
            table[i][j] = max(table[i][j-1], table[i+1][j])

print('Length:', table[0][n-1][0])
print('Sequence:', table[0][n-1][1])
