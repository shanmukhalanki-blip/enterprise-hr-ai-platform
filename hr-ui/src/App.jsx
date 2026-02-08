import { useState } from "react";
import Login from "./Login";
import Chat from "./Chat";

function App() {
  const [token, setToken] = useState(
    localStorage.getItem("token")
  );

  function handleLogin(token) {
    localStorage.setItem("token", token);
    setToken(token);
  }

  function handleLogout() {
    localStorage.removeItem("token");
    setToken(null);
  }

  if (!token) {
    return <Login onLogin={handleLogin} />;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Internal HR Chatbot</h2>

      <button
        onClick={handleLogout}
        style={{
          float: "right",
          background: "#dc3545",
          color: "white",
          border: "none",
          padding: "8px 12px",
          cursor: "pointer",
        }}
      >
        Logout
      </button>

      <Chat token={token} />
    </div>
  );
}

export default App;
