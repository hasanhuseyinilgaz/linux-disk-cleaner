# Sources for qwen

### 🔗 **Kaynak Listesi (Referanslar)**

#### **1. Temel Çalışma Prensipleri & Dosya Sistemi**

- **[1]** Red Hat Documentation – _Managing Temporary Files_:  
  https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/chap-managing_temporary_files
- **[2]** Debian Wiki – _tmpfiles.d_:  
  https://wiki.debian.org/tmpfiles.d
- **[3]** Freedesktop.org – _systemd-tmpfiles Manual_:  
  https://www.freedesktop.org/software/systemd/man/systemd-tmpfiles.html
- **[4]** Filesystem Hierarchy Standard (FHS) 3.0:  
  https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html
- **[5]** Linux man-pages project – `signal(7)`:  
  https://man7.org/linux/man-pages/man7/signal.7.html
- **[6]** TLDP – _Advanced Bash-Scripting Guide: Signals_:  
  https://tldp.org/LDP/abs/html/exitcodes.html#EXITCODESREF
- **[7]** Red Hat Customer Portal – _Difference between SIGTERM and SIGKILL_:  
  https://access.redhat.com/solutions/26181
- **[8]** systemd manual – `systemctl kill`:  
  https://www.freedesktop.org/software/systemd/man/systemctl.html#kill%20PATTERN...
- **[9]** Linux man-pages – `kill(2)`:  
  https://man7.org/linux/man-pages/man2/kill.2.html
- **[10]** ArchWiki – _systemd/Timers_:  
  https://wiki.archlinux.org/title/Systemd/Timers

---

#### **2. En İyi Uygulama Yöntemleri (Best Practices)**

- **[11]** Red Hat – _Best Practices for FHS Management_:  
  https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/managing_file_systems/index
- **[12]** Ubuntu Server Guide – _Log Rotation_:  
  https://ubuntu.com/server/docs/log-rotation
- **[13]** DigitalOcean – _How To Use Systemd Timers Instead of Cron_:  
  https://www.digitalocean.com/community/tutorials/how-to-use-systemd-timers-instead-of-cron
- **[14]** Ansible Documentation – _Configuration Management_:  
  https://docs.ansible.com/ansible/latest/user_guide/intro_configuration_management.html
- **[15]** Cloud-init Official Docs:  
  https://cloudinit.readthedocs.io/
- **[16]** systemd Security Hardening Guide (freedesktop.org):  
  https://www.freedesktop.org/software/systemd/man/systemd.exec.html

---

#### **3. Açık Kaynak Projeler (BleachBit, Stacer)**

- **[17]** BleachBit Official Website & GitHub:  
  https://www.bleachbit.org/  
  https://github.com/bleachbit/bleachbit
- **[18]** Stacer GitHub Repository:  
  https://github.com/oguzhaninan/Stacer
- **[19]** Comparison: BleachBit vs CCleaner (Linux Journal):  
  https://www.linuxjournal.com/content/bleachbit-clean-your-linux-system
- **[20]** Debian Package Tracker – BleachBit:  
  https://tracker.debian.org/pkg/bleachbit

---

#### **4. Kritik Yapılandırma Dosyaları**

- **[21]** `logrotate.conf` man page:  
  https://man7.org/linux/man-pages/man5/logrotate.conf.5.html
- **[22]** Red Hat – _Configuring logrotate_:  
  https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/assembly_managing-system-logs_configuring-basic-system-settings#configuring-log-rotation_managing-system-logs
- **[23]** systemd.unit manual:  
  https://www.freedesktop.org/software/systemd/man/systemd.unit.html
- **[24]** systemd.service manual:  
  https://www.freedesktop.org/software/systemd/man/systemd.service.html
- **[25]** `/etc/tmpfiles.d/` configuration examples (RHEL):  
  https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/assembly_managing-temporary-files_configuring-basic-system-settings

---

#### **5. Güvenlik Riskleri & CVE’ler**

- **[26]** CVE-2021-4034 (PwnKit):  
  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4034  
  https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
- **[27]** Microsoft Security Blog – _Nimbuspwn_:  
  https://msrc.microsoft.com/blog/2022/04/nimbuspwn-a-new-linux-vulnerability-collection-enabling-local-privilege-escalation/
- **[28]** CVE-2023-2163 (BPF Kernel Vulnerability):  
  https://nvd.nist.gov/vuln/detail/CVE-2023-2163
- **[29]** Red Hat Security Advisory – CVE-2016-5425:  
  https://access.redhat.com/errata/RHSA-2016:1933
- **[30]** MITRE CVE Database:  
  https://cve.mitre.org/
- **[31]** NIST National Vulnerability Database:  
  https://nvd.nist.gov/
- **[32]** OWASP – _Least Privilege Principle_:  
  https://owasp.org/www-community/attacks/Privilege_Escalation
- **[33]** Red Hat Enterprise Linux 9.2 Release Notes – _systemd timeout changes_:  
  https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/9.2_release_notes/rhel-9_2_0_release#enhancement_systemd

---

#### **Ekstra Referanslar (Genel Linux Yönetimi)**

- **[34]** The Linux Command Line (William Shotts) – Free Book:  
  https://linuxcommand.org/tlcl.php
- **[35]** Linux Foundation – _Open Source Best Practices_:  
  https://openssf.org/
- **[36]** Ubuntu Manpage – `tmpwatch` (deprecated but historical context):  
  http://manpages.ubuntu.com/manpages/focal/man8/tmpwatch.8.html
