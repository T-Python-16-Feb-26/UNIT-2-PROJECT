# The Saudi Storybook

A chapter-based Django web application that presents a narrative journey through Saudi Arabia, including its land, people, traditions, cities, royal family, future, legacy, and celebrations.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Tech Stack](#tech-stack)
4. [Getting Started](#getting-started)
5. [Routing Map](#routing-map)

## Project Overview

The Saudi Storybook is built as a server-rendered Django site with one main app (`main`) and chapter-specific pages rendered from templates. The home page acts as a table of contents, and each chapter route maps to its own dedicated view and template.

## Key Features

- Server-rendered Django pages for simple, maintainable content delivery.
- Eight chapter pages with clear URL-based navigation.
- Shared base template for consistent page layout.
- Static assets organization for CSS and chapter-specific images.
- Light/Dark mode preference using a cookie and dedicated mode-switch route.

## Tech Stack

- Python 3.12+ (recommended)
- Django 6.0.3
- SQLite (default development database)
- Bootstrap 5.3.3 (via CDN)

Dependencies are listed in `requirements.txt`.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/FadhelAlmalki/The-Saudi-Storybook.git
cd The-Saudi-Storybook
```

### 2. Create and activate a virtual environment

Windows (Git Bash):

```bash
python -m venv venv
source venv/Scripts/activate
```

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run database migrations

```bash
cd TheSaudiStorybook
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open your browser at:

```text
http://127.0.0.1:8000/
```

## Routing Map

| Route | View | Purpose |
|---|---|---|
| `/` | `home_view` | Chapter landing page |
| `/land/` | `land_view` | Chapter 1: The Land |
| `/people/` | `people_view` | Chapter 2: The People |
| `/traditions/` | `traditions_view` | Chapter 3: The Traditions |
| `/cities/` | `cities_view` | Chapter 4: The Cities |
| `/royal-family/` | `royal_family_view` | Chapter 5: The Royal Family |
| `/future/` | `future_view` | Chapter 6: The Future |
| `/legacy/` | `legacy_view` | Chapter 7: The Legacy |
| `/celebrations/` | `celebrations_view` | Chapter 8: The Celebrations |
| `/mode/<mode>/` | `mode_view` | Set light/dark mode cookie |