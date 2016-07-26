# waypointapp #

### What is this repository for? ###

Displays the content of "waypoint" database tables in SQLite format.


### How do I get set up? ###

1. Identify the assay folder
2. Set up docker volume to have access to the assay folder(s)
3. Point the configuration file to the assay folder(s)
4. docker-compose up

To build the image: docker-compose build

* Configuration

If you have an assay folder mounted which you'd like to use (instead of the included /data), then modify docker-compose.yml:

e.g.: ```/mnt/srv/public:/public```


to kill:
 sudo docker-compose kill -s SIGINT

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


### License ###

(MIT License)

Copyright (c) 2016 Shinichiro Wachi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
