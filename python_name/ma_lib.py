


def coucou():
    print("Bonjour, je suis la librairie !")
    print('__name__ = ', __name__)



def main():
    print('Appel de ma lib en direct')
    coucou()

if __name__ == "__main__":
    main()