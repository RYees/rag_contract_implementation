import React, {useState} from 'react'
import { FileUploader } from "react-drag-drop-files";
import Api from '../services/service';

const fileTypes = ["JPG", "PNG", "GIF", "PDF"];

const UploadFile = () => {
  const [file, setFile] = useState(null);
  const handleChange = (file) => {
    setFile(file);
    console.log("can", file)
    //sendFile()
  };

  const sendFile = async() =>{
    const formData = new FormData();
    formData.append('file', file);
    const response = await Api.ragengine(formData);
    console.log("foine", response)
  }

  return (
    <FileUploader 
    handleChange={handleChange} 
    name="file" 
    types={fileTypes} 
    />
  );
}

export default UploadFile

