from time import time, sleep

class SlidingWindowRateLimiter:
    def __init__(self, requests_per_window, window_size):
        self.requests_per_window = requests_per_window
        self.window_size = window_size
        self.timestamp_log = []

    def clean_old_entries(self, current_time):
        # Remove entries that are outside the time window
        self.timestamp_log = [timestamp for timestamp in self.timestamp_log if current_time - timestamp <= self.window_size]

    def allow_request(self):
        current_time = time()

        # Clean up old entries in the timestamp log
        self.clean_old_entries(current_time)

        # Check if the number of requests within the window is below the limit
        if len(self.timestamp_log) < self.requests_per_window:
            self.timestamp_log.append(current_time)
            return True
        else:
            return False

class APIHandler:
    def __init__(self):
        self.rate_limiter = SlidingWindowRateLimiter(requests_per_window=3, window_size=1)

    def process_request(self):
        if self.rate_limiter.allow_request():
            print("Request processed successfully.")
        else:
            print("Request rate limit exceeded. Please try again later.")
            # Simulate a delay or handle the request in some way
            # sleep(1)

# Example Usage
api_handler = APIHandler()

# Simulate processing requests
for _ in range(20):
    api_handler.process_request()
    sleep(0.25)
