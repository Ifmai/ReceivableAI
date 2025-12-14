API Dokümantasyonu — Temel Endpointler

Not: Aşağıda projedeki ana endpointlerin hızlı özeti yer alır. Detaylı request/response örnekleri için `docs/PROJECT_DOCUMENTATION.md` veya otomatik OpenAPI çıktısı oluşturulabilir.

1) Sağlık
- GET `/api/health/`
  - Açıklama: Servis durumunu kontrol eder.
  - Response: 200 OK, basit JSON `{ "status": "ok" }` veya benzeri.

2) Müşteriler (Customers)
- GET `/api/customers/` — liste
- POST `/api/customers/` — oluştur
- GET `/api/customers/{id}/` — detay
- PUT/PATCH `/api/customers/{id}/` — güncelle
- DELETE `/api/customers/{id}/` — silme

Alanlar (örnek): `name`, `email`, `phone`, `external_id`, `options`

3) Faturalar (Invoices)
- GET `/api/billing/invoices/` — liste ve filtreleme (customer, status, date range)
- POST `/api/billing/invoices/` — fatura oluştur
- GET `/api/billing/invoices/{id}/` — detay
- POST `/api/billing/invoices/{id}/pay/` veya `/payments/` ile ödeme ilişkilendirme

Alanlar (örnek): `invoice_number`, `customer`, `amount`, `currency`, `due_date`, `status`, `items`

4) Ödemeler (Payments)
- GET `/api/billing/payments/`
- POST `/api/billing/payments/` — ödeme ekle ve fatura ile eşleştir

Alanlar: `amount`, `method`, `transaction_id`, `invoice`, `customer`, `date`

5) Raporlar
- GET `/api/billing/reports/invoices-summary/` — fatura özet raporu
- GET `/api/billing/reports/customers-summary/` — müşteri bazlı rapor

6) Entegrasyonlar / n8n
- Webhook veya token korumalı endpointler: `/api/billing/integrations/`
- `X-INTEGRATION-TOKEN` başlığı ile korunan çağrılar olabilir.

7) Kimlik & Yetkilendirme
- Projede basit token / header bazlı doğrulama veya Django auth/DRF Token/Auth JWT bulunabilir. `settings.py` ve ilgili `Api/` görüntülerine bakın.
