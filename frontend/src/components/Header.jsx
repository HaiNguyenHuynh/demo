import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { useLocalStorage } from "../hooks/LocalStorage";

export default function Header() {
  const navigate = useNavigate();
  const [credentials] = useLocalStorage("credentials");
  const handleLogout = () => {
    localStorage.removeItem("credentials");
    navigate("/login");
  };

  return (
    <header className="max-w-[720px] m-auto py-5">
      <div className="flex justify-between">
        <p className="font-medium">SkyAuth</p>
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
