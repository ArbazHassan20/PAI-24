def build_message(**info):
    if not info:
        print("No info given\n")
        return
    
    # Looping through both the keys and values in the dictionary using the items() function
    for key, value in info.items():
        print(f"{key}: {value}\n")

# Example usage of build_message function
build_message(name="Ukkashah", age=20, occupation="student")
