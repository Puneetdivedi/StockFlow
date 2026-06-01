import React, { createContext, useState, useEffect } from "react";

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [refreshFlag, setRefreshFlag] = useState(0);

  const triggerRefresh = () => setRefreshFlag(prev => prev + 1);

  return (
    <AppContext.Provider value={{ refreshFlag, triggerRefresh }}>
      {children}
    </AppContext.Provider>
  );
};
