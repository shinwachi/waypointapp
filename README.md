# waypointapp #

### What is this repository for? ###

Displays the content of "waypoint" database tables in SQLite format.


### How do I get set up? ###

1. Identify the assay folder
2. Set up docker volume to have access to the assay folder(s)
3. Point the configuration file to the assay folder(s)
4. docker-compose up

* Configuration

If you have an assay folder mounted which you'd like to use (instead of the included /data), then modify docker-compose.yml:

e.g.: ```/mnt/srv/public:/public```


* Dependencies

The easiest way is to get [Docker](https://www.docker.com/products/overview).

If you would like to run this without container, then please take a look at the Dockerfile for what is done to set it up, especially the `pip install` section. Virtual environment is recommended.

* Database configuration
* Assay fodler files must be accesible to the docker container through docker volume

* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests

This is a dead simple server, but if you want tests, it shuld be to ensure that all assay folders in the config are accessible

* Other guidelines


### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
