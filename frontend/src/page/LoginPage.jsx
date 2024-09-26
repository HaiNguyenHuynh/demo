import { useMutation } from "@tanstack/react-query";
import React, { useState } from "react";
import { apiLogin } from "../api/services";
import { Link, useNavigate } from "react-router-dom";
import { useLocalStorage } from "../hooks/LocalStorage";
import logoFacebook from "../assets/logo-facebook.png";

export default function LoginPage() {
  const [, setCredentials] = useLocalStorage("credentials", null);
  const navigate = useNavigate();
  const [username, setUsername] = useState();
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();
  const [credentials] = useLocalStorage("credentials");
  if (credentials) {
    navigate("/");
  }
  const { mutate, isLoading } = useMutation({
    mutationKey: "addUser",
    mutationFn: () => apiLogin({ username, email, password }),
    onSuccess: (data) => {
      setCredentials(data.key);
      navigate("/");
    },
    onError: (error) => {
      alert("Login failed");
    },
  });
  const handleSubmit = (e) => {
    e.preventDefault();
    mutate();
  };
  return (
    <div>
      <div className="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
            Sign in to your account
          </h2>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <form
            className="space-y-6"
            action="#"
            method="POST"
            onSubmit={(e) => handleSubmit(e)}
          >
            <div>
              <label
                htmlFor="email"
                className="block text-sm font-medium leading-6 text-gray-900"
              >
                Username
              </label>
              <div className="mt-2">
                <input
                  onChange={(e) => setUsername(e.target.value)}
                  id="userName"
                  name="userName"
                  required
                  className="px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <label
                htmlFor="email"
                className="block text-sm font-medium leading-6 text-gray-900"
              >
                Email address
              </label>
              <div className="mt-2">
                <input
                  onChange={(e) => setEmail(e.target.value)}
                  id="email"
                  name="email"
                  type="email"
                  required
                  className="px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label
                  htmlFor="password"
                  className="block text-sm font-medium leading-6 text-gray-900"
                >
                  Password
                </label>
              </div>
              <div className="mt-2">
                <input
                  id="password"
                  name="password"
                  type="password"
                  required
                  onChange={(e) => setPassword(e.target.value)}
                  className="px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400  sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <button
                type="submit"
                className="flex w-full justify-center rounded-md bg-[#1773fb] px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Sign in
              </button>
            </div>

            <div className="flex justify-center text gap-1">
              Don't have an account?
              <Link
                className="hover:underline  text-[#1773fb]"
                to={"/register"}
              >
                Sign up
              </Link>
            </div>
          </form>

          <div className="flex justify-center flex-col items-center mt-6 gap-2">
            <div className="relative w-full flex justify-center before:z-[1] before:absolute before:w-full before:border-t before:border-gray-300 before:border-dashed before:top-1/2">
              <p className="bg-white px-2 relative z-10"> Or </p>
            </div>
            <a href="/saml2/login" className="flex items-center px-3 py-2 gap-2 rounded-md bg-[#1773fb] text-white font-medium w-full justify-center">
              {/* <img
                src={logoFacebook}
                alt="logoFB"
                className="w-5 h-5  brightness-[1000]"
              /> */}
              <p className="uppercase text-sm">Sign In with SSO</p>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
