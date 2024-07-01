import React,{useRef, useState, useEffect} from 'react'
import '../styles/chatbox.css'
import contract from '../assets/contract.png';
import { UploadFile } from '../components'

export default function ChatBox() {
  const [input, setInput] = useState("")
  const [open, setOpen] = useState(false);
  const [show, setShow] = useState(false);
  const [view, setView] = useState(false);
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
  
  async function chatWithOpenai(text) {   
      const data = {
        sender: "bot",
        text: "ai"
      };
      setChatHistory((history) => [...history, data]);
      setInput("");          
  }

  
  return (
    <>
      <div className='flex gap-20'>  
        <div className='chat_tag w-[36rem] my-20 px-4 text-center'>
            <img className='h-64 mx-auto mb-5' src={contract}/>
            <h1 className='text-4xl'>
                Contract Loaded and Ready
            </h1>
            <p className='text-lg text-gray-500'>
                You can now start discussing the contract in the chat.
            </p>
            <div className='mt-5 ml-5'>
                <p className='mb-3'>Want to replace contract?</p>
                <UploadFile className=""/>
            </div>
        </div>

        <div className='relative w-[40rem] space-y-1'>
            <div className='chatbox h-[45rem] rounded-lg border-2 border-slate-100 shadow-sm'>
                <div className=' border-slate-150 border-t-[2rem]'>
                    {chatHistory?.map((message, index) => (
                    <div key={index} className={`chatcontain ${message.sender}`}>
                        {message.sender === "user" ? (
                        <div className="user">
                            <div className="">
                            <p className="parauser">{message.text}</p>
                            </div>
                        </div>
                        ):(
                        <div className='ai'>
                        {message.sender === "bot" && (
                            <div className="user">
                                <div className="">
                                <p className="parauser">{message.text}</p>
                                </div>
                            </div>
                        )}
                        </div>
                        )}
                    </div>
                    ))}
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