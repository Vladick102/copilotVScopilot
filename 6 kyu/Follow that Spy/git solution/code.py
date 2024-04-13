def find_routes(routes):
    route_dict = {start: end for start, end in routes}
    start_location = next(
        location
        for location in route_dict.keys()
        if not any(location in route for route in route_dict.values())
    )
    itinerary = [start_location]
    while start_location in route_dict:
        start_location = route_dict[start_location]
        itinerary.append(start_location)
    return ", ".join(itinerary)
