# 🤖 Rule-Based Chatbot Framework

## 📝 Overview

This repository provides a **simple and reusable rule-based chatbot** built using Python. It is designed to be easily extended and adapted to different domains by simply updating the intents and responses. Whether you're creating a customer support bot, FAQ assistant, or a basic conversational interface, this codebase serves as a solid foundation.

## 📂 Project Structure

```
.
├── intents.json              # Contains the intents, patterns, and responses
├── main.py                  # Main script to run the chatbot
├── training.py              # Handles preprocessing and model training
├── tempCodeRunnerFile.py    # Temporary file (can be ignored)
```

## ⚙️ How It Works

* Uses a **bag-of-words model** with a **feedforward neural network** to classify user input into predefined intents.
* Intent classification is based on training data stored in `intents.json`.
* Returns predefined responses based on predicted intent.

## 💡 Features

* Fully customizable via `intents.json`
* Lightweight and fast — no external APIs required
* Easily reusable across different domains (e.g., healthcare, retail, education)
* Beginner-friendly and well-structured code

## 🚀 Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<your-username>/rule-based-chatbot.git
   cd rule-based-chatbot
   ```

2. **Install required packages:**

   ```bash
   pip install numpy nltk tensorflow
   ```

3. **Train the model:**

   ```bash
   python training.py
   ```

4. **Run the chatbot:**

   ```bash
   python main.py
   ```

## 🧠 Customization

To adapt the bot for a different domain:

* Open `intents.json`
* Add or modify intents like so:

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey"],
      "responses": ["Hello!", "Hi there!", "Greetings!"]
    },
    ...
  ]
}
```

Then retrain the model using `training.py`.

## 🔁 Example Use Cases

* FAQ bots for websites
* Automated response systems
* Educational bots for basic interaction
* Domain-specific assistants (e.g., e-commerce, banking, healthcare)

## 🛠 Future Improvements (Optional)

* Add voice input/output
* GUI using Tkinter or Streamlit
* Integrate with APIs or databases
* More advanced NLP using transformers

## 📄 License

This project is open-source and intended for educational or prototyping purposes. Feel free to reuse and adapt with attribution.

