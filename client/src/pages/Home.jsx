import React from 'react'
import "../styles/home.css"
import { UploadFile } from '../components'
import Api from '../services/service'

const Home = () => {
  const test = async() => {
    console.log(await Api.fetchTest())
  }
  


  return (
    <>
    <div className='home h-screen flex flex-col justify-center items-center'>
          <div className='text-center mb-10'>
            <button onClick={test}>test</button>
            <h1 className='text-5xl'>Intelligent Legal Contract Guidance</h1>
            <p className='text-gray-600'>Powered by Advanced AI Technology</p>
          </div>

          <div>
            <UploadFile/>
          </div>
      </div>
    </>
  )
}

export default Home