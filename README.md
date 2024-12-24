# XMAS Wish Bot

Generate funny and personalized Christmas messages using OpenAI's GPT models and Whatsapp!

## Features

- Create unique Christmas greetings
- Personalize messages with names and custom details
- Powered by OpenAI's LLM

## Usage

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Copy the `.env-template` file to `.env` and fill in the required fields.
```bash
cp .env-template .env
```

3. Generate a CSV file with the phone number, name and topic of the message. Example of contents:
```csv
+15551234567,John,Ultimate Frisbee
+15551234568,Jane,Computer Science
+15551234569,Jack,Family man
```

*Note:* The CSV file should have the following columns: `phone_number`, `name`, `topic`. You can export your contacts from your phone or use a spreadsheet editor to create the CSV file.

4. Execute the `xmaswishbot.py` script with the CSV file as an argument and the desired language. Example:
```bash
python xmaswishbot.py --csv-file <path-to-csv-file> --language Spanish
```

5. Generate your unique Christmas message!

## Requirements

- OpenAI API key
- Internet connection
- Modern web browser

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues.

## License

MIT License - feel free to use and modify!
