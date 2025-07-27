import NavbarLink from "./NavbarLink";
function Navbar() {
  return (
    <nav className="bg-primaryColor dark:bg-primaryColor-dark mt-2 mb-5 flex rounded-2xl px-5 py-4 shadow-md">
      <div className="container mx-auto">
        <h1 className="mb-3 text-2xl">Twitch Watchdog</h1>
        <ul className="flex space-x-5 border-t-1 p-1">
          <li>
            <NavbarLink path="/" label="Home" />
          </li>
          <li>
            <NavbarLink path="/login" label="Login" />
          </li>
          <li>
            <NavbarLink path="/nopage" label="Nopage" />
          </li>
          <li>
            <NavbarLink path="/about" label="About" />
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
