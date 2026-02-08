import { useState } from "react";
import { login } from "./api";

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [error, setError] = useState("");

  async function handleLogin() {
    try {
      const res = await login(username);

      // ✅ THIS IS THE KEY LINE
      onLogin(res.access_token);
    } catch (err) {
      setError("Login failed");
    }
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Login</h2>

      <input
        placeholder="Enter username (emp001)"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <button onClick={handleLogin}>Login</button>

      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}

export default Login;
