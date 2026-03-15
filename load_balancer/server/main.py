# app.py

from typing import TypedDict
from langgraph.graph import StateGraph, END


# ---------------------------
# 1️⃣ Define State
# ---------------------------

class ArticleState(TypedDict):
    topic: str
    outline: str
    article: str


# ---------------------------
# 2️⃣ Node 1
# Generate Outline
# ---------------------------

def generate_outline(state: ArticleState):

    topic = state["topic"]

    outline = f"""
    Outline for article on {topic}

    1. Introduction
    2. What is {topic}
    3. Key Concepts
    4. Applications
    5. Future of {topic}
    """

    print("✅ Outline Generated")

    return {
        "outline": outline
    }


# ---------------------------
# 3️⃣ Node 2
# Write Article
# ---------------------------

def write_article(state: ArticleState):

    outline = state["outline"]

    article = f"""
    Article based on outline:

    {outline}

    This article explains the topic in detail with examples.
    """

    print("✅ Article Written")

    return {
        "article": article
    }


# ---------------------------
# 4️⃣ Create Graph
# ---------------------------

graph = StateGraph(ArticleState)


# ---------------------------
# 5️⃣ Add Nodes
# ---------------------------

graph.add_node("generate_outline", generate_outline)
graph.add_node("write_article", write_article)


# ---------------------------
# 6️⃣ Define Flow (Edges)
# ---------------------------

graph.set_entry_point("generate_outline")

graph.add_edge("generate_outline", "write_article")

graph.add_edge("write_article", END)


# ---------------------------
# 7️⃣ Compile Graph
# ---------------------------

app = graph.compile()


# ---------------------------
# 8️⃣ Run Workflow
# ---------------------------

result = app.invoke(
    {
        "topic": "LangGraph",
        "outline": "",
        "article": ""
    }
)

print("\n🎯 FINAL RESULT\n")

print(result)

print(app.get_graph().draw_mermaid())