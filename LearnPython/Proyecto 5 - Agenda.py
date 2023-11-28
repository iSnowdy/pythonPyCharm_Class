# Proyecto Final - Agenda


class Adress:

    def __init__(self):

        self._Street = ''
        self._Flat = ''
        self._City = ''
        self._PostCode = ''

    def GetStreet(self):

        return self._Street

    def GetFlat(self):

        return self._Flat

    def GetCity(self):

        return self._City

    def GetPostCode(self):

        return self._PostCode

    def SetStreet(self, street):

        self._Street = street

    def SetFlat(self, flat):

        self._Flat = flat

    def SetCity(self, city):

        self._City = city

    def SetPostCode(self, postcode):

        self._PostCode = postcode


class Person:

    def __init__(self):

        self._Name = ''
        self._Surname = ''
        self._DateofBirth = ''

    def GetName(self):

        return self._Name

    def GetSurname(self):

        return self._Surname

    def GetDateofBirth(self):

        return self._DateofBirth

    def SetName(self, name):

        self._Name = name

    def SetSurname(self, surname):

        self._Surname = surname

    def SetDateofBirth(self, dateofbirth):

        self._DateofBirth = dateofbirth


class Phone:

    def __init__(self):

        self._LandLine = ''
        self._MobilePhone = ''
        self._WorkPhone = ''

    def GetLandLine(self):

        return self._LandLine

    def GetMobilePhone(self):

        return self._MobilePhone

    def GetWorkPhone(self):

        return self._WorkPhone

    def SetLandLine(self, landline):

        self._LandLine = landline

    def SetMobilePhone(self, mobilephone):

        self._MobilePhone = mobilephone

    def SetWorkPhone(self, workphone):

        self._WorkPhone = workphone


class Contact(Adress, Person, Phone):

    def __init__(self):

        self._Email = ''

    def GetEmail(self):

        return self._Email

    def SetEmail(self, email):

        self._Email = email

    def ShowContactInfo(self):

        print('--------------------\n')
        print('Contact Information')
        print('\tName: ', self.GetName())
        print('\tSurname(s): ', self.GetSurname())
        print('\tDate of Birth: ', self.GetDateofBirth())
        print('\tLandline: ', self.GetLandLine())
        print('\tMobile Phone: ', self.GetMobilePhone())
        print('\tWork Phone: ', self.GetWorkPhone())
        print('\tEmail: ', self._Email,'\n')
        print('Adress Information\n')
        print('\tStreet: ', self.GetStreet())
        print('\tFlat: ', self.GetFlat())
        print('\tCity: ', self.GetFlat())
        print('\tPostCode: ', self.GetPostCode(),'\n')
        print('--------------------')


class PhoneBook:

    def __init__(self, path):

        self._Contacts = [] # Creamos la lista de contactos
        self._Path = path

    def LoadContacts(self):

        try:
            file = open(self._Path, 'r')
        except:
            print('Fatal Error. This file does not exist')
        else:
            contacts = file.readline()
            file.close()
            if len(contacts) > 0:
                for contact in contacts:
                    data = contact.split('###')
                    if len(data) == 11: # 11 tipos de datos de información (nombre, apellido, etc)
                        newcontact = Contact()
                        newcontact.SetName(data[0])
                        newcontact.SetSurname((data[1]))
                        newcontact.SetDateofBirth((data[2]))
                        newcontact.SetLandLine((data[3]))
                        newcontact.SetMobilePhone((data[4]))
                        newcontact.SetWorkPhone((data[5]))
                        newcontact.SetEmail((data[6]))
                        newcontact.SetStreet((data[7]))
                        newcontact.SetFlat((data[8]))
                        newcontact.SetCity((data[9]))
                        newcontact.SetPostCode((data[10]))

                        self._Contacts = self._Contacts + [newcontact] # Añadimos toda la información previa a la lista

                print('A total of ', len(self._Contacts), ' contacts have been loaded')

    def CreateaNewContact(self, newcontact):

        self._Contacts = self._Contacts + [newcontact]

    def SaveContact(self):

        try:
            file = open(self._Path, 'w')
        except:
            print('Information could not be saved')
        else:
            for contact in self._Contacts:
                text = contact.GetName() + '   '
                text = text + contact.GetSurname() + '   '
                text = text + contact.GetDateofBirth() + '   '
                text = text + contact.GetLandLine() + '   '
                text = text + contact.GetMobilePhone() + '   '
                text = text + contact.GetWorkPhone() + '   '
                text = text + contact.GetEmail() + '   '
                text = text + contact.GetStreet() + '   '
                text = text + contact.GetFlat() + '   '
                text = text + contact.GetCity() + '   '
                text = text + contact.GetPostCode() + '   '

                file.write(text)

            file.close()

    def ShowPhoneBook(self):

        print('--------------------\n')
        print('Number of contacts: ', len(self._Contacts))
        for contacto in self._Contacts:
            contacto.ShowContactInfo()
        print('--------------------\n')

    def SearchContactbyName(self, name):

        found = []

        for contact in self._Contacts:

            if contact.GetName() == name:
                found = found + [contact]

        return found

    def SearchContactbyPhone(self, phone):

        found = []

        for contact in self._Contacts:

            if contact.GetLandLine() == phone or contact.GetMobilePhone() == phone or contact.GetWorkPhone() == phone:
                found = found + [contact]

        return found

    def DeleteContactbyName(self, name):

        found_d = []

        for contact in self._Contacts:

            if contact.GetName() != name: # Almacenamos la cantidad de contactos que no coinciden
                found_d = found_d + [contact]
        print('A total of ', len(self._Contacts) - len(found_d), 'contacts have been deleted')
        self._Contacts = found_d
        # Re-introducimos los datos que no son los que se han encontrado; pues son los que queremos guardar

    def DeleteContactbyPhone(self, phone):

        found_d = []

        for contact in self._Contacts:

            if contact.GetLandLine() == phone or contact.GetMobilePhone() == phone or contact.GetWorkPhone() == phone:
                found_d = [contact]
                print('A total of', len(found_d), 'contacts have been removed')
                self._Contacts.remove(contact)


def Options(text):

    loop = False

    while not loop:

        try:
            choice = int(input(text))
        except ValueError:
            print('It has to be a number from 1 - 6')
        else:
            loop = True

    return choice

def ShowMenu():

    asteriscos = '************'
    print(asteriscos)
    print('Phone Book Menu')
    print(asteriscos)

    print('Menu\n'
          '1) Show contacts\n'
          '2) Search contacts\n'
          '3) Create a new contact\n'
          '4) Delete a contact\n'
          '5) Save contacts\n'
          '6) Exit\n'
          )


def SearchContacts(phonebook):

    print('Searching contacts by...\n'
          '1) Name\n'
          '2) Phone\n'
          '3) Back\n')

    endSearch = False

    while not endSearch:

        choice_search = Options('Insert a number from 1 to 3: ')

        if choice_search == 1:

            founds = phonebook.SearchContactbyName(str(input('Insert the name you would like to search: ')))

            if len(founds) > 0:
                print('-------------------- Contacts found --------------------\n')
                for contact in founds:
                    contact.ShowContactInfo()
                print('------------------------------------------------------------\n')

            else:
                print('No information found')

            endSearch = True

        elif choice_search == 2:

            founds = phonebook.SearchContactbyPhone(str(input('Insert the landline/phone/work number of the person: ')))

            if len(founds) > 0:
                print('-------------------- Contacts found --------------------\n')
                for contact in founds:
                    contact.ShowContactInfo()
                print('------------------------------------------------------------\n')

            else:
                print('No information found')

            endSearch = True

        elif choice_search == 3:

            endSearch = True


def CreatenewContact(phonebook):

    newcontact = Contact()

    newcontact.SetName(str(input('Insert the name: ')))
    newcontact.SetSurname(str(input('Insert the surname(s): ')))
    newcontact.SetDateofBirth(str(input('Insert the date of birth: ')))
    newcontact.SetLandLine(str(input('Insert the landline phone number: ')))
    newcontact.SetMobilePhone(str(input('Insert the phone number: ')))
    newcontact.SetWorkPhone(str(input('Insert the work phone number: ')))
    newcontact.SetEmail(str(input('Insert the email: ')))
    newcontact.SetStreet(str(input('Insert the street: ')))
    newcontact.SetFlat(str(input('Insert the flat number: ')))
    newcontact.SetCity(str(input('Insert the city\'s name: ')))
    newcontact.SetPostCode(str(input('Insert the post code: ')))

    phonebook.CreateaNewContact(newcontact)


def DeleteaContact(phonebook):

    print('Search the contact you would like to delete by...\n'
          '1) Name\n'
          '2) Phone\n'
          '3) Back\n')

    endSearch = False

    while not endSearch:

        choice_search = Options('Insert a number from 1 to 3: ')

        if choice_search == 1:

            phonebook.DeleteContactbyName(str(input('Insert the contact\'s name you wish to delete: ')))
            endSearch = True

        elif choice_search == 2:

            phonebook.DeleteContactbyPhone(str(input('Insert the contact\'s phone that you wish to delete: ')))
            endSearch = True

        elif choice_search == 3:

            endSearch = True


def Main():

    phonebook = PhoneBook('phonebook.txt')
    phonebook.LoadContacts()

    end = False

    while not end:

        ShowMenu()
        choice = Options('What would you like to do? ')

        if choice == 1:

            phonebook.ShowPhoneBook()

        if choice == 2:

            SearchContacts(phonebook)

        if choice == 3:

            CreatenewContact(phonebook)

        if choice == 4:

            DeleteaContact(phonebook)

        if choice == 5:

            phonebook.SaveContact()

        if choice == 6:

            end = True

Main()