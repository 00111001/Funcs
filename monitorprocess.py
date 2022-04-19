import psutil
import os
import time
# To work and log with logging files
import logging

logging.basicConfig(filename='data.log', encoding='utf-8', level=logging.DEBUG)

pid = os.getpid()
print(pid)
time.sleep(5)

current_process = psutil.Process(pid);
with current_process.oneshot():
    logging.info(f'Name: {current_process.name}'
                 f'CPU: {current_process.cpu_percent()},'
                 f'MEM: {current_process.memory_percent()}'
                 f'Threads: {current_process.num_threads()}')
print(current_process.name())


#######################



class MonitoringThread(Thread):
    # Initialize MyThread
    def __init__(self):
        # Inherits from Thread
        Thread.__init__(self)
        # Instance of MyThread


    # The run Func with code that runs repeatedly
    def run(self):
        pid = os.getpid()
        current_process = psutil.Process(pid);
        while True:
            time.sleep(1)
            with current_process.oneshot():
                logging.info(f'Name: {current_process.name}'
                             f'CPU: {current_process.cpu_percent()},'
                             f'MEM: {current_process.memory_percent()}'
                             f'Threads: {current_process.num_threads()}')


if __name__ == '__main__':
    MonitoringT = MonitoringThread()
    MonitoringT.start()