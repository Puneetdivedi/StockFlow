import React from "react";
import { NavLink } from "react-router-dom";
import "./Sidebar.css";

const Sidebar = () => {
  return (
    <nav className="sidebar">
      <h2 className="sidebar-title">StockFlow</h2>
      <ul className="nav-list">
        <li>
          <NavLink to="/dashboard" className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>
            Dashboard
          </NavLink>
        </li>
        <li>
          <NavLink to="/products" className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>
            Products
          </NavLink>
        </li>
        <li>
          <NavLink to="/customers" className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>
            Customers
          </NavLink>
        </li>
        <li>
          <NavLink to="/orders" className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>
            Orders
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Sidebar;
