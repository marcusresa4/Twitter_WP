# Twitter Monitoring
Twitter Monitoring shows the impact produced as a consequence of the tweets which contain specific hashtags. Relating a user with the Tweets he has published and the repercussion that those tweets have produced. Also we can see it at the other way around, given a hashtag connect it to the tweets and the users who have written them.

## Getting Started
Our project is in a GitHub repository, [Twitter-Monitoring](https://github.com/marcusresa4/Twitter_WP).

There is a branch called [second-assignment](https://github.com/marcusresa4/Twitter_WP/tree/second-assignment) where there is the SQLiteDB and the .env file, the first file is necessary in order to see all the entitites created by us and be able to navigate through the Web App. Following the [12factor](https://12factor.net/) guideline The .env file contains all the KEYS so it's indispensable to be in the repo when you run it.
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
Being different from Docker, Django will be able in the IP of the machine, that you can get from the very beginning on the Docker Toolbox, or just running previous command. Also, after the IP, you must add .xip.io , so the web will be in:
```bash
 192.168.99.100.xip.io:8000
```
In both of them, afer the adress IP, you have to put ":8000", that is the port where the server will be deployed.
## Heroku
Moreover, our web was been deployed on Heroku platform using a docker image, and runned in the link [TwitterHeroku](https://twitterwpappheroku.herokuapp.com/) . A Postgres DB administrated by pgAdmin4 that contains the data of the SQLiteDB in the repo is used.

## Running the tests
By using Travis CI we are able to build and test the application hosted on GitHub. Travis runs the tests every time we commit to GitHub, which allows us to easily discover the code breaks.

For this second deliverable we used the behave. The tests do what humans should do like click on the drop-down for example. For this reason, we have had to use the sleep() function, in order to do it right. So, approximately it takes about 1 minut and 30 seconds to execute and pas all the tests.

We have to say that we don't have a feature for the creation of each instance because when a tweet is created a hashtag, an impact, a user and a rating are also created as well.

## How does the App Interface work
As well with all the code, we'll upload the sqlite DataBase in order that you don't need to set all the instances to view the final result.

When you'll open the Web App in the browser for the first time, you'll see the login page. You just have to press the blue Login Button and it will redirect you to the Google Accounts site, where you'll have to select your Google Account and it will automaticaly redirect to our Twitter Monitoring Web App. If it's not the first time you open the Web App in the browser or if you're already registered as a super-user you'll see the Logout page with a Logout button (useless) and a button that links you to the Web App.

Once you are in the main page of the Twitter Monitoring Web you'll see all the Tweets that all the users have written, once there, you'll be able to valorate the tweets, writte new ones, edit it...

To go to the main page just click on the Website Name on the navbar. 

## Design considerations
Our application is based on monitoring Twitter. Most of the people know how twitter works,
you can see the content from other users, write comments about this, publish whatever you
want (a feeling, criticise something you disappoint, a photo, video ...) and so other incredible
things. However, Monitoring Twitter has something especial, is a personalized twitter. What
does it mean? You are able to write tweets and edit it, obtain tweets from other users and value
its content, but what is more fascinating is when you publish a tweet with some hashtag: an
instance of it is created and you can analyse the impact that it is having, knowing the statistics
about how many retweets it has and how many FAV, that would be the like of most of the
applications.
What’s more, your tweets can be edited or deleted.
Regarding other users, you can see the last tweet that has been post by searching it by his/her
username without the @. We have only taken the last tweet due to the huge amount of
information that a user could have. There are lots of users with more than 10k tweets...
Therefore, it would be a slowly process obtaining all the tweets in some cases. So we have
considered that getting only the last tweet would be enough to see how it works.

## Changes in the model
Takint into account the models, comparing them with the ones in the first deliverable, we have
changed the authentication. The design consist in that if a user is not registered or is not
authenticated, they would be able to see de content of the page,seeing the tweets but the user
can’t rate it or publish a tweet themselves.

## Authors:
    Xavier Trullols
    Marc Resa
    Oriol Aguilar
    Guillem Guardiola

## Subject: 
Web-Project - 2019/20
