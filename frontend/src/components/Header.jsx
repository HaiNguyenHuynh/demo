import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header>
      <div className="flex items-center gap-2 bg-red-500 justify-center">
        <Link
          href="123"
          className="text-gray-800 dark:text-white hover:bg-gray-50 focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 dark:hover:bg-gray-700 focus:outline-none dark:focus:ring-gray-800"
        >
          Log in
        </Link>
        <a
          href="abc"
          className="text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800"
        >
          Get started
        </a>
      </div>
    </header>
  );
}
