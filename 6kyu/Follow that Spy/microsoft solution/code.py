def find_routes(routes):
    # Create a dictionary to store the destinations for each location
    destinations = {}
    
    # Populate the dictionary based on the provided routes
    for route in routes:
        src, dest = route
        destinations[src] = dest
    
    # Find the starting location (the one with no incoming route)
    start_location = None
    for location in destinations.keys():
        if location not in destinations.values():
            start_location = location
            break
    
    # Follow the chain of destinations to construct the correct sequence
    sequence = [start_location]
    while len(sequence) < len(routes) + 1:
        next_location = destinations[sequence[-1]]
        sequence.append(next_location)
    
    return ", ".join(sequence)