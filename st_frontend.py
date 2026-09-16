import streamlit as st
from lg_backend import chatbot
from langchain_core.messages import HumanMessage,ai_message,Tool_Message
import uuid
import datetime



#*********************************************utility fun
st.set_page_config(page_title="langraphchatbot",layout="centered")


def generate_thread_id():
    if 'chat_count' not in st.session_state:
        st.session_state['chat_count'] = 0
    st.session_state['chat_count'] += 1
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    thread_id = f"Chat No.{st.session_state['chat_count']} - {timestamp}"
    return thread_id

def reset_chat():
    thread_id=generate_thread_id()
    st.session_state['thread_id']=thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history']=[]
 

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)


def load_conversation(thread_id):
    return chatbot.get_state(config={'configurable': {'thread_id':thread_id}}).values['messages']
    
       
def delete_thread(thread_id):
    if thread_id in
    st.session_state['chat_threads']:
    st.session_state['chat_threads'].remove(thread_id)
    if thread_id in st.session_state['chat_tittles']:
        del st.session_state['chat_tittles']
        [thread_id]

def update(thread_id,user_input):
    if st.session_state['chat tittle'].get(thread_id,"NEW CHAT")=="NEW CHAT":
        st.session_state['chat tittles'][thread_id]=user_input[:30]+("..."if len(user_input)>30 else "")


def filter_threads(search_query):
    if not in search_query:
        return st.session_state['chat_threads']
        return [
            tid for tid in
            st.session_state['chat threads']
            if search_query.lower() in
            st.session_state['chat titles'].get(tid,tid).lower()
                or search_query.lower()
                or search_query.lower() in tid.lower()

        ]

    




# st.session_state -> dict -> 
#*********************************************session setup


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []
    add_thread(st.session_state['thread_id'])

if 'chat_tittles' not in st.session_state:
    st.session_state['chat_threads'] = retrive_all_threads() or []

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []
    add_thread(st.session_state['thread_id'])

#**********************************************side bar
st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

if st.sidedar.button('all conversations'):
    load_conversation()

 if st.sidebar.button('delete chats'):
    delete_thread()

if st.sidebar.button('update chats'):
    update()
st.sidebar.header("My conversations")

if st.sidebar.button('NEW CHAT'):
    reset_chat()
    st.rerun()

    search_query=st,sidebar.text_input("search chats",placeholder="type keyword...")

filter_threads=[
    tid for tid in st.session_state['chat_threads']
    if not search_query or search_query.lower() in st.session_state['chat tittles'].get(tid,tid).lower() or search_query.lower() in tid.lower
]

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])



user_input = st.chat_input('seach chat')
if user_input==st.search_query('search chat')
filter_threads()




for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id']=thread_id
        messages=load_conversation(thread_id)

        temp_msg=[]

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_msg.append({'role':role,'content':msg.content})

        st.session_state['message_history']=temp_msg

# loading the conversation history

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])



user_input = st.chat_input('Type here')

if user_input:
# first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
    
    ai_message = response['messages'][-1].content
    # first add the message to message_history
    
    with st.chat_message('assistant'):
        ai_msg=st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]}, 
                CONFIG,
                stream_mode='messages'
            )

        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_msg})