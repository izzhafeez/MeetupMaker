import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Home from "./containers/Home";

const router = (
  <Router>
    <Routes>
      <Route exact path="/" element={<Home/>}></Route>
    </Routes>
  </Router>
);

export default router;