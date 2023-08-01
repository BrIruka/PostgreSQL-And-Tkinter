# PostgreSQL-And-Tkinter Login or Register
PostgreSQL And Tkinter (Login or Register profile)

Етапи:
1. Для того щоб код працював вам потрібно створити своб Базу Данних, використовуючи модуль і додаток PostgreSQL.
2. Інструкція як встановити БД на свій віртуальний сервер - https://linuxize.com/post/how-to-install-postgresql-on-debian-10/#installing-postgresql
 (Також якщо будуть проблеми можете подивитись варіант як їх вирішував ChatGPT - https://chat.openai.com/share/d69f44ff-be4b-40f6-9107-adc52f356454)

3. В писати данні в код в функцію get_connection:

  d
 
     conn = psycopg2.connect(
     
         database="your_database",
         
         user="your_username",
         
         password="your_password",
        
         host="your_addres",
         
         port="defoult_5432",
         
         sslmode='disable'
        
     )
    
     return conn
