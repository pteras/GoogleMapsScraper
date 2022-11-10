import React from "react";

const UserInputField = () => {
  const [userInput, setUserInput] = React.useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(userInput);
  };

  const handleChange = (event) => {
    setUserInput(event.target.value);
  };

  return (
    <div>
      <form onSubmit={(e) => handleSubmit(e)}>
        <label htmlFor="userInput">Enter an address:</label>
        <input type="text" onChange={(e) => handleChange(e)} />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default UserInputField;
