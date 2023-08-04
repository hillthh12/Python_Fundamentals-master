# 1. basic

for i in range(0, 151):
    print(i)

# 2. multiples of five

for e in range(5, 1001, 5):
    print(e)

# 3. counting, the dojo way

def CodingDojo(n):
    return 'coding dojo' if not (i % 10)
        else
            'coding' if not i % 5 else
                i for i in range(1, 101)

    print(CodingDojo(0))

# 4. whoa. that sucker's huge

dojo_sum = 0

for x in range(1, 500000, 2):
    dojo_sum = dojo_sum + x
    
print(f'the sum of the odd numbers {dojo_sum}')

# 5. countdown by fours

for y in range(2018, 0, -4):
    print(y)

# 6. Flexible Counter

lowNum=2
highNum=100
mult=3
for x in range(lowNum, highNum+1):
    if(x % mult==0):
        print(x)
        