def main():
    num = get_num() 
    meow(num)

def get_num():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    return n

    
def meow(n):
    for _ in range(n):
        print("meow")


main()