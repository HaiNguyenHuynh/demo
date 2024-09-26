import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { useLocalStorage } from "../hooks/LocalStorage";
import { useCookies } from "react-cookie";

export default function Header() {
  const navigate = useNavigate();
  const [credentials] = useLocalStorage("credentials");
  const [cookies, setCookie, removeCookie] = useCookies(["role"]);
  const handleLogout = () => {
    localStorage.removeItem("credentials");
    navigate("/login");
    removeCookie("role");
  };

  return (
    <header className="max-w-[720px] m-auto py-5">
      <div className="flex justify-between">
        <Link to={"/"} className="font-medium">
          SkyAuth
        </Link>
        <div className="flex justify-center items-center gap-5">
          <Link to="#" className="">
            About
          </Link>
          <Link to="#" className="">
            Blog
          </Link>
          <Link to="#" className="">
            Tags
          </Link>
          {!credentials ? (
            <Link to="/login" className="">
              Log in
            </Link>
          ) : (
            <button onClick={() => handleLogout()}>Log out</button>
          )}
        </div>
      </div>
    </header>
  );
}
