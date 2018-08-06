def protected(func): #Funcion A
    def wrapper(password): #Funcin C
        if password == 'orozco':
            return func() #Funcion B
        else:
            print('Wrong Password')

    return wrapper

@protected #decorador que se pone antes de la funcion que se ejecuta si se cumple def protected()
def protected_func(): #Funcion B
    print('Right Password')

if __name__=='__main__':
    password = input('Write your Password: ')

    protected_func(password)
