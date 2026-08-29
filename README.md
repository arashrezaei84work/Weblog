# 📝 وبلاگ آرش | Weblog

یک پلتفرم وبلاگ‌نویسی کامل و RTL (فارسی) ساخته‌شده با Django، شامل سیستم مدیریت محتوا، پنل ادمین سفارشی، سیستم کامنت و لایک، جستجو، و بهینه‌سازی برای موتورهای جستجو (SEO).

## ✨ امکانات

- 📰 مدیریت پست‌های وبلاگ با دسته‌بندی، تصویر شاخص و وضعیت انتشار (پیش‌نویس/منتشرشده)
- 👤 سیستم احراز هویت کامل: ثبت‌نام، ورود، ویرایش پروفایل
- ✍️ امکان ساخت و ویرایش پست توسط کاربران (با تایید مدیر قبل از انتشار)
- 💬 سیستم کامنت‌گذاری با کپچا و تایید مدیر
- ❤️ لایک برای پست‌ها و کامنت‌ها
- 🔍 جستجوی مقالات
- 🎛️ **پنل مدیریت سفارشی** با طراحی گلس‌مورفیسم مدرن (مدیریت پست‌ها، کامنت‌ها، کاربران و دسته‌بندی‌ها) — مستقل از پنل ادمین جنگو
- 🗺️ Sitemap و `robots.txt` خودکار برای SEO
- 📱 طراحی کاملاً ریسپانسیو (RTL) با فونت وزیرمتن

## 🛠️ تکنولوژی‌ها

| بخش | ابزار |
|---|---|
| بک‌اند | Django 4.2 |
| دیتابیس | SQLite (پیش‌فرض توسعه) |
| فرانت‌اند | HTML, CSS خالص (بدون فریم‌ورک)، فونت Vazirmatn |
| کپچا | django-simple-captcha |
| SEO | django-robots, django.contrib.sitemaps |
| مدیریت متغیرهای محیطی | python-dotenv |

## 🚀 راه‌اندازی محلی

### پیش‌نیاز
- Python 3.10+
- pip

### مراحل

```bash
# ۱. کلون پروژه
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>

# ۲. ساخت محیط مجازی
python -m venv env
# ویندوز:
env\Scripts\activate
# مک/لینوکس:
source env/bin/activate

# ۳. نصب وابستگی‌ها
pip install -r requirements.txt

# ۴. ساخت فایل .env در ریشه‌ی پروژه
```

محتوای `.env`:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

> کلید امن می‌تونی با این دستور بسازی:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

```bash
# ۵. اجرای مایگریشن‌ها
python manage.py migrate

# ۶. ساخت کاربر ادمین
python manage.py createsuperuser

# ۷. اجرای سرور
python manage.py runserver
```

سایت روی آدرس `http://127.0.0.1:8000` در دسترسه.

## 📁 ساختار پروژه
