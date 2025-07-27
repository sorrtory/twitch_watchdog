import React, { useState } from "react";

const Login: React.FC = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError("abp");
    // Replace with your authentication logic
    if (username === "" || password === "") {
      setError("Please enter both username and password.");
      return;
    }
    // Example: send credentials to backend
    // fetch("/api/login", { ... })
    //   .then(...)
    //   .catch(...)
  };

  return (
    <div className="flex h-screen items-center justify-center">
      <div className="bg-primaryColor dark:bg-primaryColor-dark flex w-80 flex-col items-center justify-center rounded-lg p-4 shadow">
        <h2 className="text-xl font-bold">Login</h2>
        {error && (
          <p className="text-errorColor mb-4 justify-self-start">{error}</p>
        )}
        <form onSubmit={handleSubmit} className="grid justify-items-center">
          <div className="mb-4">
            <label htmlFor="username" className="mb-2 block">
              Username
            </label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="border-secondaryColor focus:border-secondaryTextColor dark:border-secondaryColor-dark dark:focus:border-secondaryTextColor-dark w-full rounded border p-2 outline-none"
              required
            />
          </div>
          <div className="mb-5">
            <label htmlFor="password" className="mb-2 block">
              Password
            </label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="border-secondaryColor focus:border-secondaryTextColor dark:border-secondaryColor-dark dark:focus:border-secondaryTextColor-dark w-full rounded border p-2 outline-none"
              required
            />
          </div>
          <button
            type="submit"
            className="btn-primary w-2/3"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
