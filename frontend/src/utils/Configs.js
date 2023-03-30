const base_url =
  process.env.REACT_APP_ENV === 'dev'
    ? 'http://localhost:4200'
    : 'http://139.180.133.79:4200'  // TODO: replace with a better way

const URL = {
  baseUrl: base_url,
  article: '/article',
  articles: '/article/all',
  admin: '/admin',
}

export default URL