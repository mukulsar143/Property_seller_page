// App.js
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Properties from './Components/Properties';
import PropertyForm from './Components/PropertyForm';
import { useState, useEffect } from 'react';
import Navbar from './Components/Navbar';
import UserForm from './Components/UserForm';
import Login from './Components/Login';


function App() {

  const [properties, setProperties] = useState([]);
  const [search, setsearch] = useState('')


  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/get/')  
      .then(response => response.json())
      .then(data => setProperties(data))
      .catch(error => console.error('Error fetching properties:', error));
  }, []);

  const handleSearch = () => {
    fetch(`http://127.0.0.1:8000/api/get/?search=${search}`)  
    .then(response => response.json())
    .then(data => setProperties(data))
    .catch(error => console.error('Error fetching properties:', error));
  };

  return (
    <>
     <Router>
      <Navbar/>
      <div>
        <Routes>
          <Route exact path="/" element = {<Properties properties = {properties} handleSearch={handleSearch} search = {search}  setsearch = {setsearch} />}>            
          </Route>
          <Route path="/add" element = {<PropertyForm />}>
          </Route>
          <Route path="/register" element = {<UserForm />}>
          </Route>
          <Route path="/login" element = {<Login />}>
          </Route>
        </Routes>
      </div>
    </Router>
    </>
  );
}

export default App;
