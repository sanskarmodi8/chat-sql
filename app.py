import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
import os

#get the groq api key
load_dotenv()
key = os.getenv('GROQ_API_KEY')

st.set_page_config(page_title="Chat with SQL DB", page_icon="🦜")
st.title("🦜 Chat with SQL DB")

# Display a warning about SQL injection
st.warning(" ⚠️ Be cautious of SQL injection risks when interacting with databases.")

mysql_host = st.sidebar.text_input("Provide MySQL Host")
mysql_user = st.sidebar.text_input("MySQL User")
mysql_password = st.sidebar.text_input("MySQL password", type="password")
mysql_db = st.sidebar.text_input("MySQL Database")

#llm
llm = ChatGroq(groq_api_key = key, model_name="Llama3-8b-8192", streaming=True)

def configure_db(host=None, user=None, password=None, db=None):
	if not (host and user and password and db):
		st.error("Please provide all MySQL connection details.")
		st.stop()
	return SQLDatabase(create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{db}"))

#configure db
try:
	db = configure_db(mysql_host, mysql_user, mysql_password, mysql_db)
except Exception as e:
	st.error("If you are using localhost as Host then you need to install the application and run on your local machine")
	st.error(e)

#toolkit
toolkit = SQLDatabaseToolkit(db=db,llm=llm)

agent = create_sql_agent(
	llm=llm,
	toolkit=toolkit,
	verbose=True,
	agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
	handle_parsing_errors=True
)

if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
	st.session_state["messages"]=[{"role":"assistant", "content":"How can I help you?"}]

for msg in st.session_state.messages:
	st.chat_message(msg["role"]).write(msg["content"])

if query:=st.chat_input(placeholder="Ask anything from the database"):
	st.session_state.messages.append({"role":"user", "content":query})
	st.chat_message("user").write(query)
	with st.chat_message("assistant"):
#		display the thinking of the agent
#		st_cb = StreamlitCallbackHandler(st.container())
#		res = agent.run(query, callbacks=[st_cb])
		res = agent.run(query)
		st.session_state.messages.append({"role":"assistant", "content":res})
		st.write(res)


