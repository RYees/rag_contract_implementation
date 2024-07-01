import { NavLink } from 'react-router-dom';
import { GoFileDirectory } from "react-icons/go";
import { RiHomeSmile2Line } from "react-icons/ri";
import { LuSettings } from "react-icons/lu";
import { AiOutlineLogout } from "react-icons/ai";
import { CgProfile } from "react-icons/cg";
import { LiaFileContractSolid } from "react-icons/lia";
import '../styles/sidebar.css';


const SideBar = () => {
   return (
     <nav className="flex flex-col justify-between h-full">
       <div className="space-y-4">
          <NavLink to="/" className="list">
              <div className="flex flex-col items-center">
                <RiHomeSmile2Line className="icons text-xl text-black" />
                <p className='list_name'>Home</p>
              </div>
          </NavLink>
          
          <NavLink to="#" className="list">
              <div className="flex flex-col items-center">
                <LiaFileContractSolid className="icons text-xl text-black" />
                <p className='list_name'>Review</p>
              </div>
          </NavLink>
       </div>
 
       <div className="flex flex-col space-y-4">
         <NavLink className="list flex flex-col" to="#">
          <div className="flex flex-col items-center">
            <CgProfile className="icons text-xl text-black"/>
            <p className='list_name'>Profile</p>
          </div>
         </NavLink>
         <NavLink className="list flex flex-col" to="#">
          <div className="flex flex-col items-center">
            <LuSettings className="icons text-xl text-black"/>
            <p className='list_name'>Setting</p>
          </div>
         </NavLink>
         <NavLink className="list flex flex-col" to="/">
          <div className="flex flex-col items-center">
            <AiOutlineLogout className="icons text-xl text-black"/>
            <p className='list_name'>Logout</p>
          </div>
         </NavLink>
       </div>
     </nav>
   );
 };



export default SideBar;