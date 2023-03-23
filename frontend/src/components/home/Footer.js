import { Link } from 'react-router-dom'
import logo_bw from '../../assets/img/logo-low-res-bw-inverted.png'

const Footer = () => {
  return (
    <footer className='footer'>
      <div className='footer__info'>
      </div>
      <div className='copyright'>
        <Link to='/'><img src={logo_bw} alt='logo' style={{ height: '3rem', paddingRight: '1rem', verticalAlign: 'text-top' }} /></Link>
        ©2023 Travel With Me. All rights reserved.
      </div>

    </footer>
  )
}

export default Footer
