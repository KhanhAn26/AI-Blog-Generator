import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("Open API Key")
client = OpenAI(api_key = api_key)

def generate_blog(paragraph_topic):
    response = client.chat.completion.create(
        model = "gpt-3.5-turbo",
        message = [
            {"role" : "user", "content" : f"Write a blog about {paragraph_topic}."}])
    return response.choice[0].message.content

if __name__ == "main":
    topic = input("Enter a blog topic:  ")
    blog = generate_blog(topic)
    print("\nGenerated Blog Paragraph:\n")
    print(blog)

