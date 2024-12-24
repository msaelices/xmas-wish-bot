import argparse
import os
import time

import dotenv
import pywhatkit
from openai import OpenAI

dotenv.load_dotenv()


# 2. Define a function to generate a funny Christmas message via OpenAI
def generate_funny_christmas_message(
    client: OpenAI, name: str, language: str, topic: str
) -> str:
    """
    Generates a funny Christmas greeting with personalization.
    """
    prompt = (
        f"Write a short, funny Christmas greeting message in the {language} language for {name} related with the topic {topic}. "
        "Keep it playful, merry, and lighthearted, but mention their name clearly."
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo" if using ChatCompletion
        temperature=0.7,
        max_tokens=100,
        messages=[
            {
                "role": "system",
                "content": prompt,
            }
        ],
    )
    message_text = str(response.choices[0].message.content)

    return message_text


def fetch_contacts(csv_path: str) -> dict:
    """
    Fetch contacts from a file or database.
    """
    # Example: Read contacts from a CSV file
    with open(csv_path) as f:
        contacts = {}
        for line in f:
            phone_number, name, topic, *rest = line.strip().split(",")
            contacts[phone_number] = {
                "name": name,
                "topic": topic,
            }
    return contacts


# 4. Send messages to each contact
def send_christmas_messages(client: OpenAI, contacts: dict, language: str):
    """
    For each contact, generate a personalized message and send it via WhatsApp.
    """
    for phone_number, data in contacts.items():
        # Generate the personalized message
        name = data["name"]
        topic = data["topic"]

        message = generate_funny_christmas_message(client, name, language, topic)

        print(f"Sending message to {name}...")

        # Send message instantly.
        # Alternatively, you can schedule a time using sendwhatmsg(phone_no, message, time_hour, time_min).
        try:
            pywhatkit.sendwhatmsg_instantly(
                phone_no=f"+{phone_number}",
                message=message,
                tab_close=True,
                wait_time=15,  # how many seconds to wait after opening the browser
            )
        except Exception as e:
            print(f"Failed to send to {name}: {e}")

        # Sleep between messages to avoid flooding or being detected as spam.
        time.sleep(10)


def main():
    # Parse CLI arguments
    parser = argparse.ArgumentParser(description="Send Christmas messages to contacts.")
    parser.add_argument("csv_path", help="Path to the CSV file with contacts.")
    parser.add_argument(
        "--language",
        default="English",
        help="Language code for the message (default: English)",
    )
    args = parser.parse_args()

    # Get the file path to the CSV file from CLI args
    csv_path = args.csv_path
    language = args.language

    # Fetch contacts from the CSV
    contacts = fetch_contacts(csv_path)
    # Send messages to each contact
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    send_christmas_messages(client, contacts, language)
    print("All messages have been sent!")


# Run the function to send messages
if __name__ == "__main__":
    main()
