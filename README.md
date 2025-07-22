# Yüz Bulanıklaştırma Uygulaması

Bu uygulama, bilgisayar kamerasından alınan görüntüdeki yüzleri otomatik olarak tespit eder ve bulanıklaştırır. Gizlilik ve sansür amaçlı kullanılabilir.

## Kullanılan Teknolojiler

- Python
- OpenCV
- Haar Cascade Sınıflandırıcı

## Proje Yapısı

```
face-blur-app
├── src
│   ├── main.py                # Uygulamanın başlangıç dosyası
│   ├── face_blur.py           # Yüz tespiti ve bulanıklaştırma fonksiyonları
│   ├── haar_cascade
│   │   └── haarcascade_frontalface_default.xml  # Hazır Haar Cascade modeli
│   └── utils.py               # Çerçeve işleme yardımcı fonksiyonları
├── requirements.txt           # Proje bağımlılıkları
└── README.md                  # Proje dokümantasyonu
```

## Kurulum

Bu uygulamayı çalıştırmak için bilgisayarınızda Python kurulu olmalıdır. Gerekli bağımlılıkları pip ile yükleyebilirsiniz.


 Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```

## Kullanım

Uygulamayı çalıştırmak için aşağıdaki komutu kullanın:

```
python src/main.py
```

Kameranızın bağlı ve erişilebilir olduğundan emin olun. Uygulama, kameradan gelen görüntüyü bir pencerede açacak ve tespit edilen yüzleri gerçek zamanlı olarak bulanıklaştıracaktır.

## Sistem Gereksinimleri

- Windows 10/11
- Bağlı ve çalışan bir webcam
- Python 3.8+ (sadece kaynak koddan çalıştırmak için)

## Sık Karşılaşılan Sorunlar

- **Cascade dosyası bulunamadı:** Dosyanın doğru yerde ve sağlam olduğundan emin olun.
- **Webcam açılamıyor:** Kameranın başka bir program tarafından kullanılmadığından emin olun.

> Not: Oluşturulan .exe dosyası sadece Windows işletim sistemlerinde çalışır.
> Uyarı: PyInstaller ile oluşturulan .exe dosyaları bazı antivirüs programları tarafından yanlışlıkla zararlı olarak algılanabilir. Dosyanın güvenli olduğundan emin olabilirsiniz.

## Geliştirici

- [Berkay Seyman](https://github.com/symNistaken)


