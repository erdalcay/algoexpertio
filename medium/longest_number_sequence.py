"""
    Given an unordered list of numbers,
    find the sequence of consecutive numbers with 
    the maximum length.

    find_max_seq_length: O(n) | O(n)
"""


def find_max_seq_length(
    sequences: list[int]
) -> int:
    # Use a hashmap (constant lookup time complexit)
    # to keep track of visited elements
    # in the input list.
    visits = {num: False for num in sequences}

    max_seq_length = 0

    for i in range(len(sequences)):
        # If the value has been visited in the past,
        # then skip.
        curr_value = sequences[i]

        if curr_value in visits and visits[curr_value]:
            continue

        # Mark the value as visited
        visits[curr_value] = True

        # Initialize the current sequence length
        # with 1, because [i] is a member of the
        # sequence itself.
        curr_seq_length = 1

        # Go forward within the sequence
        forward = sequences[i] + 1
        while forward in visits:
            # Mark the value as visited
            visits[forward] = True
            # Increase the length of the sequence
            curr_seq_length += 1
            # Go forward for one more step
            forward += 1

        # Go backwards within the sequence
        backward = sequences[i] - 1
        while backward in visits:
            # Mark the value as visited
            visits[backward] = True
            # Increase the length of the sequence
            curr_seq_length += 1
            # Go back for one more step
            backward -= 1

        # We are done with this sequence.
        # Check if it is longer than the previous
        # sequence and then set to zero
        # for the next sequence.
        max_seq_length = max(max_seq_length, curr_seq_length)
        curr_seq_length = 0

    return max_seq_length
