import { useState } from "react";
import { sendMessage } from "./api";

function Chat() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);

  async function handleSend() {
    if (!message.trim()) return;

    const res = await sendMessage(message);

    setMessages([
      ...messages,
      { from: "You", text: message },
      { from: "Bot", text: res.reply },
    ]);

    setMessage("");
  }

  return (
    <div>
      <h2>HR Chat</h2>

      <div>
        {messages.map((m, i) => (
          <p key={i}>
            <b>{m.from}:</b> {m.text}
          </p>
        ))}
      </div>

      <input
        placeholder="Ask HR..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default Chat;
