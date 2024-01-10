# Gas_utility
Link to the Youtube Video - https://youtu.be/TKn-Iv2aCs4?si=-Y_LHUj0eStukDgK

This is my Final Project for the course CS50’s Web Programming with Python and JavaScript. It is built with Django, HTML, CSS, Javascript, Python & Bootsrap.

I have built an application to provide consumer services. This application would allow customers to submit service requests online, track the status of their requests, and also message their customer support representatives.
The application would also provide customer support representatives with a tool to manage requests and provide support to customers.

# Distinctiveness and Complexity
I believe that my project meets the requirement for the following reasons:
- My project is based on an original idea, that solves a real-life personal problems.
- The web application is built with different user types: admin, customer and customer support representative.
- One of the key differentiators of my project is the authorization system I've implemented. Which is different than the projects built in the courses. 
- I've leveraged Django decorators, Groups and permissions to create a finely-tuned access control mechanism. This ensures that customers can only access pages and features     relevant to them, and the same applies to customer support representatives also.
- My project utilizes Django on the backend and Javascript on the frontend. It is also mobile responsive.

# What’s contained in each file you created

This is my file structure
```
├───gas_service_app
│   ├───migrations
│   │   └───__pycache__
│   ├───static
│   │   └───gas_service_app
│   ├───templates
│   │   └───gas_service_app
│   └───__pycache__
├───gas_utility
│   └───__pycache__
├───media
│   └───attachments
└───support
    ├───migrations
    │   └───__pycache__
    ├───static
    │   └───support
    ├───templates
    │   └───support
    └───__pycache__
```

1. **gas_service_app**:
This app is related to customers. It contains files that define the behavior and appearance of this specific app.

```
├───gas_service_app
│   │   admin.py
│   │   apps.py
│   │   decorators.py
│   │   forms.py
│   │   models.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │
│   ├───static
│   │   └───gas_service_app
│   │           index.js
│   │           styles.css
│   │
│   ├───templates
│   │   └───gas_service_app
│   │           index.html
│   │           layout.html
│   │           login.html
│   │           register.html
│   │           resolved.html
│   │           submit_request.html
│   │           track_requests.html
│   │           view_request.html
│   │
│   └───__pycache__

```

```gas_service_app/migrations```: Contains every migrations we do everytime we bring a change to our models, database.

Other Key files in this directory:
 - **admin.py**: Configuration for the app's admin  interface. 
 - **apps.py**: App-specific configuration settings.
 - **decorators.py**: Custom decorators to control access to views.
 - **forms.py**: Forms for user input.

 - **models.py**: Database models for the app.

 - **urls.py**: URL routing for the app.

 - **views.py**: Logic and views for webpages.

 - **static**: Static files like CSS and JavaScript is stored here.

 - **templates**: Directory for storing app-specific HTML templates.

2. **gas_utility**
  This is the main directory of Django project. It typically contains settings, URLs, and other project-wide configurations.

3. **media/attachments**:
This is where all image files uploaded by users is stored.

4. **support**:

```
└───support
    │   admin.py
    │   apps.py
    │   decorators.py
    │   models.py
    │   urls.py
    │   views.py
    │   __init__.py
    │
    ├───migrations
    │
    ├───static
    │   └───support
    │           index.js
    │           styles.css
    │
    ├───templates
    │   └───support
    │           edit_request.html
    │           index.html
    │           layout.html
    │           login.html
    │           register.html
    │           resolved.html
    │
    └───__pycache__
```
This app is related to customer support representatives.
   - Similar to "gas_service_app," it includes subdirectories for migrations, static files, templates, and Python cache files specific to this app.

# How to run your application

**Prerequisites**:\
Make sure you have the following installed:
- Python (3.6 or higher)
- Django framework

**Clone the repository**
```
git clone <repository-url>
cd <repository-directory>
```

**Apply the migrations**
```
python manage.py migrate

```

**Create a Superuser (Admin User) (Optional but recommended):**
```
python manage.py createsuperuser
```

**Run the Development Server:**
```
python manage.py runserver

```

**Access the Admin Interface (Optional):**\
If you created a superuser, you can access the Django admin interface at ```http://127.0.0.1:8000/admin```. Log in with your superuser credentials.
# Project's Pages
After registering this page will appear where user also has to register his mobile number to become customer.\

## Customer Interface

***Register Phone Number***
![App Screenshot](https://github.com/me50/aditya1997-debug/blob/web50/projects/2020/x/capstone/screenshots/Mobile%20Register.PNG?raw=true)

After registering his phone number this page will appear where customer can submit complaint and can also add a photo copy\
***Submit Complaint***
![App Screenshot](https://github.com/me50/aditya1997-debug/blob/web50/projects/2020/x/capstone/screenshots/Submit%20Complaint.PNG?raw=true)

All submitted complaints of a logged in customer\
***Submitted complaints***
![App Screenshot](https://github.com/me50/aditya1997-debug/blob/web50/projects/2020/x/capstone/screenshots/Submitted%20Complaints.PNG?raw=true)

On this page customer can send message to support team regarding submitted complaint
![App Screenshot](https://github.com/me50/aditya1997-debug/blob/web50/projects/2020/x/capstone/screenshots/View%20Complaint.PNG?raw=true)

***Resolved Complaints***
On this page all the resolved complaints are shown and if the customer is not satisfied he can reopen the ticket

![App Screenshot](https://github.com/me50/aditya1997-debug/blob/web50/projects/2020/x/capstone/screenshots/Resolved%20and%20reopen.PNG?raw=true)

## Customer Support Representative Interface
```http://127.0.0.1:8000/support/login``` This is the Url for Support interface.

After logging in as Support Representative
this page will appear which is the default one.
Here all the ***Pending and Submitted complaints*** of all customers are shown

![App Screenshot](https://github.com/me50/aditya1997-debug/blob/web50/projects/2020/x/capstone/screenshots/support_submitted_complaints.PNG?raw=true)

And after clicking on View Complaint. This page appears where Customer Support Representative can see the messages sent by the customer and also can message back and change the status of the complaint.

![App Screenshot](https://github.com/me50/aditya1997-debug/blob/web50/projects/2020/x/capstone/screenshots/support_view_complaint_resolve.PNG?raw=true)

# Any other additional information the staff should know about your project.

1. ``` http://127.0.0.1:8000/login ```:
This URL is for Customers Only. So if you are logged in as a *Customer Support Representative* and try to visit the above mentioned URL. Your request will be denied. So if you want to visit the customers section first log out as a Customer Support Representative.

2. ``` http://127.0.0.1:8000/support/login```:
This URL is for Customer Support Representatives Only. So if you are logged in as a *Customer* and try to visit the above mentioned URL. Your request will be denied. So if you want to visit the Support section first log out as a Customer.

# Thankyou CS50, because of you I got my first internship.
