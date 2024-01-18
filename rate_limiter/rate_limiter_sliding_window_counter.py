from time import time, sleep

class SlidingWindowCounterRateLimiter:
    def __init__(self, requests_per_window, window_size):
        self.requests_per_window = requests_per_window
        self.window_size = window_size
        self.window_start_time = time()
        self.request_count = 0

    def clean_old_entries(self, current_time):
        # Check if the current window has elapsed
        if current_time - self.window_start_time >= self.window_size:
            self.window_start_time = current_time
            self.request_count = 0

    def allow_request(self):
        current_time = time()

        # Clean up old entries in the sliding window
        self.clean_old_entries(current_time)

        # Check if the number of requests within the window is below the limit
        if self.request_count < self.requests_per_window:
            self.request_count += 1
            return True
        else:
            return False

class APIHandler:
    def __init__(self):
        self.rate_limiter = SlidingWindowCounterRateLimiter(requests_per_window=5, window_size=5)

    def process_request(self):
        if self.rate_limiter.allow_request():
            print("Request processed successfully.")
        else:
            print("Request rate limit exceeded. Please try again later.")
            # Simulate a delay or handle the request in some way
            sleep(1)

# Example Usage
api_handler = APIHandler()

# Simulate processing requests
for _ in range(10):
    api_handler.process_request()
