# 🎨 User Profile Manager

A modern, full-featured Django web application for user profile management with beautiful UI, secure authentication, and comprehensive profile customization.

![Django](https://img.shields.io/badge/Django-4.2+-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Production-brightgreen.svg)

## ✨ Features

### 🔐 Authentication & Security
- **Secure Registration**: User signup with email validation
- **Login/Logout**: Complete authentication flow
- **Password Management**: Built-in Django auth system
- **CSRF Protection**: All forms protected against cross-site request forgery
- **Session Management**: Secure user sessions

### 👤 Profile Management
- **Bio Section**: Rich text bio with 500 character limit
- **Photo Upload**: Profile picture upload with validation
- **Real-time Updates**: Instant profile updates with success feedback
- **Data Validation**: Server-side validation for all inputs

### 🎨 Modern UI/UX
- **Responsive Design**: Works perfectly on desktop and mobile
- **Beautiful Interface**: Modern gradient backgrounds and card layouts
- **Interactive Elements**: Smooth animations and hover effects
- **Accessibility**: Proper contrast ratios and keyboard navigation
- **Professional Styling**: Clean, modern design with consistent branding

### 🛡️ Data Validation
- **File Upload Limits**: 2MB maximum file size
- **Image Format Support**: PNG, JPG, JPEG only
- **Character Limits**: Bio text limited to 500 characters
- **Email Validation**: Proper email format checking
- **Password Security**: Django's built-in password validation

## 🚀 Tech Stack

- **Backend**: Django 4.2+
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design principles
- **Authentication**: Django's built-in auth system
- **File Handling**: Django's file upload system with Pillow

## 📋 Prerequisites

Before running this project, make sure you have:
- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/user-profile-manager.git
cd user-profile-manager
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django pillow
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Start Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser!

## 📖 Usage

### User Registration
1. Navigate to `/register/`
2. Fill in username, email, password, and optional bio
3. Upload a profile photo (optional)
4. Click "Register" to create your account

### Profile Management
1. After registration/login, you'll be redirected to `/profile/`
2. View your current profile information
3. Update your bio (max 500 characters)
4. Upload or change your profile photo
5. Click "Update Profile" to save changes

### Admin Panel
1. Access `/admin/` (requires superuser account)
2. Manage users and profiles
3. View uploaded media files

## 📁 Project Structure

```
user-profile-manager/
├── project/                 # Main Django project
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── application/            # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Form classes
│   ├── urls.py            # App URL configuration
│   ├── admin.py           # Admin interface
│   └── templates/         # HTML templates
│       └── application/
│           ├── register.html
│           └── profile.html
├── templates/
│   └── registration/       # Auth templates
│       ├── login.html
│       └── logged_out.html
├── media/                  # User uploaded files
├── static/                 # Static files (CSS, JS, images)
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── README.md              # This file
```

## 🎯 Key Features Explained

### Profile Photo Upload
- **Validation**: Only PNG, JPG, JPEG files allowed
- **Size Limit**: Maximum 2MB per file
- **Storage**: Files stored in `media/profile_photos/`
- **Display**: Automatic thumbnail generation with rounded corners

### Bio Management
- **Character Limit**: 500 characters maximum
- **Real-time Counter**: JavaScript prevents exceeding limit
- **Rich Text**: Multi-line textarea for better UX
- **Default Display**: Shows "No bio yet." when empty

### Security Features
- **CSRF Protection**: All forms include CSRF tokens
- **Authentication Required**: Profile updates require login
- **File Type Validation**: Prevents malicious file uploads
- **Secure Passwords**: Django's password hashing

## 🔧 Configuration

### Media Files
The app is configured to serve media files during development:

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Authentication Redirects
```python
# settings.py
LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
```

## 🧪 Testing

### Manual Testing Checklist
- [ ] User registration with valid data
- [ ] User registration with invalid data (validation errors)
- [ ] Login with correct credentials
- [ ] Login with incorrect credentials
- [ ] Profile update with bio only
- [ ] Profile update with photo only
- [ ] Profile update with both bio and photo
- [ ] File upload validation (wrong format, too large)
- [ ] Logout functionality
- [ ] Admin panel access

### Automated Testing
```bash
python manage.py test
```

## 🚀 Deployment

### Production Checklist
- [ ] Change `DEBUG = False` in settings.py
- [ ] Set up production database (PostgreSQL recommended)
- [ ] Configure static files serving
- [ ] Set up proper domain and SSL
- [ ] Configure email backend for password reset
- [ ] Set secure SECRET_KEY
- [ ] Configure ALLOWED_HOSTS

### Environment Variables
Create a `.env` file for sensitive settings:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=postgresql://user:password@localhost/dbname
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed
- Ensure responsive design works on all devices


## 🙋‍♂️ Support

If you have any questions or need help:

- 📧 Email: sailakshman212005@gmail.com
- 📖 Documentation: [Django Docs](https://docs.djangoproject.com/)

## 🔄 Future Enhancements

- [ ] Password reset functionality
- [ ] Email verification
- [ ] Social media login (Google, Facebook)
- [ ] Profile privacy settings
- [ ] User search and following system
- [ ] API endpoints for mobile app
- [ ] Dark mode toggle
- [ ] Multi-language support
- [ ] Profile analytics dashboard

---

**Made with ❤️ using Django**
