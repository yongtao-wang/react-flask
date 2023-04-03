import { Card, Content, Title, SubTitle } from 'reactbulma'
import { formatShortDate } from '../../utils/Formatter'
import '../../css/article.css'
import { Link } from 'react-router-dom'

const ArticleView = ({ article }) => {
  return (
    <Link to={`/article/${article.id}`}>
      <Card className='article__card'>
        <Card.Content>
          <Title is='5'>{article.title}</Title>
          <SubTitle is='7'>
            Published on {formatShortDate(article.created_on)}
          </SubTitle>
          <Content>{article.content}</Content>
        </Card.Content>
      </Card>
    </Link>
  )
}

export default ArticleView
