const API_BASE = "http://127.0.0.1:8000";

export async function login(username) {
  const res = await fetch(`${API_BASE}/auth/login?username=${username}`, {
    method: "POST",
  });

  if (!res.ok) {
    throw new Error("Login failed");
  }

  return res.json();
}

// 👇 ADD THIS FUNCTION (DO NOT REMOVE login)
export async function sendMessage(message) {
  const token = localStorage.getItem("token");

  const res = await fetch(`${API_BASE}/chat/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`,
    },
    body: JSON.stringify({
      employee_id: "EMP001",
      message,
    }),
  });

  if (!res.ok) {
    throw new Error("Chat failed");
  }

  return res.json();
}
