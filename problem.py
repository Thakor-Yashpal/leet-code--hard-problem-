def shortestDistance(words, target, startIndex):
    # Check if the target string is in the array
    try:
        targetIndex = words.index(target)
    except ValueError:
        return -1

    # Initialize the queue with the start index
    queue = [startIndex]
    # Initialize the distances array with infinity
    distances = [float('inf')] * len(words)
    # Set the distance of the start index to 0
    distances[startIndex] = 0

    # Iterate over the queue
    while queue:
        # Get the current index
        index = queue.pop(0)

        # Check if the current word is the target
        if words[index] == target:
            return distances[index]

        # Add the next and previous indices to the queue, if they have not been visited yet
        next_index = (index + 1) % len(words)
        if distances[next_index] == float('inf'):
            queue.append(next_index)
            distances[next_index] = distances[index] + 1
        prev_index = (index - 1 + len(words)) % len(words)
        if distances[prev_index] == float('inf'):
            queue.append(prev_index)
            distances[prev_index] = distances[index] + 1
