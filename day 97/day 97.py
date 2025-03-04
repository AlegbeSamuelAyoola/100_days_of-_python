import wikipediaapi

# Define a proper user-agent (modify to include your contact info)
user_agent = "MyPythonBot/1.0 (https://example.com/contact)"  

# Initialize Wikipedia API with the user-agent
wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language="en")

# Fetch Machiavelli's Wikipedia page
page = wiki.page("Niccolò_Machiavelli")

# Check if the page exists before accessing its content
if page.exists():
    print("Title:", page.title)
    print("\nSummary:\n", page.summary)
else:
    print("Error: The requested page does not exist.")






