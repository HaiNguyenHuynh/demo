import React from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";

export default function DefaultLayout({ children }) {
  return (
    <div>
      <Header />
      <div className="min-h-[80vh]">{children}</div>
      <Footer />
    </div>
  );
}
