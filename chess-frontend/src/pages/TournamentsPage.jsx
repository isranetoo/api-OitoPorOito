import { useEffect, useState } from "react";
import axios from "axios";
import Table from "../components/Table";

export default function TournamentsPage() {
  const [tournaments, setTournaments] = useState([]);
  const [type, setType] = useState("");

  useEffect(() => {
    let url = "http://127.0.0.1:8000/tournaments";
    if (type) url = `http://127.0.0.1:8000/tournaments/type/${type}`;
    axios.get(url)
      .then(res => setTournaments(res.data))
      .catch(err => console.error(err));
  }, [type]);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Tournaments</h1>
      <div className="flex gap-2 my-2">
        <select value={type} onChange={e => setType(e.target.value)} className="border p-1">
          <option value="">Todos</option>
          <option value="arena">Arena</option>
          <option value="round_robin">Round Robin</option>
        </select>
      </div>
      <Table columns={["id", "name", "type", "mode", "start_date", "end_date"]} data={tournaments} />
    </div>
  );
}
