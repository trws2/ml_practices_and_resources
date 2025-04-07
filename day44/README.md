# Day 44

- continue reading Modern System Design from educative.io; building blocks for modern system design
    - Load balancer
        - How would you ensure consistent routing for user sessions (e.g., a shopping cart) in a system using multiple load balancers to prevent single points of failure?
            - To ensure consistent routing for user sessions, particularly in a system with multiple load balancers, we can employ several strategies alongside consistent hashing. Here’s a more detailed approach:
                - Sticky Sessions (Session Affinity): configure the load balancers to use sticky sessions, where all requests from a user during a session are directed to the same server.
                - Session Replication: replicate session data across multiple servers to ensure that any server can handle requests for any session.
                - Consistent Hashing: as mentioned, consistent hashing ensures that a specific session ID is always routed to the same server, minimizing re-distribution of sessions when servers are added or removed.
        - Discuss solutions for maintaining session persistence in a highly available load-balancing setup.
            - Database-backed Sessions. Description: Store session data in a relational or NoSQL database. Implementation: When a user logs in or starts a session, the session data is saved to the database. Each request can then check the database for session data, ensuring consistency across servers.
            - Distributed Session Store. Description: Store session data in a centralized, distributed data store to allow any server to retrieve session information. Implementation: Use databases like Redis, Memcached, or a SQL database to persist session data. This allows all servers to access the same session information regardless of where the request is routed.






