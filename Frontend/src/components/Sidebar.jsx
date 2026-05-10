function Sidebar() {
  const left = 5;
  return (
    <div className="w-72 bg-[#313743] text-white p-5 border-r border-gray-800 flex flex-col">
      
      <h2 className="text-xl text-white mb-4">
        Inventory Alerts
      </h2>

      {/* Low Stock */}
      <div className="mb-6">
        <h3 className="text-sm text-gray-400 mb-2">Low Stock</h3>

        <div className="space-y-2">
          <div className="bg-[#191c23] p-3 rounded flex justify-between">
            <span>_2_2_Satwariya</span>
            <span className="text-gray-400">{left}</span>
          </div>
          <div className="bg-[#191c23] p-3 rounded flex justify-between">
            <span>_12_18_6543</span>
            <span className="text-gray-400">{left}</span>
          </div>
          <div className="bg-[#191c23] p-3 rounded flex justify-between">
            <span>_12_18_6543</span>
            <span className="text-gray-400">{left}</span>
          </div>
        </div>
      </div>
      <hr className="border-black-700 mb-6" />
      {/* Not Selling */}
      <div>
        <h3 className="text-sm text-gray-400 mb-2">Not Selling</h3>

        <div className="space-y-2">
          <div className="bg-[#191c23] p-3 rounded flex justify-between">
            <span>_2_2_Satwariya</span>
            <span className="text-gray-400">No sales</span>
          </div>
        </div>
      </div>

    </div>
  );
}

export default Sidebar;