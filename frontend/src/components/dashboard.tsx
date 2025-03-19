import { useState } from "react";
import { Menu, X, LayoutDashboard } from "lucide-react";

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(true);

  return (
    <div className="flex">
      {/* Sidebar */}
      <div
        className={`bg-gray-100 h-screen p-4 transition-all duration-300 ${
          isOpen ? "w-60" : "w-16"
        }`}
      >
        <button
          className="mb-4 p-2 bg-white rounded-full shadow-md"
          onClick={() => setIsOpen(!isOpen)}
        >
          {isOpen ? <X size={20} /> : <Menu size={20} />}
        </button>

        <ul className="space-y-4">
          <li className="flex items-center gap-2 text-gray-700">
            <span className="bg-blue-500 w-3 h-3 rounded-full"></span>
            {isOpen && "Dashboard"}
          </li>
          <li className="flex items-center gap-2 text-gray-700">
            <span className="bg-gray-500 w-3 h-3 rounded-full"></span>
            {isOpen && "Settings"}
          </li>
          <li className="flex items-center gap-2 text-gray-700">
            <span className="bg-gray-500 w-3 h-3 rounded-full"></span>
            {isOpen && "Profile"}
          </li>
        </ul>
      </div>

      {/* Main Content */}
      <div className="flex-1 p-6">
        <h1 className="text-xl font-semibold">Dashboard</h1>
        <div className="mt-4 border-2 border-dashed h-64 rounded-lg"></div>
      </div>
    </div>
  );
};

export default Sidebar;
