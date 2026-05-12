import { useState, useEffect } from "react";
import React from "react";

function Sidebar() {
  const [alerts, setalerts] = useState(null);
  const [today, settoday] = useState(null);
  const [debt, setdebt] = useState(null);

  const isLoggedIn = localStorage.getItem("token");

  const token = localStorage.getItem("token")

  const fetchtoday = async () => {
    const res = await fetch("http://127.0.0.1:8000/insights/today/", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await res.json();
    settoday(data);
  };
  useEffect(() => {
      fetchtoday();
    }, []);

  const fetchdebt = async () => {
    const res = await fetch("http://127.0.0.1:8000/insights/debt/", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await res.json();
    settoday(data);
  };

  const fetchalerts = async () => {
    const res = await fetch("http://127.0.0.1:8000/insights/inventory-alerts/", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await res.json();
    setalerts(data.inventory_alerts);
  };

  useEffect(() => {
      fetchalerts();
    }, []);

  if (!isLoggedIn) {
    return (
      <div className="w-72 bg-[#313743] text-white p-5 flex items-center justify-center">
        <h2 className="text-lg text-gray-300">
          Please login to view dashboard
        </h2>
      </div>
    );
  }

  return (
    <div className="w-72 bg-[#313743] text-white p-5 border-r border-gray-800 flex flex-col space-y-6">

      {/* 🔹 TODAY SALES SECTION */}
      <div>
        <h2 className="text-xl mb-3">Today's Sales</h2>

        <div className="bg-[#191c23] p-4 rounded space-y-2">
          {today && (
            <>
            <div className="flex justify-between">
              <span className="text-gray-400">Revenue</span>
              <span>₹{today.Revenue}</span>
            </div>
            <div className="flex justify-between">
              <span className="text-gray-400">Orders</span>
              <span>{today.Order}</span>
            </div>
            {today.Order == 0 ? (
              <div className="flex justify-between">
                <span className="text-gray-400" ></span>
              </div>) :
              (<div className="flex justify-between">
                <span className="text-gray-400" >Check Orders in Today's Section</span>
              </div>)
            }
            </>
          )}
        </div>
      </div>

      <hr />

      {/* 🔹 INVENTORY ALERTS */}
      <div>
        <h2 className="text-xl mb-4">Inventory Alerts</h2>

        {/* Low Stock */}
        <div className="mb-5">
          <h3 className="text-sm text-gray-400 mb-2">Low Stock</h3>

          {alerts === null ? (
              <p className="text-lg text-gray-500">No data</p>
            ) : (
              alerts.map((tile, i) => (
                <div key={i} className="flex justify-between text-lg mb-1">
                  <span>{tile.tile_type}_{tile.tile_name_number}_{tile.tile_type2}</span>
                  <span className="text-red-400">{tile.stock_quantity}</span>
                </div>
              ))
            )}
        </div>

        {/* Not Selling */}
        {/**/}

      </div>
      <hr />
      <div>
        <h2 className="text-xl mb-4">Debt Alerts</h2>
        <div>
            <div className="space-y-2">
              <div className="bg-[#191c23] p-3 rounded flex justify-between">
                <span>_2_2_Satwariya</span>
                <span className="text-yellow-400">No sales</span>
              </div>
            </div>
        </div>
      </div>
    </div>
  );
}

export default Sidebar;