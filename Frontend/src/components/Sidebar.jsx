import { useState, useEffect } from "react";
import React from "react";

function Sidebar() {
  const [alerts, setalerts] = useState(null);
  const [today, settoday] = useState(null);
  const [debt, setdebt] = useState(null);

  const isLoggedIn = localStorage.getItem("token");

  const token = localStorage.getItem("token")
  const handleamount = async (saleId) => {
    try {
      const res = await fetch(
        `http://127.0.0.1:8000/insights/pay-debt/${saleId}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (!res.ok) {
        const text = await res.text();
        console.error("Server Error:", text);
        return;
      }

      const data = await res.json();
      console.log("Paid:", data);

      fetchdebt();

    } catch (err) {
      console.error(err);
    }
  };

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
    console.log(data.debt);
    setdebt(data.debt);
  };
  useEffect(() => {
    fetchdebt();
  }, []);

  const fetchalerts = async () => {
    const res = await fetch("http://127.0.0.1:8000/insights/inventory-alerts/", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await res.json();
    console.log(data)
    setalerts(data.inventory_alerts);
  };

  useEffect(() => {
      fetchalerts();
    }, []);

  if (!isLoggedIn) {
    return (
      <div className="w-72 bg-[#292c32] text-white p-5 flex items-center justify-center">
        <h2 className="text-lg text-gray-300">
          Please login to view dashboard
        </h2>
      </div>
    );
  }

  return (
    <div className="w-72 bg-[#313743] text-white p-5 border-r border-gray-800 flex flex-col space-y-6 overflow-y-auto">

      {/* 🔹 TODAY SALES SECTION */}
      <div>
        <h2 className="text-xl mb-3">Today's Sales</h2>

        <div className="bg-[#191c23] p-4 rounded space-y-2">
          {today && (
            <>
            <div className="flex justify-between">
              <span className="text-gray-400">Revenue</span>
              <span className = "text-green-500">Rs. {today.Revenue}</span>
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
                <span className="text-gray-400 text-sm" >Check Orders in Today's Section</span>
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
        <div className="mb-5 bg-[#191c23] p-2 rounded">
          <h3 className="text-m font-medium text-white mb-2">Low Stock</h3>

          {alerts === null || alerts.length == 0 ? (
              <p className="text-m text-gray-500">No data</p>
            ) : (
              alerts.map((tile, i) => (
                <div key={i} className="flex justify-between text-sm mb-1">
                  <span>{tile.tile_type}_{tile.tile_name_number}_{tile.tile_type2}</span>
                  <span className="text-red-400">{tile.stock_quantity}</span>
                </div>
              ))
            )}
        </div>

      </div>
      <hr />
      <div>
        <h2 className="text-xl mb-4">Debt Alerts</h2>

        {(!debt || debt.length === 0) ? (
          <p className="text-sm text-gray-500">No data</p>
        ) : (
          <div className="space-y-2 max-h-[400px] overflow-y-auto">

            {debt.map((cust, i) => (
              <div
                key={i}
                className="bg-[#191c23] p-2 rounded text-sm"
              >
                <div className="flex justify-between">
                  <span className="font-medium">{cust.customer_name}</span>
                  <span className="text-red-400">
                    Rs. {cust.remaining_amount}
                  </span>
                </div>

                <div className="text-xs text-gray-400">
                  {cust.date}
                </div>

                <div className="text-xs text-gray-500 truncate">
                  {cust.address}
                </div>

                <div className="text-xs text-gray-500 flex justify-between">
                  <span>{cust.phone_number}</span>
                  <span><button onClick = {() => handleamount(cust.sale_id)} className="bg-green-900 text-white rounded p-1 font-bold hover:bg-green-700">Paid</button></span>
                </div>
              </div>
            ))}

          </div>
        )}
      </div>
    </div>
  );
}

export default Sidebar;