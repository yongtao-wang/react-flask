const base_url =
  process.env.REACT_APP_ENV === 'dev'
    ? 'http://localhost:5500'
    : 'http://47.74.11.42:5500'

const URL = {
  baseUrl: base_url,
  article: '/article',
  articles: '/article/all',
  admin: '/admin',
}

export default URL