import React from "react";
import { useEffect, useState } from "react";

const Form = () => {
  // const [userInput, setUserInput] = useState("");
  const [address, setAddress] = useState("");
  const [radius, setRadius] = useState(null);
  const [businessType, setBusinessType] = useState("");

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const handleChange = (event, setFunc) => {
    // setUserInput(event.target.value);
    setFunc(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log(JSON.stringify({ address, radius, businessType }));
    let data = await fetch("http://localhost:5000/api/scraper", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ address, radius, businessType }),
    });
    data = await data.json();
    console.log(data);
  };
  return (
    <div>
      <form onSubmit={(e) => handleSubmit(e)}>
        <label htmlFor="address">Enter an address:</label>
        <input type="text" onChange={(e) => handleChange(e, setAddress)} />
        {/* <input type="text" /> */}

        <label htmlFor="radius">Enter a radius:</label>
        <input type="text" onChange={(e) => handleChange(e, setRadius)} />
        {/* <input type="text" /> */}

        <label htmlFor="business">Enter a type of business:</label>
        <input type="text" onChange={(e) => handleChange(e, setBusinessType)} />
        {/* <input type="text" /> */}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Form;
