import axios from 'axios' 

const Api = {
  ragengine: data => axios.post('http://127.0.0.1:5000/api/rag_engine', data),
  multiquery: data => axios.post('http://127.0.0.1:5000/api/multiquery', data),
  fetchTest: data => axios.get('http://127.0.0.1:5000/'),
  uploadpdf: data => axios.get('http://127.0.0.1:5000/upload', data)
};

export default Api;