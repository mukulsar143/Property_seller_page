// PropertyList.js
import React from "react";
import { Link } from 'react-router-dom';
import "bootstrap/dist/css/bootstrap.min.css"; // Import Bootstrap CSS

function PropertyList({ properties, search, setsearch, handleSearch }) {

  const handleSubmit = (event) => {
    event.preventDefault();
    handleSearch({ location : search.location, cost : search.cost });
  };

  const user = localStorage.getItem('Role')
  
  return (
    <>
      <form className="d-flex container mt-3" onSubmit={handleSubmit} >
        <input
          className="form-control me-2"
          style={{ marginLeft: "10px", width: "200px" }}
          type="text"
          placeholder="Search..."
          name="location"
          value={search.location}
          onChange={(e) => setsearch(e.target.value)}
          aria-label="Search"
        />
        <button className="btn btn-outline-success" type="submit">
          Search
        </button>
        {user === 'property_owner' ?<Link to="/add">
          <button className="btn btn-secondary" style={{ marginLeft: "740px" }}>
            (+) Add
          </button>
        </Link>:''}
        
      </form>
      <div className="container" style={{fontFamily: 'monospace'}}>
        <h2 className="mt-3 mb-3" style={{ fontFamily: "monospace" }}>
          Properties for Sale
        </h2>
        <ul className="list-group">
          {properties.map((property) => (
            <li className="list-group-item" key={property.id}>
              <div className="d-flex w-100 justify-content-between">
                <h5 className="mb-1">{property.location}</h5>
                <small>${property.cost}</small>
              </div>
              <p className="mb-1">{property.rooms}Rooms</p>
              <small>
              Owner - {property.owner.email}
              </small>
              <br/>
              <small>
              Status - {property.status}
              </small>
            </li>
          ))}
        </ul>
    

      </div>
    </>
  );
}

export default PropertyList;
