import { useEffect, useState } from "react";
import axios from "axios";
import Table from "../components/Table";

export default function ClubsPage() {
  const [clubs, setClubs] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/clubs")
      .then(res => setClubs(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Clubs</h1>
      <Table columns={["id", "name", "description", "owner_id", "created_at"]} data={clubs} />
    </div>
  );
}
