import { useEffect, useState } from "react"
import URL from "../utils/Configs"

const useFetch = (url) => {
  const [data, setData] = useState(null)
  const [isPending, setIsPending] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const abortCtrl = new AbortController()

    const asyncFetchData = async (_url) => {
      try {
        const res = await fetch(_url, { signal: abortCtrl.signal })
        const data = await res.json()
        setIsPending(false)
        setError(null)
        setData(data)
      } catch (err) {
        if (!abortCtrl.signal?.aborted) {
          setIsPending(false)
          setError(err.message)
        }
      }
    }
    asyncFetchData(URL.baseUrl + url)

    return () => abortCtrl.abort()
  }, [url])

  return { data, isPending, error }
}

export default useFetch
