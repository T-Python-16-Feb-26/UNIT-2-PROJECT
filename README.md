# UNIT-2-PROJECT

## Saudi Tourism Guide

A responsive Django website about tourism in Saudi Arabia. The project presents important destinations in the Kingdom through a clean and modern interface with support for both light mode and dark mode.

## Project Overview

This project focuses on **Tourism in Saudi Arabia** and introduces users to popular cities, attractions, and travel experiences across the Kingdom. The website is built using Django templates, static files, and reusable layout components.

## Minimum Requirements Covered

This project satisfies the required conditions by including the following:

- Built using **Django**
- Uses **templates and template inheritance**
- Uses **dynamic URLs where applicable**
- Uses **static files** such as CSS, images, and JavaScript
- Includes a **homepage and more than 6 pages**
- Maintains a **coherent and uniform design**
- Supports **dark mode and light mode**
- Fully **responsive** across different screen sizes
- Uses **Bootstrap** and custom CSS for styling

## Current Pages

These are the main templates currently included in the project:

- `base.html`
- `home_view.html`
- `destinations.html`
- `riyadh.html`
- `jeddah.html`
- `abha.html`
- `alula.html`
- `experience_detail.html`
- `about.us.html`
- `contact_us.html`
- `search.html`
- `terms.html`

## Page Description

### `home_view.html`
The homepage introduces tourism in Saudi Arabia with a strong visual first impression, featured sections, and navigation to other parts of the website.

### `destinations.html`
A page that presents destinations in Saudi Arabia and helps users browse available places.

### `riyadh.html`
A city page dedicated to Riyadh, including tourism-related content and highlights.

### `jeddah.html`
A city page dedicated to Jeddah, including attractions, events, and visitor information.

### `abha.html`
A city page dedicated to Abha, highlighting its scenery, culture, and travel appeal.

### `alula.html`
A city page dedicated to AlUla, presenting its heritage and tourism value.

### `experience_detail.html`
A detail page for a selected tourism experience or activity.

### `about.us.html`
An about page that explains the purpose of the website and its idea.

### `contact_us.html`
A contact page for communication and user interaction.

### `search.html`
A search page to help users find content more easily, including a microphone option for voice-based search input.

### `terms.html`
A page containing the website terms and conditions or usage information.

## Features

- Modern tourism website about Saudi Arabia
- Reusable layout with template inheritance
- Multiple city pages
- Experience details page
- Search page with microphone/voice search option
- Responsive design
- Search bar with microphone/voice input option
- Light and dark theme support
- Bootstrap-based interface with custom styling

## Technologies Used

- **Python**
- **Django**
- **HTML**
- **CSS**
- **Bootstrap 5**
- **JavaScript**

## Project Structure

```bash
UNIT-2-PROJECT/
│
├── manage.py
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── main/
│   ├── templates/
│   │   └── main/
│   │       ├── abha.html
│   │       ├── about.us.html
│   │       ├── alula.html
│   │       ├── base.html
│   │       ├── contact_us.html
│   │       ├── destinations.html
│   │       ├── experience_detail.html
│   │       ├── home_view.html
│   │       ├── jeddah.html
│   │       ├── riyadh.html
│   │       ├── search.html
│   │       └── terms.html
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
└── README.md
```

## How to Run the Project

1. Clone the repository:

```bash
git clone <your-repository-link>
cd UNIT-2-PROJECT
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

### On Windows

```bash
venv\Scripts\activate
```

### On macOS / Linux

```bash
source venv/bin/activate
```

4. Install Django:

```bash
pip install django
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Open the project in the browser:

```bash
http://127.0.0.1:8000/
```

## Future Improvements

- Add more city pages
- Add database-driven content using Django models
- Add filters for destinations and experiences
- Add user accounts and saved items
- Improve search functionality
- Add more tourism media and videos

## Author

Developed as a Unit 2 Django project about tourism in Saudi Arabia.
