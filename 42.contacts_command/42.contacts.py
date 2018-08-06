import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name #se pone "_" para que las variables de instancia sean privadas
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self._contacts = [] #guarda variable privada que inicializa como una lista

    def add(self, name, phone, email): #método
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
            for idx, contact in enumerate(self._contacts):
                if contact.name.lower() == name.lower():
                    del self._contacts[idx]
                    self._save()
                    break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('*******')
        print('¡No encontrado!')
        print('*******')

    def update(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                contact.name = input('Escribe el nombre del contacto: ')
                contact.phone = input('Escribe el tel de contacto: ')
                contact.email = input('Escribe el email del contacto: ')
                print('*******')
                print('Usuario actualizado')
                print('*******')
                self._save()
                self.search(contact.name)
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

def run():
    contact_book = ContactBook() #instancia que inicializa la clase

    with open('contacts.csv', 'rt') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            if row == []:
                continue
                
            contact_book.add(row[0], row[1], row[2])

    while True:
        command = input('''
        ¿Que deseas hacer?

        [a]ñadir contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]alir

        ''')

        if command == 'a':
            name = input('Escribe el nombre del contacto: ')
            phone = input('Escribe el tel de contacto: ')
            email = input('Escribe el email del contacto: ')

            contact_book.add(name, phone, email) #agregamos métodos sobre el objeto
        elif command == 'ac':
            name = input('Escribe el nombre del contacto: ')
            contact_book.update(name)

        elif command == 'b':
            name = input('Escribe el nombre del contacto: ')
            contact_book.search(name)

        elif command == 'e':
            name = input('Escribe el nombre del contacto: ')
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__=='__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()
