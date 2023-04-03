import axios from 'axios'
import URL from './Configs'

export default axios.create({
  baseURL: URL.baseUrl,
  headers: { 'Content-Type': 'application/json' },
})

export const axiosProtected = axios.create({
  baseURL: URL.baseUrl,
  headers: {
    'Content-Type': 'application/json',
    withCredentials: true,
  },
})
