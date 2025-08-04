import { useEffect, useState } from "react";
import axios from "axios";
import Table from "../components/Table";

export default function GamesPage() {
  const [games, setGames] = useState([]);
  const [mode, setMode] = useState("");
  const [page, setPage] = useState(1);

  useEffect(() => {
    let url = `http://127.0.0.1:8000/games?page=${page}&limit=5&sort_by=started_at&order=desc`;
    if (mode) url = `http://127.0.0.1:8000/games/mode/${mode}?page=${page}&limit=5`;
    axios.get(url)
      .then(res => setGames(res.data))
      .catch(err => console.error(err));
  }, [mode, page]);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Games</h1>
      <div className="flex gap-2 my-2">
        <select value={mode} onChange={e => setMode(e.target.value)} className="border p-1">
          <option value="">Todos</option>
          <option value="blitz">Blitz</option>
          <option value="bullet">Bullet</option>
          <option value="rapid">Rapid</option>
        </select>
        <button onClick={() => setPage(p => Math.max(1, p - 1))} className="px-2 py-1 bg-gray-200">⬅</button>
        <span>Página {page}</span>
        <button onClick={() => setPage(p => p + 1)} className="px-2 py-1 bg-gray-200">➡</button>
      </div>
      <Table columns={["id", "white_player_id", "black_player_id", "mode", "result", "started_at"]} data={games} />
    </div>
  );
}
