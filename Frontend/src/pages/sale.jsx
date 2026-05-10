import { useState, useEffect } from "react";
import axios from "axios";

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

    try {
      await axios.post("http://127.0.0.1:8000/add_sale/", {
        ...form,
        items: items,
      });

      alert("Sale Added");
      setItems([]);
    } catch (err) {
      alert("Error");
    }
  };

  useEffect(() => {
    const fetchSales = async () => {
      try {
        const token = localStorage.getItem("token");

        const res = await axios.get(
          "http://127.0.0.1:8000/sales/get_sales/",
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
    <div className="p-4 text-sm text-white bg-[#020817] min-h-screen">

      <h1 className="text-lg mb-4">Add Sale</h1>

      {/* Customer */}
      <div className="grid grid-cols-2 gap-3 mb-4">
        <input name="customer_name" placeholder="Customer"
          value = {form.customer_name}
          onChange={handleChange}
          className="p-2 bg-[#0f172a] rounded" />

        <input name="phone_number" placeholder="Phone"
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


      <div className="mt-8">
        <h2 className="text-lg font-semibold mb-3">Recent Sales</h2>

        <div className="overflow-x-auto border border-gray-700 rounded-lg">
          <table className="w-full text-sm text-gray-300">

            <thead className="bg-[#1e293b] text-white">
              <tr>
                <th className="px-4 py-2">Date</th>
                <th className="px-4 py-2">Customer</th>
                <th className="px-4 py-2">Amount</th>
                <th className="px-4 py-2">Remaining</th>
                <th className="px-4 py-2">Address</th>
                <th className="px-4 py-2">Phone</th>
              </tr>
            </thead>

            <tbody>
              {recentSales.map((sale) => (
                <tr key={sale.sale_id} className="border-t border-gray-700 hover:bg-[#1e293b]">
                  <td className="px-4 py-2">{sale.date}</td>
                  <td className="px-4 py-2">{sale.customer_name}</td>
                  <td className="px-4 py-2">₹ {sale.amount}</td>
                  <td className="px-4 py-2">₹ {sale.remaining_amount}</td>
                  <td className="px-4 py-2">{sale.address}</td>
                  <td className="px-4 py-2">{sale.phone_number}</td>
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