Sistem Mimarisi — AI-Collections

1) Bileşenler
- `web` (Django REST): API, iş mantığı, modeller ve yönetim komutları.
- `db` (PostgreSQL): kalıcı veri; faturalar, müşteriler, ödemeler, loglar.
- `proxy` (opsiyonel NGINX): ters proxy, statik içerik ve TLS sonlandırma.
- `n8n`: iş akışları, otomasyon ve webhook tetikleyicileri.
- `docker-compose`: bileşenleri yerel ve üretim benzeri ortamda çalıştırmak için.

2) Veri akışı (kısa)
- Kullanıcı/servis → `web` API (REST). API doğrulama/izin kontrolü yapılır.
- `web` → `db` (Postgres) — kayıt/sorgu işlemleri.
- Hatırlatma/otomasyon: `web` içindeki belirli event'ler n8n ile webhook veya token tabanlı entegrasyonla tetiklenir.

3) Kritik dosya ve klasörler
- `collection_project/` — Django proje kaynakları
- `collection_project/manage.py` — yönetim komutları
- `billing/Models` — fatura/ödemeye dair modeller
- `docs/PROJECT_DOCUMENTATION.md` — daha detaylı iç analiz ve ER diyagramları

4) Ölçekleme / Operasyonel notlar
- Veritabanı için yedekleme ve read-replica düşünün.
- Asenkron işler (büyük raporlar / e-posta gönderimi) için task queue (Celery/RQ) eklenebilir.
- n8n iş akışları için ayrı backup ve versiyonlama tutun.
