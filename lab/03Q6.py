def save_question_to_file():
    try:
        sentence = input("Enter a sentence: ")
        
        # Check if it's a question
        if sentence.endswith("?"):
            with open("questions.txt", 'a') as file:
                file.write(sentence + "\n")
            print("Question saved successfully to questions.txt")
        else:
            print("The sentence is not a question, so it wasn't saved.")
    
    except FileNotFoundError:
        print("Error: Could not find the file.")
    except IOError:
        print("Error: An I/O error occurred while handling the file.")
    except Exception as e:
        print("An error occurred:", e)

save_question_to_file()
