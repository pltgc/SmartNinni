import RPi.GPIO as GPIO #GPIO kütüphanesi eklemiş oluyoruz
import time             #time kütüphanesini ekleyerek time,delay fonksiyonlarını kullanabiliyoruz
import vlc              #medya oynatmak için eklenen kütüphane
import blynklib         #blynk kütüphanesini ekliyoruz (nereden indirildiği proje açıklamalrında anlatılıyor)

G = vlc.MediaPlayer("/home/pltgc/ninni.mpeg")  #çalmak istediğimiz ses dosyasını tanımlıyoruz, dosyanın yolunu ekliyoruz
BLYNK_AUTH = 'w5izdAzPkqNEHZjfbJ6n-mIRS-1hCvGK'#blynk uygulamasını ilk kurarken mail olarak gelen token'ı buraya yazıyoruz 
blynk = blynklib.Blynk(BLYNK_AUTH)             #blynk kütüphanesini başlatıyoruz

LED_pin = 17           #GPIO 17 pinine LED_pin adını veriyoruz
sensor_pin = 18        #GPIO 18 pinine sensor_pin adını veriyoruz

GPIO.setmode(GPIO.BCM) #GPIO modunu BCM yazarak GPIO isimeri ile pinleri kullanacağımızı belirtiyoruz
GPIO.setup(sensor_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #sensör pinini input olarak ayarlıyoruz, ve pull down a çekerek herhangi bir giriş yokken logic 0 da tutmuş oluyoruz
GPIO.setup(LED_pin,GPIO.OUT)   #LED pinini output olarak ayarlıyoruz

#aşağıdaki satırda blynk server ini başlatarak telefondaki uygulama ile haberleşmeyi server üzerinden sağlıyoruz
blynk = blynklib.Blynk(BLYNK_AUTH, server='blynk-cloud.com', port=80, ssl_cert=None,heartbeat=10, rcv_buffer=1024, log=print)

try:
	while True:
		blynk.run()  #blynk'i çalıştırıyoruz
        
		if GPIO.input(sensor_pin) == 1:  #eğer ses seviyesi trimpotta ayarladığımız ayarın ütündeyse sensör 1 çıkışını veriyor ve bu koşulu sağlıyoruz
            time.sleep(5) #5 sn bekliyoruz
			if GPIO.input(sensor_pin) == 1: #çıkış hala 1 ise yani ses varsa hala
                print("Ses Alarmi!") #cmd ekranında Ses alarmı yazısı çıkıyor bunu ekrandan kontrol edebilmek için yaptım
                blynk.notify("ben ağlıyorum annecim") #blyn de kurduğumuz notify da "" içindeki yazı uyarı olarak telefonumuza geliyor
                G.play() #yularıda yolunu tanımladığımız ses dosyası çalıyor
                time.sleep(0.5) #0.5 sn aralıklarla döngü tekrarlanıyor
		else: #ses seviyesi ayarlanan değerden düşükse sensör çıkışı 0 veriyor
			print("Ses yok!") #cmd ekranında ses yok yazıyor yine kontrol için eklediğim bir satır
			G.stop()          #çalan ninni durduruluyor
			time.sleep(0.5)   #0.5 sn aralıklarla tekrarlanıyor   
finally:
	GPIO.cleanup()