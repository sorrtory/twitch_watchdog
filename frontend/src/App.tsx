import { Route, Routes } from "react-router-dom";

import Login from "./pages/Login";
import NotFound from "./pages/NotFound";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Bots from "./pages/Bots";

function App() {
  return (
    <div className="grid min-h-screen">
      <main className="sm:w-1/2 sm:mx-auto">
        <Routes>
          <Route
            path="/"
            element={
              <div className="container mx-auto px-5">
                <Navbar />
                <Home />
              </div>
            }
          />
          <Route
            path="/bots"
            element={
              <div className="container mx-auto px-5">
                <Navbar />
                <Bots />
              </div>
            }
          />

          <Route
            path="/about"
            element={
              <>
                <Navbar />
                <div className="text-3xl font-bold underline">About page</div>
              </>
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
