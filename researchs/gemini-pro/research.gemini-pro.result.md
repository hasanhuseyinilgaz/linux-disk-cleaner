# Research Result for gemini-pro

# Result 1:

Harika bir teknik analiz konusu. Linux üzerinde disk temizliği ve süreç (process) yönetimi, sistem kararlılığı ve performansı için kritik öneme sahiptir. Bu araçların "sihirli" görünen işlevlerinin arkasında, Linux çekirdeği (kernel) ile doğrudan iletişim kuran sistem çağrıları ve standart dosya sistemi hiyerarşisi yatar.

İşte bu teknoloji alanına dair detaylı teknik araştırma raporu, infografik taslağı ve örnek web arayüzü kodu.

---

# 📂 Linux Disk Temizleme ve Süreç Yönetimi: Teknik Araştırma Raporu

Bu rapor, Linux tabanlı sistemlerde disk alanı geri kazanımı, geçici dosya yönetimi ve süreç denetimi sağlayan araçların (System Cleaners & Task Managers) mimarisini incelemektedir.

## 1. Temel Çalışma Prensipleri

Bu tür yazılımlar üç ana mekanizma üzerinde çalışır: Dosya Sistemi Taraması, Geçici Dizin Yönetimi ve Kernel Süreç Arayüzü.

### A. Linux Dosya Sistemi ve Disk Analizi

Disk kullanımını hesaplamak için araçlar genellikle dosya sistemini "inode" (düğüm) bazında tarar.

- **statvfs / statfs:** Dosya sistemi hakkında meta veri (toplam blok, boş blok) toplamak için kullanılan sistem çağrılarıdır. `df` komutunun arkasındaki mantıktır.
- **Recursive Traversal (Özyinelemeli Tarama):** Bir dizinin boyutunu hesaplamak için araç, dizin ağacını özyinelemeli olarak tarar ve her dosyanın `st_blocks` (disk üzerinde kapladığı blok sayısı) değerini toplar. Bu, `du` komutunun çalışma mantığıdır.
- **Sparse Files:** Linux'ta bazı dosyalar (örneğin sanal makine diskleri) görünürde büyük (apparent size) ancak diskte az yer kaplıyor olabilir. İyi bir araç, bu ayrımı yapabilmelidir.

### B. /tmp ve Geçici Dosya Temizliği

`/tmp` ve `/var/tmp` dizinleri sistemin çöplüğü gibidir, ancak kritik kurallar vardır:

- **Sticky Bit (Yapışkan Bit):** `/tmp` dizini genellikle `1777` izinlerine sahiptir. Bu, herkesin dosya yazabileceği ancak **sadece dosya sahibinin (veya root'un)** silebileceği anlamına gelir. Temizleme araçları bu izni ihlal etmeden çalışmalıdır.
- **Atıme (Access Time):** Temizlik kararı genellikle dosyanın en son ne zaman erişildiğine (`atime`) veya değiştirildiğine (`mtime`) bakılarak verilir.
- **tmpfs:** Modern Linux dağıtımlarında `/tmp` genellikle RAM üzerinde (`tmpfs`) tutulur. Buradaki temizlik disk yerinden ziyade RAM tasarrufu sağlar.

### C. Process Sinyalleri ve /proc Sistemi

Linux'ta süreç yönetimi, `/proc` sanal dosya sistemi üzerinden yapılır.

- **Bilgi Toplama:** Bir sürecin CPU/RAM kullanımı `/proc/[PID]/stat` ve `/proc/[PID]/status` dosyalarından okunur.
- **Sinyal Gönderimi (Signals):** Bir süreci sonlandırmak için `kill` sistem çağrısı kullanılır:
- **SIGTERM (15):** "Lütfen kapan" sinyali. Sürecin dosyaları kaydetmesine ve düzgün kapanmasına izin verir.
- **SIGKILL (9):** "Derhal öl" sinyali. Çekirdek süreci anında öldürür, veri kaybı riski vardır.

---

## 2. En İyi Uygulama Yöntemleri (Best Practices)

Endüstri standartlarına göre güvenilir bir temizlik ve yönetim aracı şu prensiplere uymalıdır:

- **Graceful Degradation:** Bir süreç sonlandırılacaksa önce `SIGTERM` gönderilmeli, belirli bir süre (örn. 5 sn) yanıt alınamazsa `SIGKILL` uygulanmalıdır.
- **White-listing (Beyaz Liste):** Sistem için kritik olan dosyalar (örn. socket dosyaları, lock dosyaları) asla silinmemelidir.
- **Systemd Entegrasyonu:** Modern Linux'ta geçici dosyalar `systemd-tmpfiles` servisi ile yönetilir. Kendi "tekerleğinizi icat etmek" yerine bu servisin kurallarını (`.conf` dosyaları) tetiklemek daha güvenlidir.
- **Kullanıcı Bağlamı (Context):** Araç `root` olarak çalışsa bile, kullanıcıya ait önbellekleri (`~/.cache/`) temizlerken o kullanıcının yetkileriyle işlem yapmalı veya dosya sahipliğini bozmamalıdır.

---

## 3. Benzer Açık Kaynak Projeler ve Rakipler

Piyasada bu işi yapan köklü araçlar mevcuttur:

| Araç          | Tür     | Teknoloji     | Özellikler                                                                                                                                      |
| ------------- | ------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **BleachBit** | GUI/CLI | Python, GTK   | En popüler araçtır. "Shredding" (güvenli silme) özelliği vardır. Uygulamaya özel (Firefox, Chrome vb.) temizlik kuralları (CleanerML) kullanır. |
| **Stacer**    | GUI     | C++, Electron | Sistem monitörü, servis yöneticisi ve temizleyiciyi birleştirir. Görsel olarak çok gelişmiştir.                                                 |
| **ncdu**      | CLI     | C, Ncurses    | Disk kullanımını analiz etmek için en hızlı terminal aracıdır. Silme işlemi manueldir.                                                          |
| **tmpreaper** | CLI     | C             | Belirli bir süreden eski dosyaları `/tmp` dizininden silmek için kullanılan eski ama sağlam bir araçtır.                                        |

---

## 4. Kritik Yapılandırma Dosyaları ve Parametreleri

Bu araçların müdahale ettiği veya referans aldığı kritik konumlar:

- **`/etc/tmpfiles.d/*.conf` & `/usr/lib/tmpfiles.d/*.conf`:** `systemd` tarafından kullanılan, hangi dosyaların ne zaman silineceğini belirleyen kurallar.
- _Örnek:_ `d /tmp 1777 root root 10d` (10 günden eski dosyaları sil).

- **`/etc/logrotate.conf`:** Log dosyalarının ne zaman arşivleneceğini ve silineceğini belirler. Temizleme aracı buradaki ayarlarla çelişmemelidir.
- **`~/.cache/`:** Kullanıcı bazlı geçici dosyaların (tarayıcı önbelleği, küçük resimler) bulunduğu standart dizin.
- **`/var/log/`:** Sistem günlükleri. Buradaki dosyaları tamamen silmek yerine içeriğini boşaltmak (`truncate`) daha güvenlidir, aksi halde servisler log yazacak dosya bulamayabilir.

---

## 5. Güvenlik ve Risk Analizi

Bu tür araçlarda güvenlik en üst önceliktir.

### A. "rm -rf" Felaketi

Yanlış yapılandırılmış bir değişken, felakete yol açabilir.

- **Risk:** Kodda `rm -rf $DEGİSKEN/` yazıldığını ve değişkenin boş geldiğini düşünün. Komut `rm -rf /` haline gelir.
- **Önlem:** Silme fonksiyonlarında mutlaka "Sanity Check" (Akıl sağlığı kontrolü) yapılmalıdır. Kök dizin (`/`), `/etc`, `/usr` gibi kritik yollar kara listeye alınmalıdır.

### B. Race Conditions (Yarış Durumu)

- **Risk:** Araç bir dosyanın "eski" olduğunu tespit eder. Tam silme emrini verdiği milisaniyede, bir başka süreç o dosyayı günceller veya aynı isimde yeni bir dosya oluşturur.
- **Önlem:** Dosya kilitleme (file locking) mekanizmaları veya atomik işlemler kullanılmalıdır.

### C. Root Yetkileri ve SUID

- **Risk:** Aracın SUID biti ile (her zaman root yetkisiyle) çalışması, güvenlik açığı yaratır. Kötü niyetli bir kullanıcı, aracı manipüle ederek korumalı dosyaları silebilir.
- **Önlem:** Polkit (PolicyKit) kullanarak sadece gerektiğinde ve yetki onayı ile root haklarına erişilmelidir.

---

## 📊 İnfografik Metni: Linux Sistem Temizliği

_(Grafik tasarımcı için hazırlanmış metin taslağı)_

**Başlık:** Linux Sisteminizin Sağlığı: Disk ve Süreç Yönetimi

**Bölüm 1: Neden Gerekli?**

- 🧹 **Disk Şişkinliği:** Loglar ve önbellekler diski doldurur.
- 🐢 **Performans Kaybı:** Zombi süreçler RAM'i işgal eder.
- 🔒 **Gizlilik:** Tarayıcı geçmişi ve çerezler iz bırakır.

**Bölüm 2: Nasıl Çalışır?**

- **Analiz:** `statfs` ile disk haritası çıkarılır.
- **Karar:** `atime` (erişim zamanı) eski olanlar işaretlenir.
- **İnfaz:** Gereksizlere `unlink`, kilitlenmiş süreçlere `SIGKILL`.

**Bölüm 3: Güvenlik Kalkanları**

- ✅ **Sticky Bit Kontrolü:** Başkasının dosyasını silme!
- ✅ **Kritik Yol Koruması:** `/etc` ve `/boot` dokunulmazdır.
- ✅ **Graceful Kill:** Önce uyar, sonra kapat.

**Alt Bilgi:**

- _Popüler Araçlar:_ BleachBit, Stacer
- _Temel Komutlar:_ `du`, `df`, `kill`, `htop`

---

## 💻 Web Sayfası: Araç Tanıtım Sayfası (HTML/CSS)

Aşağıda, bu araştırma sonuçlarını sunan veya böyle bir aracı tanıtan basit, modern ve duyarlı (responsive) bir HTML şablonu bulunmaktadır.

```html
<!DOCTYPE html>
<html lang="tr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>LinuxCleaner - Akıllı Sistem Yönetimi</title>
    <style>
      :root {
        --primary: #2c3e50;
        --accent: #e74c3c;
        --light: #ecf0f1;
        --text: #34495e;
      }
      body {
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        line-height: 1.6;
        color: var(--text);
        background-color: var(--light);
      }
      header {
        background: var(--primary);
        color: white;
        padding: 2rem 0;
        text-align: center;
      }
      .container {
        max-width: 900px;
        margin: auto;
        padding: 20px;
      }
      .hero {
        text-align: center;
        padding: 40px 20px;
        background: white;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
      }
      .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
      }
      .card {
        background: white;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid var(--accent);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
      }
      h2 {
        color: var(--primary);
      }
      .code-block {
        background: #2d2d2d;
        color: #76ff03;
        padding: 10px;
        border-radius: 4px;
        font-family: monospace;
        overflow-x: auto;
      }
      footer {
        text-align: center;
        padding: 20px;
        margin-top: 40px;
        font-size: 0.9em;
        color: #666;
      }
      .btn {
        display: inline-block;
        background: var(--accent);
        color: white;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 4px;
        margin-top: 10px;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <header>
      <div class="container">
        <h1>LinuxCleaner & Monitor</h1>
        <p>Açık Kaynaklı Disk Temizleme ve Süreç Yönetimi Mimarisi</p>
      </div>
    </header>

    <div class="container">
      <div class="hero">
        <h2>Sisteminiz Nefes Alsın</h2>
        <p>
          Gereksiz dosya yığınlarını temizleyin, zombi süreçleri sonlandırın ve
          sistem performansını optimize edin. Güvenli, Hızlı ve Açık Kaynak.
        </p>
        <a href="#" class="btn">Teknik Dokümantasyonu İncele</a>
      </div>

      <div class="grid">
        <div class="card">
          <h3>🚀 Akıllı Disk Analizi</h3>
          <p>
            Inode tabanlı tarama ile disk kullanımını analiz eder.
            <code>statvfs</code> çağrıları ile anlık doluluk oranlarını
            raporlar.
          </p>
        </div>
        <div class="card">
          <h3>⚡ Süreç Yönetimi</h3>
          <p>
            <code>/proc</code> dosya sistemi üzerinden kaynak tüketen süreçleri
            izler. Yanıt vermeyen uygulamaları <code>SIGTERM</code> ve
            <code>SIGKILL</code> ile yönetir.
          </p>
        </div>
        <div class="card">
          <h3>🛡️ Güvenli Temizlik</h3>
          <p>
            Sistem bütünlüğü için kritik dosyaları (Whitelist) korur.
            <code>/tmp</code> temizliğinde Sticky Bit kurallarına tam uyum
            sağlar.
          </p>
        </div>
      </div>

      <br />
      <hr />
      <br />

      <section>
        <h2>Teknik Altyapı</h2>
        <p>
          Bu araç, Linux Kernel API'leri ile doğrudan haberleşerek çalışır.
          Aşağıda tipik bir temizlik döngüsünün mantığı gösterilmiştir:
        </p>

        <div class="code-block">
          # Örnek Temizlik Mantığı (Pseudocode)<br />
          if file.path in CRITICAL_PATHS:<br />
          &nbsp;&nbsp;skip()<br />
          else if file.access_time > 7_DAYS:<br />
          &nbsp;&nbsp;secure_delete(file)<br />
          log_action("Deleted: " + file.name)
        </div>

        <h3>Kritik Yapılandırma</h3>
        <ul>
          <li>
            <strong>Log Rotasyon:</strong> <code>/etc/logrotate.conf</code> ile
            uyumlu çalışır.
          </li>
          <li>
            <strong>Systemd:</strong> Geçici dosyalar için
            <code>tmpfiles.d</code> kurallarını kullanır.
          </li>
        </ul>
      </section>
    </div>

    <footer>
      <p>
        © 2026 Linux Araştırma Raporu. Açık Kaynak Topluluğu İçin
        Hazırlanmıştır.
      </p>
    </footer>
  </body>
</html>
```

### Kaynakça ve İleri Okuma

1. **Linux Man Pages:** `man du`, `man statfs`, `man kill`.
2. **Freedesktop.org:** systemd-tmpfiles dokümantasyonu.
3. **BleachBit Source Code:** GitHub repository (Python implementation details).
4. **The Linux Programming Interface:** Michael Kerrisk (Kitap - Linux sistem programlama referansı).

---

### Sizin İçin Bir Sonraki Adım

Bu rapordaki bilgileri kullanarak, **Python ve `psutil` kütüphanesi ile kendi basit disk/süreç izleme scriptinizi yazmak ister misiniz?** Böylece teorik bilgiyi pratiğe dökebiliriz.

# Result 2:

Elbette, raporda bahsettiğim teknik kavramları, sistem çağrılarını ve araçları inceleyebileceğiniz **doğrudan ve güvenilir kaynak linkleri** aşağıdadır.

Bu kaynaklar, Linux çekirdek dokümantasyonu, resmi proje sayfaları ve geliştirici kılavuzlarından seçilmiştir.

### 1. Linux Çekirdeği ve Sistem Çağrıları (Teknik Teori)

Bu sayfalar, raporda bahsedilen `statfs`, `kill` ve dosya sistemi mantığının (Inode, /proc) nasıl çalıştığını anlatan resmi "man page" (kılavuz) sayfalarıdır.

- **Linux Man Pages (Genel Dizin):** [man7.org/linux/man-pages](https://man7.org/linux/man-pages/)
- **statfs / statvfs (Disk Analizi):** [man7.org/linux/man-pages/man2/statfs.2.html](https://man7.org/linux/man-pages/man2/statfs.2.html)
- **kill (Süreç Sinyalleri):** [man7.org/linux/man-pages/man2/kill.2.html](https://man7.org/linux/man-pages/man2/kill.2.html)
- **/proc Dosya Sistemi (Süreç Bilgileri):** [man7.org/linux/man-pages/man5/proc.5.html](https://man7.org/linux/man-pages/man5/proc.5.html)
- **Dosya Hiyerarşisi Standardı (FHS):** [refspecs.linuxfoundation.org/FHS_3.0](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) (Hangi klasörün ne işe yaradığını anlatan standart).

### 2. Yapılandırma ve Systemd (Best Practices)

Modern Linux dağıtımlarında geçici dosyaların nasıl yönetildiğine dair standartlar.

- **systemd-tmpfiles (Geçici Dosya Yönetimi):** [freedesktop.org/software/systemd/man/systemd-tmpfiles.html](https://www.freedesktop.org/software/systemd/man/systemd-tmpfiles.html)
- **Logrotate (Log Yönetimi):** [linux.die.net/man/8/logrotate](https://linux.die.net/man/8/logrotate)

### 3. Açık Kaynak Projeler ve Rakipler

İncelenen araçların kaynak kodları ve proje sayfaları. Bu kodları incelemek, kendi aracınızı yazarken mantığı anlamak için en iyi yöntemdir.

- **BleachBit (Resmi Site):** [bleachbit.org](https://www.bleachbit.org/)
- **BleachBit (GitHub Kaynak Kodu):** [github.com/bleachbit/bleachbit](https://github.com/bleachbit/bleachbit) (Python ile yazılmıştır, temizlik kuralları incelenebilir).
- **Stacer (GitHub):** [github.com/oguzhaninan/Stacer](https://github.com/oguzhaninan/Stacer) (C++ ve Electron tabanlı modern arayüz).
- **ncdu (NCurses Disk Usage):** [dev.yorhel.nl/ncdu](https://dev.yorhel.nl/ncdu) (Terminal tabanlı en hızlı analiz aracı).
- **tmpreaper:** [manpages.debian.org/tmpreaper](https://www.google.com/search?q=https://manpages.debian.org/unstable/tmpreaper/tmpreaper.8.en.html)

### 4. Geliştirici Kütüphaneleri ve Kitaplar

Eğer Python ile kendi aracınızı yazacaksanız ihtiyaç duyacağınız temel kütüphane ve referans kitabı.

- **psutil (Python Process & System Utilities):** [psutil.readthedocs.io](https://psutil.readthedocs.io/en/latest/) (Disk, CPU, RAM ve süreçleri yönetmek için en popüler kütüphane).
- **The Linux Programming Interface (Michael Kerrisk):** [man7.org/tlpi](https://man7.org/tlpi/) (Linux sistem programlamanın "kutsal kitabı" kabul edilir).

---

**Bir sonraki adım:**
Bu kaynaklardan **`psutil` dokümantasyonunu** incelemenizi öneririm. Python ile sadece 5-10 satır kod yazarak sisteminizin anlık CPU ve Disk kullanımını çeken basit bir script örneği hazırlamamı ister misiniz?
