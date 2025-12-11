# AI-Collections — Proje Dokümantasyonu

Kısa açıklama: Fatura, ödeme ve hatırlatma (reminder) mikroservisi. Django REST Framework ile yazılmıştır.

## Hızlı Başlangıç
- Ortam değişkenlerini `.env` dosyasına koyun. Örnekler ve zorunlular:
  - `DJANGO_SECRET_KEY` — `collection_project/collection_project/settings.py`
  - `DJANGO_DEBUG` — `collection_project/collection_project/settings.py`
  - `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT` — `docker-compose.yml` ve `collection_project/config/start.sh`
  - `SALT_CODE` ve `X-INTEGRATION-TOKEN` — kullanılan şifreleme tuzları: `collection_project/collection_project/settings.py`

Docker ile çalıştırmak için:
- Servisleri ayağa kaldır:
  - `make up` veya `sudo docker compose -f docker-compose.yml up -d`
  - Docker build: `make build`
- Docker Compose dosyası: `docker-compose.yml`
- Proje konteyner entrypoint: `collection_project/config/start.sh`
- Proje Dockerfile: `collection_project/dockerfile`
- Gereksinimler: `collection_project/config/requirements.txt`

Yerel geliştirme:
- Sanal ortam oluşturup paketleri yükleyin veya Docker kullanın.
- Veritabanı hazır olduğunda:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
  - `python manage.py runserver`

Makefile komutları: `Makefile`

## API Özeti (başlıca endpoint'ler)
- Sağlık kontrol: GET `/api/health/` — handler: `collection_project/utils/health.py`
- Müşteriler: `/api/customers/` — router: `collection_project/customers/urls.py`, view'ler: `collection_project/customers/Api/view.py`
- Faturalar ve raporlar: `/api/billing/` — router: `collection_project/billing/Api/urls.py`
  - Fatura view'leri: `collection_project/billing/Api/Invoice/views.py`
  - Raporlar: `collection_project/billing/Api/Invoice/reports_view.py`
- Ödemeler: `collection_project/billing/Api/Payments/views.py`, `collection_project/billing/Api/Payments/serializers.py`
- Entegrasyon (n8n) endpoint: `collection_project/billing/Api/N8N/urls.py` ve view: `InvoiceReminderCandidatesView`
- Hatırlatma (notifications): `collection_project/notifications/Api/urls.py` ve view'ler: `collection_project/notifications/Api/views.py`

Örnek cURL:
- Sağlık:
  - curl -X GET http://localhost:8000/api/health/
- n8n entegrasyon (X-INTEGRATION-TOKEN gerekli):
  - curl -H "X-INTEGRATION-TOKEN: <token>" "http://localhost:8000/api/billing/integrations/invoices/reminder-candidates/?days=7"

## Önemli modeller ve yardımcılar
- Fatura modeli ve sorgu seti: `collection_project/billing/Models/InvoiceModel.py`
  - Önemli method: `Invoice.recalculate_status`
  - QuerySet metotları: `upcoming`, `overdue`, `reminder` — implementasyon: `InvoiceQuerySet`
- Ödeme modeli: `collection_project/billing/Models/PaymentsModel.py` — `save`/`delete` sonrası fatura durumu güncellenir.
- Hatırlatma logu: `collection_project/notifications/models.py`
- Müşteri modeli: `collection_project/customers/models.py`

Şifreleme / ID encode-decode:
- ID encode/decode: `collection_project/utils/sign.py` (`encode_id`, `decode_id`)
- Entegrasyon anahtarı encode/decode: `collection_project/utils/sign.py` (`encode_key`, `decode_key`)

Yetkilendirme (n8n):
- N8n istekleri için permission sınıfı: `collection_project/permission/n8n_permission.py`

Serileştiriciler:
- Invoice serileştiriciler: `collection_project/billing/Api/Invoice/serializers.py`
- Payment serileştiriciler: `collection_project/billing/Api/Payments/serializers.py`
- Reminder serileştirici: `collection_project/notifications/Api/serializers.py`

## Raporlar (InvoiceReportsSummary & CustomerReportsSummary)
- `InvoiceReportsSummary`:
  - Genel sayaçlar: toplam fatura, pending, paid, overdue.
  - Para birimi bazlı toplamlar: `total_price_invoice`, `total_paid_amount`, `total_outstanding`.
  - Önümüzdeki 7 gün (reminder) için sayaç ve para birimi bazlı toplamlar.
  - Overdue olanların 7 gün içindeki özetleri.
- `CustomerReportsSummary`:
  - Verilen müşteri için aynı sayaçlar ve para birimi bazlı toplamlar.
  - Müşterinin önümüzdeki 7 gün içerisinde gelen en fazla 5 faturası (`upcoming(days=7)`).

Not: `reports_view.py` içinde `decode_id` kullanılarak müşteri kimliği çözülür; hatalı id durumunda `NotFound` döner.

## Geliştirme notları
- ID'ler URL'lerde ve API yanıtlarında encode edilir/çözülür (`utils/sign.py`).
- `Invoice.recalculate_status` ödeme toplamına göre faturanın `status` ve `paid_amount` alanlarını günceller.
- `Invoice` modelinde `Meta.ordering` ile overdue öne alınır.
- `reports_view.py` içinde currency toplamlarını hesaplamak için `annotate` ve `F()` kullanımı mevcut; toplamların garanti olması için null durumları kontrol edilmiştir.

## Testler ve kontrol
- Django testleri: `python manage.py test`.
- Test dosyaları proje içindeki app'lerde `tests.py` veya `tests/` dizininde bulunur.

## Faydalı dosyalar
- Proje ayarları: `collection_project/collection_project/settings.py`
- Manage komut satırı: `collection_project/manage.py`
- Docker Compose: `docker-compose.yml`
- Başlangıç scripti: `collection_project/config/start.sh`

## Katkıda bulunma
- Yeni özellik için branch açın, test ekleyin, PR gönderin.
- Kod stiline dikkat edin ve database migration ekleyin.

## Lisans
- Proje root'ta lisans dosyası yok — uygun bir lisans (ör. MIT) ekleyin.
