import Card from "@mui/material/Card"
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import { formatShortDate } from "../../utils/Formatter";


const ArticleView = ({ article }) => {
  return (
    <Card sx={{width: 300}}>
      <CardHeader
        title={article.title}
        subheader={formatShortDate(article.created_on)}
      />
      <CardContent>
        <Typography color="text.primary">
          {article.content}
        </Typography>
      </CardContent>
    </Card>
  )
}

export default ArticleView
