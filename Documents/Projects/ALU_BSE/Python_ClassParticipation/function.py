
MAX_WEIGHT_LIMIT = 500

# Initialize booking data
passengers = []
total_weight = 0

def book_ticket(name, weight):
    global total_weight
    
    if weight <= 0:
        return f"Invalid weight for {name}. Must be greater than 0."
    
    if total_weight + weight > MAX_WEIGHT_LIMIT:
        return f"Cannot book {name}. Exceeds maximum weight limit."
    
    passengers.append((name, weight))
    total_weight += weight
    return f"{name} booked successfully with {weight}kg baggage."


def cancel_ticket(name):
    global total_weight
    
    for i, (passenger_name, weight) in enumerate(passengers):
        if passenger_name == name:
            del passengers[i]
            total_weight -= weight
            return f"{name}'s ticket canceled."
    
    return f"No booking found for {name}."


def total_passenger_count():
    return len(passengers)


def check_total_weight():
    return total_weight

# Example Usage
if __name__ == "__main__":
    print(book_ticket("Alice", 120))
    print(book_ticket("Bob", 200))
    print(book_ticket("Charlie", 190))  # Should fail as it exceeds limit
    print(total_passenger_count())
    print(check_total_weight())
    print(cancel_ticket("Alice"))
    print(total_passenger_count())
    print(check_total_weight())
