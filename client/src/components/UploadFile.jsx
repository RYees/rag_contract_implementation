import React, {useState} from 'react'
import { FileUploader } from "react-drag-drop-files";
import Api from '../services/service';

const fileTypes = ["JPG", "PNG", "GIF", "PDF"];

const UploadFile = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState();
  const [load, setLoad] = useState(false);

  const handleChange = (file) => {
    setFile(file);
    console.log("can", file)
    //sendFile()
  };

  const sendFile = async() =>{
    const formData = new FormData();
    formData.append('file', file);
    const response = await Api.uploadpdf(formData);
    console.log("foine", response)
  }

  async function upload_pdf_vector_db() {   
    setLoad(true)
    const requestOptions = {
      file_path: '../data/RaptorContract.pdf'
    };

    const response = await Api.uploadpdf(requestOptions);
    console.log("ov", response.data.response)
    setMessage("Analysing the document done! Ready to answer your questions.")
    setLoad(false)
     
}

  return (
    <>
      <FileUploader 
      handleChange={handleChange} 
      name="file" 
      types={fileTypes} 
      />
      <button onClick={upload_pdf_vector_db}>
        {load? 'processing...' : 'Process File'}
      </button>
      {message}
    </>
  );
}

export default UploadFile

