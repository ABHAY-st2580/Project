import { useState, useEffect } from "react";

export default function TilesPage() {
  const [form, setForm] = useState({
    tile_type: "",
    tile_type2: "",
    tile_name_number: "",
    price_per_box: "",
    stock_quantity: "",
  });

  const [search, setSearch] = useState({
    tile_type: "",
    tile_type2: "",
    tile_name_number: "",
  });

  const [tiles, setTiles] = useState([]);

  const token = localStorage.getItem("token");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSearchChange = (e) => {
    setSearch({ ...search, [e.target.name]: e.target.value });
  };

  const fetchTiles = async () => {
    const res = await fetch("http://127.0.0.1:8000/tiles/get_tile", {
      headers: { Authorization: `Bearer ${token}` },
    });
    const data = await res.json();
    setTiles(data.tiles || []);
  };

  const handleSubmit = async () => {
    const res = await fetch("http://127.0.0.1:8000/tiles/add_tile/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(form),
    });

    const data = await res.json();
    if (res.ok) {
      fetchTiles();
    } else alert(data.error);
  };

  const handleSearch = async () => {
    const res = await fetch("http://127.0.0.1:8000/tiles/get_tile/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(search),
    });

    const data = await res.json();
    if (res.ok) setTiles([data]);
  };

  useEffect(() => {
    fetchTiles();
  }, []);

  return (
    <div className="p-6 text-gray-300 bg-[#020617] min-h-screen">

      <h1 className="text-xl font-medium mb-4">Tiles</h1>

      {/* 🔷 ADD TILE */}
      <div className="bg-[#0f172a] border border-gray-800 rounded-xl p-5 mb-6">

        <h2 className="text-sm text-gray-400 mb-4">Add Tile</h2>

        <div className="grid grid-cols-3 gap-4">

          <input name="tile_type" placeholder="Tile Type"
            onChange={handleChange} className="input-dark" />

          <input name="tile_type2" placeholder="Tile Type 2"
            onChange={handleChange} className="input-dark" />

          <input name="tile_name_number" placeholder="Tile Name / Number"
            onChange={handleChange} className="input-dark" />

          <input name="price_per_box" placeholder="Price per Box"
            onChange={handleChange} className="input-dark" />

          <input name="stock_quantity" placeholder="Stock Quantity"
            onChange={handleChange} className="input-dark" />

        </div>

        <div className="flex gap-3 mt-4">
          <button onClick={handleSubmit} className="btn-blue">
            Submit Tile
          </button>
        </div>

        {/* JSON Preview */}
        <div className="bg-[#020617] mt-5 p-3 rounded text-xs text-green-400 font-mono">
{`{
  "tile_type": "${form.tile_type}",
  "tile_type2": "${form.tile_type2}",
  "tile_name_number": "${form.tile_name_number}",
  "price_per_box": "${form.price_per_box}",
  "stock_quantity": "${form.stock_quantity}"
}`}
        </div>
      </div>

      {/* 🔷 SEARCH */}
      <div className="bg-[#0f172a] border border-gray-800 rounded-xl p-5 mb-6">

        <h2 className="text-sm text-gray-400 mb-4">Search Tile</h2>

        <div className="grid grid-cols-4 gap-4">

          <input name="tile_type" placeholder="Tile Type"
            onChange={handleSearchChange} className="input-dark" />

          <input name="tile_type2" placeholder="Tile Type 2"
            onChange={handleSearchChange} className="input-dark" />

          <input name="tile_name_number" placeholder="Tile Name / Number"
            onChange={handleSearchChange} className="input-dark" />

          <button onClick={handleSearch} className="btn-blue">
            Search
          </button>

        </div>
      </div>

      {/* 🔷 TABLE */}
      <div className="overflow-x-auto scroll-m-0 max-h-[350px] overflow-y-auto border border-gray-800 rounded-xl p-3">
        <table className="w-full table-fixed text-sm text-gray-300">

          {/* HEADER */}
          <thead>
            <tr className="text-gray-500 text-xs border-b border-gray-700">
              <th className="w-[8%] text-left py-3">ID</th>
              <th className="w-[15%] text-left py-3">Type</th>
              <th className="w-[15%] text-left py-3">Type 2</th>
              <th className="w-[15%] text-left py-3">Name / Number</th>
              <th className="w-[15%] text-left py-3">Price</th>
              <th className="w-[10%] text-left py-3">Stock</th>
            </tr>
          </thead>

          {/* BODY */}
          <tbody className = "divide-y divide-gray-800">
            {tiles.map((tile) => (
              <tr
                key={tile.tile_id}
                className="border-b border-gray-800 hover:bg-[#020617] transition"
              >
                <td className="py-3">{tile.tile_id}</td>
                <td className="py-3">{tile.tile_type}</td>
                <td className="py-3">{tile.tile_type2}</td>

                <td className="py-3 font-medium text-gray-200">
                  {tile.tile_name_number}
                </td>

                <td className="py-3 text-left">
                  {tile.price_per_box}
                </td>

                <td className="py-3 text-left">
                  {tile.stock_quantity}
                </td>
              </tr>
            ))}
          </tbody>

        </table>
      </div>

    </div>
  );
}