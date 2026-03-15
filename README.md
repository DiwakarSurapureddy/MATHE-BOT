# Gemini AI Chatbot

A modern, interactive web-based chatbot powered by Google's Gemini AI model. This application provides a seamless conversational experience with persistent chat history storage.

## Features

- 🤖 **AI-Powered Conversations** - Leverages Google Gemini 2.5 Flash for intelligent responses
- 💾 **Chat History** - Persistent storage of conversation history with timestamps
- 🎨 **Clean UI** - Modern and responsive web interface
- ⚡ **Real-time Responses** - Instant AI-generated replies
- 📱 **Mobile Friendly** - Works seamlessly across all devices
- 🔄 **History Management** - View, access, and clear chat history

## Tech Stack

- **Backend**: Flask (Python web framework)
- **AI Model**: Google Generative AI (Gemini 2.5 Flash)
- **Frontend**: HTML5, CSS3, JavaScript
- **Storage**: JSON file-based persistence

## Project Structure

```
.
├── gemini chatbot/
│   └── gemini chatbot/
│       ├── app.py                 # Flask application and API endpoints
│       ├── requirements.txt        # Python dependencies
│       ├── templates/
│       │   └── index.html          # Main chatbot interface
│       └── static/
│           ├── style.css           # Styling and UI components
│           └── script.js           # Frontend logic and interactions
├── GEN.py                          # Additional generator utility
├── store.json                      # Chat history storage
├── static/                         # Additional static files
└── templates/                      # Additional templates
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google API key for Gemini AI model

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd FOR\ hack
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r gemini\ chatbot/gemini\ chatbot/requirements.txt
   ```

5. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   FLASK_DEBUG=True
   ```

## Running the Application

1. **Navigate to the application directory**
   ```bash
   cd gemini\ chatbot/gemini\ chatbot
   ```

2. **Start the Flask development server**
   ```bash
   python app.py
   ```

3. **Access the application**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Render the main chatbot interface |
| POST | `/chat` | Send a message and receive AI response |
| GET | `/history` | Retrieve all chat history |
| POST | `/clear-history` | Clear all chat history |

### Example API Requests

**Send a message:**
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, how are you?"}'
```

**Get chat history:**
```bash
curl http://localhost:5000/history
```

**Clear history:**
```bash
curl -X POST http://localhost:5000/clear-history
```

## Usage

1. Type your message in the chat input field
2. Press Enter or click the Send button
3. Wait for the AI to generate a response
4. Your conversation is automatically saved
5. View your chat history anytime
6. Clear history when needed to start fresh

## Configuration

### Environment Variables

- `GOOGLE_API_KEY` - Your Google Gemini API key (required)
- `FLASK_DEBUG` - Enable Flask debug mode (True/False)
- `FLASK_SECRET_KEY` - Secret key for Flask sessions (optional)

### Gemini Model

The application uses `gemini-2.5-flash` model by default. To change the model, edit the `app.py` file:

```python
model = genai.GenerativeModel("gemini-2.5-flash")
```

## Storage

Chat history is stored in `history.json` file with the following structure:
```json
{
  "messages": [
    {
      "user": "Your message",
      "bot": "AI response",
      "timestamp": "YYYY-MM-DD HH:MM:SS"
    }
  ]
}
```

## Troubleshooting

### Issue: GOOGLE_API_KEY not found
**Solution**: Ensure your `.env` file is in the root directory with the correct API key.

### Issue: Port 5000 already in use
**Solution**: Change the port in `app.py`:
```python
app.run(debug=True, port=5001)
```

### Issue: ModuleNotFoundError
**Solution**: Ensure all dependencies are installed:
```bash
pip install -r gemini\ chatbot/gemini\ chatbot/requirements.txt
```

## Security Considerations

⚠️ **Important Security Notes:**

- Never commit `.env` files to version control
- Keep your Google API key confidential
- Use environment variables for sensitive data
- Implement rate limiting for production use
- Add authentication for multi-user scenarios
- Validate and sanitize user inputs

## Performance Tips

- The Gemini API may take a few seconds to generate responses depending on complexity
- Chat history is stored locally; for production, consider database solutions
- Clear history periodically to maintain optimal performance

## Future Enhancements

- [ ] User authentication and multi-user support
- [ ] Database integration (MongoDB, PostgreSQL)
- [ ] Advanced chat search and filtering
- [ ] Export conversations to PDF/TXT
- [ ] Multi-language support
- [ ] Rate limiting and usage analytics
- [ ] Dark mode theme
- [ ] Voice input/output

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions, please:
- Open an issue on the GitHub repository
- Check existing documentation
- Review API documentation for Gemini

## Acknowledgments

- Google Generative AI for the Gemini API
- Flask framework for backend development
- Contributors and community support

---

**Last Updated**: March 2026
