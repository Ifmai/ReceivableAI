#!/bin/sh

DB_HOST="$POSTGRES_HOST"
DB_USER="$POSTGRES_USER"
DB_PASSWORD="$POSTGRES_PASSWORD"
DB_PORT="$POSTGRES_PORT"

echo "$DB_HOST" "$DB_USER" "$DB_PASSWORD" "$DB_PORT" "merhaba"

until PGPASSWORD="$DB_PASSWORD" pg_isready -h "$DB_HOST" -U "$DB_USER" -p "$DB_PORT"; do
  >&2 echo "Veritabanı $DB_HOST hazır değil - bekleniyor..."
  sleep 2
done

>&2 echo "Veritabanı hazır."

python manage.py makemigrations
python manage.py migrate

# Collect static files for Nginx to serve
echo "Collecting static files..."
python manage.py collectstatic --noinput || echo "collectstatic failed or nothing to collect"
# Ensure static folder permissions
mkdir -p /collection_project/staticfiles || true
chown -R root:root /collection_project/staticfiles || true

exec "$@"
