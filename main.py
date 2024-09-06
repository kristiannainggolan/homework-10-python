from fibonacci import doFibonacci

def main():
    number = int(input("Input the the number: "))
    result = doFibonacci(number)
    print(f"The Fibonacci sequence is :  {result}" )



if __name__ == "__main__":
    main()