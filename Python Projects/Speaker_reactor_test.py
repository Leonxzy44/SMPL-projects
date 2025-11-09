import time

import random

import winsound

def test_function():
    """A simple test function that simulates a task by sleeping for a random duration."""
    duration = random.uniform(0.5, 2.0)  # Sleep for a random time between 0.5 and 2 seconds
    time.sleep(duration)
    return duration
def run_tests(num_tests=5):
    """Run a series of test functions and provide auditory feedback upon completion."""
    for i in range(num_tests):
        print(f"Running test {i + 1}...")
        duration = test_function()
        print(f"Test {i + 1} completed in {duration:.2f} seconds.")
    
    # Play a sound to indicate that all tests are complete
    print("All tests completed. Playing sound...")
    winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 ms
if __name__ == "__main__":
    run_tests()
    