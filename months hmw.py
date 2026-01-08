import calendar

def display_month_names():
    """
    Displays all month names from January to December using the calendar module.
    """
    # calendar.month_name returns an array where index 0 is an empty string
    for month_index in range(1, 13):
        print(calendar.month_name[month_index])

if __name__ == "__main__":
    try:
        display_month_names()
    except Exception as e:
        print(f"An error occurred: {e}")