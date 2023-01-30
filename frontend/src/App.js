import { Routes, Route } from 'react-router-dom'
import Header from './components/home/Header'
import Footer from './components/home/Footer'
import Home from './components/home/Home'

function App() {
  return (
    <div>
      <Header />
      <Routes>
        <Route path='/' element={<Home />} />
      </Routes>
      <Footer />
    </div>
  )
}

export default App
