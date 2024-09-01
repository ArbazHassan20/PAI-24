user_url = input("Please enter your URL (http://www.): ")

if user_url.startswith("http://www."):
    new_url = user_url[11:] + ".com"
    print("Converted URL:", new_url)
else:
    print("The URL does not start with 'http://www.'. Please make sure your URL is in the correct format.")
