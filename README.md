# AirBnB Clone RESTFul API 

This repository contains the code for an API designed to emulate some functionalities of the AirBnB platform. It includes endpoints for managing states, cities, users, amenities, places, and more.

## Table of Contents
1. [Improving Storage](#improving-storage)
2. [Status of Your API](#status-of-your-api)
3. [Some Stats?](#some-stats)
4. [Not Found](#not-found)
5. [State](#state)
6. [City](#city)
7. [Amenity](#amenity)
8. [User](#user)
9. [Place](#place)

## Improving Storage

The task involves updating the storage mechanisms (`DBStorage` and `FileStorage`) to include new methods for retrieving objects and counting the number of objects in storage. This also requires adding tests for these methods.

## Status of Your API

This part requires setting up the first endpoint of the API to return the status of the API, which should respond with a JSON object containing the status as "OK".

## Some Stats?

An endpoint is created to retrieve the number of objects for each type available in the API. This endpoint returns a JSON object with counts for amenities, cities, places, reviews, states, and users.

## Not Found

The API is configured to handle 404 errors by returning a JSON-formatted response with the status code and message indicating "Not found".

## State

A view for State objects is implemented, handling various RESTful API actions including retrieving all states, retrieving a specific state, deleting a state, and creating/updating states.

## City

Similar to State, this part implements a view for City objects, including actions to retrieve all cities of a state, retrieve a specific city, delete a city, and create/update cities.

## Amenity

A view for Amenity objects is added, providing endpoints to retrieve all amenities, retrieve a specific amenity, delete an amenity, and create/update amenities.

## User

A view for User objects is implemented, offering endpoints to retrieve all users, retrieve a specific user, delete a user, and create/update users.

## Place

Finally, a view for Place objects is created, handling actions to retrieve all places of a city, retrieve a specific place, delete a place, and create/update places.

Each section includes examples of how to interact with the API using `curl` commands.


3. Run the API server:
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-branch-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-branch-name`)
6. Create a new Pull Request


## Authors

- [Brayan salazar](https://github.com/BrayanSalazar14)

- [Juan pablo restrepo](https://github.com/JuanRestrepoV)

- [Luis herrera](https://github.com/Luamix550)


