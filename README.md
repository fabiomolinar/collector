# Collector

This is just a bunch of notes I take in order not to forget things in the future. :)

## Managing the containers

- Building

```bash
# with docker
sudo docker build -t website .
# with compose
sudo docker-compose build
```

or,  **if behind a proxy**:

```bash
# with docker
sudo docker build -t website --build-arg PROXY="http://user:password@proxyserver:port" .
# with compose
sudo docker-compose build --build-arg PROXY="http://user:password@proxyserver:port" .
```

- Running

`sudo docker-compose up`

- Debugging

`sudo docker exec -it <container> /bin/bash`

## Scrapy

### Installing

Remember that to install Scrapy, it's necessary to have a few other packages installed on Ubuntu.

`sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev`

And if running Python3:

`sudo apt-get install python3 python3-dev`

### Running from terminal

To get data from a certain search text in Ali, use:

`scrapy crawl search -a searchtext=<search text>`

Example:

`scrapy crawl search -a searchtext=mp3`

### Development guidelines

It is really useful to use Scrapy's shell in order to test XPaths to be extracted from a website.

To enter a shell:

`scrapy shell`

Then, to fetch a webpage:

`fetch("<url>")`

From there, we can use:

1. The `view` function to see the fetched page on a web browser:
    - `view(response)`
2. The response object to run XPath tests
    - Examples:
        - `response.xpath('//title/text()').extract_first()`
        - `response.xpath('//title/text()').extract()`
        - `pprint(response.headers)`

### Scrapy List of useful commands

1. Create a project
    - `scrapy startproject <project name>`
2. Running spiders on terminal
    - `scrapy crawl <spider name>`
3. Scrapy shell
    - `scrapy shell`
4. Storing a spider run data into a file
    - `scrapy crawl <spider name> -o <file name>.json`
5. Using **arguments** when invoking spiders from terminal
    - `scrapy crawl <spider name> -a <tag>=<value>`
    - Example:
        - `scrapy crawl search -a searchtext=mp3`

### Pipeline to DB (dev vs prod environment)

I will manage the DBs on Django. 

To run the crawlers from my dev environment, I need to overwrite the DB_HOST paramenter to point it to the localhost where I am running postgres. Like this:

`scrapy crawl -s DB_HOST=localhost search -a searchtext=watches`

Whereas while running on the containerized environment, since the DB is running on a different container, we need to plug our Scrapy container to that container network. We can use the following command:

`sudo docker run -it --network <network name> collector bash`. E.g.:
`sudo docker run -it --network website_website_db_network collector bash`

## Scrapyd

Scrapyd is a server which run spiders by responding to HTTP requests sent to it. The easiest way to add projects and spiders to the server is to use `scrapyd-client`.

### Scrapyd list of useful commands

1. To start the service, run:
    - `scrapyd`
2. And to schedule a spider run, use the following end point:
    - `curl <server address>/schedule.json -d project=<project name> -d spider=<spider name>`
    - Example:
        - `curl http://localhost:6800/schedule.json -d project=myproject -d spider=spider2`
3. To add **arguments**, just add them using additional `-d`:
    - `curl <server address>/schedule.json -d project=<project name> -d spider=<spider name> -d <argument name>=<argument value>`

## Scrapyd-client

### How it works

1. Eggifying your project. You'll need to install setuptools for this. See Egg Caveats below.
2. Uploading the egg to the Scrapyd server through the addversion.json endpoint.
3. Steps:
    1. First, `cd` to the projec root and deploy the project with the following command:
        - `scrapyd-deploy <target> -p <project>`
        - P.S.: To avoid having to type the `target` everytime, defaults can be saved at the `scrapy.cfg` file. Example:
            ```config
            [deploy]
            url = http://scrapyd.example.com/api/scrapyd
            username = scrapy
            password = secret
            project = yourproject
            ```

## Cron jobs

One idea is to set a cron job to run a custom manage.py command periodically as mentioned [here](https://stackoverflow.com/questions/573618/django-set-up-a-scheduled-job).