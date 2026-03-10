const API_BASE = "http://localhost:8000";

export async function login(username) {
  const res = await fetch(`${API_BASE}/auth/login?username=${username}`, {
    method: "POST",
  });

  if (!res.ok) {
    throw new Error("Login failed");
  }

  return res.json();
}

export async function sendMessage(message, token) {
  const res = await fetch(`${API_BASE}/chat/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ message }),
  });

  if (!res.ok) {
    throw new Error("Chat failed");
  }

  return res.json();
}
