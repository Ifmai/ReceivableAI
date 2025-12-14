Dağıtım & Çalıştırma

Docker (önerilen)
-----------------
1. `.env` oluşturun (kök dizindeki `env_template` kullanın).

2. Servisleri ayağa kaldırın:

```bash
docker-compose up --build -d
```

3. Migrasyonları çalıştırın:

```bash
docker-compose exec web python collection_project/manage.py migrate
```

4. Yönetim kullanıcı oluşturma (opsiyonel):

```bash
docker-compose exec web python collection_project/manage.py createsuperuser
```

Geliştirme (Docker olmadan)
---------------------------
1. Sanal ortam oluşturun:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Bağımlılıkları yükleyin:

```bash
pip install -r config/requirements.txt
```

3. Migrasyon ve başlatma:

```bash
python collection_project/manage.py migrate
python collection_project/manage.py runserver
```

Loglar ve hata ayıklama
----------------------
- Docker konteyner loglarını görmek için:

```bash
docker-compose logs -f
```

Testler
------
```bash
python collection_project/manage.py test
```

Devam eden işler / İyileştirmeler
-------------------------------
- OpenAPI/Swagger dokümantasyonu otomatik uyarlaması (drf-yasg veya drf-spectacular) ekleyerek `docs/api.md`'yi makine okunur hale getirebilirsiniz.
- CI/CD pipeline ekleyin: test, lint, security taramaları ve image push adımları.
