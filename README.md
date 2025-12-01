# جیب (Jeeb) - سیستم مدیریت مالی شخصی

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
