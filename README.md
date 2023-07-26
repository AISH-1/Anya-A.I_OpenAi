# Anya A.I.

Anya A.I. is a simple AI-based chatbot powered by the OpenAI GPT-3 model. It interacts with users, responds to their queries, and performs various predefined actions, such as opening websites, playing music, providing the current time, and more.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Anya-AI.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up OpenAI API:

To use Anya A.I., you need to have access to the OpenAI GPT-3 API. Obtain your API key from OpenAI and store it in a file named `config.py`. The file should contain:

```python
# config.py
apikey = "YOUR_OPENAI_API_KEY"
```

## Usage

1. Run Anya A.I.:

```bash
python main.py
```

2. Speak to Anya A.I.:

Anya A.I. will listen to your voice inputs and respond accordingly. You can ask questions, have casual conversations, or give specific commands.

## Predefined Commands

Anya A.I. understands the following predefined commands:

- "Open {website}": Opens popular websites like YouTube, Wikipedia, Google, Facebook, and more. For example, "Open YouTube."

- "Play music": Plays a specific music file ("Dance_Monkey.mp3" by default).

- "The time": Provides the current time.

- "Open VSCode": Opens Visual Studio Code (VSCode).

- "Open Word": Opens Microsoft Word.

- "Using artificial intelligence": Invokes the OpenAI GPT-3 model to generate an AI-based response based on the provided prompt.

- "Anya Quit": Exits the Anya A.I. application.

- "Reset chat": Resets the chat history with Anya A.I.

## Contributions

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
