import { useState } from 'react'
import './App.css'
import Sidebar from './components/Sidebar'
import Navbar from './components/Navbar'
import SalePage from './pages/sale';
import Home from './pages/home';
import AuthModal from './components/AuthModal';


function App() {
  const [currentPage, setCurrentPage] = useState("home");
  return (
    <>
      <div className="h-screen flex flex-col min-h-screen bg-[#1a1e27] text-white font-light">
        <Navbar currentPage={currentPage} setCurrentPage={setCurrentPage} />
        <div className="flex flex-1 overflow-hidden flex-row-reverse">
          <Sidebar />
          
          <div className="flex-1 p-6 overflow-y-auto">
            <div className="text-2xl font-semibold mb-4">
              {currentPage == 'home' && <Home setCurrentPage={setCurrentPage} />}
              {currentPage == 'dashboard' && <h3>Your Dashboard Overview</h3>}
              {currentPage == 'tiles' && <h3>'Manage Your Tiles Inventory'</h3>}
              {currentPage == 'sales' && <SalePage />}
              {currentPage == 'login' && (
                <AuthModal isOpen={true} onClose={() => setCurrentPage("home")} />
              )}
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default App
