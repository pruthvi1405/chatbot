import { useState } from 'react';
import './App.css';
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';
import { MainContainer, ChatContainer, MessageList, Message, MessageInput, TypingIndicator } from '@chatscope/chat-ui-kit-react';


function App() {

  const API_KEY="sk-proj-vA5i98x2ighLXuHBS82sT3BlbkFJ3UkqXIhgnp8Tp7GrCtrD";

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
    const newMessages=[...messages,newMessage]
    console.log("newMessages :",newMessages );
    setMessages(newMessages);
    setTyping(true);
    await processMessagetoChatGPT(newMessages)
  };

  async function processMessagetoChatGPT(chatMessages){
      let apiMessage=chatMessages.map((messageObject)=>{
        let role="";
        if (messageObject.sender==="ChatGPT"){
          role="assistant"
        }else{
          role="user"
        }
        return {role:role,content:messageObject.message}
      })

      const systemMessage={
        role:"system",
        content:"Speak like a travel Agent"
      }

      const apiRequestBody={
        "model":"gpt-3.5-turbo",
        "messages":[
          systemMessage,
          ...apiMessage
        ]
      }

      await fetch("https://api.openai.com/v1/chat/completions",{
        method:"POST",
        headers:{
          "Authorization":"Bearer " + API_KEY,
          "Content-Type":"application/json"
        },
        body:JSON.stringify(apiRequestBody)
      }).then((data)=>{
        return data.json();
      }).then((data)=>{
        console.log(data.choices[0].message.content);
        setMessages(
          [...chatMessages,{
            message:data.choices[0].message.content,
            sender:"ChatGPT",
            direction: "incoming"
          }]
        )
        setTyping(false)
      })
  }


  return (
    <div style={{ position: "relative", height: "800px", width: "700px" }}>
      <MainContainer>
        <ChatContainer>
          <MessageList scrollBehavior='smooth' typingIndicator={typing ? <TypingIndicator content="ChatGPT is typing.." /> : null }>
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
