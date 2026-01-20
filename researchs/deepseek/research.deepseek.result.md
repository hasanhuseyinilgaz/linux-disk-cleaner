# Research Result for deepseek

# Result 1:

# Linux Disk Temizleme ve Süreç Yönetimi Araçları: Teknik Araştırma Raporu

## 1. Temel Çalışma Prensipleri

### Linux Dosya Sistemi Yapısı

Linux dosya sistemi hiyerarşik bir yapıya sahiptir ve Filesystem Hierarchy Standard (FHS) ile düzenlenir. Disk temizleme araçları genellikle şu dizinlere odaklanır:

- **/tmp**: Geçici dosyalar (tmpfiles.d ile otomatik temizlenebilir)
- **/var/tmp**: Kalıcı geçici dosyalar (daha uzun süre saklanır)
- **/var/log**: Log dosyaları (logrotate ile yönetilir)
- **/var/cache**: Önbellek dosyaları
- **~/.cache**: Kullanıcı önbellek dosyaları
- **~/.local/share/Trash**: Kullanıcı çöp kutusu

### /tmp Temizliği Mekanizmaları

**systemd-tmpfiles** modern Linux sistemlerinde /tmp temizliğini yönetir:

```bash
# /etc/tmpfiles.d/ dizinindeki konfigürasyonlar
# Örnek: 10 günden eski dosyaları sil
/var/tmp/* 1777 root root 10d
```

**tmpreaper** ve **tmpwatch** geleneksel araçlar:

```bash
tmpreaper 24h /tmp  # 24 saatten eski dosyaları temizler
```

### Process Sinyalleri ve Yönetimi

- **SIGTERM (15)**: Nazik sonlandırma (process kendini temizleyebilir)
- **SIGKILL (9)**: Zorla sonlandırma (hemen öldürür)
- **SIGHUP (1)**: Yeniden yükleme (konfigürasyon yenileme)
- **SIGSTOP (19)**: Process'i duraklatma
- **SIGCONT (18)**: Duraklatılmış process'i devam ettirme

**Kaynak**: Linux Programmer's Manual - signal(7)

## 2. En İyi Uygulama Yöntemleri ve Endüstri Standartları

### Disk Temizleme Best Practices

1. **Öncelikle analiz yap**: `du`, `ncdu`, `df` ile disk kullanımını tespit et
2. **Yedekleme**: Kritik verileri silmeden önce yedekle
3. **Kademeli temizlik**: Önce /tmp, sonra log, en son önbellek dosyaları
4. **Otomatik temizleme**: Cron job'lar ile düzenli bakım
5. **Log rotasyonu**: logrotate.conf ile log dosyalarını yönet

```bash
# Örnek cron job (haftalık temizlik)
0 2 * * 0 /usr/local/bin/cleanup-script.sh
```

### Process Yönetimi Standartları

1. **SIGTERM önce, SIGKILL sonra**: Process'e kapanma şansı ver
2. **PID dosyalarını kontrol et**: /var/run/\*.pid
3. **Process tree'yi dikkate al**: Child process'leri de temizle
4. **Systemd servislerini kullan**: Modern daemon yönetimi

**Endüstri Standartları**:

- **FHS 3.0**: Dosya sistemi standardı
- **LSB (Linux Standard Base)**: Uyumluluk standardı
- **systemd**: Modern init sistem standartları

**Kaynak**: Filesystem Hierarchy Standard, Red Hat Enterprise Linux Best Practices

## 3. Benzer Açık Kaynak Projeler ve Rakipler

### Disk Temizleme Araçları

1. **BleachBit** (Python/GTK+)
   - Özellikler: GUI/CLI, çoklu dil, 90+ temizleme preseti
   - Güçlü yanları: Kullanıcı dostu, geniş eklenti desteği
   - Zayıf yanları: GUI odaklı, sunucular için uygun değil

2. **Stacer** (JavaScript/Electron)
   - Özellikler: Sistem monitörü + temizleyici, grafiksel arayüz
   - Güçlü yanları: Kapsamlı sistem yönetimi
   - Zayıf yanları: Electron tabanlı, yüksek kaynak tüketimi

3. **ncdu** (C)
   - Özellikler: NCurses arayüz, disk kullanım analizi
   - Güçlü yanları: Hızlı, hafif, sunucu uyumlu

4. **tmpreaper/tmpwatch**
   - Özellikler: Sadece /tmp temizliği
   - Güçlü yanları: Basit, güvenilir

5. **logrotate** (C)
   - Özellikler: Log dosyası yönetimi
   - Güçlü yanları: Standart, otomatik rotasyon

### Process Yönetimi Araçları

1. **htop/top**: Interaktif process yöneticisi
2. **psmisc**: killall, pstree gibi araçlar
3. **supervisor**: Process kontrol ve monitoring

**Karşılaştırma Tablosu**:
| Araç | Dil | GUI/CLI | Ana Odak | Sunucu Uygunluğu |
|------|-----|---------|----------|------------------|
| BleachBit | Python | İkisi de | Disk temizleme | Sınırlı |
| Stacer | JavaScript | GUI | Sistem yönetimi | Hayır |
| ncdu | C | CLI | Disk analizi | Evet |
| tmpreaper | C | CLI | /tmp temizliği | Evet |
| Önerilen | C++/Python | CLI | İkili görev | Evet |

## 4. Kritik Yapılandırma Dosyaları ve Parametreleri

### Sistem Seviyesi Konfigürasyonlar

1. **/etc/tmpfiles.d/\***: Geçici dosya kuralları
2. **/etc/logrotate.conf**: Log rotasyon ayarları
3. **/etc/systemd/system/**: Systemd servis dosyaları
4. **/etc/security/limits.conf**: Process limitleri
5. **/etc/crontab**: Zamanlanmış görevler

### Güvenlik Parametreleri

```bash
# Örnek tmpfiles.d konfigürasyonu
# Type Path        Mode UID  GID  Age Argument
D     /tmp/*       1777 root root 1d  -
D     /var/tmp/*   1777 root root 30d -

# Logrotate güvenlik ayarları
/var/log/*.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
    create 640 root adm
    sharedscripts
}
```

### Process Yönetimi Parametreleri

```bash
# Systemd resource kontrolü
[Service]
MemoryLimit=512M
CPUQuota=50%
TasksMax=100
```

## 5. Güvenlik Açısından Kritik Noktalar

### Disk Temizleme Riskleri

1. **Yanlış dosya silme**: Özellikle root ile çalışırken
   - Çözüm: `--dry-run` parametresi, interaktif onay
2. **Sembolik link takip etme**: `/tmp` içindeki sembolik linkler
   - Çözüm: `-P` parametresi ile link takibini engelleme

3. **Aktif dosyaları silme**: Çalışan process'lerin kullandığı dosyalar
   - Çözüm: `lsof` ile kontrol, dosya kilitleri

4. **Log dosyalarını temizleme**: Adli analiz için gerekli log'lar
   - Çözüm: Retention policy, yedekleme

### Process Yönetimi Riskleri

1. **Önemli servisleri sonlandırma**:
   - Çözüm: Whitelist/Blacklist, critical process listesi

2. **PID yarışması (race condition)**:
   - Çözüm: PID dosyaları, systemd scope kullanımı

3. **Zombie process'ler**:
   - Çözüm: Parent process kontrolü, reaping mekanizmaları

### Güvenlik Best Practices

1. **Principle of Least Privilege**: İhtiyaç duyulan minimum yetki
2. **Audit logging**: Tüm temizleme işlemlerini logla
3. **Rollback mekanizması**: Kritik silmelerde yedekle
4. **User confirmation**: Batch işlemlerde onay iste
5. **Pattern whitelisting**: Sadece bilinen pattern'ları temizle

**Örnek güvenli kod yapısı**:

```python
def safe_delete(path, dry_run=True):
    if not os.path.exists(path):
        return False
    if os.path.islink(path):
        # Sembolik linkleri takip etme
        return False
    if is_system_critical(path):
        return False
    if dry_run:
        logging.info(f"Would delete: {path}")
        return False
    # Güvenli silme işlemi
```

### Çalıştırma Yetkileri

- **Root gerektiren işlemler**: Sistem dizinleri, diğer kullanıcıların dosyaları
- **User seviyesi işlemler**: Home directory, kullanıcı cache
- **Sudo stratejisi**: Minimal sudo yetkileri, /etc/sudoers.d/ dosyaları

---

## Kaynaklar

1. **Linux Filesystem Hierarchy Standard** (FHS 3.0)
   - https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf

2. **systemd-tmpfiles Documentation**
   - https://www.freedesktop.org/software/systemd/man/tmpfiles.d.html

3. **BleachBit Source Code & Documentation**
   - https://github.com/bleachbit/bleachbit

4. **Red Hat Enterprise Linux Security Guide**
   - https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening

5. **Linux Programmer's Manual - signal(7)**
   - `man 7 signal`

6. **Linux Audit Framework**
   - https://linux.die.net/man/8/auditd

7. **OWASP Secure Coding Practices**
   - https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/

8. **GNU Coreutils Documentation**
   - https://www.gnu.org/software/coreutils/manual/coreutils.html

---

# Özet İnfografik Metni

```
LINUX DİSK & PROCESS YÖNETİMİ - TEKNİK ÖZET

📊 TEMEL PRENSİPLER
• FHS Standardı: /tmp, /var, /home yapıları
• Tmp Temizleme: systemd-tmpfiles, 10-gün kuralı
• Process Sinyalleri: SIGTERM(15) → SIGKILL(9) hiyerarşisi

🔧 EN İYİ UYGULAMALAR
1. Analiz → Yedekleme → Kademeli Temizleme
2. Cron Job: Haftalık bakım planı
3. Logrotate: Otomatik log yönetimi
4. SIGTERM önceliği: Process'e kapanma şansı ver

🛠️ ARAÇ KARŞILAŞTIRMASI
• BleachBit: GUI odaklı, masaüstü için
• ncdu: CLI, sunucular için ideal
• Stacer: All-in-one, Electron tabanlı
• Önerilen: CLI tabanlı, C++/Python hibrit

⚙️ KRİTİK KONFİGÜRASYONLAR
• /etc/tmpfiles.d/*    → Geçici dosya kuralları
• /etc/logrotate.conf  → Log politikaları
• /etc/crontab        → Otomatik görevler
• systemd resource limits → Process kontrolleri

🚨 GÜVENLİK RİSKLERİ
• Yanlış dosya silme → --dry-run ile test
• Sembolik link tuzakları → -P parametresi
• Kritik servisleri durdurma → Whitelist kontrolü
• Yetki aşımı → Principle of least privilege

✅ GÜVENLİK BEST PRACTICES
• Audit logging: Tüm işlemler kayıt altında
• Rollback: Kritik silmelerde yedek
• User confirmation: Batch işlem onayı
• Pattern whitelisting: Sadece bilinenleri temizle
```

---

# Bulguları Sunan Web Sayfası HTML Kodu

```html
<!DOCTYPE html>
<html lang="tr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Linux Disk & Process Yönetimi Araştırması</title>
    <style>
      :root {
        --primary: #2c3e50;
        --secondary: #3498db;
        --success: #27ae60;
        --warning: #f39c12;
        --danger: #e74c3c;
        --light: #ecf0f1;
        --dark: #34495e;
      }

      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
      }

      .container {
        max-width: 1200px;
        margin: 0 auto;
        background: white;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        overflow: hidden;
      }

      header {
        background: linear-gradient(90deg, var(--primary), var(--dark));
        color: white;
        padding: 2rem;
        text-align: center;
      }

      h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
      }

      .subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
      }

      .content-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        padding: 2rem;
      }

      .card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        border-left: 5px solid var(--secondary);
        transition: transform 0.3s ease;
      }

      .card:hover {
        transform: translateY(-5px);
      }

      .card:nth-child(2) {
        border-left-color: var(--success);
      }
      .card:nth-child(3) {
        border-left-color: var(--warning);
      }
      .card:nth-child(4) {
        border-left-color: var(--danger);
      }
      .card:nth-child(5) {
        border-left-color: var(--primary);
      }

      .card h3 {
        color: var(--primary);
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 10px;
      }

      .card h3 i {
        font-size: 1.5rem;
      }

      .highlight {
        background: var(--light);
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        font-family: monospace;
        border-left: 3px solid var(--secondary);
      }

      .tool-comparison {
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0;
      }

      .tool-comparison th,
      .tool-comparison td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #ddd;
      }

      .tool-comparison th {
        background: var(--primary);
        color: white;
      }

      .tool-comparison tr:hover {
        background: #f5f5f5;
      }

      .warning-box {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 5px solid #f39c12;
      }

      .security-list {
        list-style: none;
        padding: 0;
      }

      .security-list li {
        padding: 8px 0;
        border-bottom: 1px dashed #eee;
        display: flex;
        align-items: center;
        gap: 10px;
      }

      .security-list li:before {
        content: "⚠️";
      }

      footer {
        background: var(--dark);
        color: white;
        text-align: center;
        padding: 1.5rem;
        margin-top: 2rem;
      }

      @media (max-width: 768px) {
        .content-grid {
          grid-template-columns: 1fr;
          padding: 1rem;
        }

        h1 {
          font-size: 2rem;
        }
      }
    </style>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
    />
  </head>
  <body>
    <div class="container">
      <header>
        <h1>
          <i class="fas fa-server"></i> Linux Disk & Process Yönetimi
          Araştırması
        </h1>
        <p class="subtitle">
          Disk Temizleme ve Süreç Yönetimi Araçları - Teknik Analiz
        </p>
      </header>

      <div class="content-grid">
        <div class="card">
          <h3><i class="fas fa-cogs"></i> Temel Çalışma Prensipleri</h3>
          <p>
            <strong>Linux Dosya Sistemi:</strong> FHS standardına göre
            yapılandırılmış hiyerarşik yapı.
          </p>
          <div class="highlight">
            /tmp → Geçici dosyalar<br />
            /var/log → Log dosyaları<br />
            /var/cache → Önbellek dosyaları
          </div>
          <p>
            <strong>/tmp Temizliği:</strong> systemd-tmpfiles ile otomatik
            yönetim.
          </p>
          <p>
            <strong>Process Sinyalleri:</strong> SIGTERM (nazik) → SIGKILL
            (zorunlu) hiyerarşisi.
          </p>
        </div>

        <div class="card">
          <h3><i class="fas fa-chart-line"></i> Best Practices</h3>
          <ol style="padding-left: 20px;">
            <li>Disk analizi ile başla (du, ncdu)</li>
            <li>Kritik verileri yedekle</li>
            <li>Kademeli temizlik uygula</li>
            <li>Cron job ile otomatik bakım</li>
            <li>Logrotate ile log yönetimi</li>
          </ol>
          <div class="highlight">
            # Örnek cron job<br />
            0 2 * * 0 /usr/local/bin/cleanup.sh
          </div>
        </div>

        <div class="card">
          <h3><i class="fas fa-tools"></i> Araç Karşılaştırması</h3>
          <table class="tool-comparison">
            <tr>
              <th>Araç</th>
              <th>Tip</th>
              <th>Sunucu Uygun</th>
            </tr>
            <tr>
              <td>BleachBit</td>
              <td>GUI/CLI</td>
              <td>Sınırlı</td>
            </tr>
            <tr>
              <td>Stacer</td>
              <td>GUI</td>
              <td>Hayır</td>
            </tr>
            <tr>
              <td>ncdu</td>
              <td>CLI</td>
              <td>Evet</td>
            </tr>
            <tr>
              <td>tmpreaper</td>
              <td>CLI</td>
              <td>Evet</td>
            </tr>
          </table>
          <p><strong>Önerilen:</strong> CLI tabanlı, C++/Python hibrit yapı.</p>
        </div>

        <div class="card">
          <h3><i class="fas fa-file-alt"></i> Kritik Konfigürasyonlar</h3>
          <p><strong>/etc/tmpfiles.d/*</strong> - Geçici dosya kuralları</p>
          <div class="highlight">
            # /tmp'de 1 günden eski dosyalar<br />
            D /tmp/* 1777 root root 1d -
          </div>
          <p><strong>/etc/logrotate.conf</strong> - Log yönetimi</p>
          <p><strong>/etc/crontab</strong> - Zamanlanmış görevler</p>
          <p><strong>Systemd resource limits</strong> - Process kontrolleri</p>
        </div>

        <div class="card">
          <h3><i class="fas fa-shield-alt"></i> Güvenlik Riskleri</h3>
          <ul class="security-list">
            <li>Yanlış dosya silme riski</li>
            <li>Sembolik link tuzakları</li>
            <li>Aktif dosyaları silme</li>
            <li>Kritik servisleri sonlandırma</li>
            <li>Yetki aşımı ve privilege escalation</li>
          </ul>
          <div class="warning-box">
            <strong>Çözüm:</strong> --dry-run parametresi, whitelist kontrolü,
            audit logging
          </div>
        </div>

        <div class="card">
          <h3><i class="fas fa-lightbulb"></i> Güvenlik Best Practices</h3>
          <ul style="padding-left: 20px;">
            <li>
              <strong>Principle of Least Privilege:</strong> Minimum yetki
            </li>
            <li><strong>Audit logging:</strong> Tüm işlemler kayıt altında</li>
            <li>
              <strong>Rollback mekanizması:</strong> Kritik silmelerde yedek
            </li>
            <li><strong>User confirmation:</strong> Batch işlem onayı</li>
            <li>
              <strong>Pattern whitelisting:</strong> Sadece bilinenleri temizle
            </li>
          </ul>
          <div class="highlight">
            def safe_delete(path, dry_run=True):<br />
            &nbsp;&nbsp;if is_system_critical(path):<br />
            &nbsp;&nbsp;&nbsp;&nbsp;return False
          </div>
        </div>
      </div>

      <footer>
        <p><strong>Araştırma Sonuçları Özeti</strong></p>
        <p>
          Linux disk ve process yönetimi için CLI tabanlı, güvenlik odaklı bir
          araç geliştirilmesi önerilmektedir.
        </p>
        <p>
          Araç; systemd-tmpfiles ile uyumlu, audit logging destekli, kademeli
          temizleme yapabilmeli ve process yönetiminde SIGTERM/SIGKILL
          hiyerarşisini doğru uygulamalıdır.
        </p>
        <p style="margin-top: 15px; font-size: 0.9rem; opacity: 0.8;">
          © 2024 Linux Sistem Yönetimi Araştırması | Kaynaklar: FHS 3.0, systemd
          Docs, RHEL Security Guide
        </p>
      </footer>
    </div>
  </body>
</html>
```

Bu kapsamlı araştırma raporu, Linux disk temizleme ve process yönetimi araçlarının teknik detaylarını, en iyi uygulamalarını, mevcut çözümleri ve güvenlik gereksinimlerini detaylı olarak sunmaktadır. Özellikle sunucu ortamları için CLI tabanlı, güvenlik odaklı bir araç geliştirilmesinin en uygun çözüm olduğu sonucuna varılmıştır.

# Result 2:

# Kaynaklar ve Referanslar

Aşağıda araştırmada kullanılan temel kaynakların detaylı listesini ve linklerini sunuyorum:

## 1. Linux Dosya Sistemi ve Standartları

### Filesystem Hierarchy Standard (FHS)

- **Resmi FHS 3.0 Belgesi**: https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf
- **Linux Foundation FHS Sayfası**: https://refspecs.linuxfoundation.org/fhs.shtml
- **Debian FHS Uyumluluk**: https://www.debian.org/doc/debian-policy/ch-opersys.html#s9.1

### systemd ve tmpfiles.d

- **systemd-tmpfiles resmi dokümantasyonu**: https://www.freedesktop.org/software/systemd/man/tmpfiles.d.html
- **Arch Linux tmpfiles.d Kılavuzu**: https://wiki.archlinux.org/title/Systemd-tmpfiles
- **Red Hat tmpfiles.d Açıklaması**: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sect-using_tmpfiles_for_temporary_files

## 2. Process Yönetimi ve Sinyaller

### Linux Process Sinyalleri

- **Linux man-pages signal(7)**: https://man7.org/linux/man-pages/man7/signal.7.html
- **GNU libc Signal Handling**: https://www.gnu.org/software/libc/manual/html_node/Signal-Handling.html
- **Linux Programmer's Manual**: `man 7 signal` (yerel sistemde)

### Process Yönetimi Best Practices

- **Linux Daemon Writing Guide**: https://www.freedesktop.org/software/systemd/man/daemon.html
- **IBM Developer Process Management**: https://developer.ibm.com/tutorials/l-lpic1-103-6/

## 3. Disk Temizleme Araçları ve Projeler

### BleachBit

- **Resmi Websitesi**: https://www.bleachbit.org/
- **GitHub Repository**: https://github.com/bleachbit/bleachbit
- **BleachBit Documentation**: https://docs.bleachbit.org/

### Stacer

- **GitHub Repository**: https://github.com/oguzhaninan/Stacer
- **Resmi Websitesi**: https://github.com/oguzhaninan/Stacer

### ncdu

- **Resmi Websitesi**: https://dev.yorhel.nl/ncdu
- **GitHub Repository**: https://github.com/rofl0r/ncdu

### tmpreaper ve tmpwatch

- **tmpreaper Debian Paketi**: https://packages.debian.org/stable/tmpreaper
- **tmpwatch (RHEL/CentOS)**: https://linux.die.net/man/8/tmpwatch

## 4. Güvenlik ve Best Practices

### Linux Sistem Güvenliği

- **Red Hat Enterprise Linux Security Guide**: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/
- **CIS Linux Benchmarks**: https://www.cisecurity.org/cis-benchmarks/
- **Linux Audit Framework (auditd)**: https://linux.die.net/man/8/auditd

### Güvenli Kodlama ve Silme İşlemleri

- **OWASP Secure Coding Practices**: https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/
- **Linux File Deletion Security**: https://www.linuxjournal.com/content/secure-file-deletion-linux
- **SANS Institute Linux Security**: https://www.sans.org/blog/linux-security-best-practices/

## 5. Log Yönetimi ve Rotasyon

### logrotate

- **logrotate man pages**: https://linux.die.net/man/8/logrotate
- **logrotate Configuration Guide**: https://www.digitalocean.com/community/tutorials/how-to-manage-logfiles-with-logrotate-on-ubuntu-16-04
- **RHEL logrotate Documentation**: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-logrotate

## 6. Systemd ve Servis Yönetimi

### Systemd Resource Control

- **systemd.resource-control man page**: https://www.freedesktop.org/software/systemd/man/systemd.resource-control.html
- **Systemd for Administrators**: https://www.freedesktop.org/wiki/Software/systemd/

## 7. Disk Analiz Araçları

### du, df, ncdu

- **GNU Coreutils Documentation**: https://www.gnu.org/software/coreutils/manual/coreutils.html
- **Linux disk usage analysis tools**: https://www.tecmint.com/check-linux-disk-usage-of-files-and-directories/

## 8. Cron ve Zamanlanmış Görevler

### Cron Sistemleri

- **cron man pages**: https://linux.die.net/man/8/cron
- **systemd timers vs cron**: https://opensource.com/article/20/7/systemd-timers

## 9. Önemli Referanslar ve Kılavuzlar

### Linux Documentation Project

- **TLDP (The Linux Documentation Project)**: https://tldp.org/
- **Linux System Administrator's Guide**: https://tldp.org/LDP/sag/html/index.html

### Distribüsyona Özgü Dokümanlar

- **Ubuntu Server Guide**: https://ubuntu.com/server/docs
- **Debian Administrator's Handbook**: https://debian-handbook.info/
- **Arch Linux Wiki**: https://wiki.archlinux.org/
- **Fedora Documentation**: https://docs.fedoraproject.org/

### Açık Kaynak Lisansları ve Standartlar

- **Open Source Initiative**: https://opensource.org/licenses
- **Linux Standard Base (LSB)**: https://refspecs.linuxfoundation.org/lsb.shtml

## 10. Ek Kaynaklar ve Referanslar

### Linux Kernel Dokümantasyonu

- **Kernel.org Documentation**: https://www.kernel.org/doc/html/latest/
- **Linux Kernel User's and Administrator's Guide**: https://www.kernel.org/doc/html/latest/admin-guide/

### Sistem Performansı ve Monitoring

- **Linux Performance Analysis**: http://www.brendangregg.com/linuxperf.html
- **Linux System Monitoring Tools**: https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/

---

## Ek Notlar

1. **Yerel Sistem Dokümantasyonu**: Linux sistemlerinde yerel olarak bulunan man sayfaları (`man` komutu) birincil kaynaktır:

   ```bash
   man signal
   man tmpfiles.d
   man logrotate
   man cron
   ```

2. **Distro-specific Docs**: Her Linux dağıtımının kendi resmi dokümantasyonu vardır:
   - Ubuntu: https://help.ubuntu.com/
   - Debian: https://www.debian.org/doc/
   - RHEL: https://access.redhat.com/documentation/
   - Arch: https://wiki.archlinux.org/

3. **Stack Overflow ve Topluluk Kaynakları**:
   - Unix & Linux Stack Exchange: https://unix.stackexchange.com/
   - Server Fault: https://serverfault.com/
   - Linux Questions: https://www.linuxquestions.org/

4. **Açık Kaynak Kod İncelemeleri**:
   - GitHub'da ilgili projelerin source code'ları
   - Debian/Ubuntu paket kaynak kodları
   - RPM paket spesifikasyonları

Bu kaynakların çoğuna doğrudan erişim mümkündür. Bazı kurumsal dokümanlar (Red Hat gibi) için üyelik gerekebilir, ancak temel bilgiler genellikle ücretsiz olarak erişilebilir durumdadır.
