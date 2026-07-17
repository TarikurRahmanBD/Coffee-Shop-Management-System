# ☕ Coffee Shop Management System

> A comprehensive desktop application for managing coffee shop operations with employee management, inventory tracking, and customer billing.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [How to Install & Run](#how-to-install--run)
- [Project Structure](#project-structure)
- [Usage Guide](#usage-guide)
- [About the Developer](#about-the-developer)
- [License](#license)

---

## 🎯 Project Overview

The **Coffee Shop Management System** is a professional-grade desktop application built with Python Tkinter that streamlines all aspects of coffee shop operations. This GUI-based system enables coffee shop owners and staff to efficiently manage inventory, process customer orders, handle employee records, and generate detailed billing reports—all from a single, intuitive interface.

Whether you're running a small café or a larger coffee shop, this system provides robust tools to improve operational efficiency and customer service.

---

## ✨ Key Features

### 🔐 **User Authentication & Role Management**
- **Three user roles:** Admin, Employee, and Guest
- Secure login system with account signup
- Role-based access control for different features

### 📊 **Dashboard & Analytics**
- Comprehensive dashboard for business overview
- Real-time status monitoring
- Quick access to important metrics

### 💳 **Billing & Sales Management**
- Easy-to-use billing interface
- Add/modify/delete coffee products
- Quantity management and price calculations
- Automatic total price computation
- Receipt generation and printing support
- Transaction history tracking

### 📦 **Inventory Management**
- Track coffee products and supplies
- Update stock levels
- Monitor inventory status
- Product database management

### 👥 **Employee Management**
- Add, update, and manage employee records
- Employee profile management
- Staff information database

### 💾 **Data Persistence**
- SQLite database backend
- Reliable data storage and retrieval
- Automated data management

### 🎨 **Professional User Interface**
- Modern, intuitive GUI design
- Professional branding with custom icons and logos
- Splash screen with progress indicator
- Responsive layout and design

---

## 🛠️ Technology Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.12+** | Core programming language |
| **Tkinter** | GUI framework and interface design |
| **SQLite3** | Database management |
| **Pillow** | Image processing and handling |

---

## 🚀 How to Install & Run

### Prerequisites
- **Python 3.7 or higher** installed on your system
- **pip** package manager

### Step-by-Step Installation

#### 1. **Clone or Download the Project**
```bash
# If using git
git clone https://github.com/tarikurrahmanbd/CoffeeShopManagentSystem.git
cd CoffeeShopManagentSystem

# Or manually download and extract the ZIP file
```

#### 2. **Navigate to Project Directory**
```bash
cd CoffeeShopManagentSystem
```

#### 3. **Create a Virtual Environment (Recommended)**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:
- `sqlite3` - Database management
- `pillow` - Image processing

#### 5. **Run the Application**
```bash
python run_app.py
```

The application will start with a splash screen and load into the main login window.

### Troubleshooting
- **If images don't load:** Ensure the `images/` folder is in the `CoffeeManagementSystem/` directory
- **If database errors occur:** Check that you have write permissions in the project folder
- **Missing fonts:** Verify the `fonts/` folder exists in the project directory

---

## 📁 Project Structure

```
CoffeeShopManagementSystem/
├── CoffeeManagementSystem/
│   ├── __init__.py              # Package initialization
│   ├── _bootstrap.py            # Bootstrap configuration
│   ├── run_app.py               # Main entry point
│   ├── AccountSystem.py          # Authentication & login system
│   ├── Accounts.py              # Account management
│   ├── Dashboard.py             # Main dashboard interface
│   ├── Inventory.py             # Inventory management
│   ├── Employee.py              # Employee management
│   ├── Guest.py                 # Guest interface
│   ├── admin.py                 # Admin panel
│   ├── admin_start.py           # Admin startup
│   ├── Start_App.py             # Application startup
│   ├── images/                  # UI images and icons
│   ├── fonts/                   # Custom fonts
│   └── Database/                # Database files
├── requirements.txt             # Python dependencies
├── run_app.py                   # Application launcher
└── README.md                    # This file
```

---

## 💡 Usage Guide

### **First-Time Setup**

1. **Launch the Application**
   ```bash
   python run_app.py
   ```

2. **Create an Account**
   - Click on the "Sign Up" option
   - Enter your details (username, password, etc.)
   - Select your role (Admin/Employee)
   - Click "Create Account"

3. **Login**
   - Use your credentials to log in
   - Select your role and proceed

### **For Administrators**
- Access the admin dashboard to manage the entire system
- Add/edit/delete employees
- Manage inventory and products
- View reports and analytics

### **For Employees**
- Process customer orders and billing
- Add products to cart
- Calculate totals and print receipts
- View dashboard information

### **For Guests**
- Browse available products
- View menus and pricing

---

## 👨‍💻 About the Developer

**Tarikur Rahman** | Full-Stack Developer

I'm a passionate software developer with expertise in Python, web development, and creating user-friendly applications. I love building solutions that solve real-world problems.

### 🔗 Connect with Me

| Platform | Link |
|----------|------|
| **GitHub** | [@tarikurrahmanbd](https://github.com/tarikurrahmanbd) |
| **Portfolio** | [yourtarikur.netlify.app](https://yourtarikur.netlify.app/) |
| **Email** | [tarikurrahman2008@gmail.com](mailto:tarikurrahman2008@gmail.com) |
| **Social Handle** | @tarikurrahman08 |

Feel free to reach out for collaboration, suggestions, or feedback!

---

## 📜 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

### You are free to:
- ✅ Use this project for personal and commercial purposes
- ✅ Modify and customize the code
- ✅ Distribute the project
- ✅ Use it in your own projects

### Attribution:
Please acknowledge the original developer if you use this project in any derivative work.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions, bug fixes, or improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📝 Notes

- This application requires a GUI environment (Windows, macOS, or Linux with display support)
- SQLite database files will be created automatically in the `Database/` folder on first run
- Ensure all image assets are present in the `images/` directory for proper UI rendering

---

## 🎓 Learning Resources

This project demonstrates:
- Object-Oriented Programming (OOP) principles
- Tkinter GUI development
- SQLite database integration
- File handling and image processing
- User authentication and role-based access control

Perfect for learning professional desktop application development in Python!

---

**Last Updated:** July 2026  
**Version:** 1.0.0

---

<div align="center">

**⭐ If you find this project helpful, please consider giving it a star! ⭐**

Made with ❤️ by Tarikur Rahman

</div>
