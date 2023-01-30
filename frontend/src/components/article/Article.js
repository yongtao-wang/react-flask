const Article = ({ article }) => {
  return (
    <div className="article">
      <div className="article--title">{article.title}</div>
      <div className="article--date">{article.created_on}</div>
      <div className="article--tag">{article.tags}</div>
      <div className="article--content">{article.content}</div>
    </div>
  )
}

export default Article
