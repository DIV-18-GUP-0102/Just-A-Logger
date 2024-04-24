'''
This test.py is only about me creating some test functions to to interact with the endpoints of the api.
'''

import requests

# The base URL for the Flask API running locally
BASE_URL = 'http://127.0.0.1:5000'

def test_log_event(message, log_type, severity, metadata=None):
    # Defining the log data to be sent in the POST request
    log_data = {
        "message": message,
        "type": log_type,
        "severity": severity,
        "metadata": metadata
    }

    # Sending a POST request to log the event
    response = requests.post(f"{BASE_URL}/log/transmission", json=log_data)
    print(f"Log Event Response for {log_type}:", response.json())

def test_get_logs():
    # Sending a GET request to retrieve all logs
    response = requests.get(f"{BASE_URL}/log/retrieval")
    print("Get Logs Response:", response.json())

def test_filter_logs(category, value):
    # Sending a GET request to filter logs based on category and value
    response = requests.get(f"{BASE_URL}/log/filter?category={category}&value={value}")
    print(f"Filtered Logs Response for {category}={value}:", response.json())

if __name__ == "__main__":
    '''
    Here I created a loop that will log five logs in one iteration of the loop. The logs will be numbered as
    1 to 35.
    '''
    for i in range(1, 36, 5):
        test_log_event(f"Test Log {i}", "EVE", "INFO", {"key": f"value {i}"})
        test_log_event(f"Test Log {i+1}", "ERR", "DEBUG", {"key": f"value {i+1}"})
        test_log_event(f"Test Log {i+2}", "MSG", "WARNING", {"key": f"value {i+2}"})
        test_log_event(f"Test Log {i+3}", "ERR", "CRITICAL", {"key": f"value {i+3}"})
        test_log_event(f"Test Log {i+4}", "MSG", "INFO", {"key": f"value {i+4}"})

    # Retrieving all logs
    test_get_logs()
    print("-------------------------------")

    # Filtering logs by type
    test_filter_logs("type", "ERR")
    print("-------------------------------")

    # Filtering logs by severity
    test_filter_logs("severity", "CRITICAL")
    print("-------------------------------")
    print("-------------------------------")
