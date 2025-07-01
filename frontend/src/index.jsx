import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';

function Login({ onLoggedIn }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ username, password }),
      });
      if (!response.ok) throw new Error('Login failed');
      const data = await response.json();
      localStorage.setItem('token', data.access_token);
      onLoggedIn();
    } catch (err) {
      setError('Credenciales incorrectas');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Iniciar sesión</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div>
        <input
          type="text"
          placeholder="Usuario"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>
      <div>
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <button type="submit">Entrar</button>
    </form>
  );
}

function App() {
  const [loggedIn, setLoggedIn] = useState(!!localStorage.getItem('token'));

  return (
    <div>
      {loggedIn ? (
        <h1>Studio Tokens Dashboard</h1>
      ) : (
        <Login onLoggedIn={() => setLoggedIn(true)} />
      )}
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
