import React, { useState, useEffect } from "react";

const API_URL = import.meta.env.VITE_API_URL;

export default function ProfilePage() {
  const [profile, setProfile] = useState(null);
  const token = localStorage.getItem("token");


  const fetchProfile = async () => {
    try {
      if(!token) return;
      const res = await fetch(`${API_URL}/auth/profile/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await res.json();
      console.log("PROFILE:", data);
      setProfile(data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchProfile();
  }, []);

  if (!profile) {
    return (
      <div className="p-6 text-gray-400">Loading profile...</div>
    );
  }

  return (
    <>
    <div className="bg-[#0f172a] p-5 rounded-xl border border-gray-800 flex items-center gap-4 mb-6">
      <div className="w-14 h-14 bg-gray-700 rounded-full flex items-center justify-center text-lg">
        {profile.fname?.[0]}
      </div>
      <div>
        <h2 className="text-lg">{profile.fname} {profile.lname}</h2>
        <p className="text-xs text-gray-400">{profile.role}</p>
        <p className="text-xs text-gray-500">{profile.shop_name}</p>
      </div>

    </div>
    <div className="p-6 bg-[#020617] min-h-screen text-gray-300">

      <h1 className="text-xl mb-6">Profile</h1>

      <div className="grid grid-cols-2 gap-6">

        {/* 🔷 USER INFO */}
        <div className="bg-[#0f172a] p-5 rounded-xl border border-gray-800">
          <h2 className="text-sm text-gray-400 mb-4">User Information</h2>

          <div className="space-y-3 text-sm">

            <div className="flex justify-between">
              <span className="text-gray-500">Username</span>
              <span>{profile.username}</span>
            </div>

            <div className="flex justify-between">
              <span className="text-gray-500">Name of the Owner</span>
              <span>{profile.fname} {profile.lname}</span>
            </div>

            <div className="flex justify-between">
              <span className="text-gray-500">Phone Number</span>
              <span>{profile.phone || "—"}</span>
            </div>

            <div className="flex justify-between">
              <span className="text-gray-500">Role</span>
              <span className="text-blue-400">{profile.role}</span>
            </div>

          </div>
        </div>

        {/* 🔷 SHOP INFO */}
        <div className="bg-[#0f172a] p-5 rounded-xl border border-gray-800">
          <h2 className="text-sm text-gray-400 mb-4">Shop Information</h2>

          <div className="space-y-3 text-sm">

            <div className="flex justify-between">
              <span className="text-gray-500">Shop Name</span>
              <span>{profile.shop_name}</span>
            </div>

            <div className="flex justify-between">
              <span className="text-gray-500">Location</span>
              <span>{profile.shop_address || "—"}</span>
            </div>

          </div>
        </div>

      </div>
    </div>
  </>
  );
}