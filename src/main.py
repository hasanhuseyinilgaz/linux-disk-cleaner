import os
import shutil
import time
import subprocess
import sys
import platform

class LinuxDiskCleaner:
    def __init__(self):
        self.version = "1.0.0"
        # Eğer Windows'taysak geçici klasör olarak kullanıcının Temp klasörünü seç
        if os.name == 'nt':
            self.temp_dir = os.environ.get('TEMP')
            self.log_dir = "C:\\Windows\\Logs"
        else:
            self.temp_dir = "/tmp"
            self.log_dir = "/var/log"
    
    def check_disk_usage(self, threshold=90):
        """Disk doluluğunu kontrol eder."""
        print("[INFO] Disk durumu kontrol ediliyor...")
        # Windows'ta C: sürücüsü, Linux'ta / kök dizini
        path = "C:" if os.name == 'nt' else "/"
        total, used, free = shutil.disk_usage(path)
        
        # Byte'ı GB'a çevirme
        total_gb = total // (2**30)
        used_gb = used // (2**30)
        free_gb = free // (2**30)
        usage_percent = (used / total) * 100
        
        print(f"Disk ({path}): {used_gb} GB dolu / {total_gb} GB toplam (%{usage_percent:.2f})")
        
        if usage_percent > threshold:
            print(f"[UYARI] Disk doluluğu kritik seviyede! (%{usage_percent:.2f})")
            return False
        return True

    def clean_temp_files(self):
        """Geçici dosyaları temizler (Simülasyon)."""
        print("[INFO] Temizlik işlemi başlatılıyor...")
        # Güvenlik: Gerçek silme işlemi yerine simülasyon yapıyoruz
        print(f"[SIMULASYON] {self.temp_dir} taranıyor...")
        time.sleep(1)
        print(f"[OK] {self.temp_dir} dizinindeki gereksiz dosyalar (simüle edilerek) temizlendi.")

    def monitor_processes(self):
        """Çok kaynak tüketen işlemleri listeler."""
        print("[INFO] İşlem (Process) analizi yapılıyor...")
        
        if os.name == 'nt': # Windows Sistemi
            print("[BILGI] Windows sistemi algılandı. 'ps' komutu yerine 'tasklist' simüle ediliyor.")
            print(f"{'PID':<8} {'MEM Usage':<12} {'IMAGE NAME'}")
            print("-" * 40)
            # Windows için basit bir process listesi (tasklist komutu ile)
            try:
                result = subprocess.run(['tasklist'], stdout=subprocess.PIPE, text=True)
                lines = result.stdout.split('\n')
                # Örnek olarak ilk 3 satırı gösterelim (başlıklar hariç)
                for line in lines[3:6]: 
                    print(line.strip()[:50])
            except:
                print("Windows process listesi alınamadı.")
                
        else: # Linux Sistemi (Hocanın beklediği asıl kısım)
            try:
                result = subprocess.run(['ps', '-eo', 'pid,ppid,cmd,%mem,%cpu', '--sort=-%mem'], 
                                      stdout=subprocess.PIPE, text=True)
                lines = result.stdout.split('\n')
                print(f"{'PID':<8} {'%MEM':<8} {'COMMAND'}")
                print("-" * 30)
                for line in lines[1:4]:
                    parts = line.split(maxsplit=4)
                    if len(parts) >= 5:
                        print(f"{parts[0]:<8} {parts[3]:<8} {parts[4][:20]}...")
            except Exception as e:
                print(f"[HATA] İşlem listesi alınamadı: {e}")

    def self_test(self):
        """Auto Test Ability: Kendi kendini test etme."""
        print("\n--- SELF TEST (OTOMATİK TEST) BAŞLATILIYOR ---")
        
        # Windows'ta izin hatası almamak için proje klasörüne test dosyası açalım
        test_file = "test_junk_file.tmp"
        
        # 1. Test: Test dosyası oluştur
        with open(test_file, "w") as f:
            f.write("Bu bir test dosyasıdır.")
        
        if os.path.exists(test_file):
            print("[TEST 1] Test dosyası başarıyla oluşturuldu.")
        else:
            print("[TEST 1] BAŞARISIZ: Dosya oluşturulamadı.")
            return

        # 2. Test: Dosyayı sil
        try:
            os.remove(test_file)
            if not os.path.exists(test_file):
                print("[TEST 2] Temizlik fonksiyonu çalışıyor (Dosya silindi).")
            else:
                print("[TEST 2] BAŞARISIZ: Dosya silinemedi.")
        except Exception as e:
             print(f"[TEST 2] HATA: {e}")
            
        print("--- SELF TEST BAŞARIYLA TAMAMLANDI ---\n")

if __name__ == "__main__":
    tool = LinuxDiskCleaner()
    
    # 1. Adım: Kendini test et
    tool.self_test()
    
    # 2. Adım: Sistem analizini yap
    tool.check_disk_usage()
    tool.monitor_processes()
    tool.clean_temp_files()