<<<<<<< HEAD
# Twitter Monitoring
Twitter Monitoring shows the impact produced as a consequence of the tweets which contain specific hashtags. Relating a user with the Tweets he has published and the repercussion that those tweets have produced. Also we can see it at the other way around, given a hashtag, or a statistic (i.e. number of retweets) connect it to the tweets and the users who have written them.

## Getting Started
Our project is in a GitHub repository, you can acces with this link: https://github.com/marcusresa4/Twitter_WP

You must be logged on docker, otherwise you would not be able to run it.
```bash
docker-compose up --build
```
With this command you will run Docker and Django will be able in the IP of the machine, that you can get from the very beginning on the Docker Toolbox, or just running the command:
```bash
docker-machine ip default
```

## Running the tests
By using Travis CI we are able to build and test the application hosted on GitHub. Travis runs the tests every time we commit to GitHub, which allows us to easily discover the code breaks.
## How does the App Interface work
As well with all the code, we'll upload the sqlite DataBase in order that you don't need to set all the instances to view the final result.\
When you'll open the Web App in the browser for the first time, you'll see the login page. You just have to press the blue Login Button and it will redirect you to the Google Accounts site, where you'll have to select your Google Account and it will automaticaly redirect to our Twitter Monitoring Web App. If it's not the first time you open the Web App in the browser or if you're already registered as a super-user you'll see the Logout page with a Logout button (useless) and a button that links you to the Web App.\
Once you are in the main page of the Twitter Monitoring Web you'll see all the Tweets that all the users have written, once there, you'll be able to click any hashtag or any user and you'go to the matching page.\
To go to the main page just click on the Website Name on the navbar. 
## Authors:
    Xavier Trullols
    Marc Resa
    Oriol Aguilar
    Guillem Guardiola

## Subject: 
Web-Project - 2019/20
=======
# Twitter Monitoring
Twitter Monitoring shows the impact produced as a consequence of the tweets which contain specific hashtags. Relating a user with the Tweets he has published and the repercussion that those tweets have produced. Also we can see it at the other way around, given a hashtag, or a statistic (i.e. number of retweets) connect it to the tweets and the users who have written them.

## Getting Started
Our project is in a GitHub repository, [Twitter-Monitoring] (https://github.com/marcusresa4/Twitter_WP)

### Prerequisites
    Docker or Docker Toolbox

You must be logged on docker, otherwise you would not be able to run it.
```bash
$ docker login
```
#### With Docker

```bash
$ docker-compose up --build
```
With this command you will run Docker and Django will be able in the IP localhost (127.0.0.1) 

#### With Docker Toolbox

```bash
$ docker-machine ip default
$ docker-compose up --build
```
Being different from Docker, Django will be able in the IP of the machine, that you can get from the very beginning on the Docker Toolbox, or just running previous command. 

In both of them, afer the adress IP, you have to put ":8000", that is the port where the server will be deployed.

## Running the tests
By using Travis CI we are able to build and test the application hosted on GitHub. Travis runs the tests every time we commit to GitHub, which allows us to easily discover the code breaks.

## How does the App Interface work
As well with all the code, we'll upload the sqlite DataBase in order that you don't need to set all the instances to view the final result.\
When you'll open the Web App in the browser for the first time, you'll see the login page. You just have to press the blue Login Button and it will redirect you to the Google Accounts site, where you'll have to select your Google Account and it will automaticaly redirect to our Twitter Monitoring Web App. If it's not the first time you open the Web App in the browser or if you're already registered as a super-user you'll see the Logout page with a Logout button (useless) and a button that links you to the Web App.\
Once you are in the main page of the Twitter Monitoring Web you'll see all the Tweets that all the users have written, once there, you'll be able to click any hashtag or any user and you'go to the matching page.\
To go to the main page just click on the Website Name on the navbar. 

## Authors:
    Xavier Trullols
    Marc Resa
    Oriol Aguilar
    Guillem Guardiola

## Subject: 
Web-Project - 2019/20
>>>>>>> 8831d59c6edf7bd03731dc8eca7dfcbabdafb560
