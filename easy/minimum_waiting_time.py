"""
    Given the waiting times for 
    a list of queries, arrange the 
    order of execution such that the 
    total waiting time for all queries
    to be executed is minimized.
"""
from typing import List

def minimumWaitingTime(queries: List[int]) -> int:
    if not queries:
        return 0
    
    # The minimum waiting time comes 
    # with executing queries with shorter
    # wait time first.
    queries.sort()

    # Each query waits until all the previous
    # queries to complete their execution.
    for i in range(1, len(queries) - 1):
        queries[i] = queries[i] + queries[i - 1]

    # Last element does not introduce
    # any waiting time, obviously.
    return sum(queries[:-1])
