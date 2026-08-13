import { useState } from "react";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;
function AuthModal({ isOpen, onClose }) {
  const [isLogin, setIsLogin] = useState(true);
    const [form, setForm] = useState({
    fname: "",
    lname: "",
    username: "",
    password: "",
    shop_name: "",
    shop_location: "",
    role: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleRegister = async () => {
    try {
      await axios.post(`${API_URL}/auth/register/`, form);
      alert("Registered Successfully");
      setIsLogin(true);
    } catch (err) {
      alert("Registration Failed");
      console.error(err.response?.data);
    }
  };

  const handleLogin = async () => {
    try {
      const res = await axios.post(`${API_URL}/auth/login/`, {
        username: form.username,
        password: form.password,
      });

      localStorage.setItem("token", res.data.access);
      localStorage.setItem("username", form.username);

      alert("Login Successful");
      onClose();
      window.location.reload();

    } catch (err) {
      alert("Login Failed");
    }
  };

  if (!isOpen) return null;
  
  return (
    <div className="fixed inset-0 bg-black/60 w-full h-full flex items-center justify-center z-50">

      <div className="bg-[#2f3031] text-white p-6 rounded-xl w-full max-w-md shadow-lg relative">

        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-3 right-3 text-gray-400 hover:text-white"
        >
          ✕
        </button>

        {/* Title */}
        <h2 className="text-lg font-semibold mb-4 text-center">
          {isLogin ? "Login" : "Register"}
        </h2>

        {/* Form */}
        <div className="space-y-3 text-sm">

          {/* Login Fields */}
          {isLogin && (
            <>
              <input
                type="text"
                name="username"
                placeholder="Username"
                onChange={handleChange}
                className="w-full p-2 rounded bg-[#0f172a] focus:outline-none"
              />

              <input
                name="password"
                type="password"
                placeholder="Password"
                onChange={handleChange}
                className="w-full p-2 rounded bg-[#0f172a] focus:outline-none"
              />
            </>
          )}

          {/* Register Fields */}
          {!isLogin && (
            <>
              <div className="grid grid-cols-2 gap-2">
                <input name="fname" placeholder="First Name" className="p-2 bg-[#0f172a] rounded" onChange={handleChange} />
                <input name="lname" placeholder="Last Name" className="p-2 bg-[#0f172a] rounded" onChange={handleChange} />
              </div>

              <input name="username" placeholder="Username" className="w-full p-2 bg-[#0f172a] rounded" onChange={handleChange} />

              <input name="password" type="password" placeholder="Create Password"
                className="w-full p-2 bg-[#0f172a] rounded" onChange={handleChange} />

              <input name="shop_name" placeholder="Shop Name"
                className="w-full p-2 bg-[#0f172a] rounded" onChange={handleChange} />

              <input name="shop_location" placeholder="Shop Location"
                className="w-full p-2 bg-[#0f172a] rounded" onChange={handleChange} />

              {/* Role Dropdown */}
              <select name="role" className="w-full p-2 bg-[#0f172a] rounded text-gray-300" onChange={handleChange}>
                <option value="">Select Role</option>
                <option value="OWNER">Owner</option>
                <option value="STAFF">Staff</option>
                <option value="ACCOUNTANT">Accountant</option>
              </select>
            </>
          )}

          {/* Submit Button */}
          <button className="w-full bg-blue-600 py-2 rounded hover:bg-blue-950"
            onClick={isLogin ? handleLogin : handleRegister}
          >
            {isLogin ? "Login" : "Register"}
          </button>

          {/* Switch */}
          <p className="text-center text-gray-400 text-xs">
            {isLogin ? "Don't have an account?" : "Already have an account?"}
            <span
              onClick={() => setIsLogin(!isLogin)}
              className="text-blue-400 cursor-pointer ml-1"
            >
              {isLogin ? "Register" : "Login"}
            </span>
          </p>

        </div>
      </div>
    </div>
  );
}

export default AuthModal;