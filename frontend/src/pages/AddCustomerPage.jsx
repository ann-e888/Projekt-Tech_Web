import { MainNav } from "@/components/MainNav";
import { navigationLinks } from "../config/navigationLinks";
import { UserNav } from "./CustomersPage/components/UserNav";
import { useState } from "react";

export const AddCustomerPage = () => {
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [email, setEmail] = useState("");
  const [phone_number, setNumber] = useState("");
  const [resMessage, setResMessage] = useState("");

  const getName = (event) => {
    setName(event.target.value);
  };
  const getSurname = (event) => {
    setSurname(event.target.value);
  };
  const getEmail = (event) => {
    setEmail(event.target.value);
  };
  const getNumber = (event) => {
    setNumber(event.target.value);
  };
  const submitFormHandler = async (event) => {
    event.preventDefault();
    if (
      name === "" ||
      surname === "" ||
      email === "" ||
      phone_number === "" ||
      phone_number.length !== 9
    ) {
      return;
    };

    const customerInfo = {
      name: name,
      surname: surname,
      email: email,
      phone_number: phone_number
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/customers", {
        method: "POST",
        body: JSON.stringify(customerInfo),
        headers: {
          "Content-Type": "application/json",
        },
      });
  
      console.log(response);
  
      if (!response.ok) {
        setResMessage("Could not add customer");
        throw new Error(response.message || "Could not add customer");
      }
  
      setName("");
      setSurname("");
      setEmail("");
      setNumber("");
    } catch (error) {
      console.error(error);
    }
  };
  
  return (
    <div className="hidden flex-col md:flex">
      <div className="border-b">
        <div className="flex h-16 items-center px-4">
          <MainNav className="mx-6" links={navigationLinks} />
          <div className="ml-auto flex items-center space-x-4">
            <UserNav />
          </div>
        </div>
      </div>
      <div className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex items-center justify-between space-y-2">
          <h2 className="text-3xl font-bold tracking-tight">Add customer</h2>
        </div>
        <div className="hidden h-full flex-1 flex-col space-y-8 md:flex"></div>
      </div>
      <form onSubmit={submitFormHandler} className="customerAdd">
        <label>Name</label>
        <input
          onChange={getName}
          value={name}
          placeholder="John"
          type="text"
        ></input>
        <label>Surname</label>
        <input
          onChange={getSurname}
          value={surname}
          placeholder="Smith"
          type="text"
        ></input>
        <label>Email</label>
        <input
          onChange={getEmail}
          value={email}
          placeholder="johnsmith@email.com"
          type="text"
        ></input>
        <label>Phone Number</label>
        <input
          onChange={getNumber}
          value={phone_number}
          placeholder="999 999 999"
          type="text"
        ></input>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};



