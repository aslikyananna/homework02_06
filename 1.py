Mat = [[0, "M", 0, "M", 0],
       [0, 0, "M", 0, 0],
       [0, 0, 0, 0, 0],
       ["M", "M", 0, 0, 0],
       [0, 0, 0, "M", 0]]
Mat_new = [[0, 0, 0, 0, 0]] + Mat + [[0, 0, 0, 0, 0]]
for i in range(len(Mat_new)):
    Mat_new[i].append(0)
for i in range(len(Mat_new)):
    Mat_new[i].insert(0, 0)
Mat_new = sum(Mat_new, [])
for i in range(len(Mat_new)-1):
    if Mat_new[i] != "M" and Mat_new[i+1] == "M":
        Mat_new[i] += 1
for i in range(len(Mat_new)-6):
    if Mat_new[i] != "M" and Mat_new[i+6] == "M":
        Mat_new[i] += 1
for i in range(len(Mat_new)-7):
    if Mat_new[i] != "M" and Mat_new[i+7] == "M":
        Mat_new[i] += 1
for i in range(len(Mat_new)-8):
    if Mat_new[i] != "M" and Mat_new[i+8] == "M":
        Mat_new[i] += 1
for i in range(len(Mat_new)):
    if Mat_new[i] != "M" and Mat_new[i-1] == "M":
        Mat_new[i] += 1
    if Mat_new[i] != "M" and Mat_new[i-6] == "M":
        Mat_new[i] += 1
    if Mat_new[i] != "M" and Mat_new[i-7] == "M":
        Mat_new[i] += 1
    if Mat_new[i] != "M" and Mat_new[i-8] == "M":
        Mat_new[i] += 1
new_matrix = [Mat_new[i:i+7] for i in range(0, 49, 7)]
del new_matrix[0]
del new_matrix[-1]
for i in range(len(new_matrix)):
    new_matrix[i].pop(0)
    new_matrix[i].pop(-1)
for i in new_matrix:
    print(i)




