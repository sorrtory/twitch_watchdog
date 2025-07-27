import { Route, Routes } from "react-router-dom";

import Login from "./pages/Login";
import NotFound from "./pages/NotFound";
import Navbar from "./components/Navbar";

function App() {
  return (
    <div className="min-h-screen grid">
      <main>
        <Routes>
          <Route path="/" element={<Navbar />} />
          <Route
            path="/about"
            element={
              <div className="text-3xl font-bold underline">About page</div>
            }
          />
          <Route
            path="/contact"
            element={
              <div className="text-3xl font-bold underline">Contact page</div>
            }
          />
          <Route path="/login" element={<Login />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
