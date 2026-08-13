import { useState, useEffect } from "react";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;
function SalePage() {
  const [recentSales, setRecentSales] = useState([
  ]);

  const [form, setForm] = useState({
    customer_name: "",
    amount: "",
    remaining_amount: "",
    address: "",
    phone_number: "",
  });

  const [item, setItem] = useState({
    tile_type: "",
    tile_type2: "",
    tile_name_number: "",
    quantity: "",
  });

  const [items, setItems] = useState([]);

  // Customer form
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Single item input
  const handleItemChange = (e) => {
    setItem({ ...item, [e.target.name]: e.target.value });
  };

  // Add tile
  const addItem = () => {
    if (!item.tile_type || !item.tile_name_number || !item.quantity) {
      alert("Fill all tile fields");
      return;
    }

    setItems([...items, item]);

    // reset input
    setItem({
      tile_type: "",
      tile_type2: "",
      tile_name_number: "",
      quantity: "",
    });
  };

  // Remove tile
  const removeItem = (index) => {
    const newItems = items.filter((_, i) => i !== index);
    setItems(newItems);
  };

  // Submit
  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      customer_name: form.customer_name,
      amount: Number(form.amount),
      remaining_amount: Number(form.remaining_amount),
      address: form.address,
      phone_number: form.phone_number,
      items: items.map((item) => ({
        tile_type: item.tile_type,
        tile_type2: item.tile_type2,
        tile_name_number: item.tile_name_number,
        quantity: Number(item.quantity),
      })),
    };

    // 🔥 SHOW JSON IN CONSOLE
    console.log("🔥 JSON SENT TO BACKEND:");
    console.log(JSON.stringify(payload, null, 2));

    try {
      const token = localStorage.getItem("token");
      if(!token) return;
      await axios.post(
        `${API_URL}/sale/add_sale/`,
        payload,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        }
      );

      alert("Sale Added");

      setItems([]);
      setForm({
        customer_name: "",
        amount: "",
        remaining_amount: "",
        address: "",
        phone_number: "",
      });

    } catch (err) {
      alert("Error");
      console.error(err.response?.data);
    }
  };

  useEffect(() => {
    const fetchSales = async () => {
      try {
        const token = localStorage.getItem("token");
        if(!token) return;
        const res = await axios.get(
          `${API_URL}/sale/get_sales/`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        setRecentSales(res.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchSales();
  }, []);

  return (
    <div className="p-4 text-sm text-white bg-[#020617] min-h-screen">

      <h1 className="text-lg mb-4">Add Sale</h1>

      {/* Customer */}
      <div className="grid grid-cols-2 gap-3 mb-4">
        <input name="customer_name" placeholder="Customer Name"
          value = {form.customer_name}
          onChange={handleChange}
          className="p-2 bg-[#0f172a] rounded" />

        <input name="phone_number" placeholder="Phone Number"
          value = {form.phone_number}
          onChange={handleChange}
          className="p-2 bg-[#0f172a] rounded" />

        <textarea name="address" placeholder="Address"
          value = {form.address}
          onChange={handleChange}
          className="p-2 bg-[#0f172a] rounded col-span-2" />

        <input name="amount" placeholder="Amount"
          value = {form.amount}
          onChange={handleChange}
          className="p-2 bg-[#0f172a] rounded" />
        
        <input name="remaining_amount" placeholder="Remaining Amount"
          value = {form.remaining_amount}
          onChange={handleChange}
          className="p-2 bg-[#0f172a] rounded" />
      </div>

      {/* Add Tile */}
      <div className="grid grid-cols-4 gap-2 mb-3">
        <input name="tile_type" placeholder="Type"
          value={item.tile_type}
          onChange={handleItemChange}
          className="p-2 bg-[#0f172a] rounded" />

        <input name="tile_type2" placeholder="HL/L/D/F"
          value={item.tile_type2}
          onChange={handleItemChange}
          className="p-2 bg-[#0f172a] rounded" />

        <input name="tile_name_number" placeholder="Tile Name/Number"
          value={item.tile_name_number}
          onChange={handleItemChange}
          className="p-2 bg-[#0f172a] rounded" />

        <input name="quantity" type="number" placeholder="Qty"
          value={item.quantity}
          onChange={handleItemChange}
          className="p-2 bg-[#0f172a] rounded" />
      </div>

      <button
        onClick={addItem}
        className="bg-blue-950 px-3 py-1 rounded mb-4 hover:bg-blue-700"
      >
        + Add Tile
      </button>

      {/*Tile List (LIVE) */}
      {items.length > 0 && (
        <div className="mb-4">
          <h2 className="text-sm mb-2 text-gray-300">Selected Tiles</h2>

          <div className="space-y-2">
            {items.map((tile, index) => (
              <div
                key={index}
                className="flex justify-between items-center bg-[#0f172a] p-2 rounded"
              >
                <span>
                  {tile.tile_type} | {tile.tile_name_number} | {tile.tile_type2} | {tile.quantity}
                </span>

                <button
                  onClick={() => removeItem(index)}
                  className="text-red-400 hover:text-red-600"
                >
                  Remove
                </button>
              </div>
            ))}
          </div>
        </div>
      )}
      <br/>
      {/* Submit */}
      <button
        onClick={handleSubmit}
        className="bg-blue-950 px-4 py-2 rounded hover:bg-blue-700"
      >
        Submit Sale
      </button>
      <pre className="mt-4 bg-[#0f172a] p-3 rounded text-xs text-green-400 overflow-auto">
        {JSON.stringify({
          ...form,
          items: items
        }, null, 2)}
      </pre>

      <div className="mt-10">
        <h2 className="text-lg font-semibold mb-4 text-white">Recent Sales</h2>

        <div className="overflow-x-auto rounded-lg border border-gray-700">
          <table className="w-full text-sm text-gray-300">

            {/* HEADER */}
            <thead className="bg-[#1e293b] text-gray-200">
              <tr className="text-left">
                <th className="px-5 py-3 border-r border-gray-700">Date</th>
                <th className="px-5 py-3 border-r border-gray-700">Customer</th>
                <th className="px-5 py-3 border-r border-gray-700 text-right">Amount</th>
                <th className="px-5 py-3 border-r border-gray-700 text-right">Remaining</th>
                <th className="px-5 py-3 border-r border-gray-700">Address</th>
                <th className="px-5 py-3 text-right">Phone</th>
              </tr>
            </thead>

            {/* BODY */}
            <tbody>
              {recentSales?.slice(0, 7).map((sale, index) => (
                <tr
                  key={sale.sale_id}
                  className={`border-t border-gray-700 transition ${
                    index % 2 === 0 ? "bg-[#020617]" : "bg-[#0f172a]"
                  } hover:bg-[#1e293b]`}
                >
                  <td className="px-5 py-3 border-r border-gray-700">
                    {sale.date?.slice(0, 10)}
                  </td>

                  <td className="px-5 py-3 border-r border-gray-700 font-medium text-white">
                    {sale.customer_name}
                  </td>

                  <td className="px-5 py-3 border-r border-gray-700 text-right text-green-400">
                    ₹ {sale.amount}
                  </td>

                  <td className="px-5 py-3 border-r border-gray-700 text-right text-yellow-400">
                    ₹ {sale.remaining_amount}
                  </td>

                  <td className="px-5 py-3 border-r border-gray-700 truncate max-w-[200px]">
                    {sale.address}
                  </td>

                  <td className="px-5 py-3 text-right">
                    {sale.phone_number}
                  </td>
                </tr>
              ))}
            </tbody>

          </table>
        </div>
      </div>
    </div>
  );
}

export default SalePage;