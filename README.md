# AirBnB MongoDB Analysis

A little assignment to practice importing and analyzing data within a MongoDB database.

Replace the contents of this file with a report, as described in the [instructions](./instructions.md).

### by Maya Nesen

## Dataset

I am working with AirBnB data from Paris, Ile de France, France, originally in CSV format. This data will be cleaned, as noted in the following section.

## Data Munging

In `munge.py`, I cleaned up my dataset. While it was overall already clean, there were many line breaks within certain descriptive cells which disrupted the format of the CSV. They were usually denoted as `\r` or `\n` in the original data, which I replaced with spaces. I also had to clean for any missing values, denoting them as `NaN`. Additionally, I deleted columns which were entirely empty: `description`, `neighbourhood_group_cleansed`, `bathrooms`, and `amenities`.

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

1. choose two hosts (by reffering to their `host_id` values) who are superhosts (available in the `host_is_superhost` field), and show all of the listings offered by both of the two hosts

   - only show the `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost` for each result

   ```
   db.listings.find({$or: [{host_id: 2626}, {host_id: 33534}]}, {_id: 0, name: 1, price:1, neighbourhood:1, host_name:1, host_is_superhost:1})
   ```

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

1. find all the unique `host_name` values (see [the docs](https://docs.mongodb.com/manual/reference/method/db.collection.distinct/))

   ```
   db.listings.distinct("host_name")
   ```

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

1. find all of the places that have more than 2 `beds` in a neighborhood of your choice (referred to as either the `neighborhood` or `neighbourhood_group_cleansed` fields in the data file), ordered by `review_scores_rating` descending

   - only show the `name`, `beds`, `review_scores_rating`, and `price`
   - if your data set only has blanks for all the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to filter by - include an explanation and justification for this in your report.
   - if you run out of memory for this query, try filtering `review_scores_rating` that aren't empty (`$ne`); and lastly, if there's still an issue, you can set the `beds` to match exactly 2.

   ```
   db.listings.find({$or: [{neighbourhood_cleansed: "Popincourt"}, {neighbourhood_cleansed: "Gobelins"}], beds:{$gt: 2}}, {name:1, beds:1, review_scores_rating:1, price:1})
   ```

   ```
   {
    _id: ObjectId('660c1a18b6515eb205739727'),
    name: 'Rental unit in Paris · ★4.67 · 1 bedroom · 3 beds · 1.5 baths',
    beds: 3,
    price: '$95.00',
    review_scores_rating: 4.67
   },
   {
    _id: ObjectId('660c1a18b6515eb205739735'),
    name: 'Loft in Paris · ★4.84 · 3 bedrooms · 4 beds · 2.5 baths',
    beds: 4,
    price: '$344.00',
    review_scores_rating: 4.84
   },
   {
    _id: ObjectId('660c1a18b6515eb2057397a3'),
    name: 'Condo in Paris · ★4.88 · 3 bedrooms · 3 beds · 1 bath',
    beds: 3,
    price: '$300.00',
    review_scores_rating: 4.88
   },
   {
    _id: ObjectId('660c1a18b6515eb2057397b2'),
    name: 'Rental unit in Paris · ★4.90 · 3 bedrooms · 3 beds · 1 bath',
    beds: 3,
    price: '$98.00',
    review_scores_rating: 4.9
   }
   ```

1. show the number of listings per host

   ```
   db.listings.aggregate({$group: {_id: "$host_id", countListings: {$sum: 1}}})
   ```

   ```
   { _id: 9014696, countListings: 1 },
   { _id: 47196, countListings: 1 },
   { _id: 21170107, countListings: 1 },
   { _id: 7059959, countListings: 1 },
   { _id: 1290723, countListings: 2 },
   { _id: 3457800, countListings: 2 },
   { _id: 18070352, countListings: 1 }
   ```

1. find the average `review_scores_rating` per neighborhood, and only show those that are `4` or above, sorted in descending order of rating (see [the docs](https://docs.mongodb.com/manual/reference/operator/aggregation/sort/))

   - if your data set only has blanks in the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to break down the listings by - include an explanation and justification for this in your report.

   ```
   db.listings.aggregate({$group: {_id: "$neighbourhood", avgScores: {$avg: "$review_scores_rating"}}})
   ```

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

# WHAT I NEED TO DO

The report must include:

Data set details:

The origin of your data set - what is it and where does it come from. Include a link to the URL of the source.
What format the original data file was in (CSV, JSON, or other).
Display some of the raw data from the original data file (the first 20 rows is enough - feel free to clip the text in fields to prevent line-wrapping). Use Markdown's ability to display tables - see the examples in the Markdown guide linked above.
Describe any problems that were present in the data and the scrubbing tasks that were necessary to prepare your data set for import - include any scrubbing done in Python, a text editor, or any other tool. Be specific with examples of the problems in the original data and the way in which those were solved. Feel free to show small snippets of relevant code - see the examples of code "syntax highlighting" in the Markdown guide linked above.

Analysis:

Describe each of the analyses you have performed. For each query, include:
a description of the query
the code used to perform it
up to the first three results in a preformatted text block (feel free to clip the text in fields to prevent line-wrapping)
describe any insights the analysis shows that may not be obvious to someone just viewing the raw data.
