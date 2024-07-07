
# Generate more records programmatically for brevity
general_knowledge_questions = [
    "What is the best time to visit New York?",
    "What are the must-see places in London?",
    "Which are the best restaurants in Tokyo?",
    "What is the most famous landmark in Italy?",
    "What activities can you do in Bali?",
    "Which museums should I visit in Madrid?",
    "What’s the weather like in Sydney during summer?",
    "What are the popular festivals in Brazil?",
    "Which cities should I visit in Canada?",
    "What are the best hiking trails in Switzerland?",
    "What are the best beaches in Thailand?",
    "What is the nightlife like in Berlin?",
    "What are some good day trips from Amsterdam?",
    "What cultural experiences can I have in India?",
    "What are the top shopping destinations in Dubai?",
    "Which national parks should I visit in the USA?",
    "What are the best places for skiing in Austria?",
    "What historical sites can I see in Greece?",
    "What are the top family attractions in Florida?",
    "What are the best places to stay in Hawaii?",
    "What wildlife can I see on a safari in Kenya?",
    "What are the best viewpoints in San Francisco?",
    "What’s the local cuisine like in Mexico?",
    "What are the top attractions in Istanbul?",
    "What’s the best way to travel around Australia?",
    "What are some unique experiences in South Africa?",
    "What are the must-see temples in Thailand?",
    "What are the best places for diving in the Maldives?",
    "What’s the best time of year to visit Iceland?",
    "What are the most beautiful villages in France?",
    "What’s the best way to explore the Amazon rainforest?",
    "What are the top-rated hotels in Rome?",
    "What are the best vineyards to visit in Argentina?",
    "What are the famous markets in Marrakech?",
    "What are the must-try foods in Vietnam?",
    "What are the best beaches in the Caribbean?",
    "What are the top hiking destinations in Peru?",
    "What are the best places to see cherry blossoms in Japan?",
    "What’s the best way to experience the Northern Lights?",
    "What are the top islands to visit in Greece?",
    "What are the best art galleries in New York?",
    "What are the must-do activities in New Zealand?",
    "What are the top places to visit in Scotland?",
    "What are the best historical sites in Egypt?",
    "What are the best places to stay in the Maldives?",
    "What are the best road trips in the USA?",
    "What are the must-see natural wonders in Australia?",
    "What are the best places to go snorkeling in the Caribbean?",
    "What are the top cultural sites in China?",
    "What are the best places to visit in Portugal?",
    "What are the best festivals to attend in Europe?",
    "What are the must-see landmarks in Russia?",
    "What are the best places to see wildlife in Africa?",
    "What are the top attractions in Los Angeles?",
    "What are the best spots for surfing in Hawaii?",
    "What are the must-see castles in Germany?",
    "What are the best places for street food in Asia?",
    "What are the top ski resorts in Canada?",
    "What are the must-visit cities in Italy?",
    "What are the best places for adventure sports in New Zealand?",
    "What are the top cultural experiences in South America?",
    "What are the best places to relax in the Seychelles?",
    "What are the must-see temples in India?",
    "What are the best places to visit in Norway?",
    "What are the top culinary destinations in Europe?",
    "What are the best places for whale watching in Alaska?",
    "What are the best places to explore in Antarctica?",
    "What are the top family vacation spots in the USA?",
    "What are the best places for a romantic getaway in France?",
    "What are the must-visit attractions in Dubai?",
    "What are the best places for scuba diving in Indonesia?",
    "What are the best places to experience autumn in the USA?",
    "What are the top beach destinations in Mexico?",
    "What are the must-see ruins in Peru?",
    "What are the best places to see wildlife in Australia?",
    "What are the best places to visit in Ireland?",
    "What are the top UNESCO World Heritage Sites in Europe?",
    "What are the best hiking trails in Patagonia?",
    "What are the best places for a city break in Europe?",
    "What are the top safari destinations in Africa?",
    "What are the best places to experience local culture in Asia?",
    "What are the must-see sites in Rome?",
    "What are the best places for birdwatching in Costa Rica?",
    "What are the top destinations for food lovers in Asia?",
    "What are the best places to visit in Spain?",
    "What are the best islands to visit in the Caribbean?",
    "What are the top places to visit in Central America?",
    "What are the best cities for architecture in Europe?",
    "What are the must-see places in Iceland?",
    "What are the best places for mountain climbing in the Himalayas?",
    "What are the best cities to visit in Eastern Europe?",
    "What are the top cultural festivals in Asia?",
    "What are the best places for a road trip in Australia?",
    "What are the must-see waterfalls in South America?",
    "What are the best places to visit in Croatia?",
    "What are the top family-friendly destinations in Asia?",
    "What are the best places to see autumn foliage in Japan?",
    "What are the top wine regions in Italy?",
    "What are the best places to visit in South Korea?",
    "What are the must-see national parks in Canada?",
    "What are the best places to visit in Finland?",
    "What are the top diving spots in the Red Sea?",
    "What are the best places for outdoor activities in Norway?",
    "What are the must-see landmarks in Washington, D.C.?",
    "What are the best places to visit in the Netherlands?",
    "What are the top culinary experiences in the Middle East?",
    "What are the best places for a beach holiday in Europe?",
    "What are the best places to visit in Belgium?",
    "What are the top cultural destinations in North America?",
    "What are the best places to visit in Malaysia?",
    "What are the must-see sights in Sydney?",
    "What are the best places for nature lovers in New Zealand?",
    "What are the top winter destinations in Europe?",
    "What are the best places to visit in the Philippines?",
    "What are the top attractions in Las Vegas?",
    "What are the must-visit places in Chile?",
    "What are the best places to visit in Sri Lanka?",
    "What are the top adventure destinations in South America?",
    "What are the must-see places in Prague?",
    "What are the best places to visit in the French Riviera?",
    "What are the best places to visit in Turkey?",
    "What are the top tourist destinations in Africa?",
    "What are the best places to visit in the Caribbean?",
    "What are the must-visit places in Budapest?",
    "What are the top destinations for hiking in Europe?",
    "What are the best places for a city break in Asia?",
    "What are the best places to visit in Morocco?",
    "What are the top attractions in Rio de Janeiro?",
    "What are the best places for island hopping in Greece?",
    "What are the must-see places in Lisbon?",
    "What are the best places to visit in Austria?",
    "What are the top cultural destinations in Africa?",
    "What are the best places to visit in Costa Rica?",
    "What are the must-see places in Havana?",
    "What are the best places to visit in Vietnam?",
    "What are the top destinations for art lovers in Europe?",
    "What are the best places to visit in the Seychelles?",
    "What are the must-see places in Cape Town?",
    "What are the top adventure destinations in Australia?",
    "What are the best places to visit in Germany?",
    "What are the must-visit places in the Swiss Alps?",
    "What are the best places to visit in Greece?",
    "What are the top destinations for winter sports in Europe?",
    "What are the best places to visit in Argentina?",
    "What are the must-see places in New Zealand?",
    "What are the best places to visit in Peru?",
    "What are the top destinations for cultural experiences in India?",
    "What are the best places to visit in Thailand?",
    "What are the must-see places in Mexico City?",
    "What are the best places to visit in Cambodia?",
    "What are the top destinations for nature lovers in Canada?",
    "What are the best places to visit in Brazil?",
    "What are the must-see places in Paris?",
    "What are the best places to visit in Scotland?",
    "What are the top destinations for wine lovers in France?",
    "What are the best places to visit in Iceland?",
    "What are the must-see places in Tokyo?",
    "What are the best places to visit in Spain?",
    "What are the top destinations for beach holidays in the Maldives?",
    "What are the best places to visit in South Africa?",
    "What are the must-see places in New York City?",
    "What are the best places to visit in Australia?",
    "What are the top destinations for cultural experiences in Japan?",
    "What are the best places to visit in Italy?",
    "What are the must-see places in London?",
    "What are the best places to visit in Indonesia?",
    "What are the top destinations for history lovers in Egypt?",
    "What are the best places to visit in China?",
    "What are the must-see places in Los Angeles?",
    "What are the best places to visit in Malaysia?",
    "What are the top destinations for nature enthusiasts in New Zealand?",
    "What are the best places to visit in Switzerland?",
    "What are the must-see places in Berlin?",
    "What are the best places to visit in Thailand?",
    "What are the top destinations for foodies in Italy?",
    "What are the best places to visit in the United States?",
    "What are the must-see places in Rome?",
    "What are the best places to visit in Greece?",
    "What are the top destinations for art and culture in Paris?",
    "What are the best places to visit in Mexico?",
    "What are the must-see places in Amsterdam?",
    "What are the best places to visit in the Caribbean?",
    "What are the top destinations for adventure seekers in Costa Rica?",
    "What are the best places to visit in Vietnam?",
    "What are the must-see places in Barcelona?",
    "What are the best places to visit in the Seychelles?",
    "What are the top destinations for outdoor activities in Norway?",
    "What are the best places to visit in Portugal?",
    "What are the must-see places in Sydney?",
    "What are the best places to visit in Japan?",
    "What are the top destinations for wine tasting in Argentina?",
    "What are the best places to visit in Austria?",
    "What are the must-see places in Istanbul?",
    "What are the best places to visit in South America?",
    "What are the top destinations for nature lovers in Kenya?",
    "What are the best places to visit in South Africa?",
    "What are the must-see places in Hong Kong?",
    "What are the best places to visit in Thailand?",
    "What are the top destinations for scuba diving in Indonesia?",
    "What are the best places to visit in the Philippines?",
    "What are the must-see places in Moscow?",
    "What are the best places to visit in Europe?",
    "What are the top destinations for winter sports in Canada?",
    "What are the best places to visit in Egypt?",
    "What are the must-see places in Cape Town?",
    "What are the best places to visit in Malaysia?",
    "What are the top destinations for hiking in Switzerland?",
    "What are the best places to visit in Greece?",
    "What are the must-see places in Rio de Janeiro?",
    "What are the best places to visit in the Maldives?",
    "What are the top destinations for cultural experiences in Japan?",
    "What are the best places to visit in Australia?",
    "What are the must-see places in Madrid?",
    "What are the best places to visit in China?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in South Korea?",
    "What are the must-see places in Bangkok?",
    "What are the best places to visit in Italy?",
    "What are the top destinations for adventure sports in New Zealand?",
    "What are the best places to visit in Turkey?",
    "What are the must-see places in Dubai?",
    "What are the best places to visit in the Caribbean?",
    "What are the top destinations for cultural experiences in Europe?",
    "What are the best places to visit in Vietnam?",
    "What are the must-see places in Los Angeles?",
    "What are the best places to visit in Scotland?",
    "What are the top destinations for food lovers in Asia?",
    "What are the best places to visit in Argentina?",
    "What are the must-see places in Istanbul?",
    "What are the best places to visit in Spain?",
    "What are the top destinations for adventure travel in Costa Rica?",
    "What are the best places to visit in the Seychelles?",
    "What are the must-see places in Berlin?",
    "What are the best places to visit in Portugal?",
    "What are the top destinations for cultural tourism in Africa?",
    "What are the best places to visit in the United States?",
    "What are the must-see places in London?",
    "What are the best places to visit in Japan?",
    "What are the top destinations for beach holidays in the Maldives?",
    "What are the best places to visit in Switzerland?",
    "What are the must-see places in Paris?",
    "What are the best places to visit in New Zealand?",
    "What are the top destinations for cultural experiences in Italy?",
    "What are the best places to visit in Mexico?",
    "What are the must-see places in New York City?",
    "What are the best places to visit in Thailand?",
    "What are the top destinations for nature lovers in Norway?",
    "What are the best places to visit in China?",
    "What are the must-see places in Rome?",
    "What are the best places to visit in Indonesia?",
    "What are the top destinations for adventure travel in South America?",
    "What are the best places to visit in Malaysia?",
    "What are the must-see places in Athens?",
    "What are the best places to visit in the Philippines?",
    "What are the top destinations for cultural tourism in Japan?",
    "What are the best places to visit in Argentina?",
    "What are the must-see places in Venice?",
    "What are the best places to visit in Europe?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in Greece?",
    "What are the must-see places in Sydney?",
    "What are the best places to visit in Brazil?",
    "What are the top destinations for cultural experiences in India?",
    "What are the best places to visit in the United States?",
    "What are the must-see places in Barcelona?",
    "What are the best places to visit in Thailand?",
    "What are the top destinations for nature lovers in Canada?",
    "What are the best places to visit in New Zealand?",
    "What are the must-see places in Mexico City?",
    "What are the best places to visit in Italy?",
    "What are the top destinations for adventure travel in Australia?",
    "What are the best places to visit in Turkey?",
    "What are the must-see places in Paris?",
    "What are the best places to visit in South Korea?",
    "What are the top destinations for cultural tourism in Europe?",
    "What are the best places to visit in the Maldives?",
    "What are the must-see places in Lisbon?",
    "What are the best places to visit in Spain?",
    "What are the top destinations for food lovers in Asia?",
    "What are the best places to visit in Switzerland?",
    "What are the must-see places in Tokyo?",
    "What are the best places to visit in Vietnam?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in the Seychelles?",
    "What are the must-see places in Berlin?",
    "What are the best places to visit in Australia?",
    "What are the top destinations for cultural tourism in Japan?",
    "What are the best places to visit in France?",
    "What are the must-see places in Dubai?",
    "What are the best places to visit in Malaysia?",
    "What are the top destinations for adventure travel in South America?",
    "What are the best places to visit in Canada?",
    "What are the must-see places in New York City?",
    "What are the best places to visit in the Philippines?",
    "What are the top destinations for cultural tourism in Italy?",
    "What are the best places to visit in the Caribbean?",
    "What are the must-see places in Bangkok?",
    "What are the best places to visit in Greece?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in Portugal?",
    "What are the must-see places in Cape Town?",
    "What are the best places to visit in South America?",
    "What are the top destinations for nature lovers in Norway?",
    "What are the best places to visit in Thailand?",
    "What are the must-see places in Rio de Janeiro?",
    "What are the best places to visit in Vietnam?",
    "What are the top destinations for adventure travel in Australia?",
    "What are the best places to visit in China?",
    "What are the must-see places in Los Angeles?",
    "What are the best places to visit in the United States?",
    "What are the top destinations for cultural tourism in Europe?",
    "What are the best places to visit in South Africa?",
    "What are the must-see places in Rome?",
    "What are the best places to visit in Indonesia?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in New Zealand?",
    "What are the must-see places in Tokyo?",
    "What are the best places to visit in Italy?",
    "What are the top destinations for adventure travel in South America?",
    "What are the best places to visit in the Maldives?",
    "What are the must-see places in Paris?",
    "What are the best places to visit in Spain?",
    "What are the top destinations for cultural tourism in Japan?",
    "What are the best places to visit in Switzerland?",
    "What are the must-see places in New York City?",
    "What are the best places to visit in Thailand?",
    "What are the top destinations for nature lovers in Norway?",
    "What are the best places to visit in the Seychelles?",
    "What are the must-see places in Berlin?",
    "What are the best places to visit in France?",
    "What are the top destinations for cultural tourism in Europe?",
    "What are the best places to visit in Canada?",
    "What are the must-see places in Bangkok?",
    "What are the best places to visit in the Philippines?",
    "What are the top destinations for adventure travel in Australia?",
    "What are the best places to visit in Greece?",
    "What are the must-see places in Los Angeles?",
    "What are the best places to visit in the United States?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in Italy?",
    "What are the must-see places in Sydney?",
    "What are the best places to visit in Vietnam?",
    "What are the top destinations for cultural tourism in Japan?",
    "What are the best places to visit in Portugal?",
    "What are the must-see places in Rio de Janeiro?",
    "What are the best places to visit in South Africa?",
    "What are the top destinations for adventure travel in South America?",
    "What are the best places to visit in Malaysia?",
    "What are the must-see places in New York City?",
    "What are the best places to visit in the Seychelles?",
    "What are the top destinations for nature lovers in Norway?",
    "What are the best places to visit in the Caribbean?",
    "What are the must-see places in Rome?",
    "What are the best places to visit in the Maldives?",
    "What are the top destinations for cultural tourism in Europe?",
    "What are the best places to visit in China?",
    "What are the must-see places in Cape Town?",
    "What are the best places to visit in Australia?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in Indonesia?",
    "What are the must-see places in Tokyo?",
    "What are the best places to visit in Switzerland?",
    "What are the top destinations for adventure travel in South America?",
    "What are the best places to visit in New Zealand?",
    "What are the must-see places in Paris?",
    "What are the best places to visit in the United States?",
    "What are the top destinations for cultural tourism in Japan?",
    "What are the best places to visit in Greece?",
    "What are the must-see places in Bangkok?",
    "What are the best places to visit in Canada?",
    "What are the top destinations for nature lovers in Norway?",
    "What are the best places to visit in Spain?",
    "What are the must-see places in Berlin?",
    "What are the best places to visit in Malaysia?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in France?",
    "What are the must-see places in New York City?",
    "What are the best places to visit in the Philippines?",
    "What are the top destinations for cultural tourism in Europe?",
    "What are the best places to visit in Vietnam?",
    "What are the must-see places in Rio de Janeiro?",
    "What are the best places to visit in the Maldives?",
    "What are the top destinations for adventure travel in South America?",
    "What are the best places to visit in Portugal?",
    "What are the must-see places in Sydney?",
    "What are the best places to visit in the United States?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in China?",
    "What are the must-see places in Tokyo?",
    "What are the best places to visit in Greece?",
    "What are the top destinations for cultural tourism in Japan?",
    "What are the best places to visit in the Seychelles?",
    "What are the must-see places in Los Angeles?",
    "What are the best places to visit in Spain?",
    "What are the top destinations for nature lovers in Norway?",
    "What are the best places to visit in the Philippines?",
    "What are the must-see places in New York City?",
    "What are the best places to visit in Italy?",
    "What are the top destinations for adventure travel in Australia?",
    "What are the best places to visit in France?",
    "What are the must-see places in Bangkok?",
    "What are the best places to visit in the Caribbean?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in Portugal?",
    "What are the must-see places in Cape Town?",
    "What are the best places to visit in the United States?",
    "What are the top destinations for cultural tourism in Europe?",
    "What are the best places to visit in Indonesia?",
    "What are the must-see places in Rome?",
    "What are the best places to visit in the Maldives?",
    "What are the top destinations for adventure travel in South America?",
    "What are the best places to visit in Canada?",
    "What are the must-see places in Sydney?",
    "What are the best places to visit in the Philippines?",
    "What are the top destinations for nature lovers in Norway?",
    "What are the best places to visit in Greece?",
    "What are the must-see places in Los Angeles?",
    "What are the best places to visit in South Africa?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in Japan?",
    "What are the must-see places in Bangkok?",
    "What are the best places to visit in China?",
    "What are the top destinations for cultural tourism in Japan?",
    "What are the best places to visit in the Seychelles?",
    "What are the must-see places in Tokyo?",
    "What are the best places to visit in Italy?",
    "What are the top destinations for adventure travel in Australia?",
    "What are the best places to visit in Portugal?",
    "What are the must-see places in Paris?",
    "What are the best places to visit in the Maldives?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in Indonesia?",
    "What are the must-see places in New York City?",
    "What are the best places to visit in the United States?",
    "What are the top destinations for nature lovers in Norway?",
    "What are the best places to visit in Greece?",
    "What are the must-see places in Los Angeles?",
    "What are the best places to visit in the Philippines?",
    "What are the top destinations for cultural tourism in Europe?",
    "What are the best places to visit in Vietnam?",
    "What are the must-see places in Rio de Janeiro?",
    "What are the best places to visit in the Maldives?",
    "What are the top destinations for adventure travel in South America?",
    "What are the best places to visit in Portugal?",
    "What are the must-see places in Cape Town?",
    "What are the best places to visit in the United States?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in China?",
    "What are the must-see places in Tokyo?",
    "What are the best places to visit in the Seychelles?",
    "What are the top destinations for cultural tourism in Japan?",
    "What are the best places to visit in Greece?",
    "What are the must-see places in Los Angeles?",
    "What are the best places to visit in France?",
    "What are the top destinations for adventure travel in Australia?",
    "What are the best places to visit in Italy?",
    "What are the must-see places in New York City?",
    "What are the best places to visit in Vietnam?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in Spain?",
    "What are the must-see places in Berlin?",
    "What are the best places to visit in the Maldives?",
    "What are the top destinations for cultural tourism in Europe?",
    "What are the best places to visit in Switzerland?",
    "What are the must-see places in Sydney?",
    "What are the best places to visit in the United States?",
    "What are the top destinations for nature lovers in Norway?",
    "What are the best places to visit in Portugal?",
    "What are the must-see places in Rome?",
    "What are the best places to visit in the Seychelles?",
    "What are the top destinations for wildlife watching in Africa?",
    "What are the best places to visit in China?",
    "What are the must-see places in Tokyo?",
    "What are the best places to visit in the Philippines?",
    "What are the top destinations for cultural tourism in Japan?",
    "What are the best places to visit in Greece?",
    "What are the must-see places in Los Angeles?",
    "What are the best places to visit in France?",
    "What are the top destinations for adventure travel in Australia?",
    "What are the best places to visit in Italy?",
    "What are the must-see places in New York City?",
    "What are the best places to visit in Vietnam?",
    "What are the top destinations for wildlife watching in Africa"
    ]


proprietary_questions = [
    "How much does a round-trip flight from New York to Tokyo cost?",
    "What are the rates for business class tickets to London from Sydney?",
    "Can you provide details on the honeymoon packages for the Maldives?",
    "What is the price range for all-inclusive family vacations to the Caribbean?",
    "How much does a cruise package to Alaska cost for two people?",
    "What are the prices for eco-friendly travel packages in Costa Rica?",
    "Can you give me information on budget-friendly tours to Europe?",
    "How expensive are luxury safari packages in Africa?",
    "What are the costs associated with solo traveler tours to Southeast Asia?",
    "What is the price for a week-long stay in a five-star hotel in Paris?",
    "Can you provide a breakdown of the costs for ski vacation packages in Switzerland?",
    "How much would it cost for a guided tour of ancient ruins in Greece?",
    "What are the prices for adventure sports packages in New Zealand?",
    "Can you give me details on the cost of a cultural tour of India?",
    "What are the rates for guided tours of the Grand Canyon from Las Vegas?",
    "How much does a family trip to Disney World in Orlando cost?",
    "What is the price of a luxury river cruise in Europe?",
    "Can you provide information on the cost of food and accommodation in Japan?",
    "What are the expenses associated with a wine tasting tour in Tuscany?",
    "How much does a weekend getaway package to New York City cost?",
    "What is the price range for honeymoon cruises in the Mediterranean?",
    "Can you give me details on the cost of a historical tour of Egypt?",
    "What are the rates for beach resort packages in the Caribbean?",
    "How expensive are ski holiday packages in the Swiss Alps?",
    "What is the cost of a golf vacation in Scotland?",
    "Can you provide information on the prices for wellness retreats in Bali?",
    "What are the costs associated with scuba diving packages in the Great Barrier Reef?",
    "How much does a culinary tour of Italy cost?",
    "What is the price for a photography tour in Iceland?",
    "Can you give me details on the cost of a luxury train journey across Canada?",
    "What are the rates for cultural immersion trips to Morocco?",
    "How expensive are private yacht charters in the Mediterranean?",
    "What is the cost of a yoga retreat in Thailand?",
    "How much does a safari adventure in South Africa cost?",
    "What are the prices for spiritual retreats in India?",
    "Can you provide information on the cost of wine tours in Napa Valley?",
    "What is the price range for Northern Lights viewing tours in Norway?",
    "How expensive are guided hikes in the Rockies?",
    "How much does it cost to rent a car for a week in Los Angeles?",
    "What are the fees for guided tours of the Vatican in Rome?",
    "Can you provide details on the cost of a helicopter tour of New York City?",
    "What is the price for a beachfront villa rental in the Bahamas?",
    "How expensive are hot air balloon rides over Cappadocia, Turkey?",
    "What are the rates for private island rentals in the Maldives?",
    "How much does it cost for a guided fishing trip in Alaska?",
    "What are the prices for luxury spa retreats in Switzerland?",
    "Can you give me information on the cost of horseback riding tours in Iceland?",
    "What is the price range for guided tours of the Great Wall of China?",
    "How expensive are river cruises on the Danube River in Europe?",
    "What are the costs associated with private guided tours of Machu Picchu?",
    "How much does a snorkeling excursion in the Great Barrier Reef cost?",
    "What is the price of a sunrise hot air balloon ride in the Serengeti?",
    "Can you provide details on the cost of a cultural immersion program in Japan?",
    "What are the rates for gourmet food tours in France?",
    "How expensive are cooking classes in Tuscany, Italy?",
    "What is the cost of a guided wine tasting tour in Bordeaux?",
    "How much does it cost for a guided hike to Everest Base Camp?",
    "What are the prices for guided photography tours in Patagonia?",
    "Can you give me information on the cost of a luxury yacht charter in the Caribbean?",
    "What is the price range for helicopter skiing adventures in British Columbia?",
    "How expensive are private villa rentals in Santorini, Greece?",
    "What are the costs associated with cultural festivals tours in India?",
    "How much does it cost to attend the Oktoberfest in Munich, Germany?",
    "What is the price of a private cooking class in Bangkok, Thailand?",
    "Can you provide details on the cost of a wildlife safari in Tanzania?",
    "What are the rates for guided kayaking tours in New Zealand?",
    "How expensive are multi-country European tour packages?",
    "What is the cost of a guided cycling tour through the Loire Valley in France?",
    "How much does it cost for a day pass to Disneyland in California?",
    "What are the prices for luxury train journeys across India?",
    "Can you give me information on the cost of a private tour of the Louvre Museum in Paris?",
    "What is the price range for eco-lodges in the Amazon Rainforest?",
    "How expensive are private plane charters for island hopping in the Philippines?",
    "What are the costs associated with guided meditation retreats in Nepal?",
    "How much does it cost for a wine and cheese tasting tour in Provence, France?",
    "What is the price of a guided birdwatching tour in Costa Rica?",
    "Can you provide details on the cost of a cultural heritage tour in Morocco?",
    "What are the rates for luxury spa treatments in Bali?",
    "How expensive are private guided tours of the Kremlin in Moscow?",
    "What is the cost of a guided volcano hiking tour in Hawaii?",
    "How much does it cost for a ghost tour in New Orleans?",
    "What are the prices for luxury river cruises in Asia?",
    "Can you give me information on the cost of a private safari in Botswana?",
    "What is the price range for guided aurora borealis tours in Iceland?",
    "How expensive are private vineyard tours in California's Napa Valley?"
]


import nltk
import ssl

# nltk.data.path.append('/Users/pruthvi/nltk_data')  # Replace with your desired path
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

data=[]
for question in general_knowledge_questions:
  # Tokenization
  tokens = word_tokenize(question)

  # Stopword removal
  stop_words = set(stopwords.words('english'))
  filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

  # Lemmatization
  lemmatizer = WordNetLemmatizer()
  lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

  # Convert tokens back to a sentence (for TF-IDF vectorization)
  cleaned_question = ' '.join(lemmatized_tokens)

  # TF-IDF Vectorization
  vectorizer = TfidfVectorizer()
  tfidf_matrix = vectorizer.fit_transform([cleaned_question])

  str=""
  for i in vectorizer.get_feature_names_out():
    str+= i+" "
  data.append({"text":str,"label": "general_knowledge"})
for question in proprietary_questions:
  # Tokenization
  tokens = word_tokenize(question)

  # Stopword removal
  stop_words = set(stopwords.words('english'))
  filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

  # Lemmatization
  lemmatizer = WordNetLemmatizer()
  lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

  # Convert tokens back to a sentence (for TF-IDF vectorization)
  cleaned_question = ' '.join(lemmatized_tokens)

  # TF-IDF Vectorization
  vectorizer = TfidfVectorizer()
  tfidf_matrix = vectorizer.fit_transform([cleaned_question])

  str=""
  for i in vectorizer.get_feature_names_out():
    str+= i+" "
  data.append({"text":str,"label": "proprietary_information"})

df = pd.DataFrame(data)
X = df['text']
y = df['label']

# Split data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline = Pipeline([
    ('vect', CountVectorizer()),  # Convert text to word count vectors
    ('clf', MultinomialNB())      # Multinomial Naive Bayes classifier
])

# Train the pipeline
pipeline.fit(X_train, y_train)
print("Training Multinomial Naive Bayes...")
pipeline.fit(X_train, y_train)

# Make predictions on the test set
y_pred = pipeline.predict(X_test)

# Evaluate the classifier
print("\nMultinomial Naive Bayes Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
def preprocess_text(text):
    tokens = word_tokenize(text)
    filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words and word.isalpha()]
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    return ' '.join(lemmatized_tokens)
# Predict using all classifiers on new sentences
new_sentences = [
    "What are the top tourist attractions in Paris?",
    "How much would a flight ticket from Singapore to London cost?",
    "Can you provide details on the family holiday packages available for Europe",
    "What is the best time to visit Japan?"
]

print("\nPredictions:")
for sentence in new_sentences:
    print(f"Sentence: {sentence}")
    sentence=preprocess_text(sentence)
    X_new = [sentence]
    prediction = pipeline.predict(X_new)
    print(f"{prediction}")
    print()

# Function to classify a new sentence
def classify_sentence(sentence):
    sentence=preprocess_text(sentence)
    X_new = [sentence]
    prediction = pipeline.predict(X_new)
    return [prediction[0],sentence]

# Examples
examples = [
    "What’s the best place to visit in Singapore?",
    "what are the packages for singapore?",
    "best tourist packages for Paris"
]

for example in examples:
    print(f"Sentence: {example}")
    print(f"Classified as: {classify_sentence(example)}\n")
