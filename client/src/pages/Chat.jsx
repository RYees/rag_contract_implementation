import React from 'react'
import { SideBar, ChatBox } from '../components/index'

const Chat = () => {
  return (
    <div className="flex h-screen">
      <div className="w-24 bg-blue-100 p-4">
        <SideBar/>
      </div>
      <div className="flex-grow p-4">
        <ChatBox/>
      </div>
    </div>
  )
}

export default Chat