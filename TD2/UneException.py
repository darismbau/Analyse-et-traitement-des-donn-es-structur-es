#Exercice 1 : une exception
def diviser1(a, b):
    c = a / b
    return c

if __name__ =='__main__':
    a = float(input("saisir a:"))
    b = float(input ("saisir b: "))
    c = diviser1(a, b)
    print(f'{a} / {b} = {c}')



#Avec try-except
def diviser1(a, b):
    c = a / b
    return c

if __name__ =='__main__':
    try:
        a = float(input("saisir a:"))
        b = float(input ("saisir b: "))
        c = diviser1(a, b)
        print(f'{a} / {b} = {c}')
    except:
        print('erreur de saisie')


#Pour remedier à l'erreur "ZERODivisionError"
#On a plus tendance à le resoudre dans def. Mais toutefois ça depend de notre vision de chose.
#Dans ce cas, on l'a resolu dans IF
def diviser1(a, b):
    c = a / b
    return c

if __name__ =='__main__':
    a = float(input("saisir a:"))
    b = float(input ("saisir b: "))
    if b != 0:  #On utilise plutôt un IF, c'est plus court. pas besoin d'utiliser les excptions.
        c = diviser1(a, b)
        print(f'{a} / {b} = {c}')
    else:
        print("pas de res")

#Value error, voici un vrai traitement de l'exception !
def diviser1(a, b):
    c = a / b
    return c

if __name__ =='__main__':
    try :
        a = float(input("saisir a:"))
        b = float(input ("saisir b: "))
    except ValueError as e:  # e L'objet de l'excpetion qu'on recupere /
        print(f'Mauvaise saisie')
    else:
        c = diviser1(a, b)
        print(f'{a} / {b} = {c}')

 # Differentes possibilités

def diviser1(a, b):
    c = a / b
    return c

if __name__ =='__main__':
    try:
        a = float(input("saisir a:"))
        b = float(input ("saisir b: "))
    except ValueError as e:
        print(f'Mauvaise saisie {e}')
    except TypeError as e:
        print(f'Impossible de convertir  {e}')

    else:
        try:
            c = diviser1(a, b)
        except ZeroDivisionError:
            print("Division impossible")
        else:
            print(f'{a} / {b} = {c}')
    finally : #Dans ce code là que j'aie une exception ou pas, ce code executera le finally !
        print("Enfin la fin")

#Exo cette fois-ci avec la boule WHILE, Tant que
def diviser1(a, b):
    c = a / b
    return c

if __name__ =='__main__':
    divisionsestbienpasse = False
    while not divisionsestbienpasse:
        try:
            a = float(input("saisir a:"))
            b = float(input("saisir b: "))
        except ValueError as e:
            print(f'Mauvaise saisie {e}')
        except TypeError as e:
            print(f'Impossible de convertir  {e}')

        else:
            try:
                c = diviser1(a, b)
            except ZeroDivisionError:
                print("Division impossible")
            else:
                print(f'{a} / {b} = {c}')
        finally:  # Dans ce code là que j'aie une exception ou pas, ce code executera le finally !
            print("Enfin la fin")

































