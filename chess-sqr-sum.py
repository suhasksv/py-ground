d=1
curr=1
# https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem
for i in range(2, 65):
    curr = curr*2
    d = d + curr
    print (i ,curr)

'''
18,446,744,073,709,551,615
'''
# dd


print("The sum is :",d)
