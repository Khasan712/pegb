# pegb

<h2>Introduction</h2>
    
    This project done based on Pegb technical assesment task. I have used Python, Django,
    DjangoRestFramework for implementing Api, PostgreSQL for databses, Celery package for 
    background task (sending email message) and Dockerized the project.


<h2>Note</h2>
    
    I will start to explain the project architecture.
    The project root directory is "config" folder.
    In this project there is one app "v1" folder.
    In this folder there are models, views, utils, product and serializers folders.
    
    In "models" folder there are three files. orders.py for Order proccess table.
    products.py for product, category, discount tables. users.py file for user table and also there are
    staff and customer proxy model for separate this two role in admin dashboard.

    "serializers" and "users" folders created based on "models" folder.

    I have used two classes for creating api CreateApiView from generics and also ModelViewSets.
    For sending email message when customer registered, i used django core mail module inside celery task,
    because sending email takes a litl bit more time, user should to be wait the backend response a lot.
    On the other hand, for sending email message every time i have used django signals and also
    i used django signals for counting customer order count when order count riches customer categorization
    count, customer category changes.

    Everything working the same based on technical assesment test tasks. 
    Tasks are
    Users, Onboarding, Products, Customer categorization, discounts, shopping cart, orders. 
    
    

<h2>Deployment</h2>

    1) First of all, need to git clone project.
        
        git clone https://github.com/Khasan712/pegb.git


    2) Create .env file and write this inside .env file.
        SECRET_KEY=<SECRET_KEY>
        DEBUG=False
        ALLOWED_HOSTS=<ALLOWED_HOSTS>
        
        DB_ENGINE=postgresql_psycopg2
        POSTGRES_DB=<DB NAME>
        POSTGRES_USER=<DB USER>
        POSTGRES_PASSWORD=<DB PASSWORD>
        POSTGRES_HOST=<DB HOST (DOCKER SERVICE)>
        POSTGRES_PORT=<DB PORT>
        
        EMAIL_USE_TLS=True
        EMAIL_HOST=smtp.gmail.com
        EMAIL_PORT=587
        EMAIL_HOST_USER=<SENDER EMAIL PASSWORD>
        EMAIL_HOST_PASSWORD=<APP PASSWORD>
    
    3) Start docker compose
        docker compose up --build -d
    
    4) Start using app.




    