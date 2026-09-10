TOTAL_TICKETS = 10
MAX_TICKETS_PER_BUYER = 4

def get_ticket_count(remaining_tickets):
    """Get and validate the number of tickets requested by a buyer."""

    # Continue asking until the buyer enters an allowable ticket amount.
    while True:
        # Prevent a buyer from requesting more tickets than are available.
        maximum_tickets = min(MAX_TICKETS_PER_BUYER, remaining_tickets)

        tickets = int(input(
            f"How many tickets would you like to purchase (1-{maximum_tickets})? "
        ))
        # Accept the purchase only when it falls within the allowed range.
        if 1 <= tickets <= maximum_tickets:
            return tickets

        print("Invalid number. Please enter a valid number of tickets.")

def display_remaining(remaining_tickets):
    """Display the number of tickets still available."""

    # Show buyers how many tickets remain after each purchase.
    print(f"Tickets remaining: {remaining_tickets}")


def main():
    """Run the cinema ticket pre-sale program."""

    # Start the sale with the full number of available tickets.
    remaining_tickets = TOTAL_TICKETS
    total_buyers = 0

    # Continue selling tickets until the entire inventory is sold.
    while remaining_tickets > 0:
        tickets = get_ticket_count(remaining_tickets)

        # Update the ticket inventory after the current purchase.
        remaining_tickets -= tickets

        # Count each completed purchase as one buyer.
        total_buyers += 1
        display_remaining(remaining_tickets)

    # Display the final results after all the tickets have been sold.
    print("All tickets have been sold.")
    print(f"Total number of buyers: {total_buyers}")

if __name__ == "__main__":
    main()