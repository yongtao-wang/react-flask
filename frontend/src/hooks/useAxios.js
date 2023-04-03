import { useEffect, useState } from 'react'
import axios from '../utils/Axios'

const useAxiosFactory = () => {
  const [data, setData] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const [abortCtrl, setAbortCtrl] = useState()

  const asyncAxiosAPI = async (config) => {
    const { axiosInstance, method, url, requestConfig = {} } = config

    try {
      setIsLoading(true)
      const ctrl = new AbortController()
      setAbortCtrl(ctrl)
      const response = await axiosInstance[method.toLowerCase()](url, {
        ...requestConfig,
        signal: ctrl.signal,
      })
      setError(null)
      setData(response.data)
    } catch (err) {
      // Not in the 200 response range
      if (!abortCtrl.signal?.aborted) {
        setError(err.message)
        setData()
      }
    } finally {
      setIsLoading(false)
    }
  }

  useEffect(() => {
    return () => abortCtrl && abortCtrl.abort()
  }, [abortCtrl])

  return { data, isLoading, error, asyncAxiosAPI }
}

export const useAxiosGet = (url, config = {}) => {
  const { data, isLoading, error, asyncAxiosAPI: api } = useAxiosFactory()
  const axiosGet = (_api, _url, _config) => {
    _api({
      axiosInstance: axios,
      method: 'GET',
      url: _url,
      requestConfig: _config,
    })
  }
  useEffect(() => {
    axiosGet(api, url, config)
  }, []) // eslint-disable-line react-hooks/exhaustive-deps

  return { data, isLoading, error }
}

export const useAxiosPost = (url, config) => {
  const { data, isLoading, error, asyncAxiosAPI: api } = useAxiosFactory()
  const axiosPost = (_api, _url, _config) => {
    _api({
      axiosInstance: axios,
      method: 'POST',
      url: _url,
      requestConfig: _config,
    })
  }

  useEffect(() => {
    axiosPost(api, url, config)
  }, []) // eslint-disable-line react-hooks/exhaustive-deps

  return { data, isLoading, error }
}

export const useAxiosDelete = (url, config = {}) => {
  const { data, isLoading, error, asyncAxiosAPI: api } = useAxiosFactory()
  const axiosDelete = (_api, _url, _config) => {
    _api({
      axiosInstance: axios,
      method: 'DELETE',
      url: _url,
      requestConfig: _config,
    })
  }

  useEffect(() => {
    axiosDelete(api, url, config)
  }, []) // eslint-disable-line react-hooks/exhaustive-deps

  return { data, isLoading, error }
}
