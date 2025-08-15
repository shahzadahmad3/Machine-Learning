# Write a program to calculate the square of numbers in parallel using multiprocessing.

# Use a Queue to share data between processes.
from multiprocessing import Process, Queue

def square_numbers(queue, result_queue):
    """Fetch numbers from queue, compute square, and store results in result_queue."""
    while not queue.empty():  # Process numbers until the queue is empty
        num = queue.get()  # Get a number from the queue
        result_queue.put((num, num ** 2))  # Put (number, squared value) in result_queue

if __name__=='__main__':
    numbers=[1,2,3,4,5]

    number_queue=Queue()
    result_queue=Queue()

    for num in numbers:
        number_queue.put(num)

    p1=Process(target=square_numbers, args=(number_queue, result_queue))
    p2=Process(target=square_numbers, args=(number_queue, result_queue))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not result_queue.empty():
        num, squared=result_queue.get()
        print(f"The square of {num} is {squared}")