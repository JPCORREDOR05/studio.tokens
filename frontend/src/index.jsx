import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import './styles.css';

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
    <form onSubmit={handleSubmit} className="container">
      <h2>Iniciar sesión</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <input
        type="text"
        placeholder="Usuario"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type="submit">Entrar</button>
    </form>
  );
}

function Dashboard({ onLogout }) {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    fetch('http://localhost:8000/reports/summary', {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then(setSummary)
      .catch(() => setSummary(null));
  }, []);

  if (!summary) return <p className="container">Cargando...</p>;

  return (
    <div className="container">
      <h2>Resumen</h2>
      <ul>
        {summary.models.map((m) => (
          <li key={m.model_id}>
            {m.name}: {m.tokens} tokens – USD {m.usd.toFixed(2)} – COP{' '}
            {m.cop.toFixed(0)}
          </li>
        ))}
      </ul>
      <p>Total USD: {summary.total_usd.toFixed(2)}</p>
      <p>Total COP: {summary.total_cop.toFixed(0)}</p>
      <button onClick={onLogout}>Cerrar sesión</button>
    </div>
  );
}

function App() {
  const [loggedIn, setLoggedIn] = useState(!!localStorage.getItem('token'));

  const handleLogout = () => {
    localStorage.removeItem('token');
    setLoggedIn(false);
  };

  return (
    <div>
      <header>
        <h1>Studio Tokens</h1>
      </header>
      {loggedIn ? (
        <Dashboard onLogout={handleLogout} />
      ) : (
        <Login onLoggedIn={() => setLoggedIn(true)} />
      )}
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
