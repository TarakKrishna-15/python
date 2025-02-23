# main.py

from feedback import is_valid_ratings, add_feedback, calculate_average, print_report

def main():
    customer_data = {}
    loyalty_threshold = 4.5

    while True:
        action = input("Feedback (add/report/exit): ").strip().lower()

        if action == "add":
            name = input("Name: ").strip()
            ratings_input = input("Ratings (e.g., [4.5, 5]): ").strip()

            # Validate ratings
            ratings = eval(ratings_input)  # Use eval for list input (e.g., [4, 4.5])
            if is_valid_ratings(ratings):
                add_feedback(customer_data, name, ratings)
                avg_rating = calculate_average(customer_data[name])
                print(f"Updated Avg: {avg_rating:.2f}")
            else:
                print("Invalid ratings. Please enter a list of numbers between 0 and 5.")

        elif action == "report":
            print_report(customer_data, loyalty_threshold)

        elif action == "exit":
            print("bye!")
            break

        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()


