n = int(input('Enter n '))
def eratosfen(n):
    line = list(range(2,n+1))
    for i in line:
        line = list(filter(lambda x: x == i or x % i != 0, line))
        if i**2 > n:
            break
    return line
def test_eratosfen(q):
    if q == [2,3,5,7]:
        print('Function works correctly')

print('Prime numbers is ', eratosfen(n))
test_eratosfen(eratosfen(10))