import React from "react";
import { Link } from "react-router-dom";
import { useCookies } from "react-cookie";

export default function Header() {
  const [cookies] = useCookies();

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
          {!cookies.role ? (
            <Link to="/login" className="">
              Log in
            </Link>
          ) : (
            <a href="/api/logout">Log out</a>
          )}
        </div>
      </div>
    </header>
  );
}
