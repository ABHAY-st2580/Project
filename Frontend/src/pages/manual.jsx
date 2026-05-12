function ManualPage() {
  return (
    <div className="p-6 text-white bg-[#020617] min-h-screen font-extralight">

      {/* Header */}
      <h1 className="text-3xl font-light mb-6 text-center">
        TileTracker User Manual
      </h1>

      {/* Sections */}
      <div className="space-y-6 max-w-5xl mx-auto">

        {/* 1. Register & Login */}
        <div className="bg-[#1e293b] p-5 rounded-xl shadow-md">
          <h2 className="text-xl font-light mb-3">Getting Started</h2>

          <p className="text-sm text-gray-300 mb-2">Register your account:</p>
          <ul className="list-disc ml-5 text-sm text-gray-400 space-y-1">
            <li>Click Login - Register</li>
            <li>Enter name, username, password</li>
            <li>Add shop name & location</li>
            <li>Select role (Owner/Staff)</li>
          </ul>

          <p className="text-sm text-gray-300 mt-3">Login:</p>
          <ul className="list-disc ml-5 text-sm text-gray-400">
            <li>Enter username & password</li>
            <li>Access all features after login</li>
          </ul>
        </div>

        {/* 2. Dashboard */}
        <div className="bg-[#1e293b] p-5 rounded-xl shadow-md">
          <h2 className="text-xl font-light mb-3">Dashboard</h2>
          <p className="text-sm text-gray-400">
            View total sales, revenue insights, and business performance.
            Helps you understand growth and trends.
          </p>
        </div>

        {/* 3. Tiles */}
        <div className="bg-[#1e293b] p-5 rounded-xl shadow-md">
          <h2 className="text-xl font-light mb-3">Tiles Management</h2>
          <ul className="list-disc ml-5 text-sm text-gray-400 space-y-1">
            <li>Add new tiles</li>
            <li>Update stock</li>
            <li>Manage tile types (HL / L / D / F / AT)</li>
          </ul>
        </div>

        {/* 4. Sales */}
        <div className="bg-[#1e293b] p-5 rounded-xl shadow-md">
          <h2 className="text-xl font-light mb-3">Add Sales</h2>

          <ol className="list-decimal ml-5 text-sm text-gray-400 space-y-1">
            <li>Enter customer details</li>
            <li>Fill amount & remaining amount</li>
            <li>Add tile details</li>
            <li>Click + Add Tile (multiple allowed)</li>
            <li>Click Submit Sale</li>
          </ol>

          <p className="text-sm text-blue-400 mt-2">
            Stock updates automatically after sale
          </p>
        </div>

        {/* 5. Sidebar */}
        <div className="bg-[#1e293b] p-5 rounded-xl shadow-md">
          <h2 className="text-xl font-light mb-3">Inventory Alerts</h2>

          <p className="text-sm text-gray-400 mb-2">
            Right-side panel shows:
          </p>

          <ul className="list-disc ml-5 text-sm text-gray-400 space-y-1">
            <li>Low Stock tiles</li>
            <li>Not Selling tiles</li>
          </ul>

          <p className="text-sm text-blue-400 mt-2">
            Helps you manage inventory smartly
          </p>
        </div>

        {/* 6. Recent Sales */}
        <div className="bg-[#1e293b] p-5 rounded-xl shadow-md">
          <h2 className="text-xl font-light mb-3">Recent Sales</h2>
          <p className="text-sm text-gray-400">
            Shows last 5-7 sales with customer name, amount, and date.
          </p>
        </div>

        {/* 7. Logout */}
        <div className="bg-[#1e293b] p-5 rounded-xl shadow-md">
          <h2 className="text-xl font-light mb-3">Logout</h2>
          <p className="text-sm text-gray-400">
            Click profile (top right) → Logout to end session.
          </p>
        </div>

      </div>

    </div>
  );
}

export default ManualPage;