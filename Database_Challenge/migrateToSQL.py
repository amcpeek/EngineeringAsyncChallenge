

import json

# 1. create tables in the database

# CREATE TABLE orders (
#     UUID VARCHAR(255) PRIMARY KEY,
#     customerName VARCHAR(100),
#     cellPhone VARCHAR(100),
#     email VARCHAR(100),
#     address VARCHAR(255),
#     orderTotal VARCHAR(255),
#     discountCode VARCHAR(255)
# );
# note: I decided to keep the cellphone and orderTotal varchar

# CREATE TABLE coaching_services (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     type VARCHAR(255)
# );
# note: type was not included in the data given, but I included it to make it easier to conceptualize

# CREATE TABLE book_sets (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255)
# );
# note: name was not included in the data given, but I included it to make it easier to conceptualize

# CREATE TABLE service_orders (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     orderUUID VARCHAR(255),
#     coachingServiceId INT
# );


# CREATE TABLE book_orders (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     orderUUID VARCHAR(255),
#     bookSetId INT
# );


# 2. insert into tables

with open('data.json', 'r') as f:
    json_data = json.load(f)
    for jd in json_data:
        # insert into orders
        print(f'''INSERT INTO orders
        (UUID, customerName, cellPhone, email, address, orderTotal, orderDate, discountCode) VALUES
        ('{jd["UUID"]}', '{jd["customerName"]}', '{jd["cellPhone"]}', '{jd["email"]}', '{jd["address"]}',
        '{jd["orderTotal"]}', '{jd["orderDate"]}', '{jd["discountCode"]}' );''')

        if 'coachingServiceID' in jd:
            for n in jd['coachingServiceID']:
                # insert into coaching_services
                #assume database is set up with autoincrementing ids
                print(f'INSERT INTO coaching_services (id) VALUES ({n});')
                # insert into service_orders
                #assume database is set up with autoincrementing ids
                print(
                    f'''INSERT INTO service_orders (orderUUID, coachingServiceId) VALUES ('{jd["UUID"]}', {n});''')

        if 'bookSetID' in jd:
            for n in jd['bookSetID']:
                # insert into book_sets
                #assume database is set up with autoincrementing ids
                print(f'INSERT INTO book_set (id) VALUES ({n});')
                # insert into book_orders
                #assume database is set up with autoincrementing ids
                print(
                    f'''INSERT INTO service_orders (orderUUID, bookSetId) VALUES ( '{jd["UUID"]}', {n});''')
