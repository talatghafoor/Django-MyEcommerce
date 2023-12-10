# MY ECOMMERCE

Welcome to the documentation for your e-commerce website built with Django and Bootstrap templates.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Introduction

This project is a full-fledged e-commerce website developed using the Django framework and styled with Bootstrap templates. It provides a user-friendly interface for customers to browse through different product categories, view product details, add products to their shopping cart, and manage their accounts.

## Features

1. **Product Categories:** Navigate through various product categories to find the items you're looking for.

2. **Product Listing:** View a list of products within each category with details such as name, price, and a brief description.

3. **Product Details:** Click on a product to view its detailed information on a dedicated product page.

4. **Shopping Cart:** Add products to the shopping cart, manage quantities, and proceed to checkout.

5. **User Authentication:** Users can register, log in, and log out securely to manage their profiles and track order history.

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/talatghafoor/Django-MyEcommerce.git
   cd Django-MyEcommerce
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver

## Usage
1. **Admin Panel:** 

    Access the Django admin panel at http://localhost:8000/admin using the superuser credentials.

2. **User Registration:**

    Visit http://localhost:8000/register to create a new user account.

3. **User Login:**

    Log in with your credentials at http://localhost:8000/login.

4. **Browse Products:**

    Explore different product categories and view product details.

5. **Add to Cart:**

    Add products to the shopping cart and manage quantities.

6. **Checkout:**

    Proceed to checkout to complete the purchase.

## Dependencies
**Django**

**Bootstrap**

    For a complete list of dependencies, refer to the requirements.txt file.


## Snaps
![Screenshot](Snaps\Home.png)
![Screenshot](Snaps\Register.png)
![Screenshot](Snaps\Login.png)
![Screenshot](Snaps\Cart.png)







