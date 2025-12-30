# Logistics and Delivery Optimization System
# Stage 3 – Advanced Application

Bu proje, üniversite dersi kapsamında geliştirilen bir **Lojistik ve Teslimat Yönetim Sistemi**dir.  
Proje aşamalı olarak ilerlemiştir ve bu repo **Stage 3 (Advanced Application)** seviyesini temsil etmektedir.

---

# Proje Aşamaları Özeti

# Stage 1 – Architecture
- Package, Courier, Hub, Route ve DeliverySystem sınıfları tasarlandı
- Nesne tabanlı mimari kuruldu

# Stage 2 – Basic Implementation
- Paket kayıt sistemi
- Paket takip (tracking ID ile arama)
- Paket sıralama (öncelik, ağırlık, varış noktası)
- Hub’lar arası mesafe hesaplama

# Stage 3 – Advanced Application (BU AŞAMA)
✔ Multi-hub routing  
✔ Zaman ve mesafe optimizasyonu  
✔ Web tabanlı veri girişi ve raporlama  
✔ Algoritmalar ve performans analizi  
✔ Veritabanı (SQLite) entegrasyonu  

---

# Kullanılan Teknolojiler

- **Python 
- *Flask (Web Framework)
- *SQLite (Database)
- *HTML / CSS
- *Object Oriented Programming (OOP)

---

# Proje Klasör Yapısı                                                                         


---

## Web Özellikleri (Stage 3)

# Paket Ekleme
- Web arayüzünden yeni paket kaydı
- Tracking ID ile sistemde saklama

# Paket Takibi
- Tracking ID girilerek paket durumu görüntüleme

#Rota Optimizasyonu
- Hub’lar arası **en kısa mesafe hesaplama**
- Greedy / Dijkstra mantığına uygun yapı

# Raporlama
- Ortalama teslimat süresi
- Başarı oranı
- Toplam paket sayısı

---

##Kullanılan Algoritmalar

- *Mesafe Hesabı:* Öklidyen mesafe
- *En Kısa Yol:*Dijkstra (basitleştirilmiş)
- *Teslimat Gruplama: Aynı hedefe giden paketleri gruplayarak rota oluşturma
- *Sıralama:** Priority, weight, destination bazlı sorting

---

# Çalıştırma

```bash
python app.py



