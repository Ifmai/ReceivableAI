ReceivableAI — Fatura, Ödeme & Hatırlatma Servisi
------------------

Bu repo, fatura yönetimi, ödemeler ve hatırlatmalar için hazırlanmış bir Django REST servisidir. Servis Docker ile çalışacak şekilde yapılandırılmıştır ve n8n ile entegrasyon desteği içerir.

Önemli özellikler
------------------
- Fatura CRUD işlemleri
- Ödeme kaydı ve eşleme
- Hatırlatma (reminder) loglama ve tetikleme
- Raporlama endpointleri
- n8n entegrasyonları ve webhook desteği

Technology Stack
----------------
| Category | Technology |
|---|---|
| Backend Framework | ![Django REST](https://img.shields.io/badge/Django%20REST-092E20?style=for-the-badge&logo=django&logoColor=white) |
| Database | ![Postgres](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white) |
| Containerization & Services | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)&nbsp;![n8n](https://img.shields.io/badge/n8n-6CC24A?style=for-the-badge) |
| Languages | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| Development Tools | ![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code)&nbsp;![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman) |
| Libraries (from `requirements.txt`) | ![Django 4.0](https://img.shields.io/badge/Django-4.0-092E20?style=for-the-badge&logo=django&logoColor=white)&nbsp;![DRF 3.15.1](https://img.shields.io/badge/DRF-3.15.1-00BCD4?style=for-the-badge)&nbsp;![django-filter 23.5](https://img.shields.io/badge/django--filter-23.5-8A2BE2?style=for-the-badge)&nbsp;![Pillow 10.4.0](https://img.shields.io/badge/Pillow-10.4.0-FFB6C1?style=for-the-badge)&nbsp;![Requests 2.32.3](https://img.shields.io/badge/Requests-2.32.3-005A9C?style=for-the-badge)&nbsp;![psycopg2-binary 2.9.9](https://img.shields.io/badge/psycopg2--binary-2.9.9-336791?style=for-the-badge) |

Gereksinimler
----------------
- Python 3.11
- Docker & Docker Compose (opsiyonel ama önerilir)
- PostgreSQL (Docker ile otomatik sağlanır)

Hızlı Kurulum (Docker ile) — önerilen
------------------------------------------------
1. Ortam değişkeni şablonunu kullanarak `.env` oluşturun:

	 - Kök dizindeki `env_template` dosyasını inceleyin ve kopyalayın:

		 cp env_template .env

	 - Önemli değişkenler:
		 - `DJANGO_SECRET_KEY` — Django secret key
		 - `DJANGO_DEBUG` — `True`/`False`
		 - `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`
		 - `SALT_CODE`, `X-INTEGRATION-TOKEN` (n8n veya entegrasyonlar için)

2. Servisleri ayağa kaldırın:

```bash
docker-compose up --build
# veya repository içinde tanımlı ise
make up
```

3. Veritabanı migrasyonlarını uygula (container içinde veya yönetim konteyneri ile):
(Dev aşamasında çalıştırırken hızlı yapabilmeniz için start.sh dosyasında yazılmıştır. /config/start.sh)

```bash
docker exec web python collection_project/manage.py migrate
```

Geliştirme (Docker olmadan)
---------------------------------
1. Sanal ortam oluşturun ve aktif edin:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Bağımlılıkları yükleyin:

```bash
pip install -r config/requirements.txt
```

3. Veritabanı ayarlarını yapın (env) ve migrasyonları çalıştırın, ardından server'ı başlatın:

```bash
python collection_project/manage.py migrate
python collection_project/manage.py runserver
```

Örnek data seti yüklemek için
--------
Docker ile içeriye gönderdiğim test.py dosyasını çalıştırarak ekleyebilirsiniz:

```bash
docker exec collection_project_container python test.py
```

Docker komutları (kısa)
------------------------
- `make up` — Servisleri ayağa kaldırır (eğer `Makefile` var ve yapılandırılmışsa)
- `make down` — Servisleri durdurur
- `make re` — Yeniden başlatır

Önemli dosyalar
----------------
- Proje ayarları: [collection_project/collection_project/settings.py](collection_project/collection_project/settings.py)
- Yönetim komutları: [collection_project/manage.py](collection_project/manage.py)
- Docker Compose: [docker-compose.yml](docker-compose.yml)
- Dökümantasyon: [docs/PROJECT_DOCUMENTATION.md](docs/PROJECT_DOCUMENTATION.md)
- Dokümantasyon (detaylı): [docs/README.md](docs/README.md)

API kısa açıklama
-------------------
- Sağlık kontrolü: `GET /api/health/`
- Müşteri endpointleri: `/api/customers/`
- Fatura endpointleri: `/api/billing/invoices/`
- Ödeme endpointleri: `/api/billing/payments/`
- Raporlama: `/api/billing/reports/`

Katkıda bulunma
------------------
1. Yeni bir branch oluşturun: `git checkout -b feature/isim`
2. Değişikliklerinize test ekleyin.
3. PR oluşturun ve açıklama ekleyin.

Lisans
-------
Bu proje MIT lisansı ile lisanslanmıştır. Lisans metni için kök dizindeki [LICENSE](LICENSE) dosyasına bakın.

İletişim
---------
Projeyle ilgili sorular veya katkı teklifleri için repository sahibi ile iletişime geçin.
