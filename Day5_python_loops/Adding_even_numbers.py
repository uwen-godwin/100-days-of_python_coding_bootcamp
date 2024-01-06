# A program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

target = int(input())

even_num = 0
for number in range(0, target + 1, 2):
    even_num += number
    print(even_num)
