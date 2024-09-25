import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="max-w-[720px] m-auto py-5">
      <div className="flex justify-between">
        <p className="font-medium">Starter</p>
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
          <Link to="/login" className="">
            Log in
          </Link>
        </div>
      </div>
    </header>
  );
}
