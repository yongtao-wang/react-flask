import { Routes, Route } from "react-router-dom";

import Home from "./components/home/Home";
import Header from "./components/home/Header";
import Footer from "./components/home/Footer";

function App() {
  return (
    <div>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
