# don't try this at home!
n_files = 100000000
files = []

for i in range(n_files):
    files.append(open('killmac.txt'))

# OSError: [Errno 24] Too many open files