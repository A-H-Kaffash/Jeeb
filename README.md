# Jeeb (جیب) - Personal Finance Management System

> [🇮🇷 Persian Documentation (مستندات فارسی)](#-مستندات-فارسی)

## Introduction

**Jeeb** (meaning "pocket" in Persian) is a personal finance management application built with the **Django** framework. It allows users to manage their financial accounts, categories, and transactions.

---

## Project Structure

```
Jeeb/
├── manage.py                 # Django entry point for running commands
├── requirements.txt          # Project dependencies
├── Jeeb/                     # Main Django settings folder
│   ├── __init__.py
│   ├── settings.py           # Project settings
│   ├── urls.py               # Main URL routing
│   ├── wsgi.py               # WSGI entry point
│   └── asgi.py               # ASGI entry point
└── core/                     # Main application
    ├── models.py             # Database models
    ├── views.py              # Views and APIs
    ├── urls.py               # Application URL routing
    ├── admin.py              # Admin panel configuration
    ├── signals.py            # Signals
    ├── tests.py              # Tests
    └── management/commands/  # Custom management commands
        └── process_transactions.py
```

---

## Models

The project has 4 main models:

### 1. Account
Stores users' financial accounts.

| Field | Type | Description |
|-------|------|-------------|
| `name` | CharField | Account name (unique) |
| `owner` | ForeignKey(User) | Account owner |
| `card_number` | CharField | Card number |
| `balance` | DecimalField | Balance |

### 2. Category
Transaction categories (income or expense).

| Field | Type | Description |
|-------|------|-------------|
| `name` | CharField | Category name |
| `transaction_type` | CharField | Transaction type: `INCOME` or `EXPENSE` |
| `user` | ForeignKey(User) | User |
| `description` | TextField | Description |

### 3. Transaction
Users' financial transactions.

| Field | Type | Description |
|-------|------|-------------|
| `user` | ForeignKey(User) | User |
| `account` | ForeignKey(Account) | Account |
| `amount` | DecimalField | Amount |
| `category` | ForeignKey(Category) | Category |
| `date` | DateField | Transaction date |
| `description` | TextField | Description |
| `is_processed` | BooleanField | Is processed? |

### 4. Token
Authentication token for each user.

| Field | Type | Description |
|-------|------|-------------|
| `user` | OneToOneField(User) | User |
| `string` | CharField | Token string (64 characters) |

---

## APIs (Views)

The project has 3 main APIs:

### 1. User Registration
- **Endpoint:** `POST /api/register`
- **Parameters:**
  - `username`: Username
  - `email`: Email
  - `password`: Password

### 2. User Login
- **Endpoint:** `POST /api/login`
- **Parameters:**
  - `username`: Username
  - `password`: Password
- **Response:** Authentication token

### 3. Submit Transaction
- **Endpoint:** `POST /api/submit-transaction/`
- **Parameters:**
  - `token`: User token
  - `amount`: Amount
  - `category_id`: Category ID
  - `account_id`: Account ID
  - `description`: Description (optional)
  - `date`: Transaction date (format: `YYYY-MM-DD`, optional)

---

## Signals

When a new user is created, automatically:
1. Two default categories are created:
   - `Default Expense`
   - `Default Income`
2. A unique 64-character token is generated

---

## Management Commands

### Process Transactions
To process scheduled transactions:
```bash
python manage.py process_transactions
```
This command processes transactions whose date has arrived and have not yet been processed.

---

## Admin Panel

All models are registered in the Django admin panel:
- **Path:** `/admin/`
- **Models:** Account, Category, Transaction, Token

---

## Installation and Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Create Admin User
```bash
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
python manage.py runserver
```

---

## Dependencies

- Django 5.2.8
- asgiref 3.11.0
- sqlparse 0.5.4
- tzdata 2025.2

---

## Database

The project uses **SQLite3** by default. The database file is stored in `db.sqlite3`.

---

## Development Notes

- The project is in **DEBUG** mode and security changes should be applied before deploying to production.
- `SECRET_KEY` should be changed to a secure value.
- `ALLOWED_HOSTS` should be configured for production environment.

---

---

# 🇮🇷 مستندات فارسی

## معرفی
**جیب** یک اپلیکیشن مدیریت مالی شخصی است که با استفاده از فریم‌ورک **Django** توسعه داده شده است. این برنامه به کاربران امکان می‌دهد حساب‌های مالی، دسته‌بندی‌ها و تراکنش‌های خود را مدیریت کنند.

---

## ساختار کلی پروژه

```
Jeeb/
├── manage.py                 # نقطه ورود Django برای اجرای دستورات
├── requirements.txt          # وابستگی‌های پروژه
├── Jeeb/                     # پوشه تنظیمات اصلی Django
│   ├── __init__.py
│   ├── settings.py           # تنظیمات پروژه
│   ├── urls.py               # مسیریابی اصلی URL ها
│   ├── wsgi.py               # نقطه ورود WSGI
│   └── asgi.py               # نقطه ورود ASGI
└── core/                     # اپلیکیشن اصلی
    ├── models.py             # مدل‌های دیتابیس
    ├── views.py              # View ها و API ها
    ├── urls.py               # مسیریابی URL های اپلیکیشن
    ├── admin.py              # تنظیمات پنل ادمین
    ├── signals.py            # سیگنال‌ها
    ├── tests.py              # تست‌ها
    └── management/commands/  # دستورات مدیریتی سفارشی
        └── process_transactions.py
```

---

## مدل‌ها (Models)

پروژه دارای ۴ مدل اصلی است:

### ۱. Account (حساب)
حساب‌های مالی کاربران را ذخیره می‌کند.

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `name` | CharField | نام حساب (یکتا) |
| `owner` | ForeignKey(User) | صاحب حساب |
| `card_number` | CharField | شماره کارت |
| `balance` | DecimalField | موجودی |

### ۲. Category (دسته‌بندی)
دسته‌بندی تراکنش‌ها (درآمد یا هزینه).

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `name` | CharField | نام دسته‌بندی |
| `transaction_type` | CharField | نوع تراکنش: `INCOME` یا `EXPENSE` |
| `user` | ForeignKey(User) | کاربر |
| `description` | TextField | توضیحات |

### ۳. Transaction (تراکنش)
تراکنش‌های مالی کاربران.

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `user` | ForeignKey(User) | کاربر |
| `account` | ForeignKey(Account) | حساب |
| `amount` | DecimalField | مبلغ |
| `category` | ForeignKey(Category) | دسته‌بندی |
| `date` | DateField | تاریخ تراکنش |
| `description` | TextField | توضیحات |
| `is_processed` | BooleanField | آیا پردازش شده است؟ |

### ۴. Token (توکن)
توکن احراز هویت برای هر کاربر.

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `user` | OneToOneField(User) | کاربر |
| `string` | CharField | رشته توکن (۶۴ کاراکتر) |

---

## API ها (Views)

پروژه دارای ۳ API اصلی است:

### ۱. ثبت نام کاربر
- **مسیر:** `POST /api/register`
- **پارامترها:**
  - `username`: نام کاربری
  - `email`: ایمیل
  - `password`: رمز عبور

### ۲. ورود کاربر
- **مسیر:** `POST /api/login`
- **پارامترها:**
  - `username`: نام کاربری
  - `password`: رمز عبور
- **خروجی:** توکن احراز هویت

### ۳. ثبت تراکنش
- **مسیر:** `POST /api/submit-transaction/`
- **پارامترها:**
  - `token`: توکن کاربر
  - `amount`: مبلغ
  - `category_id`: شناسه دسته‌بندی
  - `account_id`: شناسه حساب
  - `description`: توضیحات (اختیاری)
  - `date`: تاریخ تراکنش (فرمت: `YYYY-MM-DD`، اختیاری)

---

## سیگنال‌ها (Signals)

هنگام ایجاد کاربر جدید، به صورت خودکار:
1. دو دسته‌بندی پیش‌فرض ایجاد می‌شود:
   - `Default Expense` (هزینه پیش‌فرض)
   - `Default Income` (درآمد پیش‌فرض)
2. یک توکن منحصر به فرد ۶۴ کاراکتری ایجاد می‌شود

---

## دستورات مدیریتی (Management Commands)

### پردازش تراکنش‌ها
برای پردازش تراکنش‌های زمان‌بندی شده:
```bash
python manage.py process_transactions
```
این دستور تراکنش‌هایی که تاریخ آنها رسیده و هنوز پردازش نشده‌اند را پردازش می‌کند.

---

## پنل ادمین

تمام مدل‌ها در پنل ادمین Django ثبت شده‌اند:
- **مسیر:** `/admin/`
- **مدل‌ها:** Account، Category، Transaction، Token

---

## نصب و راه‌اندازی

### ۱. نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```

### ۲. اجرای مهاجرت‌ها
```bash
python manage.py migrate
```

### ۳. ایجاد کاربر ادمین
```bash
python manage.py createsuperuser
```

### ۴. اجرای سرور توسعه
```bash
python manage.py runserver
```

---

## وابستگی‌ها

- Django 5.2.8
- asgiref 3.11.0
- sqlparse 0.5.4
- tzdata 2025.2

---

## پایگاه داده

پروژه به صورت پیش‌فرض از **SQLite3** استفاده می‌کند. فایل دیتابیس در `db.sqlite3` ذخیره می‌شود.

---

## یادداشت‌های توسعه

- پروژه در حالت **DEBUG** است و قبل از استقرار در محیط تولید، باید تغییرات امنیتی اعمال شود.
- `SECRET_KEY` باید به یک مقدار امن تغییر کند.
- `ALLOWED_HOSTS` باید برای محیط تولید تنظیم شود.
