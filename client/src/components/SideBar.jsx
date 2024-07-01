import { NavLink } from 'react-router-dom';
import '../styles/sidebar.css';

const SideBar = () => {
 return (
 <nav className='float-left'>
       <ul className='flex flex-col justify-between bg-slate-600'>
         <div>
            <li>
               <NavLink to="/">Home</NavLink>
            </li>
            <li>
               <NavLink to="" className='flex flex-col'>
                  Upload <small>Another</small>
               </NavLink>
            </li>
         </div>

         <div>
            <li>
               <NavLink to="/profile">Profile</NavLink>
            </li>
            <li>
               <NavLink to="/setting">Setting</NavLink>
            </li>
            <li>
               <NavLink to="/">Logout</NavLink>
            </li>
         </div>
       </ul>
 </nav>
 );
};

export default SideBar;