import { Content, Title, SubTitle } from 'reactbulma'
import { formatShortDate } from '../../utils/Formatter'
import { useAxiosGet } from '../../hooks/useAxios'
import URL from '../../utils/Configs'
import { useParams } from 'react-router-dom'
import '../../css/article.css'

const Article = () => {
  const { id } = useParams()
  const {
    data: article,
    error,
    isLoading,
  } = useAxiosGet(URL.article + `/${id}`)

  return (
    <div className='article'>
      {isLoading && <p>Loading article...</p>}
      {error && <div>{error}</div>}
      {article && (
        <div>
          <Title is='3' className='article__title--full'>
            {article.title}
          </Title>
          <SubTitle is='6'>Author: {article.author}</SubTitle>
          <SubTitle is='6'>
            Published on: {formatShortDate(article.created_on)}
          </SubTitle>
          <Content medium>{article.content}</Content>
        </div>
      )}
    </div>
  )
}

export default Article
