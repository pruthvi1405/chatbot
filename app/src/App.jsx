import { useState } from 'react';
import axios from 'axios';
import './App.css';
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';
import { MainContainer, ChatContainer, MessageList, Message, MessageInput, TypingIndicator } from '@chatscope/chat-ui-kit-react';

function App() {
  const [typing, setTyping] = useState(false);

  const [messages, setMessages] = useState([
    {
      message: "Hello, I am your TravelAgent",
      sender: "ChatGPT",
      direction: "incoming"
    }
  ]);

  const handleSend = async (message) => {
    const newMessage = {
      message: message,
      sender: "user",
      direction: "outgoing"
    };
    const newMessages = [...messages, newMessage];
    setMessages(newMessages);
    setTyping(true);
    await processMessageToChatGPT(newMessages);
  };

  async function processMessageToChatGPT(chatMessages) {
    let apiMessages = chatMessages.map((messageObject) => {
      let role = messageObject.sender === "ChatGPT" ? "assistant" : "user";
      return { role: role, content: messageObject.message };
    });

    const systemMessage = {
      role: "system",
      content: "Speak like a travel agent"
    };

    const apiRequestBody = {
      model: "gpt-3.5-turbo",
      messages: [
        systemMessage,
        ...apiMessages
      ]
    };

    axios.post('http://localhost:5001/chat', {
      messages: apiRequestBody.messages
    })
    .then(response => {
      const chatGPTMessage = response.data.at(-1).content;
      setMessages([...chatMessages, {
        message: chatGPTMessage,
        sender: "ChatGPT",
        direction: "incoming"
      }]);
      setTyping(false);
    })
    .catch(error => {
      console.error("Error fetching response from Flask backend:", error);
      setTyping(false);
    });
  }

  return (
    <div style={{ position: "relative", height: "800px", width: "700px" }}>
      <MainContainer>
        <ChatContainer>
          <MessageList typingIndicator={typing ? <TypingIndicator content="ChatGPT is typing.." /> : null }>
            {messages.map((message, i) => (
              <Message key={i} model={message} />
            ))}
          </MessageList>
          <MessageInput placeholder="Type message here" onSend={handleSend} />
        </ChatContainer>
      </MainContainer>
    </div>
  );
}

export default App;
