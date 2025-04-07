# Day 43

- continue reading Modern System Design from educative.io; building blocks for modern system design
    - Domain name service
        - Why does DNS sacrifice strong consistency to achieve high performance and scalability?
            - This is due to the following reasons:
                - Response from DNS must be returned swiftly to resolve the IP address of a web url. Therefore, the DNS service must achieve high performance.
                - We have billions of users from around the world that need to use DNS to get IP addressed to access internet. Therefore, the DNS service must achieve scalability.
                - DNS prioritizes **eventual consistency** because it processes significantly more read operations than write operations. Updates to DNS records propagate lazily, allowing for faster responses to queries without overloading the infrastructure.
        - what is the difference between UDP and TCP?
            - In computer networks, UDP (User Datagram Protocol) and TCP (Transmission Control Protocol) are two fundamental protocols for data transmission. Here are the key differences between them:
                - Connection Type
                    - TCP: Connection-oriented. It establishes a connection before data transfer.
                    - UDP: Connectionless. It sends data without establishing a connection.
                - Reliability
                    - TCP: Reliable. It ensures data is received in order and without errors, using acknowledgments and retransmissions.
                    - UDP: Unreliable. There are no guarantees for delivery, order, or error-checking.
                - Speed
                    - TCP: Slower due to handshaking and error-checking mechanisms.
                    - UDP: Faster since it has minimal overhead and no connection establishment.
                - Data Transmission
                    - TCP: Data is sent as a stream of bytes, maintaining order.
                    - UDP: Data is sent as discrete packets, without a guarantee of order.
                - Use Cases
                    - TCP: Suitable for applications where accuracy is crucial (e.g., web browsing, email).
                    - UDP: Ideal for applications that require speed and can tolerate some data loss (e.g., video streaming, online gaming).
                - Header Size
                    - TCP: Larger header (20 bytes minimum) due to additional control information.
                    - UDP: Smaller header (8 bytes), leading to less overhead.
                - In sum, TCP is reliable and ordered, making it suitable for critical data transmission, while UDP is faster and simpler, ideal for applications that prioritize speed over reliability.
        - DNS caching improves performance but introduces the risk of stale data. Suppose an organization updates its website’s IP address, but many users still access the old IP due to caching. Propose a strategy to minimize disruption in such scenarios.
            - Set a short TTL so that updated record can be fetched.
            - Use a CDN to help mitigate the cache issue, as CDNs often have their own cache mechanisms and can route user to the correct content regardless of DNS caching
            - Inform user that there is an update in IP address
            - Maintain both old and new IP addresses for a period of time before the old address is gone, make both address point to the same server or load balancer.












