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

## Authors:
    Xavier Trullols
    Marc Resa
    Oriol Aguilar
    Guillem Guardiola

## Subject: 
Web-Project - 2019/20