# from https://www.tryexponent.com/courses/ml-engineer/ml-coding/implement-2d-convolutional-filter

def conv2d(data, kernel):
    rows, cols = len(data), len(data[0])
    k = len(kernel)

    res = [] 
    for i in range(rows - k + 1):
        row_val = []
        for j in range(cols - k + 1):
            val = 0

            for p in range(k):
                for q in range(k):
                    val += data[i+p][j+q] * kernel[p][q]
            row_val.append(val)
        res.append(row_val[::])

    return res

assert conv2d([[1, -1, 0],[-3, 0, 2],[8, 9, 1]], [[1, -1],[-1, 1]]) == [[5,1],[-2,-10]]

