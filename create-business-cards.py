class BaseContact: # Definicja klasy podstawowej BaseContact 
    def __init__(self, imie, nazwisko, telefon_prywatny, adres_email):
       self.imie = imie
       self.nazwisko = nazwisko
       self.telefon_prywatny = telefon_prywatny
       self.adres_email = adres_email
       
       #variables 
       self._len_imin = len(imie)+ len(nazwisko)+1

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.telefon_prywatny} {self.adres_email}'
    def contact(self):    
        return f'Wybieram number {self.telefon_prywatny} i dzwonię do {self.imie} {self.nazwisko}'
    
    @property
    def len_imin(self):
        return self._len_imin

class BusinessContact(BaseContact): # Definicja klasy rozszeżającej klasę podstawową BaseContact o atrybuty służbowe
    def __init__(self,nazwa_firmy, stanowisko,telefon_sluzbowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko
        self.telefon_sluzbowy = telefon_sluzbowy
    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.adres_email} {self.nazwa_firmy} {self.stanowisko} {self.telefon_sluzbowy}'
    def contact(self):    
        return f'Wybieram number {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}'    

### Tworzę funkcje create BaseContact i BusinessContact

from faker import Faker
fake = Faker()

def create_contacts(conType,number):
    """
    Creates a certain number of business cards of a passed type "conType" and assigns them to a list name_list[]
    Arguments:
    conType = [BaseContact,BusinessContact]
    number = integer
    """
    name_list =[]
    print();print("Wybrałeś typ = ", conType);print("Liczba wizytówek stworzona =", number); print()
    if conType == BaseContact:    
        for i in range(number):
            faker_p = BaseContact(imie = fake.first_name(), nazwisko =fake.last_name(), telefon_prywatny=fake.phone_number(), adres_email= fake.email())
            name_list.append(faker_p) #print("Typ =", conType, i)
            print(name_list[i])
        print()
    elif conType == BusinessContact:    
        for i in range(number):
            faker_p = BusinessContact(imie = fake.first_name(), nazwisko =fake.last_name(), telefon_prywatny=fake.phone_number(), adres_email= fake.email(), nazwa_firmy = fake.company(), stanowisko = fake.job(), telefon_sluzbowy = fake.phone_number())
            name_list.append(faker_p) #print("Typ =", conType, i)
            print(name_list[i])
        print()
    else:
        print("Wybierz właściwy typ kontaktu (BaseContact lub BusinessContact")

create_contacts(BaseContact,3)
create_contacts(BusinessContact,3)

