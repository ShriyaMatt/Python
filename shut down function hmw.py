def shutdown_decision(user_input: str):
    """
    Simulates a shutdown decision.
    :param user_input: User's response (expected 'yes' or 'no')
    """
    # Normalize input to lowercase and strip spaces
    choice = user_input.strip().lower()

    if choice == "yes":
        print("Shutting down...")
        # Actual shutdown command (commented for safety)
        # import os
        # os.system("shutdown /s /t 1")  # Windows
        # os.system("sudo shutdown now")  # Linux/Mac
    elif choice == "no":
        print("Abort shutting down.")
    else:
        print("Sorry, invalid input.")

# Main program
if __name__ == "__main__":
    try:
        user_response = input("Do you want to shut down the computer? (yes/no): ")
        shutdown_decision(user_response)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")