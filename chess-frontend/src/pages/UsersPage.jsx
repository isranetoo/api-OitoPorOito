import { useEffect, useState } from "react";
import axios from "axios";
import Table from "../components/Table";

export default function UsersPage() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/users")
      .then(res => setUsers(res.data.data || res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Users</h1>
      <Table columns={["id", "username", "email", "country_code", "bio"]} data={users} />
    </div>
  );
}
