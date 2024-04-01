// PropertyForm.js
import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { useNavigate } from "react-router-dom";

function PropertyForm() {
  const [forms, setForms] = useState({ email: "", password: "", role: "" });
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("http://127.0.0.1:8000/api/accounts/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(forms),
    });
    let json = await res.json();

    if (json.response.success) {
      navigate("/");
      localStorage.setItem("Role", json.data.role);
      localStorage.setItem('token', json.response.token)
      alert("Login In Successfully", "success");
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
        Login to Continew Home Page...{" "}
      </h2>
      <div className="mb-3">
        <label htmlFor="address" className="form-label">
          Email
        </label>
        <input
          type="text"
          id="address"
          name="email"
          className="form-control"
          placeholder="Enter address"
          value={forms.email}
          onChange={onchangvalue}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="role" className="form-label">
          Role
        </label>
        <select
          id="role"
          className="form-select"
          value={forms.role}
          name="role"
          onChange={onchangvalue}
        >
          <option value="">Role</option>
          <option value="property_owner">Property Owner</option>
          <option value="buyer">Buyer</option>
        </select>
      </div>
      <div className="mb-3">
        <label htmlFor="address" className="form-label">
          Password
        </label>
        <input
          type="password"
          id="password"
          className="form-control"
          name="password"
          placeholder="Enter Rooms"
          value={forms.password}
          onChange={onchangvalue}
        />
      </div>
      <button type="submit" className="btn btn-primary">
        Login
      </button>
    </form>
  );
}

export default PropertyForm;
