import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { useCookies } from "react-cookie";
import { apiLogout } from "../api/services";
import { useMutation } from "@tanstack/react-query";

export default function Header() {
  const navigate = useNavigate();
  const [cookies] = useCookies();
  const { mutate, isLoading } = useMutation({
    mutationKey: "logout",
    mutationFn: () => apiLogout(),
    onSuccess: () => {
      navigate("/login");
    },
  });

  const handleLogout = () => {
    mutate();
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
          {!cookies.role ? (
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
