import { Link } from "react-router-dom";
import { useLocation } from "react-router-dom";

type NavbarLinkProps = {
  label: string;
  path: string;
};

function NavbarLink({ label, path, ...props }: NavbarLinkProps) {
  const location = useLocation();
  const active = location.pathname === path;
  return (
    <Link
      {...props}
      to={path}
      className={` ${active ? "border-secondaryTextColor hover:border-primaryTextColor dark:border-secondaryTextColor-dark dark:hover:border-primaryTextColor-dark border-b-2 transition-colors" : ""} `}
    >
      {label}
    </Link>
  );
}

export default NavbarLink;
