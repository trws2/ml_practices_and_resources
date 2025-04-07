# Day 43

- continue reading Modern System Design from educative.io; building blocks for modern system design
    - Domain name service
        - Why does DNS sacrifice strong consistency to achieve high performance and scalability?
            - This is due to the following reasons:
                - Response from DNS must be returned swiftly to resolve the IP address of a web url. Therefore, the DNS service must achieve high performance.
                - We have billions of users from around the world that need to use DNS to get IP addressed to access internet. Therefore, the DNS service must achieve scalability.
                - DNS prioritizes **eventual consistency** because it processes significantly more read operations than write operations. Updates to DNS records propagate lazily, allowing for faster responses to queries without overloading the infrastructure.






