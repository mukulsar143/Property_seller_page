// Navbar.js
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from 'react-router-dom';

function Navbar() {
  const user = localStorage.getItem('Role')
  const naviagte = useNavigate()

  const logout = () =>{
    localStorage.removeItem('Role')
    localStorage.removeItem('token')
    naviagte('/login')
  }
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <Link to='/' className="navbar-brand" style={{marginLeft:'20px', fontFamily:"cursive"}}>Property</Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
           { user?<button type="submit" className="btn btn-primary" onClick={logout} style={{marginRight: '10px'}}>Log Out</button>:
            <><Link to='/register'><button type="submit" className="btn btn-primary" style={{marginRight: '10px'}}>Register</button></Link>
            <Link to='/login'><button type="submit" className="btn btn-primary" style={{marginRight: '10px'}}>Login</button></Link></>}
          </ul>
        </div>
    </nav>
  );
}

export default Navbar;
