
# Printer queue simulation in Python

import time
import random


class PrinterClass:
    def __init__(self):
        self.queue = []

    def addLocalJobs(self, jobs):
        self.queue.append(jobs)

    def process_queue(self):
        while self.queue:
            job = self.queue.pop(0)
            print(f"Printing job {job}")

            # Simulate printing time
            time.sleep(random.uniform(0.5, 1.5))

            print(f"Job {job} completed")


def main():
    printer_queue = PrinterClass()

    # Add some jobs to the queue
    for i in range(1, 6):
        printer_queue.addLocalJobs(f"Job{i}")

    # Process the queue
    printer_queue.process_queue()


if __name__ == "__main__":
    main()
=======
# Printer queue simulation in Python

import time
import random


class PrinterClass:
    def __init__(self):
        self.queue = []

    def addLocalJobs(self, jobs):
        self.queue.append(jobs)

    def process_queue(self):
        while self.queue:
            job = self.queue.pop(0)
            print(f"Printing job {job}")

            # Simulate printing time
            time.sleep(random.uniform(0.5, 1.5))

            print(f"Job {job} completed")


def main():
    printer_queue = PrinterClass()

    # Add some jobs to the queue
    for i in range(1, 6):
        printer_queue.addLocalJobs(f"Job{i}")

    # Process the queue
    printer_queue.process_queue()


if __name__ == "__main__":
    main()

