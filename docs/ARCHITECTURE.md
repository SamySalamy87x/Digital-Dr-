# Digital Dr Architecture

## Purpose

Digital Dr is an applied AI healthcare-management prototype for doctors and healthcare teams. The platform is intended to support patient-record workflows, appointment coordination, medical-history documentation, and AI-assisted educational guidance.

## Product boundary

Digital Dr is not a regulated medical device and must not be used for autonomous diagnosis, treatment decisions, emergency triage, or replacement of licensed clinical judgment.

## Logical modules

```text
User Interface
  ├─ Doctor dashboard
  ├─ Patient profile views
  ├─ Appointment management
  └─ AI assistant interaction layer

Backend API
  ├─ Authentication and authorization
  ├─ Doctor and patient records
  ├─ Appointment services
  ├─ GPT conversation logging
  └─ Billing/subscription hooks

Data Layer
  ├─ PostgreSQL core records
  ├─ Audit logs
  ├─ Conversation metadata
  └─ Configuration tables

Integrations
  ├─ OpenAI / Custom GPT layer
  ├─ PayPal billing
  ├─ Google Calendar
  └─ Optional communication providers
```

## Security controls required before production

- JWT authentication with strong secret management.
- Password hashing with bcrypt or equivalent.
- Role-based access control for doctors, admins, and patients.
- Audit logging for patient-record access.
- No real patient data in development repositories.
- Environment variables stored outside Git.
- HTTPS-only deployment.
- Backup and restore procedures for database records.

## Data governance

Any production version must define privacy policy, consent model, retention policy, deletion workflow, and compliance requirements for the target jurisdiction before onboarding real users.
