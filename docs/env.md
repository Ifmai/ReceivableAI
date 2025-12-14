Ortam Değişkenleri (env)

Kök dizindeki `env_template` dosyası proje için örnek değişkenleri içerir. Aşağıda en kritik değişkenlerin açıklamaları bulunur.

- `DJANGO_SECRET_KEY` — Django için gizli anahtar. Prod ortamda güçlü, rastgele bir değer kullanın.
- `DJANGO_DEBUG` — `True`/`False`. Prod için `False` olmalı.
- `POSTGRES_DB` — Veritabanı adı.
- `POSTGRES_USER` — Veritabanı kullanıcı adı.
- `POSTGRES_PASSWORD` — Veritabanı parolası.
- `POSTGRES_HOST` — Postgres host (Docker Compose içinde servis adı olabilir, ör. `db`).
- `POSTGRES_PORT` — Postgres port (varsayılan 5432).
- `SALT_CODE` — İmza veya hash işlemleri için salt.
- `X-INTEGRATION-TOKEN` — n8n veya dış entegrasyonların çağrıları için kullanılabilecek ortak token.
