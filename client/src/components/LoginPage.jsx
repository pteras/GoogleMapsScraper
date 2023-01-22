import React, { useState } from "react";
import httpClient from "../httpClient";

export const LoginPage = () => {
  const [username, setUsername] = useState([""]);
  const [password, setPasswords] = useState([""]);

  const logInUser = async () => {
    console.log(username, password);

    try {
      const response = await httpClient.post("//localhost:5000/login", {
        username,
        password,
      });
      console.log(response);
      window.location.href = "/";
    } catch (err) {
      if (err.response.status === 401) {
        alert("Invalid credentials");
      }
    }
  };

  return (
    <div className="form_login">
      <div className="title">Authentication</div>
      <div className="subtitle">Continue by logging in:</div>
      <form>
        <div className="input-container">
          <label className="placeholder">
            <strong>Username:</strong>
          </label>
          <input
            className="input"
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            id=""
          />
        </div>
        <div className="input-container">
          <label className="placeholder">
            <strong>Password:</strong>
          </label>
          <input
            className="input"
            type="password"
            value={password}
            onChange={(e) => setPasswords(e.target.value)}
            id=""
          />
        </div>
        <button type="button" className="button" onClick={() => logInUser()}>
          <strong>Log In</strong>
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
