#Gerekli Kitaplıkları İçe Aktarma
import csv
import datetime


with open("Menu.txt", "w") as menu_file:
    menu_file.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: TürkPizza\n4: Sade Pizza\n* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n* Teşekkür ederiz!")

# Üst sınıf oluştur “pizza”
class Pizza:
    def __init__(self):
        self.description = "Pizza"
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return 0


class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza"
    
    def get_cost(self):
        return 50


class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita Pizza"
    
    def get_cost(self):
        return 60


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Türk Pizza"
    
    def get_cost(self):
        return 70


class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Sade Pizza"
    
    def get_cost(self):
        return 45

# Üst sınıf oluştur “Decorator”
class Decorator(Pizza):
    def __init__(self, component):
        super().__init__()
        self.component = component
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
        return self.component.get_description() + " "  + Pizza.get_description(self)


class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Zeytin Soslu"

    def get_cost(self):
        return self.component.get_cost() + 8


class Mantarlar(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mantarlı Soslu"

    def get_cost(self):
        return self.component.get_cost() + 15


class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Keçi Peynirli Soslu"

    def get_cost(self):
        return self.component.get_cost() + 12


class Et(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Etli Soslu"

    def get_cost(self):
        return self.component.get_cost() + 20


class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Soğanlı Soslu"

    def get_cost(self):
        return self.component.get_cost() + 8


class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mısır Soslu"

    def get_cost(self):
        return self.component.get_cost() + 7

# Main fonksiyon oluşturma kısmı 
def main():
    # Menüyü okuma modunda açma
    with open("Menu.txt", "r") as menu:
        print(menu)


if __name__ == '__main__':
    pizza = None
    # if else ile yakalama kısımları
    while not pizza:
        try:
            base_choice = int(input(
                "Lütfen bir pizza tabanı seçiniz: (1-Klasik, 2-Margarita, 3-TürkPizza, 4-Sade Pizza) "))
            if base_choice == 1:
                pizza = KlasikPizza()
            elif base_choice == 2:
                pizza = MargaritaPizza()
            elif base_choice == 3:
                pizza = TurkPizza()
            elif base_choice == 4:
                pizza = SadePizza()
            else:
                print("Bu rakamın karşılığı yoktur 1 ile 4 arasında giriniz.")
        except ValueError:
            print("Bu rakamın karşılığı yoktur 1 ile 4 arasında giriniz.")

    while True:
        try:
            sos_choice = int(input(
                "Lütfen bir sos seçiniz: (11-Zeytin, 12-Mantarlar, 13-Keçi Peyniri, 14-Et, 15-Soğan, 16-Mısır) "))
            if sos_choice == 11:
                pizza = Zeytin(pizza)
            elif sos_choice == 12:
                pizza = Mantarlar(pizza)
            elif sos_choice == 13:
                pizza = KeciPeyniri(pizza)
            elif sos_choice == 14:
                pizza = Et(pizza)
            elif sos_choice == 15:
                pizza = Sogan(pizza)
            elif sos_choice == 16:
                pizza = Misir(pizza)
            else:
                print("Bu rakamın karşılığı yoktur 11 ile 16 arasında giriniz.")
            break
        except ValueError:
            print("Bu rakamın karşılığı yoktur 11 ile 16 arasında giriniz.")

    aciklama = input("Açıklama: ")
      # Siprariş Bilgileri yazdırma
    order_time = datetime.datetime.now()
    
    print("------------------------")
    print("Siparişiniz tamamlandı!")
    print("Sipariş tarihi:", order_time.strftime("%d-%m-%Y %H:%M"))
    print("Sipariş bilgisi:", pizza.get_description())
    print("Toplam fiyat:", pizza.get_cost(), "TL")
    print("Sipariş Açıklaması: ", aciklama)
    print("------------------------")
    print()
    # Ödeme Ekranı
    print("------ÖDEME ALANI------")
    name = input("İsim: ")
    tc_no = input("TC Kimlik Numarası: ")
    while len(tc_no) != 11:
        print("TC Kimlik Numarası geçersiz!")
        tc_no = input("TC Kimlik Numarası: ")
    cc_no = input("Kredi Kartı Numarası: ")
    cc_password = input("Kredi Kartı Şifresi: ")
    while len(cc_password) != 4:
        print("Kredi kartı geçersiz şifresi! Lütfen 4 haneli şifre giriniz!")
        cc_password = input("Kredi Kartı Şifresi: ")
    print("------------------------")
    print()
    print("Merhaba " + name + " siparişiniz oluşturulmuştur. ")
    print()

# Siparişleri Database'e ekleme
    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, tc_no, cc_no, pizza.get_description(), order_time.strftime("%d-%m-%Y %H:%M"), cc_password])