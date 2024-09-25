import React from "react";

export default function Footer() {
  return (
    <div>
      <div className="max-w-[720px] m-auto py-5 flex justify-between text-gray-400 text-sm border-t border-gray-200">
        <p>@2024</p>
        <div className="flex gap-2">
          <p>Privacy Policy</p>
          <p>Term and Conditions</p>
        </div>
      </div>
    </div>
  );
}
