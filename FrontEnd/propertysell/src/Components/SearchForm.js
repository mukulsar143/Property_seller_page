// SearchForm.js
import React from 'react';
import { Link } from 'react-router-dom';

function SearchForm({ handleSearch, search, setsearch }) {

  const handleSubmit = (event) => {
    event.preventDefault();
    handleSearch({ location : search.location, cost : search.cost });
  };

  return (
    <>
    <form className="d-flex container mt-3" onSubmit={handleSubmit}>
            <input className="form-control me-2" style={{marginLeft: '10px' ,width : "200px"}} type="text" placeholder="Search..." name='location' value={search.location} onChange={e => setsearch(e.target.value)} aria-label="Search" />
            <button className="btn btn-outline-success" type="submit">Search</button>
            <Link to='/sell'><button className="btn btn-secondary" style={{marginLeft:'740px'}}>(+) Add</button></Link>
    </form>
    </>
  );
}

export default SearchForm;
