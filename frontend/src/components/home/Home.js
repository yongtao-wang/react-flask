import URL from '../../utils/Configs'
import ArticleView from '../article/ArticleView'
import { useAxiosGet } from '../../hooks/useAxios'
import '../../css/home.css'

const Articles = ({ articles }) => {
  return (
    <div className='article__area'>
      {articles.map((article) => (
        <div className='card__wrapper' key={article.id}>
          <ArticleView article={article} />
        </div>
      ))}
    </div>
  )
}

const Home = () => {
  const { data: articles, error, isLoading } = useAxiosGet(URL.articles)

  return (
    <div>
      {error && <p>Error loading.</p>}
      {isLoading && <p>Loading...</p>}
      {articles && <Articles articles={articles} />}
    </div>
  )
}

export default Home
