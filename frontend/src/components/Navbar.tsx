import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-primaryColor p-5 pb-0 shadow-md rounded-2xl mx-2 md:mx-10 mt-2">
      <div className="container mx-auto text-primaryTextColor">
        <h1 className="text-2xl mb-3">Twitch Watchdog</h1>
        <ul className="flex space-x-5 p-1">
          <li>
            <Link
              to="/"
              className="border-secondaryColor border-b-2 hover:border-primaryTextColor transition-colors"
            >
              Home
            </Link>
          </li>
          <li>
            <Link to="/login" className="">
              Login
            </Link>
          </li>
          <li>
            <Link to="/nopage" className="">
              Nopage
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
