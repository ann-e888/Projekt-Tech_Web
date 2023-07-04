import { useState, useEffect } from "react";
import { MainNav } from "@/components/MainNav";
import { DataTable } from "./components/DataTable";
import { Columns } from "./components/Columns";
import { UserNav } from "./components/UserNav";
import { navigationLinks } from "../../config/navigationLinks";


export const CustomersPage = () => {
  const [customersInfo, setCustomersInfo] = useState([]);

  const fetchCustomersInfo = () => {
    fetch("http://127.0.0.1:8000/customers")
      .then((res) => res.json())
      .then((data) => {
        const mappedData = data.map((customer) => ({
          fullname: `${customer.name} ${customer.surname}`,
          email: customer.email,
          phoneNumber: customer.phone_number,
        }));
        setCustomersInfo(mappedData);
      });
  };
  
  
  useEffect(() => {
    fetchCustomersInfo();
  }, []);

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
          <h2 className="text-3xl font-bold tracking-tight">Customers</h2>
        </div>
        <div className="hidden h-full flex-1 flex-col space-y-8 md:flex">
        <DataTable
            data={customersInfo}
            columns={Columns}
          />
        </div>
      </div>
    </div>
  );
};



