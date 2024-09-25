import React from "react";
import imageMountain from "../assets/mountain.jpg";
import img1 from "../assets/img1.jpg";
import img2 from "../assets/img2.jpg";
import img3 from "../assets/img3.jpg";
import img4 from "../assets/img4.jpg";

const dataBlog = [
  {
    img: img1,
    title:
      "Living Light: The Minimalist Lifestyle and its Environmental Impact",
    date: "2 Feb, 2024",
  },
  {
    img: img2,
    title: "Elevation Your Style with Minimal Environmental Footprint",
    date: "2 Feb, 2024",
  },
  {
    img: img3,
    title:
      "Designing Tranquility: How Minimalist Spaces Support Eco-Friendly Living",
    date: "2 Feb, 2024",
  },
  {
    img: img4,
    title: "Wander Wisely: Sustainable Travel Tips for the Minimalist Explore",
    date: "2 Feb, 2024",
  },
];
export default function LandingPageNew() {
  return (
    <div className="py-10">
      <div className="max-w-[720px] m-auto">
        <div className="flex justify-center flex-col items-center">
          <p className="text-4xl">
            Starter - a Minimalist <br /> Personal Blog Template.
          </p>
          <br />
          <p className="font-light">
            "Starter" is a, well stater theme designed by ... for Ghost <br />{" "}
            (CMS), 11tr, enhance, astro and many other site generators
          </p>
          <br />
        </div>
        <div className="flex flex-col gap-2 justify-center items-center">
          <img src={imageMountain} alt="" className="rounded-lg" />
          <p className="italic text-gray-400 text-sm">Exploring the mountain</p>
        </div>

        <div className="flex flex-col gap-5 w-[80%] m-auto">
          <div className="mb-5 mt-10 text-lg">Recent Publication</div>

          {dataBlog.map((val, index) => (
            <div key={index} className="flex justify-between gap-5">
              <div className="flex flex-col gap-2">
                <div>
                  <p className="text-gray-600 text-xs">{val.date}</p>
                </div>
                <p className="text-base cursor-pointer">{val.title}</p>
              </div>
              <div>
                <img
                  src={val.img}
                  className="h-[100px] min-w-[200px] object-cover rounded-lg cursor-pointer"
                />
              </div>
            </div>
          ))}
          <button className="px-20 py-1 rounded-xl bg-slate-100 w-fit self-center mt-10">
            View More
          </button>
        </div>
      </div>
    </div>
  );
}
