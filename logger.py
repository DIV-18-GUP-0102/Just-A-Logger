from datetime import datetime
import json

# Here I'm defining a global variable to control the maximum size of the circular linked list
MAX_LOG_SIZE = 30

class LogNode:
    def __init__(self, log_entry):
        # Initializing a LogNode with the log entry
        self.log_entry = log_entry
        self.next = None

class CircularLinkedList:
    def __init__(self):
        # Initializing a CircularLinkedList with head, tail, and size attributes
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, log_entry):
        # I'm appending a new log entry to the circular linked list
        new_node = LogNode(log_entry)
        if not self.head:
            # If the list is empty, I set the new node as both head and tail
            self.head = new_node
        else:
            # If the list is not empty, I set the new node as the next node of the current tail
            self.tail.next = new_node
        # Then I update the tail to the new node and make it circular by connecting its next to the head
        self.tail = new_node
        self.tail.next = self.head
        # I also increment the size of the circular linked list
        self.size += 1

    def remove_oldest(self):
        # Here I'm removing the oldest log entry from the circular linked list if it exceeds the maximum size
        if self.size > MAX_LOG_SIZE:
            # If the size exceeds the maximum, I move the head to its next node
            self.head = self.head.next
            # I also update the tail to maintain circularity
            self.tail.next = self.head
            # And decrement the size of the circular linked list
            self.size -= 1

class Logger:
    def __init__(self):
        # Here I'm initializing a Logger with a circular linked list to store log entries
        self.log_entries = CircularLinkedList()

    def log(self, message, log_type="MSG", severity="INFO", metadata=None):
        # Logging a new event with the provided data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "type": log_type,
            "severity": severity,
            "message": message,
            "metadata": metadata
        }

        # I converted the log entry to a JSON string and appended it to the circular linked list
        json_log_entry = json.dumps(log_entry)
        self.log_entries.append(json_log_entry)
        # Then I removed the oldest log entry if the list exceeds the maximum size
        self.log_entries.remove_oldest()

    def format_log_entry(self, log_entry):
        # Here I'm formatting a log entry into a readable string
        formatted_log = f"[{log_entry['timestamp']}] [{log_entry['type']}] [{log_entry['severity']}] {log_entry['message']}"
        if log_entry['metadata']:
            formatted_log += f" - Metadata: {log_entry['metadata']}"
        return formatted_log

    def display_logs(self):
        # Here I'm displaying all the log entries in the circular linked list
        current_node = self.log_entries.head
        while current_node:
            print(current_node.log_entry)
            current_node = current_node.next
            if current_node == self.log_entries.head:
                break

    def filter_logs(self, category, value):
        # Here I'm filtering logs based on its severity level or its type 
        filtered_logs = []
        current_node = self.log_entries.head
        while current_node:
            log_entry = json.loads(current_node.log_entry)
            # I check if the log entry matches the category (severity or type) and value (for severity there are four kinds and for type there are three: event, message, error)
            if log_entry.get(category) == value:
                filtered_logs.append(log_entry)
            current_node = current_node.next
            # I break the loop if I've traversed the entire circular linked list
            if current_node == self.log_entries.head:
                break
        # Finally, I return the filtered logs
        return filtered_logs

