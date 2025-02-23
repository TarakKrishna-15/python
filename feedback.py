# feedback.py

def is_valid_ratings(ratings):
    return all(0 <= rating <= 5 for rating in ratings)

def add_feedback(customer_data, name, ratings):
    if name in customer_data:
        customer_data[name].extend(ratings)
    else:
        customer_data[name] = ratings

def calculate_average(ratings):
    return sum(ratings) / len(ratings) if ratings else 0

def print_report(customer_data, loyalty_threshold):
    for name, ratings in customer_data.items():
        avg_rating = calculate_average(ratings)
        if avg_rating >= loyalty_threshold:
            status = "Qualifies for reward"
        else:
            status = "Does not qualify for reward"
        print(f"{name}'s average rating: {avg_rating:.2f}")
        print(f"Reward status: {status}\n")
