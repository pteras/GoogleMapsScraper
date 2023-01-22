import React from "react";
import { useState } from "react";
import "../css/styles.css";
import httpClient from "../httpClient";

const Form = () => {

  const [user, setUser] = useState(null);

  // TODO: Fix this so it doesn't do unneccesary requests
  useState (() => {
    (async () => {
      try {
      const response = await httpClient.get("//localhost:5000/@me");
      setUser(response.data.username);
      } catch (error) {
        console.log("Not authenticated")
      }
    })();
  });

  const [address, setAddress] = useState("");
  const [radius, setRadius] = useState(null);
  const [businessType, setBusinessType] = useState("restaurant");
  const [isFetched, setIsFetched] = useState(false);

  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (event, setFunc) => {
    // setUserInput(event.target.value);
    setFunc(event.target.value);
  };

  const color = (rating) => {
    if (rating >= 4) {
      return "green";
    } else if (rating < 4) {
      return "yellow";
    } else {
      return "red";
    }
  };

  const color_open = (open_now) => {
    if (open_now) {
      return "green";
    } else return "red";
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    console.log(JSON.stringify({ address, radius, businessType }));
    let data = await fetch("http://localhost:5000/api/scraper", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ address, radius, businessType }),
    });
    data = await data.json();
    setIsFetched(true);

    setLoading(false);
    data.success ? setData(data.data) : setError(data.error);

    console.log(data);
  };
  return (
    <div className="form">
      <div>
        {user != null ? (
          <a href="/login">
            <div className="subtitle">
              <strong>Logged in as {user}</strong>
            </div>
          </a>
        ) : (
          <a href="/login">
            <button className="logbtn">
              <strong>Login</strong>
            </button>
          </a>
        )}
      </div>
      <div className="title">Google Maps Scraper</div>
      <div className="subtitle">Start searching places!</div>
      <form onSubmit={(e) => handleSubmit(e)}>
        <div className="input-container">
          <input
            id="address"
            className="input"
            type="text"
            placeholder=" "
            required
            onChange={(e) => handleChange(e, setAddress)}
          />
          <label htmlFor="address" className="placeholder">
            <strong>Enter an address: </strong>
          </label>
          {/* <input type="text" /> */}
        </div>
        <div className="input-container">
          <input
            id="radius"
            className="input"
            type="text"
            placeholder=" "
            required
            onChange={(e) => handleChange(e, setRadius)}
          />
          <label htmlFor="radius" className="placeholder">
            <strong>Radius in meters: </strong>
          </label>
          {/* <input type="text" /> */}
        </div>
        <div className="input-container">
          <select
            name="businessType"
            id="business"
            className="input"
            onChange={(e) => handleChange(e, setBusinessType)}
          >
            <option value="restaurant">Restaurant</option>
            <option value="bar">Bar</option>
            <option value="cafe">Cafe</option>
            <option value="atm">ATM</option>
            <option value="gym">Gym</option>
            <option value="church">Church</option>
            <option value="zoo">Zoo</option>
            <option value="plumber">Plumber</option>
            <option value="parking">Parking</option>
            <option value="airport">Airport</option>
          </select>

          {/* <input id="business" className="input" type="text" placeholder=" " onChange={(e) => handleChange(e, setBusinessType)} /> */}

          <label htmlFor="business" className="placeholder">
            <strong>Choose the business type: </strong>
          </label>
          {/* <input type="text" /> */}

        </div>

        {user != null ? (
          <button type="submit" className="button">
          <strong>Submit</strong>
        </button>
        ) : (
            <div>
              <br></br>
              <br></br>
              <a href="/login" className="button">
              <div className="subtitle">You are not logged in.</div>
              </a>
            </div>
        )}

      </form>

      {loading && (
        <div className="lds-ellipsis">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
        </div>
      )}

      {data.length > 0 && (
        <ul className="ul">
          <br></br>
          {data.map((item) => (
            <li key={item.name}>
              <h3 className="panel_header">{item.name}</h3>
              <p3>{item.address}</p3>
              <p>{`Distance: ${item.distance.value} ${
                item.distance.unit === "m" ? "meters" : "kilometers"
              } `}</p>
              <p style={{ color: color(item.rating) }}>
                {isNaN(item.rating) ? item.rating : `Rated ${item.rating} `}
              </p>
              <p style={{ color: color_open(item.open_now) }}>
                {item.open_now ? "Open" : "Closed"}
              </p>
              <br></br>
            </li>
          ))}
        </ul>
      )}

      {data.length === 0 && isFetched && (
        <div className="input-container">
          <h3 className="panel_header">No results found.</h3>
        </div>
      )}

      {error && <div>{error}</div>}
    </div>
  );
};

export default Form;
