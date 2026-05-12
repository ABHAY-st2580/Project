import { useState } from 'react'
import './App.css'
import Sidebar from './components/Sidebar'
import Navbar from './components/Navbar'
import SalePage from './pages/sale';
import TilePage from './pages/tilepage';
import TodayPage from './pages/today';
import ManualPage from './pages/manual';
import RecommendationPage from './pages/dashboard';
import Home from './pages/home';
import AuthModal from './components/AuthModal';


function App() {
  const [currentPage, setCurrentPage] = useState("home");
  return (
    <>
      <div className="h-screen flex flex-col min-h-screen bg-[#1a1e27] text-white font-light">
        <Navbar currentPage={currentPage} setCurrentPage={setCurrentPage} />
        <div className="flex flex-1 overflow-hidden">
          {/* flex-row-reverse for reversing the sidebar from left to right...*/}
          <Sidebar />
          
          <div className="flex-1 p-6 overflow-y-auto">
            <div className="text-2xl font-semibold mb-4">
              {currentPage == 'home' && <Home setCurrentPage={setCurrentPage} />}
              {currentPage == 'dashboard' && <RecommendationPage />}
              {currentPage == 'sales' && <SalePage />}
              {currentPage == 'tiles' && <TilePage />}
              {currentPage == 'manual' && <ManualPage />}
              {currentPage == 'today' && <TodayPage />}
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
