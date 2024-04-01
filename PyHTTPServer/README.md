# PyHTTPServer - HTTP Server from scratch in Python

[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) is the
protocol that powers the web. PyHTTPServer is an HTTP/1.1 server
that is capable of serving multiple clients.

## Status of development:

1. Bind to a Port         ![100%](https://progress-bar.dev/100)
2. Respond with 200       ![100%](https://progress-bar.dev/100)
3. Respond with 404       ![100%](https://progress-bar.dev/100)
4. Respond with Content   ![100%](https://progress-bar.dev/100)
5. Parse Headers          ⬜
6. Concurrent Connections ⬜
7. Get a file             ⬜
8. Post a file            ⬜
9. Examples to demonstrate PyHTTPServer in action!
    1. Exmaple 01  ✔️
    
    
        ![Exmaple 01](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/examples/Exmaple-01.png)
    2. Example 02  ✔️
    
    
        ![Exmaple 02](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/examples/Exmaple-02.png)

## Future improvements envisioned:

1. Functionality 1
    1. Feature 1
    2. Feature 2
2. Functionality 2
    1. Feature 1
    2. Feature 2
3. Functionality 3
    1. Feature 1
    2. Feature 2
4. Functionality 4
    1. Feature 1
    2. Feature 2
    
## Detailed Explanations of each Functionality:

1. Bind to a Port
    - Task:
        1. Start a TCP server on port 4221
    - Test:
        1. Run `python3 app/main.py` in one terminal session
        2. Run `nc -vz 127.0.0.1 4221` in another terminal session
        3. Check output
            - ![Client](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/misc-data/Functionality-01-Bind-to-a-Port-01.png)
2. Respond with 200
    - Task:
        1. Accept a TCP connection
        2. Read data from the connection (we'll get to parsing it in later stages)
        3. Respond with `HTTP/1.1 200 OK\r\n\r\n`
    - Test:
        1. Run `python3 app/main.py` in one terminal session
        2. Run `curl -v -X GET http://localhost:4221/` in another terminal session
        3. Check output
            - ![PyHTTPServer](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/misc-data/Functionality-02-Respond-with-200-01.png)
            - ![Client](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/misc-data/Functionality-02-Respond-with-200-02.png)
3. Respond with 404
    - Task:
        1. Extract the path from the HTTP request
        2. If the path is "/", respond with a 200 OK response
        3. Otherwise, respond with a 404 Not Found response
    - Test:
        1. Run `python3 app/main.py` in one terminal session
        2. Run `curl -v -X GET http://localhost:4221/` in 2nd terminal session
        3. Run `curl -v -X GET http://localhost:4221/index.html` in 3rd terminal session
        4. Check output
            - ![PyHTTPServer](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/misc-data/Functionality-03-Respond-with-404-01.png)
            - ![Client1](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/misc-data/Functionality-03-Respond-with-404-02.png)
            - ![Client2](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/misc-data/Functionality-03-Respond-with-404-03.png)
4. Respond with Content
    - Task:
        1. Extract the path from the HTTP request
        2. If the path is "/", respond with a 200 OK response
        3. If the path starts with "/echo/", respond with a 200 OK with remaining string in the path as body
        4. Otherwise, respond with a 404 Not Found response
    - Test:
        1. Run `python3 app/main.py` in one terminal session
        2. Run `curl -v -X GET http://localhost:4221/` in 2nd terminal session
        3. Run `curl -v -X GET http://localhost:4221/index.html` in 3rd terminal session
        4. Run `curl -v -X GET http://localhost:4221/echo/test/content` in 4th terminal session
        4. Check output
            - ![PyHTTPServer](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/misc-data/Functionality-04-Respond-with-Content-01.png)
            - ![Client1](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/misc-data/Functionality-04-Respond-with-Content-02.png)
            - ![Client2](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/misc-data/Functionality-04-Respond-with-Content-03.png)
            - ![Client3](https://github.com/ancilcleetus/Personal-Projects/blob/main/PyHTTPServer/misc-data/Functionality-04-Respond-with-Content-04.png)
