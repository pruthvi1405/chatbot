import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('travel_agent.db')

# Create a cursor object
cursor = conn.cursor()

# #Create the tables
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS flights (
#         flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         departure_city TEXT,
#         arrival_city TEXT,
#         class TEXT,
#         price REAL,
#         currency TEXT
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS hotels (
#         hotel_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         city TEXT,
#         star_rating INTEGER,
#         price_per_night REAL,
#         currency TEXT
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS packages (
    #     package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     destination TEXT,
    #     type TEXT,
    #     price REAL,
    #     currency TEXT
    # )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS tours (
    #     tour_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     location TEXT,
    #     type TEXT,
    #     price REAL,
    #     currency TEXT
    # )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS cruises (
    #     cruise_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     destination TEXT,
    #     duration TEXT,
    #     price REAL,
    #     currency TEXT
    # )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS car_rentals (
#         rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         city TEXT,
#         price_per_day REAL,
#         currency TEXT
#     )
# ''')

# flights_data = [
#     ('New York', 'Tokyo', 'economy', 1200.00, 'USD'),
#     ('Sydney', 'London', 'business', 3500.00, 'AUD')
#     ('Los Angeles', 'Paris', 'economy', 900.00, 'USD'),
#     ('Chicago', 'Berlin', 'first', 2000.00, 'USD'),
#     ('Miami', 'Dubai', 'economy', 1500.00, 'USD'),
#     ('Toronto', 'Hong Kong', 'business', 2500.00, 'CAD'),
#     ('San Francisco', 'Rome', 'economy', 1000.00, 'USD'),
#     ('Vancouver', 'Singapore', 'business', 3000.00, 'CAD'),
#     ('Boston', 'Madrid', 'economy', 800.00, 'USD'),
#     ('Washington', 'Seoul', 'first', 1800.00, 'USD'),
#     ('Las Vegas', 'Bangkok', 'economy', 1100.00, 'USD'),
#     ('Dallas', 'Moscow', 'business', 2600.00, 'USD'),
#     ('Atlanta', 'Amsterdam', 'economy', 950.00, 'USD'),
#     ('Houston', 'Istanbul', 'first', 2100.00, 'USD'),
#     ('Philadelphia', 'Beijing', 'economy', 1300.00, 'USD'),
#     ('Denver', 'Lisbon', 'business', 2800.00, 'USD'),
#     ('Phoenix', 'Mumbai', 'economy', 1400.00, 'USD'),
#     ('Seattle', 'Athens', 'business', 2700.00, 'USD'),
#     ('Orlando', 'Cairo', 'economy', 1600.00, 'USD'),
#     ('San Diego', 'Vienna', 'first', 2200.00, 'USD'),
#     ('San Antonio', 'Prague', 'economy', 1200.00, 'USD'),
#     ('Portland', 'Warsaw', 'business', 2900.00, 'USD'),
#     ('Indianapolis', 'Budapest', 'economy', 1500.00, 'USD'),
#     ('Columbus', 'Zurich', 'business', 3100.00, 'USD'),
#     ('Charlotte', 'Brussels', 'first', 2300.00, 'USD')
# ]

# # Insert multiple rows into flights table
# cursor.executemany('''
#     INSERT INTO flights (departure_city, arrival_city, class, price, currency)
#     VALUES (?, ?, ?, ?, ?)
# ''', flights_data)
# conn.commit()
# hotels_data = [
#     ('New York', 5, 300.00, 'USD'),
#     ('Tokyo', 4, 200.00, 'JPY'),
#     ('Paris', 5, 250.00, 'EUR'),
#     ('London', 4, 220.00, 'GBP'),
#     ('Berlin', 3, 180.00, 'EUR'),
#     ('Rome', 4, 210.00, 'EUR'),
#     ('Madrid', 5, 240.00, 'EUR'),
#     ('Vienna', 4, 230.00, 'EUR'),
#     ('Prague', 3, 150.00, 'CZK'),
#     ('Sydney', 5, 260.00, 'AUD'),
#     ('Melbourne', 4, 210.00, 'AUD'),
#     ('Brisbane', 3, 190.00, 'AUD'),
#     ('Dubai', 5, 300.00, 'AED'),
#     ('Bangkok', 4, 200.00, 'THB'),
#     ('Singapore', 5, 270.00, 'SGD'),
#     ('Hong Kong', 4, 230.00, 'HKD'),
#     ('Toronto', 3, 180.00, 'CAD'),
#     ('Vancouver', 4, 210.00, 'CAD'),
#     ('Montreal', 5, 240.00, 'CAD'),
#     ('Chicago', 4, 220.00, 'USD'),
#     ('Los Angeles', 5, 280.00, 'USD'),
#     ('San Francisco', 4, 250.00, 'USD'),
#     ('Miami', 3, 200.00, 'USD'),
#     ('Las Vegas', 4, 220.00, 'USD'),
#     ('Orlando', 5, 260.00, 'USD'),
#     ('Seattle', 4, 230.00, 'USD'),
#     ('Boston', 3, 210.00, 'USD'),
#     ('Houston', 4, 240.00, 'USD'),
#     ('Atlanta', 5, 270.00, 'USD'),
#     ('Dallas', 4, 230.00, 'USD')
# ]

# # Insert multiple rows into hotels table
# cursor.executemany('''
#     INSERT INTO hotels (city, star_rating, price_per_night, currency)
#     VALUES (?, ?, ?, ?)
# ''', hotels_data)

# packages_data = [
#     ('Paris', 'romantic', 1500.00, 'USD'),
#     ('Hawaii', 'family', 2000.00, 'USD'),
#     ('Tokyo', 'adventure', 1800.00, 'JPY'),
#     ('New York', 'city tour', 1200.00, 'USD'),
#     ('Sydney', 'beach', 2500.00, 'AUD'),
#     ('Rome', 'historical', 1600.00, 'EUR'),
#     ('Dubai', 'luxury', 3000.00, 'AED'),
#     ('Bangkok', 'cultural', 1400.00, 'THB'),
#     ('London', 'romantic', 2000.00, 'GBP'),
#     ('Berlin', 'historical', 1300.00, 'EUR'),
#     ('Vienna', 'classical', 1700.00, 'EUR'),
#     ('Prague', 'romantic', 1100.00, 'CZK'),
#     ('Hong Kong', 'city tour', 1900.00, 'HKD'),
#     ('Singapore', 'luxury', 2100.00, 'SGD'),
#     ('Toronto', 'adventure', 1500.00, 'CAD'),
#     ('Vancouver', 'beach', 1600.00, 'CAD'),
#     ('Los Angeles', 'city tour', 1400.00, 'USD'),
#     ('San Francisco', 'romantic', 1800.00, 'USD'),
#     ('Miami', 'beach', 1500.00, 'USD'),
#     ('Las Vegas', 'luxury', 2500.00, 'USD'),
#     ('Orlando', 'family', 2200.00, 'USD'),
#     ('Seattle', 'adventure', 1700.00, 'USD'),
#     ('Boston', 'historical', 1300.00, 'USD'),
#     ('Chicago', 'city tour', 1600.00, 'USD'),
#     ('Atlanta', 'cultural', 1200.00, 'USD'),
#     ('Dallas', 'luxury', 1900.00, 'USD'),
#     ('Houston', 'historical', 1500.00, 'USD'),
#     ('Philadelphia', 'romantic', 1400.00, 'USD'),
#     ('Phoenix', 'adventure', 1700.00, 'USD'),
#     ('San Diego', 'beach', 2000.00, 'USD')
# ]

# # Insert multiple rows into packages table
# cursor.executemany('''
#     INSERT INTO packages (destination, type, price, currency)
#     VALUES (?, ?, ?, ?)
# ''', packages_data)

# tours_data = [
#     ('Grand Canyon', 'adventure', 500.00, 'USD'),
#     ('Eiffel Tower', 'sightseeing', 100.00, 'EUR'),
#     ('Great Wall of China', 'historical', 300.00, 'CNY'),
#     ('Machu Picchu', 'adventure', 400.00, 'PEN'),
#     ('Colosseum', 'historical', 150.00, 'EUR'),
#     ('Pyramids of Giza', 'historical', 200.00, 'EGP'),
#     ('Sydney Opera House', 'sightseeing', 250.00, 'AUD'),
#     ('Santorini', 'romantic', 350.00, 'EUR'),
#     ('Safari in Kenya', 'adventure', 800.00, 'KES'),
#     ('Niagara Falls', 'sightseeing', 120.00, 'USD'),
#     ('Statue of Liberty', 'historical', 100.00, 'USD'),
#     ('Banff National Park', 'adventure', 450.00, 'CAD'),
#     ('Tokyo Tower', 'sightseeing', 130.00, 'JPY'),
#     ('Great Barrier Reef', 'adventure', 600.00, 'AUD'),
#     ('Yellowstone National Park', 'adventure', 400.00, 'USD'),
#     ('Venice Canals', 'romantic', 300.00, 'EUR'),
#     ('Alhambra', 'historical', 150.00, 'EUR'),
#     ('Taj Mahal', 'historical', 250.00, 'INR'),
#     ('Christ the Redeemer', 'sightseeing', 200.00, 'BRL'),
#     ('Mount Fuji', 'adventure', 500.00, 'JPY'),
#     ('Buckingham Palace', 'historical', 150.00, 'GBP'),
#     ('Mount Kilimanjaro', 'adventure', 700.00, 'TZS'),
#     ('Angkor Wat', 'historical', 300.00, 'KHR'),
#     ('Petra', 'historical', 400.00, 'JOD'),
#     ('Iguazu Falls', 'adventure', 500.00, 'BRL')
# ]

# # Insert multiple rows into tours table
# cursor.executemany('''
#     INSERT INTO tours (location, type, price, currency)
#     VALUES (?, ?, ?, ?)
# ''', tours_data)

# cruises_data = [
#     ('Caribbean', '7 days', 1200.00, 'USD'),
#     ('Mediterranean', '10 days', 1500.00, 'EUR'),
#     ('Alaska', '14 days', 2000.00, 'USD'),
#     ('Baltic Sea', '7 days', 1400.00, 'EUR'),
#     ('Hawaii', '5 days', 1100.00, 'USD'),
#     ('Australia', '12 days', 1800.00, 'AUD'),
#     ('New Zealand', '10 days', 1700.00, 'NZD'),
#     ('South Pacific', '15 days', 2200.00, 'USD'),
#     ('Norwegian Fjords', '7 days', 1600.00, 'EUR'),
#     ('Panama Canal', '8 days', 1300.00, 'USD'),
#     ('Mexico', '5 days', 1000.00, 'USD'),
#     ('Southeast Asia', '10 days', 1900.00, 'SGD'),
#     ('South America', '14 days', 2100.00, 'USD'),
#     ('Galapagos Islands', '7 days', 2500.00, 'USD'),
#     ('Antarctica', '20 days', 3000.00, 'USD'),
#     ('Transatlantic', '12 days', 1600.00, 'USD'),
#     ('Greek Isles', '9 days', 1700.00, 'EUR'),
#     ('Canary Islands', '7 days', 1500.00, 'EUR'),
#     ('Japan', '10 days', 1800.00, 'JPY'),
#     ('China', '8 days', 1400.00, 'CNY'),
#     ('Black Sea', '7 days', 1300.00, 'EUR'),
#     ('Red Sea', '6 days', 1200.00, 'USD'),
#     ('Indian Ocean', '14 days', 2400.00, 'USD'),
#     ('Western Mediterranean', '10 days', 2000.00, 'EUR'),
#     ('Eastern Mediterranean', '12 days', 2100.00, 'EUR'),
#     ('Adriatic Sea', '8 days', 1400.00, 'EUR'),
#     ('Rhone River', '7 days', 1700.00, 'EUR'),
#     ('Danube River', '9 days', 1800.00, 'EUR'),
#     ('Mekong River', '10 days', 1500.00, 'USD'),
#     ('Amazon River', '12 days', 2200.00, 'USD')
# ]

# # Insert multiple rows into cruises table
# cursor.executemany('''
#     INSERT INTO cruises (destination, duration, price, currency)
#     VALUES (?, ?, ?, ?)
# ''', cruises_data)

# car_rentals_data = [
#     ('New York', 50.00, 'USD'),
#     ('Los Angeles', 45.00, 'USD'),
#     ('Chicago', 40.00, 'USD'),
#     ('Houston', 42.00, 'USD'),
#     ('Phoenix', 38.00, 'USD'),
#     ('Philadelphia', 47.00, 'USD'),
#     ('San Antonio', 41.00, 'USD'),
#     ('San Diego', 44.00, 'USD'),
#     ('Dallas', 43.00, 'USD'),
#     ('San Jose', 39.00, 'USD'),
#     ('Austin', 36.00, 'USD'),
#     ('Jacksonville', 37.00, 'USD'),
#     ('Fort Worth', 48.00, 'USD'),
#     ('Columbus', 46.00, 'USD'),
#     ('Charlotte', 49.00, 'USD'),
#     ('San Francisco', 51.00, 'USD'),
#     ('Indianapolis', 35.00, 'USD'),
#     ('Seattle', 52.00, 'USD'),
#     ('Denver', 53.00, 'USD'),
#     ('Washington', 54.00, 'USD'),
#     ('Boston', 55.00, 'USD'),
#     ('El Paso', 33.00, 'USD'),
#     ('Nashville', 34.00, 'USD'),
#     ('Detroit', 32.00, 'USD'),
#     ('Oklahoma City', 31.00, 'USD'),
#     ('Portland', 30.00, 'USD')
# ]

# # Insert multiple rows into car_rentals table
# cursor.executemany('''
#     INSERT INTO car_rentals (city, price_per_day, currency)
#     VALUES (?, ?, ?)
# ''', car_rentals_data)
# conn.commit()

cursor.execute('''
    SELECT name FROM sqlite_master WHERE type='table';
''')

# # Fetch and print all tables
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])

def print_table_contents(table_name):
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    print(f"{table_name.capitalize()} table contents:")
    for row in rows:
        print(row)

print_table_contents('flights')
print_table_contents('hotels')
print_table_contents('packages')
print_table_contents('tours')
print_table_contents('cruises')
print_table_contents('car_rentals')

# Commit the changes and close the connection

conn.close()
