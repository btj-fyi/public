Requirements & Goals:
- Availability: The extent to which a system or service is operational and accessible, often quantified as a percentage of uptime over a give timeframe.
- Reliability: The consistency and dependability of a system or service to perform its intedended function(s).
- Latency: The time delay between the initiation of a request and the corresponding response, typically measured in milliseconds or seconds.
- Durability: The ability of a system or service to maintain data integrity and accessibility despite failures or errors. 
- *ACID-ity*: Atomicity, Consistency, Isolation, Durability
- - Atomicity: The property to ensure that a transation is treated as a single, indivisble unit of work, either fully completed or full aborted without partial updates or inconsistencies.
- - Consistenty: The property ensuring that data remains valid and accurate before and after transactions, maintaing integrirty and adhering to predefined rules and constraings.
- - [Isolation](https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-isolation-levels.html): The property ensuring that transactions operate independtly of each other, preventing interferences and maintaining data integrity by prodiving each transaction with a view of the database as if it were the only one accessing it.
- - Durability: The property ensuring that once a transaction is committed, its change are permanent and persist even in the event of a system failure, guranteeing data integrity and recoverability.
*NoSQL is often *not* ACID-compliant

Estimates & Constraints:
- read-heavy vs write-heavy
- Queries per second (QPS)
- ingress vs egress
- 5 year storage
- 10 year storage
- caching and 80/20 rules

System API(s):
- 

Database Design & Storage
- [SQL vs NoSQL](https://www.educative.io/collection/page/5668639101419520/5649050225344512/5728116278296576/)
- Partitioning
-- Range-based
-- Hash-based
-- Vertical
- Sharding
-- Partion-based
-- Joins & Denormalization
-- Referential integrity
--- [Consistent Hashing](https://www.educative.io/collection/page/5668639101419520/5649050225344512/
5709068098338816/)
- Replication
- Object Storage (eg Amazon S3, HDFS)
- Redundancy
- Indexes - Better for reads. Worse for writes (sometimes).
-- [B-trees](https://razberry.substack.com/p/btree-factorio)
-- R-trees
-- GIST
- Transactions

System Design & Algorithms:
- Encoding
-- Hashing
-- base64
- Key Generation Service (KGS)
- [Caches](https://www.educative.io/collection/page/5668639101419520/5649050225344512/5643440998055936) (eg Redis, Memcache, )
-- Eviction Policies
--- Least Recently Used
--- Most Recently Used
-- Cahce Misses
-- Content Delivery Network (CDN)
- Cache Invalidation
-- Write-through
-- Write-around
-- Write-back
- Load Balancers (LB)
-- Round-robin
- Single Points of Failure
- Pre-generation
- Client-Server Communcation
-- Pull
-- Push
--- [Long Poll](https://en.wikipedia.org/wiki/Push_technology#Long_polling)
-- [WebSockets](https://www.educative.io/collection/page/5668639101419520/5649050225344512/5715426797420544)
-- [WebTransport](https://developer.mozilla.org/en-US/docs/Web/API/WebTransport)
-- Hybrid
- Chunking
- Queues
- Deduplication
-- Post-process
-- In-line
- Trees
-- Trie
-- QuadTree
- Abuse Prevention
-- Rate Limiting
--- Fixed Window
--- Rolling Window
- Hash Tables
- Scalability
-- Vertical
-- Horizontal
- Consistency, Availability, Partion Tolerance (CAP)
*CAP is still a theory although it is widely applicable. 




