import { Link } from 'react-router-dom'
import logo_bw from '../../assets/img/logo-low-res-bw-inverted.png'

const Footer = () => {
  return (
    <footer className='footer'>
      <div className='footer__info'>
      </div>
      <div className='copyright'>
        <table>
          <tr>
            <td>
              <Link to='/'><img src={logo_bw} alt='logo' style={{ height: '3rem', paddingTop: '2px', paddingRight: '2px' }} /></Link>
            </td>
            <td style={{ verticalAlign: 'top' }}>
              ©2023 Travel With Me. All rights reserved.
            </td>
          </tr>
        </table>
      </div>

    </footer>
  )
}

export default Footer
