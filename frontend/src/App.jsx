import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [message, setMessage] = useState("");

  const [mode, setMode] = useState("fast");

  const [chatType, setChatType] = useState("chat");

  const [messages, setMessages] = useState(() => {

    const saved = localStorage.getItem(
      "chat_history"
    );

    return saved
      ? JSON.parse(saved)
      : [];

  });

  const [pdfFile, setPdfFile] = useState(null);
  const [imageFile, setImageFile] = useState(null);

  useEffect(() => {

    localStorage.setItem(
      "chat_history",
      JSON.stringify(messages)
    );

  }, [messages]);

  const uploadPDF = async () => {

    if (!pdfFile) return;

    const formData = new FormData();

    formData.append(
      "file",
      pdfFile
    );

    await axios.post(
      "http://127.0.0.1:8000/upload",
      formData
    );

    alert("PDF Uploaded");
  };

  const analyzeImage = async () => {

    if (!imageFile) return;

    const userMessage = {
      type: "user",
      text: `[IMAGE] ${message}`
    };

    setMessages(prev => [
      ...prev,
      userMessage
    ]);

    const formData = new FormData();

    formData.append(
      "file",
      imageFile
    );

    formData.append(
      "question",
      message || "Describe this image"
    );

    const response = await axios.post(
      "http://127.0.0.1:8000/vision",
      formData
    );

    const aiMessage = {
      type: "ai",
      text: response.data.answer
    };

    setMessages(prev => [
      ...prev,
      aiMessage
    ]);

    setMessage("");
  };

  const solveMath = async () => {

    if (!message) return;

    const userMessage = {
      type: "user",
      text: `[MATH] ${message}`
    };

    setMessages(prev => [
      ...prev,
      userMessage
    ]);

    const response = await axios.post(
      "http://127.0.0.1:8000/math/solve",
      {
        expression: message
      }
    );

    const aiMessage = {
      type: "ai",
      text: response.data.answer
    };

    setMessages(prev => [
      ...prev,
      aiMessage
    ]);

    setMessage("");
  };

  const sendMessage = async () => {

    if (!message) return;

    const userMessage = {
      type: "user",
      text: message
    };

    setMessages(prev => [
      ...prev,
      userMessage
    ]);

    const response = await axios.post(
      "http://127.0.0.1:8000/chat",
      {
        message: message,
        mode: mode,
        use_pdf: chatType === "pdf"
      }
    );

    const aiMessage = {
      type: "ai",
      text: response.data.answer
    };

    setMessages(prev => [
      ...prev,
      aiMessage
    ]);

    setMessage("");
  };

  const clearChats = () => {

    localStorage.removeItem(
      "chat_history"
    );

    setMessages([]);
  };

  return (

    <div className="app">

      <div className="sidebar">

        <h2>Study AI</h2>

        <h4>Assistant Mode</h4>

        <select
          value={chatType}
          onChange={(e) =>
            setChatType(e.target.value)
          }
        >

          <option value="chat">
            💬 Chat
          </option>

          <option value="pdf">
            📄 PDF
          </option>

        </select>

        <br />

        <h4>Model</h4>

        <select
          value={mode}
          onChange={(e) =>
            setMode(e.target.value)
          }
        >
          <option value="fast">
            ⚡ Fast
          </option>

          <option value="deep">
            🧠 Deep
          </option>

          <option value="auto">
            🤖 Auto
          </option>

        </select>

        <br />

        <h4>PDF</h4>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) =>
            setPdfFile(
              e.target.files[0]
            )
          }
        />

        <button
          onClick={uploadPDF}
        >
          Upload PDF
        </button>

        <hr />

        <h4>Images</h4>

        <input
          type="file"
          accept="image/*"
          onChange={(e) =>
            setImageFile(
              e.target.files[0]
            )
          }
        />

        <button
          onClick={analyzeImage}
        >
          Analyze Image
        </button>

        <hr />

        <button
          onClick={solveMath}
        >
          Solve Math
        </button>

        <button
          onClick={clearChats}
        >
          Clear Chats
        </button>

      </div>

      <div className="main">

        <div className="header">
          AI Study Assistant
        </div>

        <div className="chat-area">

          {messages.map(
            (msg, index) => (

            <div
              key={index}
              className={`message ${msg.type}`}
            >
              {msg.text}
            </div>

          ))}

        </div>

        <div className="input-area">

          <input
            value={message}
            onChange={(e) =>
              setMessage(
                e.target.value
              )
            }
            placeholder="Ask anything..."
          />

          <button
            onClick={sendMessage}
          >
            Send
          </button>

        </div>

      </div>

    </div>

  );
}

export default App;