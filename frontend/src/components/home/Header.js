import { Link, NavLink } from 'react-router-dom'
import logo from '../../assets/img/logo-low-res-trans-right.png'

const Links = () => (
  <div className='links'>
    <NavLink to='/'>Home</NavLink>
    <NavLink to='/guide'>Travel Guide</NavLink>
    <NavLink to='/about'>About Me</NavLink>
  </div>
)

const Navbar = () => (
  <nav className='navbar'>
    <div className='logo'>
      <Link to='/'>
        <img src={logo} alt='travel-with-me' />
      </Link>
    </div>
    <Links />
  </nav>
)

const Header = () => {
  return (
    <div>
      <Navbar />
    </div>
  )
}

export default Header
