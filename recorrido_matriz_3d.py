cubo = [[[1,2],[3,4]], [[5,6],[7,8]]]
for i in range(len(cubo)):
    for j in range(len(cubo[i])):
        for k in range(len(cubo[i][j])):
            print(f"cubo[{i}][{j}][{k}] = {cubo[i][j][k]}")