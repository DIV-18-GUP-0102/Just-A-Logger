# Logger System:

This is an attempt to solve a problem statement I saw about creating a simple logger system capable of logging **"*various types of events, messages, and errors* "**  having  **" *API endpoints for logging events and retrieving logged data*"** and **"*a circular linked list data structure to store logged data*"**.

## Overview

The system consists of:

1. *app.py*: This file contains the Flask application responsible for handling HTTP requests and responses. It exposes endpoints for logging events, retrieving logs, and filtering logs.

2. *logger.py*: This file contains the Logger class, which is responsible for logging events, maintaining a circular linked list of log entries, and filtering log entries based on category and value.

3. API endpoints in *app.py*:
   a. '/log/transmission' - for storing the data in the circular linked list.
   b. '/log/retrieval' - for logging all teh data to the console/command line.
   c. '/log/filter' - for retrieving logs according to filters specified by the user in *test.py*


## Notes about this project:

1. For the most part I just assumed the format and structure of what a log may have. Therefore the logs' field are pretty basic. 

2. Format of logged message: 
   ```json
   {
      "timestamp": "2024-04-24 05:09:30", 
      "type": "MSG", 
      "severity": "WARNING", 
      "message": "Test message 3", 
      "metadata": {"key": "value 3"}
   }
   ```

3. For the ```type``` of logs, I assumed three types: error (ERR), event (EVE) and message (MSG).

4. I studied and came to know that several ```severity``` levels that you can use to categorize log messages, as per  Python's ```logging``` module, are as:
   + DEBUG: Detailed information, typically used for debugging purposes.
   + INFO: Confirmation that things are working as expected.
   + WARNING (or WARN): Indication that something unexpected happened or may need attention.
   + ERROR: Indicates a more serious problem, typically something that prevented a part of the application from functioning correctly.
   + CRITICAL: Indicates a very serious error, often indicating that the application itself may be unable to continue running.

5. Since the problem statement mentioned to use a circular linked list as storage, I created a global variable to control the maximum size of the circular linked list
    ```python
    MAX_LOG_SIZE = 30.
    ```
6. Since the circular linked list is defined size, the logging is done so that the old entries/nodes are removed when the list is full and if the number of log entries is less than the size of the linked list, it is appending and logging by adding new nodes to the circular linked list

7. We just have to run *app.py*, and when it starts running on the local server, we can check/test its functionality through *test.py*.
        
