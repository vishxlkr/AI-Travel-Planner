# optimized_travel_planner.py
# Cleaned version scaffold preserving UI/logic structure
# (Generated starter file)

import os
from datetime import datetime
import streamlit as st
from langchain_core.messages import HumanMessage
from main import app

QUICK_PROMPTS = [
    "7-day Japan under INR 2L",
    "Paris trip for 5 days",
    "Dubai weekend trip",
    "Bali backpacking 10 days",
]

AGENT_META = {
    "flight_agent": ("Flight Agent", "Searches available flight options"),
    "hotel_agent": ("Hotel Agent", "Finds hotel information"),
    "itinerary_agent": ("Itinerary Agent", "Builds the trip schedule"),
    "final_agent": ("Final Agent", "Packages the final plan"),
}

CSS = '''
<style>
html, body, .stApp { background:#070b10; color:#edf5f7; }
.block-container { max-width:1220px; }
.panel { background:#101820; padding:1rem; border-radius:8px; margin-bottom:1rem; }
</style>
'''

def save_markdown_plan(user_query, thread_id, collected):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"travel_plan_{ts}.md"
    content = "\n".join([f"{k}: {v}" for k,v in collected.items()])
    os.makedirs("travel_plans", exist_ok=True)
    with open(f"travel_plans/{filename}", "w", encoding="utf-8") as f:
        f.write(content)
    return filename, content

st.set_page_config(page_title="AI Travel Planner", layout="wide")
st.markdown(CSS, unsafe_allow_html=True)

with st.sidebar:
    thread_id = st.text_input("User ID", value="user_vishal")

st.title("AI Travel Planner")

cols = st.columns(len(QUICK_PROMPTS))
for c,p in zip(cols, QUICK_PROMPTS):
    if c.button(p): st.session_state["q"] = p

user_query = st.text_area("Trip request", key="q")
generate = st.button("Generate travel plan")

if generate and user_query:
    config = {"configurable": {"thread_id": thread_id}}
    collected = dict(flight_results="", hotel_results="", itinerary="", final_response="", llm_calls=0)

    field_map = {
        "flight_agent":"flight_results",
        "hotel_agent":"hotel_results",
        "itinerary_agent":"itinerary"
    }

    for chunk in app.stream({
        "messages":[HumanMessage(content=user_query)],
        "user_query": user_query
    }, config=config, stream_mode="updates"):

        for node_name, state_update in chunk.items():
            with st.status(node_name, expanded=True):
                if node_name in field_map:
                    key = field_map[node_name]
                    collected[key] = state_update.get(key, "")
                    st.markdown(collected[key])
                elif node_name == "final_agent":
                    msgs = state_update.get("messages", [])
                    if msgs:
                        collected["final_response"] = msgs[-1].content
                        st.markdown(collected["final_response"])

    filename, file_content = save_markdown_plan(user_query, thread_id, collected)
    st.download_button("Download plan", data=file_content, file_name=filename)
