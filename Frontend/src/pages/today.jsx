import React, { useState, useEffect } from "react";

const API_URL = import.meta.env.VITE_API_URL;
export default function TodayPage() {
  const [selectedSale, setSelectedSale] = useState(null);
  const [today, setToday] = useState([]);

  const token = localStorage.getItem("token");

  const fetchToday = async () => {
    if(!token) return;
    try {
      const res = await fetch(`${API_URL}/insights/today/`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await res.json();

      console.log("API:", data);
      setToday(data.today_sales || []);
      
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchToday();
  }, []);

  return (
    <div>
      <h2 className="text-xl mb-3">Today's Orders</h2>

      <div className="max-h-[250px] overflow-y-auto space-y-2">

        {today.length === 0 ? (
          <p className="text-sm text-gray-500">No orders</p>
        ) : (
          today.map((sale, i) => (
            <div
              key={i}
              className="bg-[#191c23] p-2 rounded cursor-pointer hover:bg-[#222733]"
            >
              <div className="flex justify-between text-sm">
                <span>{sale.customer_name}</span>
                <span className="text-green-400">Rs. {sale.amount} Paid</span>
              </div>

              <div className="text-xs text-gray-400">
                {sale.address}
              </div>

              <div className="text-xs text-gray-400">
                {sale.phone_number}
              </div>

              <div className="text-xs text-gray-300 border-t border-gray-700 pt-2">
                {sale.items && sale.items.length > 0 ? (
                  sale.items.map((item, idx) => (
                    <div key={idx} className="flex justify-between">
                      <span className="truncate">{item.tile_type}</span>
                      <span className="truncate">{item.tile_name_number}</span>
                      <span className="truncate">{item.tile_type2}</span>
                      <span className="text-blue-400">x{item.quantity}</span>
                    </div>
                  ))
                ) : (
                  <span className="text-gray-500">No items</span>
                )}
              </div>
            </div>
          ))
        )}

      </div>
    </div>
  );
}