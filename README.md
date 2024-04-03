
---

# Paralel Sayı Yazdırma

Bu Python betiği, threading ve time modüllerini kullanarak iki ayrı thread oluşturur ve her biri 0'dan 19'a kadar olan sayıları yazdırır. Her iki thread de aynı `print_numbers()` fonksiyonunu hedef alır.

## Kullanım

1. Kodu çalıştırmak için Python 3 gereklidir.
2. Terminal veya komut istemcisinde betiği çalıştırın:

    ```
    python parallel_number_printing.py
    ```

3. Kod, iki ayrı thread oluşturacak ve her biri 0'dan 19'a kadar olan sayıları ekrana yazdıracaktır. Her iki thread arasında bir saniye gecikme olacaktır.

## Dikkat Edilmesi Gereken Noktalar

- Kodun doğru çalışması için `threading` ve `time` modüllerinin yüklü olması gerekmektedir.
- Thread'lerin tamamlanmasını beklemek için `join()` yöntemi kullanılmıştır.
- Kodun sonunda "İşlem bitti" mesajı ekrana yazdırılır.

## Lisans

Bu kod parçası, MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.

--- 
