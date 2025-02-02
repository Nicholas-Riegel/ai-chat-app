import { useState } from 'react'
import './App.css'

function App() {

  const [aiResponse, setAiResponse] = useState('');

  const sendMessage = async () => {

    let input = document.getElementById('text-area').value;

    const response = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ input }),
    });
    
    input = '';

    const data = await response.json();
    setAiResponse(data.response);
  };
  

  return (
    <>
      <h1>Chat App</h1>
      <div id="chat-container">{aiResponse}</div>
      <textarea id="text-area" placeholder="Type your message here..."></textarea>
      <div id="btn-div">
        <button onClick={sendMessage}>Send</button>
      </div>
    </>
  )
}

export default App