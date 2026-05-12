import { useState } from "react";

function Navbar({ currentPage, setCurrentPage }) {
  const [menuOpen, setMenuOpen] = useState(false);

  const token = localStorage.getItem("token");
  const username = localStorage.getItem("username");

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("username");
    window.location.reload();
  };

  return (
    <nav className="bg-[#131212] text-white shadow-md font-extralight">
      <div className="max-w-7xl mx-auto px-6 py-2 flex items-center justify-between border-1 border-blue-900">
        <div className="flex items-center gap-2">
          <img
            src="/tileicon.png"
            alt="TileTracker Logo"
            className="w-8 h-8"
          />
          <h1 className="text-2xl font-semibold">TileTracker</h1>
        </div>
        {/* Logo */}


        {/* Menu */}
        <div className="hidden md:flex space-x-8 items-center text-lg">
          {/* HOME */}
          <button
            onClick={() => setCurrentPage("home")}
            className={`transition ${
              currentPage === "home"
                ? "text-blue-400"
                : "hover:text-blue-400"
            }`}
          >
            Home
          </button>

          {/* DASHBOARD */}
          <button
            onClick={() => setCurrentPage("dashboard")}
            className={`transition ${
              currentPage === "dashboard"
                ? "text-blue-400"
                : "hover:text-blue-400"
            }`}
          >
            Dashboard
          </button>
            <button
            onClick={() => setCurrentPage("today")}
            className={`transition ${
              currentPage === "today"
                ? "text-blue-400"
                : "hover:text-blue-400"
            }`}
          >
            Today
          </button>
          {/* TILES */}
          <button
            onClick={() => setCurrentPage("tiles")}
            className={`transition ${
              currentPage === "tiles"
                ? "text-blue-400"
                : "hover:text-blue-400"
            }`}
          >
            Tiles
          </button>

          {/* SALES */}
          <button
            onClick={() => setCurrentPage("sales")}
            className={`transition ${
              currentPage === "sales"
                ? "text-blue-400"
                : "hover:text-blue-400"
            }`}
          >
            Sales
          </button>
          <button
            onClick={() => setCurrentPage("manual")}
            className={`transition ${
              currentPage === "manual"
                ? "text-blue-400"
                : "hover:text-blue-400"
            }`}
          >
            Manual
          </button>

        </div>

        {/* Right Side */}
        <div className="relative">

          {!token ? (
            <button
              className="bg-blue-600 px-5 py-1 rounded-lg hover:bg-blue-700"
              onClick={() => setCurrentPage("login")}
            >
              Login
            </button>
          ) : (
            <div className="relative group cursor-pointer">

              {/* Username */}
              <div className="flex items-center gap-2">
                <div className="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center">
                  {username?.charAt(0).toUpperCase()}
                </div>
                <span>{username}</span>
              </div>

              {/* Dropdown */}
              <div className="absolute right-0 mt-2 w-40 bg-[#2f3031] rounded-lg shadow-lg opacity-0 group-hover:opacity-100 transition duration-200">

                <div className="px-4 py-2 hover:bg-[#3a3b3c] cursor-pointer">
                  Profile
                </div>

                <div className="px-4 py-2 hover:bg-[#3a3b3c] cursor-pointer">
                  Settings
                </div>

                <div
                  onClick={handleLogout}
                  className="px-4 py-2 hover:bg-red-500 cursor-pointer"
                >
                  Logout
                </div>

              </div>
            </div>
          )}

        </div>
      </div>
    </nav>
  );
}

export default Navbar;