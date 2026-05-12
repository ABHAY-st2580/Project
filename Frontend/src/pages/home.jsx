import React from "react";
import tileImg from "../assets/tileimage2.jpg";
import bgImg from "../assets/tileimage3.jpg";


function Home({ setCurrentPage }) {
  const token = localStorage.getItem("token");

  return (
    <div className="text-white font-light">

      {/* HERO SECTION */}

      <section className="min-h-[80vh] flex items-center justify-center px-6 bg-gradient-to-b from-[#0f172a] to-[#1e293b]">

        <div className="grid md:grid-cols-2 gap-8 items-center max-w-6xl w-full">

          {/* LEFT TEXT */}
          <div className="text-center md:text-left">
            <h1 className="text-3xl md:text-4xl font-semibold mb-4">
              Manage Your Tile Business Smartly
            </h1>

            <p className="text-gray-300 mb-6">
              Track stock, manage sales, monitor low inventory and grow your tile shop efficiently with TileTracker.
            </p>

            <button
              onClick={() => setCurrentPage(token ? "dashboard" : "login")}
              className="bg-blue-600 px-6 py-2 rounded-lg hover:bg-blue-700"
            >
              {token ? "Go to Dashboard" : "Get Started"}
            </button>
          </div>

          {/* RIGHT IMAGE */}
          <div className="flex justify-center">
            <img
              src={tileImg}
              alt="Tiles"
              className="w-64 md:w-80 rounded-lg shadow-lg"
            />
          </div>

        </div>

      </section>
      <hr className="border-gray-700 my-2" />
      {/* 🔥 FEATURES */}
      <section className="py-16 px-6 bg-[#020617]">
        <h2 className="text-3xl font-light text-center mb-10">
          <b>Key Features</b>
        </h2>

        <div className="grid md:grid-cols-3 gap-6 max-w-6xl mx-auto">

          <div className="bg-[#0f172a] p-6 rounded-xl shadow-md">
            <h3 className="text-xl font-semibold mb-2">Stock Management</h3>
            <p className="text-gray-400 text-sm">
              Add, update and track tile inventory in real-time.
            </p>
          </div>

          <div className="bg-[#0f172a] p-6 rounded-xl shadow-md">
            <h3 className="text-xl font-semibold mb-2">Sales Tracking</h3>
            <p className="text-gray-400 text-sm">
              Record multiple tile sales and maintain transaction history.
            </p>
          </div>

          <div className="bg-[#0f172a] p-6 rounded-xl shadow-md">
            <h3 className="text-xl font-semibold mb-2">Low Stock Alerts</h3>
            <p className="text-gray-400 text-sm">
              Instantly know which tiles are running low.
            </p>
          </div>
          <div className="bg-[#0f172a] p-6 rounded-xl shadow-md center col-span-3">
            <h3 className="text-xl font-semibold mb-2">Grow Your Business</h3>
            <p className="text-gray-400 text-sm">
              Use insights to optimize your inventory and boost sales.
              Check the combination of tiles that are selling the most and focus on them to increase your revenue.
            </p>
          </div>
        </div>
      </section>
      <hr className="border-gray-700 my-2" />
      {/* 🔥 HOW IT WORKS */}
      <section className="py-16 px-6 bg-[#020617]">
        <h2 className="text-3xl font-light text-center mb-10">
          <b>How It Works</b>
        </h2>

        <div className="grid md:grid-cols-3 gap-6 max-w-6xl mx-auto text-center">

          <div className="bg-[#0f172a] p-6 rounded-xl shadow-md">
            <h3 className="text-xl font-semibold mb-2">1. Register</h3>
            <p className="text-gray-400 text-sm">
              Create your shop account.
            </p>
          </div>

          <div className="bg-[#0f172a] p-6 rounded-xl shadow-md">
            <h3 className="text-xl font-semibold mb-2">2. Add Tiles</h3>
            <p className="text-gray-400 text-sm">
              Upload your tile inventory.
            </p>
          </div>

          <div className="bg-[#0f172a] p-6 rounded-xl shadow-md">
            <h3 className="text-xl font-semibold mb-2">3. Track Sales</h3>
            <p className="text-gray-400 text-sm">
              Manage and monitor sales easily.
            </p>
          </div>
          
        </div>
        <div className="text-center mt-10">
          <button
            onClick={() => setCurrentPage('manual')}
            className="text-amber-300 hover:text-amber-700"
          >
            View User Manual...
          </button>
        </div>
      </section>
      <hr className="border-gray-700 my-2" />

      <section
        className="py-20 text-center text-white bg-cover bg-center"
        style={{
          backgroundImage: `url(${bgImg})`,
        }}
      >
        {/* Overlay (important for readability) */}
        <div className="bg-black/60 py-16 px-6">

          <h2 className="text-3xl font-semibold mb-6">
            Start Managing Your Tiles Today
          </h2>

          <button
          onClick={() => setCurrentPage(token ? "dashboard" : "login")}
          className="bg-white text-black px-4 py-1 rounded-lg font-light hover:bg-gray-400 transition">
            {token ? "Go to Dashboard" : "Create Account"}
          </button>

        </div>
      </section>
    </div>
  );
}

export default Home;