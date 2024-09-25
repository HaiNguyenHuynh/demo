import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header>
      <div className="flex justify-center items-center gap-10 pt-5">
        <Link to="/login" className="text-xl font-semibold">
          Log in
        </Link>
      </div>
    </header>
  );
}
