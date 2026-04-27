# Ai-news-summarizer
📰 AI News Summarizer

An AI-powered full-stack web application that fetches real-time news and summarizes it into clean, readable insights using LLMs + search tools with a modern animated UI.

✨ Features
🔍 Real-time news search using Tavily API
🧠 AI-powered summarization using Mistral / LangChain
🎨 Modern animated UI with glassmorphism design
🧩 Block-wise news card layout
⚡ Fast Flask backend API
🌐 Auto-opens browser on launch
📱 Responsive frontend (mobile-friendly)
🧠 Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
AI Framework: LangChain
LLM: Mistral AI
Search API: Tavily
Environment: Python-dotenv
📁 Project Structure
newssummarizer/
│
├── app.py
├── .env
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/news-summarizer.git
cd news-summarizer
2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Setup environment variables

Create a .env file:

MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
5. Run the application
python app.py

👉 The app will automatically open in your browser:

http://127.0.0.1:5000/
🚀 How it works
User Input → Flask Backend → Tavily Search → LangChain LLM → Summary → UI Cards
🖥️ UI Preview
Glassmorphism cards
Animated news blocks
Dark modern theme
Responsive grid layout
📌 Example Use Cases
Latest AI news summaries
Tech trend tracking
Research quick reading
Daily news digest
