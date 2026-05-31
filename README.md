# SolveMate AI

SolveMate AI is a math-focused chatbot built with Flask and Google's Gemini model. It gives step-by-step solutions, stores chat history locally, and includes a polished responsive interface with theme and view controls.

## Features

- Math-only assistant for solving equations, calculus, trig, and general problems
- Step-by-step responses with a final answer section
- Quick Response from the SolveMate AI
- Light and dark theme toggle
- Desktop and mobile preview toggle
- Responsive single-page frontend
- Local JSON history persistence

## Tech Stack

- Backend: Flask
- AI: Google Generative AI (Gemini)
- Frontend: HTML, CSS, JavaScript
- Storage: JSON files

## Project Structure

```text
.
├── app.py
├── templates/
│   └── home.html
├── static/
│   └── style.css
├── history.json
├── store.json
├── README.md
└── .gitignore
```

## Prerequisites

- Python 3.8 or newer
- pip
- A Google Gemini API key

## Setup

1. Clone the repository.

2. Create a virtual environment.
   ```bash
   python -m venv .venv
   ```

3. Activate it on Windows.
   ```bash
   .venv\Scripts\activate
   ```

4. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

5. Add your API key to `.env`.
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   FLASK_DEBUG=True
   ```

## Run the App

```bash
python app.py
```

Then open:

```text
http://localhost:5000
```

## How It Works

- Type a math question and send it.
- The assistant returns a structured solution.
- The conversation is saved in `history.json`.
- Click any history item to replay that chat in the main panel.
- Delete history items individually using the delete icon.

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | Load the UI |
| POST | `/chat` | Send a math question |
| GET | `/history` | Read saved chat history |
| DELETE | `/delete-history/<index>` | Delete one history item |
| POST | `/clear-history` | Clear all saved history |
| GET | `/suggest` | Get a random sample problem |

## History Format

```json
{
  "messages": [
    {
      "user": "Solve 2x + 5 = 17",
      "bot": "STEP 1: ...",
      "timestamp": "2026-05-31 11:30:00"
    }
  ]
}
```

## Notes

- `history.json` is created automatically when you send your first message.
- `store.json` is treated as local data and is not meant for version control.
- The frontend is fully contained in `templates/home.html`.

## Troubleshooting

- If the app does not start, confirm your API key is present in `.env`.
- If a port is already in use, stop the other process or change the port in `app.py`.
- If the UI looks stale, refresh the browser after restarting the Flask server.

## License

Add your preferred license here if you plan to publish the project.
