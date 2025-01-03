🛒E-Commerce Project
This is a full-stack E-Commerce web application built using Django. The project allows users to browse product categories on the homepage, view product details, and manage products
from the admin panel. The homepage displays clickable category images that lead to detailed product listings.

📋Features
🖼️ Homepage with Categories: Displays product categories with images.
📄 Product Details Page: Clicking a category shows all products in that category.
🛠️ Admin Panel: Manage categories and products through Django's admin interface.
🖥️ Responsive Design: Mobile-friendly and user-friendly interface.

🏗️ Technologies Used
Python (v3.8+)
Django (v4.0+)
HTML5 / CSS3
Bootstrap (optional for styling)
SQLite (default Django database)

🛠️ Installation and Setup
Follow the steps below to set up the project on your local machine:

1️⃣ Clone the Repository
bash
git clone https://github.com/sinchana0111/shop-project.git
cd ecommerce-project
2️⃣ Create a Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
3️⃣ Install Dependencies
bash
pip install -r requirements.txt
4️⃣ Run Migrations
bash
python manage.py makemigrations
python manage.py migrate
5️⃣ Create a Superuser
bash
python manage.py createsuperuser
6️⃣ Run the Server
bash
python manage.py runserver
7️⃣ Access the Application
Open your browser and visit: http://127.0.0.1:8000/
Admin panel: http://127.0.0.1:8000/admin

📂 Project Structure
csharp
Copy code
ecommerce-project/
├── app/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   ├── base.html
│   │   ├── phome.html
│   │   ├── category_details.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── manage.py
├── db.sqlite3
├── README.md
└── requirements.txt
🖼️ Screenshots
📌 Homepage
The homepage displays clickable product categories with images.

📌 Category Details Page
Clicking a category image shows all products in that category with their details.

📚 Usage Instructions
Homepage: View product categories.
Category Details Page: Click on any category to view products under that category.
Admin Panel: Use the Django admin panel to manage categories and products.
🔧 Customization
You can customize the following files:

templates/phome.html: Modify the homepage template.
templates/category_details.html: Modify the category details page template.
static/css/style.css: Add your custom styles.
🤝 Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any feature you’d like to add.
📧 Contact
If you have any questions or suggestions, feel free to reach out:

Email: sinchanansoraba2002@gmail.com
GitHub: https://github.com/sinchana0111



