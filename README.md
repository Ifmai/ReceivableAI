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
| Languages | Python |
| Development Tools | VSCode, Postman, Redis (optional) |

## Usage

```
$ make           # list commands
$ make up        # start services
$ make down      # stop containers
$ make re        # restart everything
$ make clean     # cleanup unused items
```

## DB Diagram

```
Invoice
 ├── id
 ├── external_invoice_id
 ├── customer_id (FK)
 ├── total_price
 ├── paid_amount
 ├── currency
 ├── status
 ├── due_date
 └── timestamps

Payment
 ├── id
 ├── invoice_id (FK)
 ├── amount
 ├── paid_at

ReminderLog
 ├── id
 ├── invoice_id (FK)
 ├── channel
 ├── status
 ├── sent_at
 ├── preview / subject
```