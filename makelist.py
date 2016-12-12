#opens a new file
file = open('file.txt', 'w')
n = 1
#define n as one, runs the process while n is less than 10
while n <= 10:
    file.write(str(n) + '. ' + input('write something') + '\n')
    n += 1
#closes the file
file.close()
