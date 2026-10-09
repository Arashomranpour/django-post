<div align="center">

# 📝 Django Post App

**A simple blog app with registration and login, two user roles and an admin who can ban users.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)

</div>

---

## ✨ Features

- 🔐 **Authentication** - sign up, login and logout.
- ✍️ **Create and delete posts.**
- 👥 **Two types of users**
  - 🛡️ **Moderators** can delete other users' posts.
  - 🙂 **Simple users** manage their own posts.
- 🚫 **Admin** can ban users.
- 📧 Email template and token helper prepared for account activation.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/django-post.git
cd django-post/postapp

python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install django django-browser-reload

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/.

## 🔗 Routes

| Route | Purpose |
|---|---|
| `/` , `/home` | All posts |
| `/sign-up` | Create an account |
| `/login/`, `/logout` | Authentication |
| `/createpost` | Write a post |

## 📁 Project Structure

```
postapp/
├── manage.py
├── postapp/          # Project settings and root URLs
└── post_module/      # App: post model, forms, views, tokens, templates
```

## 🛠️ Tech Stack

`Python` · `Django` · `SQLite`
