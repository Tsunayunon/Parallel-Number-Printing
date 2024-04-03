# threading ve time modüllerini içe aktarıyoruz.
import threading
import time

# 0'dan 19'a kadar olan sayıları yazdıran bir fonksiyon tanımlıyoruz.
def print_numbers():
    for i in range(20):  # 0'dan 19'a kadar döngü oluşturur.
        time.sleep(1)  # Her sayı arasında 1 saniye bekler.
        print(i)  # Sayıyı ekrana yazdırır.

# İki ayrı thread oluşturuyoruz, her ikisi de 'print_numbers' fonksiyonunu hedef alıyor.
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Oluşturulan her iki thread'i de başlatıyoruz.
thread1.start()
thread2.start()

# Her iki thread'in de tamamlanmasını bekliyoruz.
# Bu, 'print_numbers' fonksiyonunun her iki thread için de tamamlanana kadar programın devam etmemesini sağlar.
thread1.join()
thread2.join()

# Her iki thread tamamlandığında, "İşlem bitti" mesajını yazdırıyoruz.
print("İşlem bitti")
