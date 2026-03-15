from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage



load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.title("Lesson21 提出課題: LLM機能を搭載したWebアプリ")

st.write("##### 専門家を選んでください。")
st.write("質問の内容に応じて、以下から専門家の種類を選択してください。")

selected_item = st.radio(
    "専門家の種類を選択してください。",
    ["ファッション", "ダイエット"]
)

st.write("##### 質問内容を入力してください。")
input_message = st.text_input(label="質問内容を入力してください。")

st.divider()


if st.button("実行") and selected_item == "ファッション":
    messages = [
    SystemMessage(content="You are an outstanding fashion expert."),
    HumanMessage(content=input_message),
    ]
    result = llm(messages)
    st.divider()
    st.write(f"ファッション専門家の回答: {result.content}")

elif st.button("実行") and selected_item == "ダイエット":
    messages = [
    SystemMessage(content="You are an outstanding diet expert."),
    HumanMessage(content=input_message),
    ]
    result = llm(messages)
    st.divider()
    st.write(f"ダイエット専門家の回答: {result.content}")

