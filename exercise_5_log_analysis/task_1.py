# Task 1: Analyze the log file and count: total requests, successful requests, and failed requests.
# Save the results to a text file.

from pathlib import Path
import sys

SERVER_LOGS_LIST_PATH = Path(__file__).parent / "server_logs.txt"
SERVER_LOGS_ANALYSIS_PATH = Path(__file__).parent / "server_logs_analysis.txt"


def get_log_data():
    try:
        with open(SERVER_LOGS_LIST_PATH) as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File ({SERVER_LOGS_LIST_PATH}) was not found")
        sys.exit()


logs_data = get_log_data()
print("Total number of requests: ", len(logs_data))

succeeded_requests = list(filter(lambda x: x.strip()[-3] == ("2"), logs_data))
print("Total number of succeeded requests: ", len(succeeded_requests))

failed_requests = list(
    filter(lambda x: x.strip()[-3] == "4" or x.strip()[-3] == "5", logs_data))
print("Total number of failed requests: ", len(failed_requests))


with open(SERVER_LOGS_ANALYSIS_PATH, "w") as file:
    file.writelines([
        f"Total number of requests: {len(logs_data)}\n",
        f"Total number of succeeded requests: {len(succeeded_requests)}\n",
        f"Total number of failed requests: {len(failed_requests)}\n",
    ])
    print(f"File ({SERVER_LOGS_ANALYSIS_PATH}) was created.")
