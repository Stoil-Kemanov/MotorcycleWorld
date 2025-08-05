# Motorcycle World - Django Web Application

🌐 Live Demo: https://motorcycle-world-sk-hzbzfzf9cbb0h6bh.italynorth-01.azurewebsites.net

A comprehensive web platform for motorcycle enthusiasts featuring product catalogs, personalized recommendations, shopping cart functionality, and services directory.

## 🚀 Setup Instructions

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Copy .env.example to .env and fill in your actual values
5. Install requirements: `pip install -r requirements.txt`
6. Run migrations: `python manage.py migrate`
7. Create superuser: `python manage.py createsuperuser`
8. Run server: `python manage.py runserver`

## 📋 Project Overview

Motorcycle World is a comprehensive Django web application designed as a one-stop platform for motorcycle riders. It combines e-commerce functionality with personalized recommendations and community features to create a complete motorcycle ecosystem.

## ✨ Core Features

### 🔐 Authentication & User Management
- Custom email-based user authentication
- Comprehensive user profiles with riding preferences
- Personal motorcycle inventory management
- Role-based permissions (Superuser, Staff, Intern groups)

### 🏍️ Product Catalog System
- **Motorcycles**: Complete specifications, images, pricing
- **Parts**: Categorized with compatibility matching
- **Accessories**: Motorcycle gear and equipment
- **Clothing**: Riding apparel with fit and style options
- **Services**: Directory of motorcycle service providers

### 🎯 Intelligent Recommendation Engine
- **Find My Bike**: Personalized motorcycle recommendations using advanced scoring algorithm
- **Find My Clothing**: Gear recommendations based on body type and riding style
- Compatibility scoring considers:
  - Riding style preferences
  - Experience level
  - Body type and physical measurements
  - Engine power and size appropriateness

### 🛒 Shopping Cart System
- Universal cart supporting all product types
- Session-persistent storage
- Quantity management and price calculations
- Simulated checkout process with order confirmation

### 🔍 Advanced Search
- Universal search across all product categories
- Category / key word / price range filtering
- Category-specific results

### 🚔 Additional Services
- MVR traffic fines checking integration
- Service provider directory with specializations

## 🏗️ Technical Architecture

### Apps Structure
- **accounts**: User authentication, profiles, recommendations
- **motorcycles**: Product catalog (motorcycles, parts, accessories)
- **clothing**: Riding apparel and gear
- **services**: Service provider directory
- **cart**: Shopping cart functionality
- **common**: Shared utilities, mixins, and choices

### Key Technical Features
- **Custom User Model**: Email-based authentication
- **Abstract Base Models**: DRY principle with shared functionality
- **Django Mixins**: Reusable timestamp and validation logic
- **Generic Foreign Keys**: Universal shopping cart implementation
- **Custom Validators**: Phone number and data validation
- **Template Inheritance**: Consistent UI across the application
- **Permission System**: Granular access control

### Database Design
- PostgreSQL-ready models with proper relationships
- Many-to-many relationships for part compatibility
- Generic foreign keys for flexible cart system
- Proper model inheritance and abstract base classes

## 🎨 Frontend Features
- **Responsive Bootstrap 5 Design**
- **Dynamic Navigation**: Context-aware menus and user states  
- **Interactive Elements**: Color-coded compatibility scores
- **Professional UI/UX**: Consistent design language
- **Form Validation**: Client and server-side validation
- **Image Handling**: Fallbacks and responsive display

## 🔧 Admin Features
- **Customized Django Admin**: Enhanced interface with filters and search
- **Staff Permissions**: Granular content management access
- **User Group Management**: Role-based access control

## 🧪 Quality Assurance
- Comprehensive test suite covering models, views, and forms
- Custom validation and error handling
- Security features with proper authentication checks
- Clean, maintainable code architecture

## 📊 Recommendation Algorithm

The intelligent recommendation system uses a sophisticated scoring algorithm that evaluates:

### Motorcycle Recommendations (100-point scale):
- **Riding Style Match** (30 points): Direct and cross-compatibility scoring
- **Experience Level** (25 points): Engine size appropriate for skill level  
- **Body Type Compatibility** (20 points): Ergonomic considerations
- **Engine Power** (15 points): Power-to-experience matching
- **Height Considerations** (10 points): Comfort and reach factors

### Clothing Recommendations (100-point scale):
- **Style Compatibility** (40 points): Riding style to clothing style matching
- **Fit Matching** (35 points): Body type to clothing fit correlation
- **Size Optimization** (25 points): Height/weight to sizing logic
