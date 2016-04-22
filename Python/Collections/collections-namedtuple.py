# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

n = int(raw_input()) # n is the number of students
columns = raw_input().split()
Student = namedtuple('Student', columns)

sum = 0
for i in range(n):
    student_i = Student(*raw_input().split())
    sum += float(student_i.MARKS)

avg = sum/n
print "%.2f" %  avg