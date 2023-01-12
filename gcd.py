#Collins Wanga

#Program to compute GCD
def main():
    x = int(input('Input the first integer: '))
    y = int(input('Input the second integer: '))
    print('The GCD of ',x,' and ',y,' is ',)
    while y!= 0:
        x_prime = y
        y_prime = x % y
        x = x_prime
        y = y_prime
    print(x)
main()
