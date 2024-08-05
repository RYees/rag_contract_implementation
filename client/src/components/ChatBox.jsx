import React,{useRef, useState, useEffect} from 'react'
import '../styles/chatbox.css'
import contract from '../assets/contract.png';
import { UploadFile } from '../components'
import Api from '../services/service';

export default function ChatBox() {
  const [input, setInput] = useState("")
  const [open, setOpen] = useState(false);
  const [show, setShow] = useState(false);
  const [view, setView] = useState(false);
  const [load, setLoad] = useState(false);
  const [chatHistory, setChatHistory] = useState([]);
   
  const handler = (event) => {
    if (event.keyCode === 13) {      
      handleChatInput();
    }
  };

  function handleChatInput() {
    const data = { sender: "user", text: input };
    if (input !== "") {
      setChatHistory((history) => [...history, data]);
      chatWithOpenai(input);    
      setInput("");  
    }
  }
  
  async function chatWithOpenai(query) {   
      setLoad(true)
      const requestOptions = {
        question: query
      };

      const response = await Api.ragengine(requestOptions);
 
      const data = {
        sender: "bot",
        text: response.data
      };

      setChatHistory((history) => [...history, data]);
      setInput("");     
      setLoad(false)     
  }

  
  return (
    <>
      <div className='flex flex-col sm:flex-row md:flex-row lg:flex-row xl:flex-row 2xl:flex-row gap-6 sm:gap-20 md:gap-20 lg:gap-20 xl:gap-20 2xl:gap-20'>  
        <div className='chat_tag sm:w-[36rem] md:w-[36rem] lg:w-[36rem] xl:w-[36rem] 2xl:w-[36rem] sm:my-20 md:my-20 lg:my-20 xl:my-20 2xl:my-20 px-4 text-center'>
            <div className='hidden sm:block md:block lg:block xl:block 2xl:block'>
              <img className='h-64 mx-auto mb-5' src={contract}/>
              <h1 className='text-4xl'>
                  Contract Loaded and Ready
              </h1>
              <p className='text-lg text-gray-500'>
                  You can now start discussing the contract in the chat.
              </p>
            </div>
            <div className='mx-16 sm:mx-0 md:mx-0 lg:mx-0 xl:mx-0 2xl:mx-0 sm:mt-5 sm:ml-5 w-10 sm:w-full md:w-full lg:w-full xl:w-full 2xl:w-full'>
                <p className='mb-3 w-96 sm:w-full md:w-full lg:w-full xl:w-full 2xl:w-full'>Want to replace contract?</p>
                <UploadFile className=""/>
            </div>
        </div>

        <div className='relative w-[35rem] sm:w-[40rem] md:w-[40rem] lg:w-[40rem] xl:w-[35rem] 2xl:w-[20rem] space-y-1'>
            <div className='chatbox h-[40rem] rounded-lg border-2 border-slate-100 shadow-sm overflow-auto'>
                <div className='border-slate-150 border-t-[2rem]'>
                    {chatHistory?.map((message, index) => (
                    <div key={index} className={`${message.sender} ml-4 mt-3`}>
                        {message.sender === "user" ? (
                        <div className="user">
                            <div className="mx-1 my-2">
                            <p className="">{message.text}</p>
                            </div>
                        </div>
                        ):(
                        <div className='ai mt-1 py-2 mx-6'>
                        {message.sender === "bot" && (
                            <div className="user">
                                <div className="bg-white p-3 rounded inline-block max-w-fit">                               
                                  <p className="text-gray-500">{message.text}</p>                                
                                </div>
                            </div>
                        )}
                        </div>
                        )}
                    </div>
                    ))}
                     {load? <p className='mx-6'><small>loading...</small></p>:null}
                </div>
            </div>

            <div className='bg-slate-100'>        
                <input             
                    className="w-[100%] text-sm py-2 text-center border-2 border-slate-100 rounded-full p-1"    
                    type="text"
                    value={input}
                    placeholder="Type your question"
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => handler(e)}
                />
            </div>
        </div>
      </div>
    </>
  )
}