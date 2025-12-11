#!/usr/bin/env python3
"""Populate the local database with sample data for development.

Usage:
  python test.py

This script will:
 - configure Django settings
 - exit if any Customer records already exist (to avoid duplicates)
 - create sample customers, invoices and payments
 - print a short summary at the end

Run this after you created and migrated the database (fresh DB).
"""
import os
import sys
from decimal import Decimal
from datetime import date, timedelta


# --- Setup Django environment ---
# Ensure the inner project package (where apps live) is on sys.path when running from repo root
PROJECT_PACKAGE_DIR = os.path.join(os.path.dirname(__file__), 'collection_project')
if PROJECT_PACKAGE_DIR not in sys.path:
    sys.path.insert(0, PROJECT_PACKAGE_DIR)

# Use the same settings module as `manage.py`
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "collection_project.settings")
try:
    import django
except ModuleNotFoundError:
    sys.stderr.write("Django is not installed in the current Python environment.\n")
    sys.stderr.write("Options to fix:\n")
    sys.stderr.write("  1) Use the bundled venv in this repo (recommended if present):\n")
    sys.stderr.write("       ./env/bin/python test.py\n")
    sys.stderr.write("  2) Activate a virtualenv and install requirements:\n")
    sys.stderr.write("       source env/bin/activate\n")
    sys.stderr.write("       pip install -r collection_project/config/requirements.txt\n")
    sys.stderr.write("       python test.py\n")
    sys.stderr.write("  3) Or install Django globally (not recommended):\n")
    sys.stderr.write("       pip install Django\n")
    sys.exit(1)

django.setup()

from customers.models import Customer
from billing.Models.InvoiceModel import Invoice, Status, Currency
from billing.Models.PaymentsModel import Payment
from django.db.utils import OperationalError


def create_customers():
    data = [
        {"name": "Acme LTD", "tax_number": "TAX1001", "e_mail": "billing@acme.test", "phone": 53000000001},
        {"name": "Beta Inc", "tax_number": "TAX1002", "e_mail": "accounts@beta.test", "phone": 53000000002},
        {"name": "Gamma LLC", "tax_number": "TAX1003", "e_mail": "finance@gamma.test", "phone": 53000000003},
    ]
    created = []
    for item in data:
        c = Customer.objects.create(**item)
        created.append(c)
    return created


def create_invoices(customers):
    today = date.today()
    invoices = []

    # Acme: 1 overdue, 1 upcoming
    inv1 = Invoice.objects.create(
        customer=customers[0],
        external_invoice_id="ACME-INV-001",
        total_price=Decimal('1500.00'),
        currency=Currency.TL,
        issue_date=today - timedelta(days=40),
        due_date=today - timedelta(days=10),
    )
    inv1.recalculate_status()
    invoices.append(inv1)

    inv2 = Invoice.objects.create(
        customer=customers[0],
        external_invoice_id="ACME-INV-002",
        total_price=Decimal('750.00'),
        currency=Currency.USD,
        issue_date=today,
        due_date=today + timedelta(days=5),
    )
    inv2.recalculate_status()
    invoices.append(inv2)

    # Beta: 1 paid invoice
    inv3 = Invoice.objects.create(
        customer=customers[1],
        external_invoice_id="BETA-INV-001",
        total_price=Decimal('2000.00'),
        currency=Currency.EUR,
        issue_date=today - timedelta(days=20),
        due_date=today - timedelta(days=5),
    )
    # create a payment that covers the invoice
    Payment.objects.create(invoice=inv3, amount=Decimal('2000.00'), payment_date=today - timedelta(days=3), method='BANK_TRANSFER')
    inv3.refresh_from_db()
    invoices.append(inv3)

    # Gamma: several invoices
    for i in range(1, 4):
        inv = Invoice.objects.create(
            customer=customers[2],
            external_invoice_id=f"GAMMA-INV-00{i}",
            total_price=Decimal(str(100 * i)),
            currency=Currency.TL,
            issue_date=today - timedelta(days=2 * i),
            due_date=today + timedelta(days=7 * i),
        )
        inv.recalculate_status()
        invoices.append(inv)

    return invoices


def summary():
    from django.db.models import Count
    c_count = Customer.objects.count()
    inv_count = Invoice.objects.count()
    pay_count = Payment.objects.count()
    print("\n=== Sample Data Summary ===")
    print(f"Customers: {c_count}")
    print(f"Invoices: {inv_count}")
    print(f"Payments: {pay_count}")
    print("===========================\n")


def main():
    # Prevent accidental re-inserts
    try:
        if Customer.objects.exists():
            print("Database already contains customers. Aborting to avoid duplicate sample data.")
            print("If you want to re-create sample data drop DB or remove existing rows first.")
            sys.exit(0)
    except OperationalError as exc:
        sys.stderr.write("\nCould not connect to the configured database.\n")
        sys.stderr.write(f"Reason: {exc}\n\n")
        sys.stderr.write("Possible fixes:\n")
        sys.stderr.write(" 1) If you use Docker Compose, start services so the DB hostname resolves:\n")
        sys.stderr.write("      docker compose up -d\n")
        sys.stderr.write("    Then run this script inside the same compose network or wait until DB is reachable.\n")
        sys.stderr.write(" 2) If you have a local Postgres, point the app to it before running this script:\n")
        sys.stderr.write("      export POSTGRES_HOST=127.0.0.1\n")
        sys.stderr.write("      python test.py\n")
        sys.stderr.write(" 3) Quick local fallback (sqlite) — create a temporary env var to force sqlite fallback:\n")
        sys.stderr.write("      export FORCE_SQLITE=1\n")
        sys.stderr.write("      python test.py\n")
        sys.stderr.write("    (Or ask me to enable an automatic sqlite fallback in this script.)\n")
        sys.exit(1)

    print("Creating sample customers...")
    customers = create_customers()
    print("Creating sample invoices and payments...")
    create_invoices(customers)
    summary()


if __name__ == '__main__':
    main()
