import json


def print_q_table(q_values_file):
    try:
        # Load Q-values from the JSON file
        with open(q_values_file, 'r') as f:
            q_values = json.load(f)

        # Display the Q-table
        print("Q-Table:")
        for state, action_values in q_values.items():
            print(f"State: {state}")

            # Check if action_values is a dictionary or a list
            if isinstance(action_values, dict):
                # Case: action_values is a dictionary
                for action, q_value in action_values.items():
                    print(f"  Action: {action} | Q-Value: {q_value}")
            elif isinstance(action_values, list):
                # Case: action_values is a list (handle differently if needed)
                print("  Action values are stored as a list:")
                for idx, q_value in enumerate(action_values):
                    print(f"  Action {idx}: Q-Value: {q_value}")
            else:
                print("  Invalid format for action values.")

    except FileNotFoundError:
        print(f"Error: File '{q_values_file}' not found.")


# Example usage: Print Q-table from 'qvalues.json' file
q_values_file = 'qvalues.json'
print_q_table(q_values_file)
