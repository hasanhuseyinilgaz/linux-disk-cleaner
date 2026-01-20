# Sources for mistral

### 1. Temel Çalışma Prensipleri

- **`/tmp` Temizliği ve `systemd-tmpfiles`:**
  - [systemd.io - Using /tmp/ and /var/tmp/ Safely](https://systemd.io/TEMPORARY_DIRECTORIES/)
  - [Ask Ubuntu - How is the /tmp directory cleaned up?](https://askubuntu.com/questions/20783/how-is-the-tmp-directory-cleaned-up)
  - [Linux Bash - Managing Temporary Files in `/tmp` and `/var/tmp`](https://www.linuxbash.sh/post/managing-temporary-files-in-tmp-and-vartmp)

- **Process Sinyalleri ve Dosya Yönetimi:**
  - [Super User - How to cleanup tmp folder safely on Linux](https://superuser.com/questions/499039/how-to-cleanup-tmp-folder-safely-on-linux)
  - [Stack Overflow - Can /tmp in Linux ever fill up?](https://stackoverflow.com/questions/537437/can-tmp-in-linux-ever-fill-up)

---

### 2. En İyi Uygulama Yöntemleri ve Endüstri Standartları

- **Düzenli Temizlik ve Log Yönetimi:**
  - [Baeldung - How to Clean Up a Linux System](https://www.baeldung.com/linux/clean-up-linux-system)
  - [WafaiCloud - Efficient Disk Cleanup Techniques for Linux Servers](https://wafaicloud.com/blog/efficient-disk-cleanup-techniques-for-linux-servers/)
  - [Interserver - Best Practices for Maintaining Free Disk Space in Ubuntu Systems](https://www.interserver.net/tips/kb/best-practices-for-maintaining-free-disk-space-in-ubuntu-systems/)

- **Paket Önbelleği ve Kernel Temizliği:**
  - [LinuxVox - Linux Disk Cleanup: A Comprehensive Guide](https://linuxvox.com/blog/linux-cleanup-disk/)

---

### 3. Benzer Açık Kaynak Projeler ve Rakip Araçlar

- **BleachBit ve Stacer:**
  - [Baeldung - BleachBit tanıtımı](https://www.baeldung.com/linux/clean-up-linux-system)
  - [TecMint - Stacer ve BleachBit karşılaştırması](https://www.tecmint.com/free-disk-space-ubuntu-linux-mint/)
  - [FOSS Linux - CCleaner Alternatives for Ubuntu](https://www.fosslinux.com/134058/ccleaner-alternatives-for-ubuntu-a-fresh-look-at-system-cleaning-tools.htm)
  - [AlternativeTo - Stacer ve BleachBit alternatifleri](https://alternativeto.net/software/bleachbit/)

---

### 4. Kritik Yapılandırma Dosyaları ve Parametreleri

- **`/etc/tmpfiles.d/` ve `/etc/logrotate.conf`:**
  - [Linux Bash - tmpfiles.d ve logrotate açıklamaları](https://www.linuxbash.sh/post/managing-temporary-files-in-tmp-and-vartmp)
  - [WafaiCloud - logrotate ve tmpfiles.d kullanımı](https://wafaicloud.com/blog/efficient-disk-cleanup-techniques-for-linux-servers/)

---

### 5. Güvenlik Açısından Kritik Noktalar

- **Dosya Koruma ve Root Yetkileri:**
  - [HostZealot - How to Protect Files and Folders from Deletion on Linux](https://www.hostzealot.com/blog/how-to/how-to-protect-files-and-folders-from-deletion-on-linux)
  - [IT'S FOSS - Prevent Files And Folders From Accidental Deletion Or Modification In Linux](https://itsfoss.gitlab.io/post/prevent-files-and-folders-from-accidental-deletion-or-modification-in-linux/)
  - [AccuWebHosting - How to Prevent File/Directory Modification, Deletion and Renaming in Linux](https://www.accuwebhosting.com/knowledgebase/3352/How-to-Prevent-Fileor-Directory-Modification-Deletion-and-Renaming-in-Linux.html)
  - [Server Fault - Protect a file from being deleted even by root](https://serverfault.com/questions/648573/linux-is-there-a-way-to-prevent-protect-a-file-from-being-deleted-even-by-root)

---

### Ek Kaynaklar

- [LinuxLinks - Best Free and Open Source Linux System Cleaning Tools](https://www.linuxlinks.com/systemcleaning/)
- [Make Tech Easier - Best Linux System Cleaning Tools](https://www.maketecheasier.com/best-linux-system-cleaning-tools/)
