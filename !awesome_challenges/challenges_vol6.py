t = int(input())  # Number of test cases.
# Loop for all testcases.
for _ in range(t):
    length = int(input())
    segments = input()
    sour, sweet, final = (0 for i in range(3))
    for segment in segments:
        if segment == '0':
            if sweet > 0:
                final += 1
            # Reset sweet segment
            sweet = 0
        else:
            sweet += 1
    if sweet > sour:
        print(length - sour)
# --------------------------------------------
while True:
    t = int(input())  # Number of test cases.
    n, c = (int(x) for x in input().split())  # Number of stalls and cows.
    xn = []
    for stall in range(n):
        xi = int(input())  # Stall location.
        xn.append(xi)
    xn.sort(reverse=True)
    print(xn[0] - xn[n - c])
# ------------------------------------------
def getPairsCount(sum_):
    count = 0  # Initialize result
    sums = []

    # Consider all possible pairs
    # and check their sums

    for i in range(1000):
        i = str(i).zfill(3)
        if i[0] == '0':
            i = i[1] + i[2]
        i = int(i)
        if i < sum_:
            i = str(i)
            if len(i) == 2:
                j = i[0]
                j, i = int(j), int(i)
                count = check_sum(i, j, sum_, count, sums)
                i = str(i)
                j = i[1]
                j, i = int(j), int(i)
                count = check_sum(i, j, sum_, count, sums)
            elif len(i) == 3:
                j = i[0] + i[1]
                count = check_sum(i, j, sum_, count, sums)
                i = str(i)
                j = i[0] + i[2]
                count = check_sum(i, j, sum_, count, sums)
                i = str(i)
                j = i[1] + i[2]
                count = check_sum(i, j, sum_, count, sums)
    return count, sums


def check_sum(i_, j_, sum_to_check, count_, sums):
    j_, i_ = int(j_), int(i_)
    if j_ + i_ == sum_to_check:
        count_ += 1
        sums.append(str(i_) + ' + ' + str(j_) + ' = ' + str(sum_to_check))
    return count_


# Driver function
for n in range(int(input())):
    suma = int(input())
    output = getPairsCount(suma)
    print(output[0])
    for out in output[1]:
        print(out)
# ----------------------------------------------
columns = int(input())
if columns == 0:
    break
encripted = list(input())
array = []
message = ''
bin_ = 0
while encripted:
    row = []
    for column in range(columns):
        row.append(encripted.pop(0))
    if bin_ == 1:
        row.reverse()
        bin_ = 0
    else:
        bin_ = 1
    array.append(row)
for column in range(len(array[0])):
    for row in range(len(array)):
        message += array[row][column]
print(message)
