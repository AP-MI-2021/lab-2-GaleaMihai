def is_prime(n):
    '''
    Verifica daca un numar e prim
    :param n:
    :return: true or false
    '''
    ePrim = 1
    if n == 1 or n == 0:
        return False

    for i in range(2, n//2+1):
        if n % i == 0:
            ePrim = 0
            return False

    if ePrim:
        return True

def get_goldbach(n):
    '''
    Returneaza numarul prim mai mic care poate apartine sumei cerute
    :param n:
    :return:
    '''
    i = 2
    var = True
    while var:
        if is_prime(i):
            j = n-i
            if is_prime(j):
                var = False
        i = i+1
    if i > n:
        return 0
    return i-1

def test_get_goldbach():
    assert get_goldbach(10) == 3
    assert get_goldbach(24) == 5
    assert get_goldbach(30) == 7


def invers(n):
    '''
    Returneaza inversul unui numar
    :param n:
    :return:
    '''
    inv = 0  # type: int
    while n > 0:
        inv = inv*10 + n % 10
        n = n//10
    return inv

def is_palindrome(n):
    '''
    Verifica daca un numar este palindrom.
    :param n:
    :return:
    '''
    if n == invers(n):
        return True
    else:
        return False

def test_is_palindrom():
    assert is_palindrome(12321) == True
    assert is_palindrome(1232) == False
    assert is_palindrome(10) == False

def is_superprime(n):
    '''
    Verifica daca un numar este super prim.
    :param n:
    :return:
    '''
    while is_prime(n):
        n = n // 10
    if n == 0:
        return True
    else:
        return False

def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(237) == False
    assert is_superprime(11) == False

def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(float(x))
    return l

def printMenu():
    print("3.Problema 3:")
    print("4.Problema 5:")
    print("5.Problema 6:")
    print("x.Exit.")

def main():
    test_get_goldbach()
    test_is_palindrom()
    test_is_superprime()
    while True:
        printMenu()
        optiune = input("Optiunea: ")
        if optiune == "3":
            n = int(input("n = "))
            if get_goldbach(n) != 0:
                print(get_goldbach(n))
                print("si")
                print(n-get_goldbach(n))
            else:
                print("Nu se poate")
        elif optiune == "5":
            n = int(input("n = "))
            if is_palindrome(n):
                print("Este")
            else:
                print("Nu este")
        elif optiune == "6":
            n = int(input("n = "))
            if is_superprime(n):
                print("Este")
            else:
                print("Nu este")
        elif optiune == "x":
            break

if __name__ == '__main__':
    main()