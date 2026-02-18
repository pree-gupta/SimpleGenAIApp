from langchain.memory import ConversationBufferMemory

## Make the tutor feel aware and continuous, not stateless.

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
