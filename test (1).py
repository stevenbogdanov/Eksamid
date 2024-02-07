class Kalkulaator: 
    def __init__(self, a, b):  # Defineerib meetodi __init__, mis võtab kaks argumendiks a ja b ning määrab need klassi atribuutideks
        self.a = a  # Määrab esimese argumendi klassi atribuudiks a
        self.b = b  # Määrab teise argumendi klassi atribuudiks b

    def liitmine(self):  # Defineerime meetodi liitmine, mis liidab a ja b
        return self.a + self.b

    def lahutamine(self):  # Defineerib meetodi lahutamine, mis lahutab b a-st
        return self.a - self.b

    def korrutamine(self):  # Defineerib meetodi korrutamine, mis korrutab a ja b
        return self.a * self.b

    def jagamine(self):  # Defineerib meetodi jagamine, mis jagab a ja b
        if self.b != 0:  # Kontrollib nulliga jagamise vältimiseks
            return self.a / self.b
        else:
            return "Viga: Nulliga jagamine!"  # Tagastab veateate, kui jagaja on null

    def jaak(self):  # Defineerib meetodi jaak, mis leiab a jagatise b jäägi
        return self.a % self.b

    def astendamine(self):  # Defineerib meetodi astendamine, mis astendab a b-ni
        return self.a ** self.b

    def ruutjuur(self):  # Defineerib meetodi ruutjuur, mis leiab a ruutjuure
        return self.a ** 0.5

    def absoluutväärtus(self):  # Defineerib meetodi absoluutväärtus, mis leiab a ja b absoluutväärtused
        return abs(self.a), abs(self.b)

    def eksponentsiaal(self):  # Defineerib meetodi eksponentsiaal, mis leiab a ja b eksponentsiaalid
        return self.a ** self.a, self.b ** self.b

    def kuup(self):  # Defineerib meetodi kuup, mis leiab a ja b kuubid
        return self.a ** 3, self.b ** 3


def menüü():  # Defineerime funktsiooni menüü, mis prindib välja kalkulaatori kasutusmenüü
    valikud = ('1. Liitmine\n2. Lahutamine\n3. Korrutamine\n4. Jagamine\n5. Jäägi leidmine\n6. Astendamine\n7. Ruutjuure leidmine\n8. Absoluutväärtus\n9. Eksponentsiaal\n10. Kuup\n0. Välju')
    print(valikud)


a = int(input("Sisesta esimene number: ")) 
b = int(input("Sisesta teine number: ")) 

kalkulaator = Kalkulaator(a, b)

while True:
    menüü()

    valik = int(input('Sisesta oma valik: '))  # Küsib kasutajalt valiku ning muudab selle täisarvuks

    if valik == 1:  # Kui kasutaja valik on 1
        print("Tulemus: ", kalkulaator.liitmine())  # Prindib välja liitmise tulemuse
    elif valik == 2:  # Kui kasutaja valik on 2
        print("Tulemus: ", kalkulaator.lahutamine())  # Prindib välja lahutamise tulemuse
    elif valik == 3:  # Kui kasutaja valik on 3
        print("Tulemus: ", kalkulaator.korrutamine())  # Prindib välja korrutamise tulemuse
    elif valik == 4:  # Kui kasutaja valik on 4
        print("Tulemus: ", kalkulaator.jagamine())  # Prindib välja jagamise tulemuse
    elif valik == 5:  # Kui kasutaja valik on 5
        print("Tulemus: ", kalkulaator.jaak())  # Prindib välja jäägi leidmise tulemuse
    elif valik == 6:  # Kui kasutaja valik on 6
        print("Tulemus: ", kalkulaator.astendamine())  # Prindib välja astendamise tulemuse
    elif valik == 7:  # Kui kasutaja valik on 7
        print("Tulemus: ", kalkulaator.ruutjuur()) # Prindib välja ruutjuure tulemuse
    elif valik == 8: # Kui kasutaja valik on 8
        print("Absoluutväärtus: ", kalkulaator.absoluutväärtus()) # Prindib välja absoluutväärtuse tulemuse
    elif valik == 9: # Kui kasutaja valik on 9
        print("Eksponentsiaal: ", kalkulaator.eksponentsiaal()) # Prindib välja ekspontsiaali tulemuse
    elif valik == 10: # Kui kasutaja valik on 10
        print("Kuup: ", kalkulaator.kuup()) # Prindib välja kuubi tulemuse
    elif valik == 0: # Kui kasutaja valik on 0
        print('Kalkulaatori sulgemine.') # Prindib välja "Kalkulaatori sulgemine"
        break
    else:
        print('Vigane valik. Palun vali menüüst.')
