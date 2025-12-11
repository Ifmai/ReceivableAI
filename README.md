# AI-Collections — Billing, Payments & Reminder Microservice

## Index
- [Technology Stack](#technology-stack)
- [Usage](#usage)
- [Architecture Diagram](#architecture-diagram)
- [DB Diagram](#db-diagram)
- [Supported Features](#supported-features)

## Technology Stack

| Category | Technology |
|---------|------------|
| Server | NGINX |
| Backend Framework | Django REST Framework |
| Database | PostgreSQL |
| Containerization | Docker / Docker Compose |
| Messaging / Automation | n8n |
````markdown
# AI-Collections — Fatura, Ödeme & Hatırlatma Servisi

Kısa açıklama: Bu proje, faturaların, ödemelerin ve hatırlatmaların yönetildiği bir Django REST servisidir. Docker ile çalışacak şekilde yapılandırılmıştır.

## Hızlı Başlangıç

1. Ortam değişkenlerini ayarlayın. `env_template` dosyasını kullanarak `.env` oluşturun ve özellikle aşağılarını doldurun:
	- `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`
	- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`
	- `SALT_CODE`, `X-INTEGRATION-TOKEN` (n8n entegrasyon için)

2. Docker ile başlatma (önerilen):

```bash
make up        # servisleri ayağa kaldırır
make down      # durdurur
make re        # yeniden başlatır
```

3. Docker kullanmadan geliştirme:

```bash
python -m venv .env
source .env/bin/activate
pip install -r collection_project/config/requirements.txt
python collection_project/manage.py migrate
python collection_project/manage.py runserver
```

## Önemli Dosyalar ve Konumlar

- Proje ayarları: `collection_project/collection_project/settings.py`
- Yönetim komutları: `collection_project/manage.py`
- Docker Compose: `docker-compose.yml`
- Başlangıç scripti: `collection_project/config/start.sh`
- Proje dökümü: `docs/PROJECT_DOCUMENTATION.md`

## API Özet (Hızlı)

- Sağlık: GET `/api/health/`
- Müşteriler: `/api/customers/`
- Faturalar: `/api/billing/invoices/` (create, list, detail)
- Ödemeler: `/api/billing/payments/`
- Raporlar: `/api/billing/reports/` (InvoiceReportsSummary, CustomerReportsSummary)
- N8N entegrasyonları: `/api/billing/integrations/` (X-INTEGRATION-TOKEN ile korunmuş olabilir)

Detaylı API endpointleri ve request/response örnekleri için `docs/PROJECT_DOCUMENTATION.md` dosyasına bakın.

## Testler

Projede Django testleri bulunur. Çalıştırmak için:

```bash
python collection_project/manage.py test
```

## Katkıda Bulunma

- Yeni özellik için branch açın.
- Değişikliklere test ekleyin.
- PR gönderin ve açıklama ekleyin.

## Lisans

Root dizinde lisans dosyası yok. İsterseniz MIT veya uygun başka bir lisans ekleyin.

````