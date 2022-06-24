# SmartNinni
Bu proje Marmara Üniversitesi Dr.  Öğr. Üyesi Serkan Aydın Hocamızın Gömülü Sistemler ve Mobil Uygulamalar dersinde bize kattığı bilgiler doğrultusunda ödev olarak hazırlanmıştır.
Proje konusu bebek ağlaması veya sesi olduğunda ninni çalan ve bir dijital çıkış veren bir sistem, ben  bir LED e çıkış verdim bunun yerine uygun bir röle bağlayıp beşik sallama sistemi de oluşturulabilir diye düşünerek, 
Adım adım ilk aşamadan son aşamaya kadar projeyi anlatmaya çalışacağım,
1.olarak raspberry pi kurulumu ile başlayacağım,
Ben projemde Raspberry Pi 3 Model B kullandım, Raspi setimde adaptör, raspi ve SD card vardı.  https://www.sdcard.org/downloads/formatter/ linkinden indirdiğim format programı ile SD karta format attım, 
![image](https://user-images.githubusercontent.com/107412386/175521020-6c1fb3f4-5bfd-41ab-a152-dc1e67d135fc.png)
Daha sonra https://www.raspberrypi.com/software/ linkinden indirdiğim işletim sistemi yükleme arayüzü ile SD karta işletim sistemini yükledim.
![image](https://user-images.githubusercontent.com/107412386/175521037-2c55be61-270c-4e38-8389-6fd9b5bb5987.png)
Kullandığım raspi 4 adet USB girişi, 1 adet HDMI girişi, 1 adet ethernet girişine sahiptir. Aynı zamanda kablosuz bağlantı yapacak donanımı da sahiptir. Bu sebeple ben internet bağlantısını wifi den bağlanarak yaptım.
HDMI girişini kullanarak raspiye ekran bağladım, ayrıca klavye ve mause da bağladım.
Raspiye enerji verdiğimde ve bahsettiğim donanımları bağladığımda aşağıdaki görselde paylaştığım ekran geldi ve bilgisayar gibi kullanmaya başladım.
![image](https://user-images.githubusercontent.com/107412386/175523255-6fe5cf9c-34f2-4c90-82ad-e9ce55aa776e.png)
Yukarıdaki pin tablosunu kullanarak ses sensörümü GPIO18 (12.pin) , LED'i ise GPIO 17 (11.pin) ye bağladım. 
![image](https://user-images.githubusercontent.com/107412386/175523882-db53f194-a01a-4cf5-bdc9-9e44b5f6ee92.png)
Ses algılamısını raspide bulunan jack girşine mikrofon bağlayarak yapacaktım fakat raspideki bu jack giriş olarak değil ses çıkışı almak için kullanıldığını öğrendim, bu sebeple ses çıkışı almak için kullandığım hoparlörü buraya bağladım, ses girişini üzerinde trimpot ile ses seviyesi algılayabileceğim, dijital bir çıkış veren ses sensör ile yaptım.



