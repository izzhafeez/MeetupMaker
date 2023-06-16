import React, { useRef } from 'react';

import Navbar from "./components/layout/navbar";
import router from "./router";

const App = () => {
  return (
    <div className="vh-100 bg-light">
      <Navbar/>
      {router}
    </div>
  );
};

export default App;
