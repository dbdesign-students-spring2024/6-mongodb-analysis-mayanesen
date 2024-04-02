# AirBnB MongoDB Analysis

A little assignment to practice importing and analyzing data within a MongoDB database.

Replace the contents of this file with a report, as described in the [instructions](./instructions.md).

### by Maya Nesen

## Dataset

I am working with [AirBnB data](https://insideairbnb.com/get-the-data/) from Paris, Ile de France, France, originally in CSV format. Download the original data set [here](https://data.insideairbnb.com/france/ile-de-france/paris/2023-12-12/data/listings.csv.gz). This data will be cleaned, as noted in the following section.

Below are the first 10 rows:

| id    | listing_url                        | scrape_id      | last_scraped | source          | name                                                      | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | neighborhood_overview                                                                                  | picture_url                                                                                | host_id                                 | host_url                                | host_name  | host_since    | host_location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | host_about                                                                                                                                   | host_response_time | host_response_rate | host_acceptance_rate                                                                                | host_is_superhost                                                                                      | host_thumbnail_url                                                                                         | host_picture_url                                                                                              | host_neighbourhood  | host_listings_count | host_total_listings_count | host_verifications                                      | host_has_profile_pic         | host_identity_verified       | neighbourhood                | neighbourhood_cleansed | neighbourhood_group_cleansed | latitude           | longitude                   | property_type      | room_type       | accommodates | bathrooms | bathrooms_text | bedrooms | beds   | amenities | price   | minimum_nights | maximum_nights | minimum_minimum_nights | maximum_minimum_nights | minimum_maximum_nights | maximum_maximum_nights | minimum_nights_avg_ntm | maximum_nights_avg_ntm | calendar_updated | has_availability | availability_30 | availability_60 | availability_90 | availability_365 | calendar_last_scraped | number_of_reviews | number_of_reviews_ltm | number_of_reviews_l30d | first_review | last_review | review_scores_rating | review_scores_accuracy | review_scores_cleanliness | review_scores_checkin | review_scores_communication                                | review_scores_location | review_scores_value                                    | license       | instant_bookable | calculated_host_listings_count | calculated_host_listings_count_entire_homes | calculated_host_listings_count_private_rooms | calculated_host_listings_count_shared_rooms | reviews_per_month |
| ----- | ---------------------------------- | -------------- | ------------ | --------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | --------------------------------------- | --------------------------------------- | ---------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------- | ------------------------- | ------------------------------------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------- | ---------------------------- | ------------------ | --------------------------- | ------------------ | --------------- | ------------ | --------- | -------------- | -------- | ------ | --------- | ------- | -------------- | -------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------- | ---------------- | --------------- | --------------- | --------------- | ---------------- | --------------------- | ----------------- | --------------------- | ---------------------- | ------------ | ----------- | -------------------- | ---------------------- | ------------------------- | --------------------- | ---------------------------------------------------------- | ---------------------- | ------------------------------------------------------ | ------------- | ---------------- | ------------------------------ | ------------------------------------------- | -------------------------------------------- | ------------------------------------------- | ----------------- |
| 3109  | https://www.airbnb.com/rooms/3109  | 20231212042736 | 2023-12-12   | city scrape     | Rental unit in Paris · ★5.0 · 1 bedroom · 1 bed · 1 bath  | Good restaurants<br />very close the Montparnasse Station<br />15 m from the center of Paris                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Alésia                                                                                                 | https://a0.muscache.com/pictures/baeae9e2-cd53-4ac3-b1bc-4055c0bb2e77.jpg                  | 3631                                    | https://www.airbnb.com/users/show/3631  | Anne       | 2008-10-14    | Paris, France                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                              | within a few hours | 100%               | 100%                                                                                                | f                                                                                                      | https://a0.muscache.com/im/users/3631/profile_pic/1375800198/original.jpg?aki_policy=profile_small         | https://a0.muscache.com/im/users/3631/profile_pic/1375800198/original.jpg?aki_policy=profile_x_medium         | Alésia              | 1                   | 2                         | ['email', 'phone']                                      | t                            | f                            | Paris, Île-de-France, France | Observatoire           |                              | 48.83191           | 2.3187                      | Entire rental unit | Entire home/apt | 2            |           | 1 bath         |          | 1      | []        | $150.00 | 2              | 30             | 2                      | 2                      | 30                     | 30                     | 2.0                    | 30.0                   | today            | t                | 30              | 60              | 90              | 365              | 2023-12-12            | 98                | 0                     | 0                      | 2010-07-17   | 2023-11-20  | 100.0                | 10.0                   | 10.0                      | 10.0                  | 10.0                                                       | 10.0                   | 10.0                                                   | 7510300081933 | f                | 2                              | 0                                           | 0                                            | 0                                           | 0.18              |
| 5396  | https://www.airbnb.com/rooms/5396  | 20231212042736 | 2023-12-12   | city scrape     | Rental unit in Paris · ★4.5 · 1 bedroom · 1 bed · 1 bath  | very close the Montparnasse Station<br />15 m from the center of Paris<br />Good restaurants                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Alésia                                                                                                 | https://a0.muscache.com/pictures/19601485/0b486f13_original.jpg?aki_policy=large           | 7903                                    | https://www.airbnb.com/users/show/7903  | Simon      | 2009-02-23    | Paris, France                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                              | within an hour     | 95%                | 85%                                                                                                 | f                                                                                                      | https://a0.muscache.com/im/pictures/user/5b24e109-fc53-4145-8672-395d5584333e.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/5b24e109-fc53-4145-8672-395d5584333e.jpg?aki_policy=profile_x_medium | Alésia              | 1                   | 2                         | ['email', 'phone']                                      | t                            | t                            | Paris, Île-de-France, France | Observatoire           |                              | 48.833494          | 2.31852                     | Entire rental unit | Entire home/apt | 2            |           | 1 bath         |          | 1      | []        | $99.00  | 2              | 60             | 2                      | 2                      | 60                     | 60                     | 2.0                    | 60.0                   | today            | t                | 30              | 60              | 90              | 365              | 2023-12-12            | 140               | 0                     | 0                      | 2010-07-27   | 2023-11-27  | 89.0                 | 9.0                    | 9.0                       | 9.0                   | 10.0                                                       | 9.0                    | 7510600689349                                          | f             | 2                | 0                              | 0                                           | 0                                            | 0.33                                        |
| 7397  | https://www.airbnb.com/rooms/7397  | 20231212042736 | 2023-12-12   | city scrape     | Rental unit in Paris · ★4.5 · 1 bedroom · 1 bed · 1 bath  | many restaurants, supermarkets, bakeries and other shops in the neighborhood<br />15 m from the center of Paris<br />A few minutes from the Seine, Notre-Dame, the Louvre, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Batignolles-Monceau                                                                                    | https://a0.muscache.com/pictures/273510/b8dd9243_original.jpg?aki_policy=large             | 19240                                   | https://www.airbnb.com/users/show/19240 | Michaël    | 2009-06-17    | Paris, France                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | I am a real estate developer, working in Paris. I like going out, meeting new people and traveling around the world.                         | within an hour     | 91%                | 100%                                                                                                | f                                                                                                      | https://a0.muscache.com/im/pictures/user/efc00b5b-5bd5-48a3-b3e3-8bbcfbdf8800.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/efc00b5b-5bd5-48a3-b3e3-8bbcfbdf8800.jpg?aki_policy=profile_x_medium | Batignolles-Monceau | 1                   | 2                         | ['email', 'phone', 'reviews', 'jumio', 'government_id'] | t                            | t                            | Paris, Île-de-France, France | Batignolles-Monceau    |                              | 48.881905          | 2.316725                    | Entire rental unit | Entire home/apt | 2            |           | 1 bath         |          | 1      | []        | $95.00  | 10             | 120            | 10                     | 10                     | 120                    | 120                    | 10.0                   | 120.0                  | today            | t                | 30              | 60              | 90              | 365              | 2023-12-12            | 167               | 0                     | 0                      | 2010-07-06   | 2023-11-18  | 90.0                 | 9.0                    | 10.0                      | 10.0                  | 9.0                                                        | 9.0                    | 7510900228284                                          | f             | 1                | 0                              | 0                                           | 0                                            | 0.39                                        |
| 7964  | https://www.airbnb.com/rooms/7964  | 20231212042736 | 2023-12-12   | city scrape     | Rental unit in Paris · ★4.5 · 1 bedroom · 1 bed · 1 bath  | The hotel is 200 meters from the Pere Lachaise cemetery.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Reuilly                                                                                                | https://a0.muscache.com/pictures/10995260/039a4ccf_original.jpg?aki_policy=large           | 21852                                   | https://www.airbnb.com/users/show/21852 | Andrea     | 2009-07-03    | Paris, France                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Hi, my name is Andrea, I'm Italian, I've been living in Paris for many years. I'm always happy to meet new people. I can't wait to meet you. | within an hour     | 97%                | 98%                                                                                                 | f                                                                                                      | https://a0.muscache.com/im/pictures/user/a8cbdaae-1612-49db-a0f9-100f88019050.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/a8cbdaae-1612-49db-a0f9-100f88019050.jpg?aki_policy=profile_x_medium | Reuilly             | 1                   | 2                         | ['email', 'phone']                                      | t                            | t                            | Paris, Île-de-France, France | Reuilly                |                              | 48.847868          | 2.398204                    | Entire rental unit | Entire home/apt | 2            |           | 1 bath         |          | 1      | []        | $70.00  | 10             | 120            | 10                     | 10                     | 120                    | 120                    | 10.0                   | 120.0                  | today            | t                | 30              | 60              | 90              | 365              | 2023-12-12            | 64                | 0                     | 0                      | 2010-07-08   | 2023-11-18  | 88.0                 | 10.0                   | 10.0                      | 9.0                   | 9.0                                                        | 9.0                    | 7511200133126                                          | f             | 2                | 0                              | 0                                           | 0                                            | 0.27                                        |
| 7992  | https://www.airbnb.com/rooms/7992  | 20231212042736 | 2023-12-12   | city scrape     | Rental unit in Paris · ★4.5 · 1 bedroom · 1 bed · 1 bath  | Cozy small studio, located in the heart of the Marais. Ideal for a couple or a solo traveler.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Hôtel-de-Ville                                                                                         | https://a0.muscache.com/pictures/5534d3a1-94be-487e-8594-d334f8ac498d.jpg?aki_policy=large | 24215                                   | https://www.airbnb.com/users/show/24215 | Delphine   | 2009-07-13    | Paris, France                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | In the heart of Paris, ideal for discovering Paris on foot. Very lively area with many restaurants, bars, museums and shops.                 | within an hour     | 100%               | 100%                                                                                                | f                                                                                                      | https://a0.muscache.com/im/pictures/user/6c9a1cb4-f0d0-41ff-8331-4827ed83df23.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/6c9a1cb4-f0d0-41ff-8331-4827ed83df23.jpg?aki_policy=profile_x_medium | Hôtel-de-Ville      | 1                   | 2                         | ['email', 'phone', 'reviews', 'jumio', 'government_id'] | t                            | t                            | Paris, Île-de-France, France | Hôtel-de-Ville         |                              | 48.857576          | 2.358962                    | Entire rental unit | Entire home/apt | 2            |           | 1 bath         |          | 1      | []        | $125.00 | 10             | 120            | 10                     | 10                     | 120                    | 120                    | 10.0                   | 120.0                  | today            | t                | 30              | 60              | 90              | 365              | 2023-12-12            | 120               | 0                     | 0                      | 2010-07-14   | 2023-11-25  | 96.0                 | 10.0                   | 10.0                      | 10.0                  | 10.0                                                       | 10.0                   | 7510400285898                                          | f             | 1                | 0                              | 0                                           | 0                                            | 0.37                                        |
| 10588 | https://www.airbnb.com/rooms/10588 | 20231212042736 | 2023-12-13   | city scrape     | Rental unit in Paris · ★4.90 · Studio · 1 bed · 1 bath    | Montmartre, the neighborhood surrounding the studio, maintains its physical charm and the village atmosphere remains remarkably intact. True montmartrians however, use their feet to visit the area. This is the perfect way to enjoy the unique architecture of the area: there are tiny exquisite squares, wooden houses, hidden parks, winding streets, small terraces and long stairways plus the Butte’s famous vineyard. <br /><br />Many shops and stores are close to the apartment: bakery, butcher, supermarkets, restaurants, cafes, clubs, laundromats, and doctors.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | https://a0.muscache.com/pictures/445734/5d7d275e_original.jpg                                          | 37107                                                                                      | https://www.airbnb.com/users/show/37107 | Michael                                 | 2009-09-08 | Paris, France | Licensed California Architect living in Paris I am a AIA member Feel free to contact me If you have any questions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | within a day                                                                                                                                 | 100%               | t                  | https://a0.muscache.com/im/users/37107/profile_pic/1333994771/original.jpg?aki_policy=profile_small | https://a0.muscache.com/im/users/37107/profile_pic/1333994771/original.jpg?aki_policy=profile_x_medium | Montmartre                                                                                                 | 3                                                                                                             | 5                   | ['email', 'phone']  | t                         | t                                                       | Paris, Ile-de-France, France | Buttes-Montmartre            |                              | 48.88725               | 2.34518                      | Entire rental unit | Entire home/apt             | 2                  |                 | 1 bath       |           | 1              | []       | $75.00 | 30        | 300     | 30             | 30             | 300                    | 300                    | 30.0                   | 300.0                  |                        | t                      | 22               | 49               | 64              | 216             | 2023-12-13      | 22               | 1                     | 0                 | 2011-03-13            | 2022-12-16             | 4.9          | 4.9         | 4.85                 | 5.0                    | 4.9                       | 4.65                  | "Available with a mobility lease only (""bail mobilité"")" | f                      | 3                                                      | 3             | 0                | 0                              | 0.14                                        |
| 11265 | https://www.airbnb.com/rooms/11265 | 20231212042736 | 2023-12-13   | city scrape     | Rental unit in Paris · ★4.90 · 1 bedroom · 1 bed · 1 bath | The apartment is located at the foot of charming Butte Montmartre. This historical area has now become truly « bourgeois bohême » with fashionable boutiques, galleries and young creators workshops. <br />But it has kept its old charm, with small steep streets and pretty cobbled squares, and its artistic soul, that which was born in the 19th century when Van Gogh, Toulouse Lautrec, Picasso, Modigliani, installed their easels inspired by the places. More recently it was the frame of many movies among which <br />« Le Fabuleux Destin d’Amélie Poulain ». It is like a village in the heart of Paris.<br />Montmartre is also unique for entertainment. Within 500 meters from the appartment are some of Paris most sought after places :<br />- le Sacré Cœur, 370 m<br />- le Moulin Rouge, 550 m<br />- le Moulin de la Galette, 300 m<br />- le cabaret Michou, 150 m<br />- les Vignes de Montmartre, 500 m<br />- concert hall la Cigale, 200 m<br />Also in the vicinity, are :<br />- 2 theaters, le Théâtre | https://a0.muscache.com/pictures/miso/Hosting-11265/original/da545dc1-8a12-4dad-813b-b2ba8c56dbc3.jpeg | 41718                                                                                      | https://www.airbnb.com/users/show/41718 | Sylvie                                  | 2009-09-28 | Paris, France | I usually live in Paris, but with my husband Daniel we love to travel, and particularly to sail, which we do each summer in the mediterranean waters. Therefore I rent my appartment in the summer from June to September. I've lived in several districts of Paris but finally decided to anchor in Montmartre, because it is charming, friendly, human scaled and very lively, and also perfectly served by public transportation, which makes family, friends, entertainment ... within easy reach. It combines perfectly all the benefits of a large metropolis and the charms of a very familiar spot. Since I stopped working I went back to school ... history, philosophy, political sciences, art, are on my weekly agenda together with gymnastics and pilates. With Daniel who is a great cook, we love to have people in for friendly evenings - we shaped the appartment specially for our social life - in between the joyful invasions of our grandchildren, a bunch of five aged two to eight. | N/A                                                                                                                                          | N/A                | 93%                | f                                                                                                   | https://a0.muscache.com/im/users/41718/profile_pic/1259122401/original.jpg?aki_policy=profile_small    | https://a0.muscache.com/im/users/41718/profile_pic/1259122401/original.jpg?aki_policy=profile_x_medium     | Montmartre                                                                                                    | 1                   | 1                   | ['email', 'phone']        | t                                                       | t                            | Paris, Île-de-France, France | Buttes-Montmartre            |                        | 48.88494                     | 2.33997            | Entire rental unit          | Entire home/apt    | 2               |              | 1 bath    |                | 1        | []     | $145.00   | 7       | 120            | 7              | 7                      | 120                    | 120                    | 7.0                    | 120.0                  |                        | t                | 0                | 0               | 0               | 18              | 2023-12-13       | 30                    | 8                 | 0                     | 2016-06-12             | 2023-10-02   | 4.9         | 4.9                  | 4.93                   | 4.76                      | 4.83                  | 4.97                                                       | 4.9                    | 7511801401834                                          | f             | 1                | 1                              | 0                                           | 0                                            | 0.33                                        |
| 11487 | https://www.airbnb.com/rooms/11487 | 20231212042736 | 2023-12-13   | city scrape     | Rental unit in Paris · ★4.44 · Studio · 1 bed · 1 bath    | This studio is in a building from 19th century (Hausmann ) with a paved yard . <br />Very well located in the Heart of Paris , near the place of Republic , the place des Vosges (one of the most ancient place of Paris ) and the place of La Bastille . It is a very lively neighborhood with wine bars ,art gallery and shops .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | https://a0.muscache.com/pictures/miso/Hosting-11487/original/f118ec4a-83ae-4501-993d-b756ec282001.jpeg | 42666                                                                                      | https://www.airbnb.com/users/show/42666 | Brigitte                                | 2009-10-01 | France        | ..                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | within a day                                                                                                                                 | 100%               | 50%                | t                                                                                                   | https://a0.muscache.com/im/users/42666/profile_pic/1262689368/original.jpg?aki_policy=profile_small    | https://a0.muscache.com/im/users/42666/profile_pic/1262689368/original.jpg?aki_policy=profile_x_medium     | République                                                                                                    | 1                   | 1                   | ['email', 'phone']        | t                                                       | t                            | Paris, Ile-de-France, France | Popincourt                   |                        | 48.86441                     | 2.37139            | Entire rental unit          | Entire home/apt    | 1               |              | 1 bath    |                | 1        | []     | $60.00    | 30      | 305            | 30             | 30                     | 305                    | 305                    | 30.0                   | 305.0                  |                        | t                | 1                | 1               | 1               | 148             | 2023-12-13       | 9                     | 4                 | 0                     | 2012-07-02             | 2023-11-01   | 4.44        | 4.44                 | 4.67                   | 4.56                      | 4.44                  | 4.67                                                       | 4.11                   | Available with a mobility lease only ("bail mobilité") | f             | 1                | 1                              | 0                                           | 0                                            | 0.06                                        |
| 11798 | https://www.airbnb.com/rooms/11798 | 20231212042736 | 2023-12-12   | city scrape     | Loft in Paris · ★4.84 · 1 bedroom · 1 bed · 1 bath        | Je suis juste à côté du quartier chinois qui est très exotique. En même temps, il y a toutes les commodités à côté de chez moi (Restaurants, boulangeries, épicerie bio, petit traiteur italien....)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | https://a0.muscache.com/pictures/22458692/09eb352b_original.jpg                                        | 44444                                                                                      | https://www.airbnb.com/users/show/44444 | Laurence                                | 2009-10-08 | Paris, France | Very dynamic personn, curious, who loves travelling and discovering the world and the differents cultures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | within a day                                                                                                                                 | 100%               | 78%                | f                                                                                                   | https://a0.muscache.com/im/users/44444/profile_pic/1336311264/original.jpg?aki_policy=profile_small    | https://a0.muscache.com/im/users/44444/profile_pic/1336311264/original.jpg?aki_policy=profile_x_medium     | Place d'Italie - Quartier Chinois                                                                             | 1                   | 2                   | ['email', 'phone']        | t                                                       | t                            | Paris, Île-de-France, France | Gobelins                     |                        | 48.8246                      | 2.3667             | Entire loft                 | Entire home/apt    | 2               |              | 1 bath    |                | 1        | []     | $143.00   | 4       | 30             | 1              | 4                      | 30                     | 30                     | 4.0                    | 30.0                   |                        | t                | 21               | 51              | 81              | 356             | 2023-12-12       | 121                   | 9                 | 0                     | 2012-09-21             | 2023-10-21   | 4.84        | 4.92                 | 4.8                    | 4.94                      | 4.95                  | 4.83                                                       | 4.77                   | 7511300241931                                          | f             | 1                | 1                              | 0                                           | 0                                            | 0.89                                        |
| 12268 | https://www.airbnb.com/rooms/12268 | 20231212042736 | 2023-12-13   | previous scrape | Rental unit in Paris · 1 bedroom · 1 bed · 1 bath         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | https://a0.muscache.com/pictures/4142889/d43dff74_original.jpg                                         | 47196                                                                                      | https://www.airbnb.com/users/show/47196 | Charles                                 | 2009-10-20 | Paris, France | Charles, living in Paris. Please have a look at my comments if you want to know more about me.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | N/A                                                                                                                                          | N/A                | N/A                | f                                                                                                   | https://a0.muscache.com/im/users/47196/profile_pic/1373006654/original.jpg?aki_policy=profile_small    | https://a0.muscache.com/im/users/47196/profile_pic/1373006654/original.jpg?aki_policy=profile_x_medium     | XI Arrondissement                                                                                             | 1                   | 3                   | ['email', 'phone']        | t                                                       | f                            |                              | Popincourt                   |                        | 48.85186                     | 2.3857             | Private room in rental unit | Private room       | 2               |              | 1 bath    |                | 1        | []     |           | 6       | 40             | 6              | 6                      | 40                     | 40                     | 6.0                    | 40.0                   |                        |                  | 0                | 0               | 0               | 0               | 2023-12-13       | 1                     | 0                 | 0                     | 2010-05-28             | 2010-05-28   | 0.0         |                      |                        | 5.0                       |                       |                                                            |                        |                                                        |               |                  | 0.2                            |

## Data Munging

In `munge.py`, I cleaned up my dataset. While it was overall already clean, there were several issues that needed to be fixed.

There were many line breaks within certain descriptive cells which disrupted the format of the CSV. They were usually denoted as `\r` or `\n` in the original data, which I replaced with spaces. For example:

```
Independent photographer.
Cyclist. Often on the road.

I only rent my apartment when I am travelling. But everything is organized so that you can have a good time and feel like at home.

As a guest, I try to be communicative and discreet at the same time.
```

I had to remove additional commas or quotation marks which disrupted the import of the CSV, such as `['email', 'phone']`.

I also had to clean for any missing values, denoting them as `NaN`. Additionally, I deleted columns which were entirely empty: `description`, `neighbourhood_group_cleansed`, `bathrooms`, and `amenities`.

Here is my data:

[Original Data](./data/listings.csv)

[Cleaned Data](./data/listings_clean.csv)

## Import into MongoDB

After adding my cleaned CSV to CyberDuck, here is the command I use to import the dataset:

```
mongoimport --headerline --type csv --db mn2405 --collection listings --host class-mongodb.cims.nyu.edu --file listings_clean.csv --username mn2405 --password (my_password)
```

## Data Analysis in MongoDB

1. Show exactly two documents from the `listings` collection in any order.

   This displays the first two rows of the collection.

   ```
   db.listings.find().limit(2)
   ```

   Here is the result:

   ```
   [
   {
    _id: ObjectId('660c1a18b6515eb20573971c'),
    id: 3109,
    listing_url: 'https://www.airbnb.com/rooms/3109',
    scrape_id: Long('20231212042736'),
    last_scraped: '2023-12-12',
    source: 'city scrape',
    name: 'Rental unit in Paris · ★5.0 · 1 bedroom · 1 bed · 1 bath',
    neighborhood_overview: 'Good restaurants<br />very close the Montparnasse Station<br />15 m from the center of Paris',
    picture_url: 'https://a0.muscache.com/pictures/baeae9e2-cd53-4ac3-b1bc-4055c0bb2e77.jpg',
    host_id: 3631,
    host_url: 'https://www.airbnb.com/users/show/3631',
    host_name: 'Anne',
    host_since: '2008-10-14',
    host_location: 'Paris_ France',
    host_about: NaN,
    host_response_time: 'within a few hours',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/3631/profile_pic/1375800198/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/3631/profile_pic/1375800198/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Alésia',
    host_listings_count: 1,
    host_total_listings_count: 2,
    host_verifications: '[-email-_ -phone-]',
    host_has_profile_pic: 't',
    host_identity_verified: 'f',
    neighbourhood: 'Paris_ Île-de-France_ France',
    neighbourhood_cleansed: 'Observatoire',
    latitude: 48.83191,
    longitude: 2.3187,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms_text: '1 bath',
    bedrooms: NaN,
    beds: 1,
    price: '$150.00',
    minimum_nights: 2,
    maximum_nights: 30,
    minimum_minimum_nights: 2,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 30,
    maximum_maximum_nights: 30,
    minimum_nights_avg_ntm: 2,
    maximum_nights_avg_ntm: 30,
    calendar_updated: NaN,
    has_availability: 't',
    availability_30: 21,
    availability_60: 30,
    availability_90: 60,
    availability_365: 327,
    calendar_last_scraped: '2023-12-12',
    number_of_reviews: 4,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '2017-10-28',
    last_review: '2019-10-24',
    review_scores_rating: 5,
    review_scores_accuracy: 5,
    review_scores_cleanliness: 5,
    review_scores_checkin: 5,
    review_scores_communication: 5,
    review_scores_location: 5,
    review_scores_value: 5,
    license: Long('7511409139079'),
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.05
   },
   {
    _id: ObjectId('660c1a18b6515eb20573971d'),
    id: 5396,
    listing_url: 'https://www.airbnb.com/rooms/5396',
    scrape_id: Long('20231212042736'),
    last_scraped: '2023-12-14',
    source: 'city scrape',
    name: 'Rental unit in Paris · ★4.59 · Studio · 1 bed · 1 bath',
    neighborhood_overview: 'You are within walking distance to the Louvre_ Notre Dame_ Le Marais_ Les Halles_ Chatelet_ St. Germain_ Les Tuileries_ le Jardin des Plantes_ St. Michel_ Sorbonne_ Institut du Monde Arab_ the Bastille and the Latin Quarter.',
    picture_url: 'https://a0.muscache.com/pictures/52413/f9bf76f5_original.jpg',
    host_id: 7903,
    host_url: 'https://www.airbnb.com/users/show/7903',
    host_name: 'Borzou',
    host_since: '2009-02-14',
    host_location: 'Paris_ France',
    host_about: 'We have spent a lot of time traveling for work and leisure. We understand what people need when they-re away from home. Guillaume and his partners manage arrivals and checkins_ adding a friendly touch to every visitor. We all genuinely love Paris and try to make it easy for people to come and visit the city.',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/7903/profile_pic/1280002723/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/7903/profile_pic/1280002723/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Saint-Paul - Ile Saint-Louis',
    host_listings_count: 2,
    host_total_listings_count: 3,
    host_verifications: '[-email-_ -phone-]',
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Paris_ Ile-de-France_ France',
    neighbourhood_cleansed: 'Hôtel-de-Ville',
    latitude: 48.85247,
    longitude: 2.35835,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms_text: '1 bath',
    bedrooms: NaN,
    beds: 1,
    price: '$146.00',
    minimum_nights: 1,
    maximum_nights: 1125,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: NaN,
    has_availability: 't',
    availability_30: 0,
    availability_60: 0,
    availability_90: 0,
    availability_365: 0,
    calendar_last_scraped: '2023-12-14',
    number_of_reviews: 374,
    number_of_reviews_ltm: 48,
    number_of_reviews_l30d: 5,
    first_review: '2009-06-30',
    last_review: '2023-12-11',
    review_scores_rating: 4.59,
    review_scores_accuracy: 4.61,
    review_scores_cleanliness: 4.56,
    review_scores_checkin: 4.8,
    review_scores_communication: 4.84,
    review_scores_location: 4.95,
    review_scores_value: 4.56,
    license: Long('7510402838018'),
    instant_bookable: 'f',
    calculated_host_listings_count: 2,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 2.12
   }
   ]
   ```

1. Show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the `pretty()` function.

   This displays the first ten rows of the collection.

   ```
   db.listings.find().limit(10).pretty()
   ```

   Here is the result:

   ```
   {
    _id: ObjectId('660c1a18b6515eb20573971c'),
    id: 3109,
    listing_url: 'https://www.airbnb.com/rooms/3109',
    scrape_id: Long('20231212042736'),
    last_scraped: '2023-12-12',
    source: 'city scrape',
    name: 'Rental unit in Paris · ★5.0 · 1 bedroom · 1 bed · 1 bath',
    neighborhood_overview: 'Good restaurants<br />very close the Montparnasse Station<br />15 m from the center of Paris',
    picture_url: 'https://a0.muscache.com/pictures/baeae9e2-cd53-4ac3-b1bc-4055c0bb2e77.jpg',
    host_id: 3631,
    host_url: 'https://www.airbnb.com/users/show/3631',
    host_name: 'Anne',
    host_since: '2008-10-14',
    host_location: 'Paris_ France',
    host_about: NaN,
    host_response_time: 'within a few hours',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/3631/profile_pic/1375800198/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/3631/profile_pic/1375800198/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Alésia',
    host_listings_count: 1,
    host_total_listings_count: 2,
    host_verifications: '[-email-_ -phone-]',
    host_has_profile_pic: 't',
    host_identity_verified: 'f',
    neighbourhood: 'Paris_ Île-de-France_ France',
    neighbourhood_cleansed: 'Observatoire',
    latitude: 48.83191,
    longitude: 2.3187,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms_text: '1 bath',
    bedrooms: NaN,
    beds: 1,
    price: '$150.00',
    minimum_nights: 2,
    maximum_nights: 30,
    minimum_minimum_nights: 2,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 30,
    maximum_maximum_nights: 30,
    minimum_nights_avg_ntm: 2,
    maximum_nights_avg_ntm: 30,
    calendar_updated: NaN,
    has_availability: 't',
    availability_30: 21,
    availability_60: 30,
    availability_90: 60,
    availability_365: 327,
    calendar_last_scraped: '2023-12-12',
    number_of_reviews: 4,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '2017-10-28',
    last_review: '2019-10-24',
    review_scores_rating: 5,
    review_scores_accuracy: 5,
    review_scores_cleanliness: 5,
    review_scores_checkin: 5,
    review_scores_communication: 5,
    review_scores_location: 5,
    review_scores_value: 5,
    license: Long('7511409139079'),
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.05
   },
   {
    _id: ObjectId('660c1a18b6515eb20573971d'),
    id: 5396,
    listing_url: 'https://www.airbnb.com/rooms/5396',
    scrape_id: Long('20231212042736'),
    last_scraped: '2023-12-14',
    source: 'city scrape',
    name: 'Rental unit in Paris · ★4.59 · Studio · 1 bed · 1 bath',
    neighborhood_overview: 'You are within walking distance to the Louvre_ Notre Dame_ Le Marais_ Les Halles_ Chatelet_ St. Germain_ Les Tuileries_ le Jardin des Plantes_ St. Michel_ Sorbonne_ Institut du Monde Arab_ the Bastille and the Latin Quarter.',
    picture_url: 'https://a0.muscache.com/pictures/52413/f9bf76f5_original.jpg',
    host_id: 7903,
    host_url: 'https://www.airbnb.com/users/show/7903',
    host_name: 'Borzou',
    host_since: '2009-02-14',
    host_location: 'Paris_ France',
    host_about: 'We have spent a lot of time traveling for work and leisure. We understand what people need when they-re away from home. Guillaume and his partners manage arrivals and checkins_ adding a friendly touch to every visitor. We all genuinely love Paris and try to make it easy for people to come and visit the city.',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/7903/profile_pic/1280002723/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/7903/profile_pic/1280002723/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Saint-Paul - Ile Saint-Louis',
    host_listings_count: 2,
    host_total_listings_count: 3,
    host_verifications: '[-email-_ -phone-]',
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Paris_ Ile-de-France_ France',
    neighbourhood_cleansed: 'Hôtel-de-Ville',
    latitude: 48.85247,
    longitude: 2.35835,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms_text: '1 bath',
    bedrooms: NaN,
    beds: 1,
    price: '$146.00',
    minimum_nights: 1,
    maximum_nights: 1125,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: NaN,
    has_availability: 't',
    availability_30: 0,
    availability_60: 0,
    availability_90: 0,
    availability_365: 0,
    calendar_last_scraped: '2023-12-14',
    number_of_reviews: 374,
    number_of_reviews_ltm: 48,
    number_of_reviews_l30d: 5,
    first_review: '2009-06-30',
    last_review: '2023-12-11',
    review_scores_rating: 4.59,
    review_scores_accuracy: 4.61,
    review_scores_cleanliness: 4.56,
    review_scores_checkin: 4.8,
    review_scores_communication: 4.84,
    review_scores_location: 4.95,
    review_scores_value: 4.56,
    license: Long('7510402838018'),
    instant_bookable: 'f',
    calculated_host_listings_count: 2,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 2.12
   }
   ```

1. Choose two hosts (by reffering to their `host_id` values) who are superhosts (available in the `host_is_superhost` field), and show all of the listings offered by both of the two hosts. Only show the `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost` for each result

   I used an `$or` statement to show data which matches either of the two hosts with id's `2626` and `33534`. Then the projection limits the fields to only show the `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost`.

   ```
   db.listings.find({$or: [{host_id: 2626}, {host_id: 33534}]}, {_id: 0, name: 1, price:1, neighbourhood:1, host_name:1, host_is_superhost:1})
   ```

   Here is the data:

   ```
   [
   {
    name: 'Rental unit in Paris · ★4.73 · 2 bedrooms · 2 beds · 1 bath',
    host_name: 'Franck',
    host_is_superhost: 't',
    neighbourhood: NaN,
    price: '$140.00'
   },
   {
    name: 'Rental unit in Paris · ★4.92 · 1 bedroom · 1 bed · 1 bath',
    host_name: 'Elisabeth',
    host_is_superhost: 't',
    neighbourhood: 'Paris_ Ile-de-France_ France',
    price: '$130.00'
   },
   {
    name: 'Rental unit in Paris · ★4.61 · 1 bedroom · 1 bed · 1 bath',
    host_name: 'Franck',
    host_is_superhost: 't',
    neighbourhood: NaN,
    price: '$42.00'
   }
   ]
   ```

1. Find all the unique `host_name` values (see [the docs](https://docs.mongodb.com/manual/reference/method/db.collection.distinct/))

   This uses the `distinct` function to find all unique `host_name` values.

   ```
   db.listings.distinct("host_name")
   ```

   Here is the data:

   ````
   [
   NaN,                    'Aaron',               'Abdel Hamid',
   'Abel',                 'Abigail',             'Abye',
   'Achren',               'Addala',              'Adel',
   'Adeline',              'Adil',                'Adila',
   'Adrian',               'Adriano',             'Adrien',
   'Adèle',                'Adélaïde',            'Adélaïde Et Philippe',
   'Afoufou',              'Agathe',              'Agence Rental',
   'Agnes',                'Agnia',               'Agnès',
   'Ahouva',               'Akim',                'Alain',
   'Alban',                'Albane',              'Alberic',
   'Albert',               'Ale',                 'Alejandro',
   'Alessandra',           'Alessandra Et Louis', 'Alex',
   'Alexander',            'Alexandra',           'Alexandre',
   'Alexandre & Séverine', 'Alexandre Et Chani',  'Alexandrine',
   'Alexia',               'Alexia Et Emmanuel',  'Alexis',
   'Ali',                  'Alia',                'Alice',
   'Alice Et Juliette',    'Alienor',             'Aliette',
   'Aline',                'Alix',                'Aliyah & Philippe',
   'Alizée',               'Almudena',            'Alvaro',
   'Amanda',               'Amandine',            'Amar',
   'Amaryllis',            'Amaury',              'Ame',
   'Amel',                 'Amelie',              'Ameyes',
   'Amin',                 'Amit',                'Amy',
   'Amélia',               'Amélie',              'Amélie Et Clément',
   'Ana',                  'Ana Et Emmanuel',     'Ana Maria Concepcion',
   'Anas',                 'Anaïs',               'Anaïs Et Julien',
   'Andrea',               'Andreas',             'Andree',
   'Andrew',               'André',               'André-Arnaud',
   'André-Luiz',           'Andrée',              'Andy',
   'Ange',                 'Angel',               'Angeliq',
   'Angelique',            'Angi And Nadia',      'Anh Thy',
   'Anita',                'Anjuli',              'Ann',
   'Anna',                 'Anna And Dylan',      'Anna Et Nicolas',
   'Annabelle',
   ... 1564 more items
   ]```

   ````

1. Find all of the places that have more than 2 `beds` in a neighborhood of your choice (referred to as either the `neighborhood` or `neighbourhood_group_cleansed` fields in the data file), ordered by `review_scores_rating` descending.

   - Only show the `name`, `beds`, `review_scores_rating`, and `price`.
   - If your data set only has blanks for all the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to filter by - include an explanation and justification for this in your report.
   - If you run out of memory for this query, try filtering `review_scores_rating` that aren't empty (`$ne`); and lastly, if there's still an issue, you can set the `beds` to match exactly 2.

   This formula uses an `$or` statement to filter for the neighborhoods Popincourt and Gobelins, and another criteria for having more than two beds. The projection also filters the results to show just the `name`, `beds`, `review_scores_rating`, and `price`.

   ```
   db.listings.find({$or: [{neighbourhood_cleansed: "Popincourt"}, {neighbourhood_cleansed: "Gobelins"}], beds:{$gt: 2}}, {_id:0, name:1, beds:1, review_scores_rating:1, price:1})
   ```

   Here is the data:

   ```
   {
    name: 'Rental unit in Paris · ★4.67 · 1 bedroom · 3 beds · 1.5 baths',
    beds: 3,
    price: '$95.00',
    review_scores_rating: 4.67
   },
   {
    name: 'Loft in Paris · ★4.84 · 3 bedrooms · 4 beds · 2.5 baths',
    beds: 4,
    price: '$344.00',
    review_scores_rating: 4.84
   },
   {
    name: 'Condo in Paris · ★4.88 · 3 bedrooms · 3 beds · 1 bath',
    beds: 3,
    price: '$300.00',
    review_scores_rating: 4.88
   },
   {
    name: 'Rental unit in Paris · ★4.90 · 3 bedrooms · 3 beds · 1 bath',
    beds: 3,
    price: '$98.00',
    review_scores_rating: 4.9
   }
   ```

1. Show the number of listings per host.

   I use here the aggregation pipleine to count the listings, grouping by the host_id.

   ```
   db.listings.aggregate({$group: {_id: "$host_id", countListings: {$sum: 1}}})
   ```

   Here are some of the results. Most hosts have just one listing, but some have more.

   ```
   { _id: 9014696, countListings: 1 },
   { _id: 47196, countListings: 1 },
   { _id: 21170107, countListings: 1 },
   { _id: 7059959, countListings: 1 },
   { _id: 1290723, countListings: 2 },
   { _id: 3457800, countListings: 2 },
   { _id: 18070352, countListings: 1 }
   ```

1. Find the average `review_scores_rating` per neighborhood, and only show those that are `4` or above, sorted in descending order of rating (see [the docs](https://docs.mongodb.com/manual/reference/operator/aggregation/sort/)).

   - If your data set only has blanks in the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to break down the listings by - include an explanation and justification for this in your report.

   I use an aggregation pipeline to find the average ratings and to group it by the neighborhood.

   ```
   db.listings.aggregate({$group: {_id: "$neighbourhood", avgScores: {$avg: "$review_scores_rating"}}})
   ```

   Here is the data. Unless there is no score in the rating's cell (marked as `NaN`), they are marked with each neighborhood:

   ```
   {_id: 'Boulogne-Billancourt_ Île-de-France* France',
   avgScores: NaN },
   { _id: 'Paris 4e arrondissement* Île-de-France* France',
   avgScores: 4.775},
   {_id: 'Paris-10E-Arrondissement* Île-de-France* France',
   avgScores: 4.55},
   { _id: 'Levallois-Perret* Île-de-France* France', avgScores: 4.85 },
   { _id: 'Paris* France', avgScores: 4.7196 }
   ```
