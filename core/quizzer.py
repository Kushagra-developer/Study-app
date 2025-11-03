from utils.gemini_helper import generate_response

def generate_quiz(text: str) -> str:
    """Generate quiz questions or flashcards from a topic or passage."""
    prompt = f"""
You are a Study Assistant that creates quizzes for learning.

If the input is a topic name (e.g., "DBMS", "Machine Learning"), 
create questions on that topic.
If it's a text passage, generate questions from the given content.
Each question should include 4 options (A-D) and the correct answer below.
The types of questions can be:
- Multiple Choice
- True/False
- Fill in the Blanks
- Descriptive
Content: {text}
"""
    return generate_response(prompt.strip())
