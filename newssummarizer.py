from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import webbrowser
import threading

from langchain_tavily import TavilySearch
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

app = Flask(__name__)

# -------------------
# AI + SEARCH SETUP
# -------------------
search_tool = TavilySearch(max_results=5)

llm = ChatMistralAI(model="mistral-medium")

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Summarize the following news articles in 2-3 concise sentences:

{news}
""")

chain = prompt | llm | StrOutputParser()

# -------------------
# ROUTES
# -------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    query = data.get("query")

    # Step 1: Search news
    news_result = search_tool.invoke(query)

    # Step 2: Summarize
    result = chain.invoke({"news": news_result})

    return jsonify({"summary": result})


# -------------------
# AUTO OPEN BROWSER
# -------------------
def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")


# -------------------
# MAIN
# -------------------
if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True, use_reloader=False)