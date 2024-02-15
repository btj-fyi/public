Imgur is a free image hosting service. Imgur will continue to host images that are being viewed, however if an image has not been viewed for some time it will be automatically removed. In order to prevent images from being removed we can progromattically view them every so often. 

In order to do this we will need the following:
1. some storage for our Imgur image's URLs
2. an app to load Imgur pages in such a way that the requests (a) will not be blocked or throttled and (b) count as legitmate views
3. an interface to add and remove URLs from our service (eg CLI, web app, API, etc)

Our service will be inherently ~~read-heavy because each URL will only be added once but read periodically.~~* However, Imgur URLs are short, about 35 chararacters, so the data being read will be very small - something like 35 bytes per URL.**

*Correction: our service will be more or less balanced because for each row we select we will also update. 

**Note: This estimate is accurate but does not include the unique_id and last/next_load_date.

We would like the service to be reliable and durable but it is not a requirement - ACID-ity is not needed.

There is a likelihood that this service could be used to maliciously load Imgur pages or even non-Imgur pages. The interval at which pages are loaded should not be configurable and if a request is rejected it should not be repeated. Non-Imgur URLs should not be allowed. 

# Storage:
We can be reasonably assured the Imgur URLs are already unique because if they were not then they would be useless to Imgur. 

~~The vast majority of our queries should not be based on the URL itself but rather the status of a particular URL (eg WAITING, READY, DONE, SKIP, STOP, and ERROR)~~

~~An autoincremnting int can be used as the primary key. A clustered index may be used to increase performance.~~

We have a few options to consider.
1. We could implement a queue over our database
2. We could use a dedicated queue like RabbitMQ or Redis Queue
3. We could use both Redis Queue and our database together.
By choosing Redis Queue we will be able to simulatenously implement a queue and benefit from caching. While also using our database(s) as a source of truth.

If we add a column for the date the URL was last loaded and index on it, we can easily select the URLs where last_load_date is more than X days from today.

We can then push these URLs onto our queue. For each URL that is removed from the queue and loaded, its last_load_date is updated in the database. We then attest completion to the queue.  

The last_load_date also provides a natural opportunity for partioning of the database.

Alternatively, we could use next_load_date and select all the URLs where next_load_date is today. 

# Application:
Depending on how Imgur is setup could use cURL (and should if it is enough) or a browser automation framework such as Selenium.

We may need to specify a User Agent for cURL to work. 

**APIs**:
- add_url(url)
- remove_url(url, unique_id[optional])
- load_url(url, unique_id[optional])

# Interface:
Minimally, we can implement a REST API who's endpoints maps 1:1 to our APIs listed above, in the application section. 

If we use a simple framework such a Flask, adding a web interface a top our API endpoints should be trivial.  


# Reflection:
I think I moved too quickly into the particulars of the implementation of the storage components. It would have been beneficial to think more generally about the desired APIs before examining the storage components so closely. 

I also forgot to describe the implementation of the anti-abuse features although I did include the possibility of malicious use of the system. 

# References
- [Redis Queue](https://redis.com/glossary/redis-queue/)
- [Using your Database as a Queue?](https://codeopinion.com/using-your-database-as-a-queue/)
- [Implementing State Machines in PostgreSQL](https://felixge.de/2017/07/27/implementing-state-machines-in-postgresql/)
- [Modeling States and Transitions In Relation Databases](http://v1.monkey-robot.com/2014/05/modeling-states-and-transitions-in-relational-databases)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) 
