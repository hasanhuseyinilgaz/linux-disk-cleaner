# Sources for deepseek

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
