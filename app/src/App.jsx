import { useState } from 'react';
import './App.css';
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';
import { MainContainer, ChatContainer, MessageList, Message, MessageInput, TypingIndicator } from '@chatscope/chat-ui-kit-react';

function App() {
  const [typing, setTyping] = useState(false);
  const [messages, setMessages] = useState([
    {
      message: "Hello, I am ChatGPT",
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

    setMessages(prevMessages => [...prevMessages, newMessage]);
    setTyping(true);

    // Simulating a response delay
    setTimeout(() => {
      const chatGPTMessage = {
        message: "This is a response from ChatGPT.",
        sender: "ChatGPT",
        direction: "incoming"
      };
      setMessages(prevMessages => [...prevMessages, chatGPTMessage]);
      setTyping(false); // Set typing indicator to false after receiving a response
    }, 10000);
  };

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
