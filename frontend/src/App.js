import { Routes, Route } from "react-router-dom"
import Header from "./components/home/Header"
import Footer from "./components/home/Footer"
import Home from "./components/home/Home"
import Article from "./components/article/Article"

function App() {
  return (
    <main>
      <Header />
      <Routes>
        {/* public routes */}
        <Route path='/' element={<Home />} />
        <Route path='/article/:id/*' element={<Article />} />
      </Routes>
      <Footer />
    </main>
  )
}

export default App
