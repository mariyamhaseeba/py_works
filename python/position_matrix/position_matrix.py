arr=[
    [2,0,1],
    [1,1,0],
    [2,0,3]
]
for row in range(0,3):
    for col in range(0,3):
        value=col+row-arr[row][col]
        print(value,end="\t")
    print()