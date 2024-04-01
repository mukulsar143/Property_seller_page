// PropertyForm.js
import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

function PropertyForm() {
  const [forms, setForms] = useState({
    location: "",
    cost: "",
    rooms: "",
    status: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("http://127.0.0.1:8000/api/properties/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Token ${localStorage.getItem("token")}`,
      },
      body: JSON.stringify(forms),
    });
    let json = await res.json();

    if (json.success) {
      alert("Added..");
      setForms('')
    } else {
      alert("semething went wrong..");
    }
  };

  const onchangvalue = (e) => {
    setForms({ ...forms, [e.target.name]: e.target.value });
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 border rounded container mt-3">
      <h2 className="mt-3 mb-3" style={{ fontFamily: "monospace" }}>
        Add Properties...
      </h2>
      <div className="mb-3">
        <label htmlFor="address" className="form-label">
          Location
        </label>
        <input
          type="text"
          id="address"
          className="form-control"
          name="location"
          placeholder="Enter address"
          value={forms.location}
          onChange={onchangvalue}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="address" className="form-label">
          Cost
        </label>
        <input
          type="text"
          id="address"
          className="form-control"
          name="cost"
          placeholder="Enter Cost"
          value={forms.cost}
          onChange={onchangvalue}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="address" className="form-label">
          Rooms
        </label>
        <input
          type="text"
          id="address"
          className="form-control"
          name="rooms"
          placeholder="Enter Rooms"
          value={forms.rooms}
          onChange={onchangvalue}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="status" className="form-label">
          Status
        </label>
        <select
          id="status"
          className="form-select"
          value={forms.status}
          name="status"
          onChange={onchangvalue}
        >
          <option value="">Status</option>
          <option value="available">Available</option>
          <option value="sold_out">Sold Out</option>
        </select>
      </div>
      <button type="submit" className="btn btn-primary">
        Add
      </button>
    </form>
  );
}

export default PropertyForm;
