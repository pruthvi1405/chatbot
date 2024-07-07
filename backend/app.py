from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
from model import classify_sentence
import sqlite3
import re

app = Flask(__name__)
CORS(app)
load_dotenv()

client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

table_keywords = {
    'flights': ['flight', 'departure', 'arrival', 'class', 'price', 'currency'],
    'hotels': ['hotel', 'city', 'star', 'rating', 'night', 'price', 'currency'],
    'packages': ['package', 'destination', 'type', 'price', 'currency'],
    'tours': ['tour', 'location', 'type', 'price', 'currency'],
    'cruises': ['cruise', 'destination', 'duration', 'price', 'currency'],
    'car_rentals': ['car', 'rental', 'city', 'price', 'day', 'currency']
}

def identify_table(sentence):
    sentence = sentence.lower()
    table_scores = {table: 0 for table in table_keywords.keys()}
    
    for table, keywords in table_keywords.items():
        for keyword in keywords:
            if keyword in sentence:
                table_scores[table] += 1
    
    # Find the table with the highest score
    identified_table = max(table_scores, key=table_scores.get)
    
    # Return specific instructions based on the identified table
    if identified_table == "hotels":
        return ("Just provide a valid SQL query without additional texts for fetching hotel details from the hotels table "
                "(hotel_id INTEGER PRIMARY KEY AUTOINCREMENT, city TEXT, star_rating INTEGER, price_per_night REAL, currency TEXT) "
                "using the keywords in the following sentence: ")
    elif identified_table == "flights":
        return ("Just provide a valid SQL query without additional texts for fetching flight details from the flights table "
                "(flight_id INTEGER PRIMARY KEY AUTOINCREMENT, departure_city TEXT, arrival_city TEXT, class TEXT, price REAL, currency TEXT) "
                "using the keywords in the following sentence: ")
    elif identified_table == "car_rentals":
        return ("Just provide a valid SQL query without additional texts for fetching rental details from the car_rentals table "
                "(rental_id INTEGER PRIMARY KEY AUTOINCREMENT, city TEXT, price_per_day REAL, currency TEXT) "
                "using the keywords in the following sentence: ")
    elif identified_table == "packages":
        return ("Just provide a valid SQL query without additional texts for fetching package details from the packages table "
                "(package_id INTEGER PRIMARY KEY AUTOINCREMENT, destination TEXT, type TEXT, price REAL, currency TEXT) "
                "using the keywords in the following sentence: ")
    elif identified_table == "tours":
        return ("Just provide a valid SQL query without additional texts for fetching tour details from the tours table "
                "(tour_id INTEGER PRIMARY KEY AUTOINCREMENT, location TEXT, type TEXT, price REAL, currency TEXT) "
                "using the keywords in the following sentence: ")
    elif identified_table == "cruises":
        return ("Just provide a valid SQL query without additional texts for fetching cruise details from the cruises table "
                "(cruise_id INTEGER PRIMARY KEY AUTOINCREMENT, destination TEXT, duration TEXT, price REAL, currency TEXT) "
                "using the keywords in the following sentence: ")
    else:
        return "Help like a travel agent using the keywords provided"





def extract_and_capitalize_sql(response):
    # Extract the SQL query between ```sql and ```
    start_idx = response.find("```sql") + len("```sql")
    end_idx = response.find("```", start_idx)
    sql_query = response[start_idx:end_idx].strip()
    
    # Regular expression to find city names in the query
    city_pattern = re.compile(r"departure_city = '([^']+)' AND arrival_city = '([^']+)'", re.IGNORECASE)
    
    # Find the city names
    match = city_pattern.search(sql_query)
    if match:
        departure_city = match.group(1).title()
        arrival_city = match.group(2).title()
        
        # Replace with capitalized city names
        new_query = city_pattern.sub(
            f"departure_city = '{departure_city}' AND arrival_city = '{arrival_city}'", 
            sql_query
        )
        return new_query
    else:
        return sql_query


def handle_general(api_messages,messages):
    try:
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages= api_messages
        )
        chat_gpt_message=response.choices[0].message.content

        response_message = {
            'role': 'assistant',
            'content': chat_gpt_message
        }

        messages.append(response_message)
        return messages

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def handle_propriety(api_messages, messages, sentence):
    print(sentence)
    try:
        prompt=identify_table(sentence)
        # Constructing the prompt for the AI model
        # prompt = (
        #     "Just provide a valid SQL query without additional texts for fetching flight details from the flights table "
        #     "(flight_id INTEGER PRIMARY KEY AUTOINCREMENT, departure_city TEXT, arrival_city TEXT, class TEXT, price REAL, currency TEXT) "
        #     "using the keywords in the following sentence: " + sentence
        # )
        # Generating the SQL query using GPT-3.5-turbo
        print(prompt+sentence)
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are an assistant that generates SQL queries."},
                {"role": "user", "content": prompt+sentence}
            ]
        )
        # sql_query=(response.choices[0].message.content)  # Printing the generated SQL query
        sql_query=extract_and_capitalize_sql(response.choices[0].message.content)
        print(sql_query)

        conn = sqlite3.connect('travel_agent.db')
        # Create a cursor object
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        conn.close()
        print(result)
        result_string = '\n'.join([str(row) for row in result])
        print(result_string)
        response1 = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "Provide information like a travel agent from the details fetched "},
                {"role": "user", "content": result_string}
            ]
        )

        print(response1.choices[0].message.content)
        # Constructing the assistant's message
        # chat_gpt_message = "This is proprietary information."
        
        response_message = {
            'role': 'assistant',
            'content': response1.choices[0].message.content
        }
        
        messages.append(response_message)
        return messages
    except sqlite3.Error as e:
        print("SQLite Error: ", e)
    except Exception as e:
        return {'error': str(e)}, 500
    

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data.get('messages', [])
    api_messages = [{'role': 'user', 'content': msg['content']} for msg in messages]
    system_message = {'role': 'system', 'content': 'Speak like a travel Agent'}
    api_messages.insert(0, system_message)

    classified=classify_sentence(messages[-1]['content'])
    print(classified[0])
    if classified[0]=="general_knowledge":
        return_message=handle_general(api_messages,messages)
        return jsonify(return_message), 200
    else:
        return_message=handle_propriety(api_messages,messages,classified[1])
        return jsonify(return_message), 200

    # try:
    #     response = client.chat.completions.create(
    #         model='gpt-3.5-turbo',
    #         messages= api_messages
    #     )
    #     chat_gpt_message=response.choices[0].message.content

    #     response_message = {
    #         'role': 'assistant',
    #         'content': chat_gpt_message
    #     }

    #     messages.append(response_message)
    #     return jsonify(messages), 200

    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)
