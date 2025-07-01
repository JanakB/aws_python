from collections import Counter
from multiprocessing import Pool

def mapper(data):
    # Perform mapping operation on each input data element
    # and return key-value pairs
    results = []
    # Example: Counting the frequency of each word
    for word in data.split(): #splits the input data
        results.append((word, 1)) # append the inputs
    return results

def map_reduce(data, mapper_func, num_workers):
    # Split the input data and distribute it across multiple workers
    pool = Pool(processes=num_workers)
    mapped_data = pool.map(mapper_func, data)
    pool.close() #to close the pool
    pool.join() # wait for completion of all process for final result

    # Flatten the mapped data, join array
    '''
    process1 =[('hello', 1), ('world', 1), ('hello', 1)]
    procees2 =[('world', 1), ('python', 1), ('world', 1)]
    mapped_data -> [process1,proces2] =
    [[('hello', 1), ('world', 1), ('hello', 1)],[('world', 1), ('python', 1), ('world', 1)]]
    flatten data ->[('hello', 1), ('world', 1), ('hello', 1), ('world', 1), ('python', 1), ('world', 1)]
    '''
    flattened_data = [item for sublist in mapped_data for item in sublist]
    # Reduce the data using Counter
    word_count = Counter()
    for key, value in flattened_data:
        word_count[key] += value
    return word_count

# Example usage
if __name__ =='__main__':
    # Input data from two tiles
    data = [
        "hello world hello",
        "world python world",
        "hello hello hello",
        "world python world",
        "hello hello hello",
        "world python world",
        "hello hello hello",
        "world python world",
        "hello hello hello",
        "world python world",
        "hello hello hello"

    ]

    # Perform MapReduce operation
    result = map_reduce(data, mapper, num_workers=2)
    # print(result)
    # Print the final result
    for key, value in result.items():
        print(f"{key}: {value}")