import React from 'react'
import { SideBar, ChatBox } from '../components/index'

const Chat = () => {
  return (
    <div className="flex h-screen">
      <div className="w-24 bg-blue-100 p-4 hidden sm:block md:block lg:block xl:block 2xl:border-s-black">
        <SideBar/>
      </div>
      <div className="flex-grow p-4 sm:ml-14 md:ml-14 lg:ml-14 xl:ml-14 2xl:ml-14">
        <ChatBox/>
      </div>
    </div>
  )
}

export default Chat