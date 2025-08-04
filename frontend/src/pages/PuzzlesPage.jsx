import { useEffect, useState } from "react";
import axios from "axios";
import Table from "../components/Table";

export default function PuzzlesPage() {
  const [puzzles, setPuzzles] = useState([]);
  const [difficulty, setDifficulty] = useState("");

  useEffect(() => {
    let url = "http://127.0.0.1:8000/puzzles";
    if (difficulty) url = `http://127.0.0.1:8000/puzzles/difficulty/${difficulty}`;
    axios.get(url)
      .then(res => setPuzzles(res.data))
      .catch(err => console.error(err));
  }, [difficulty]);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Puzzles</h1>
      <div className="flex gap-2 my-2">
        <select value={difficulty} onChange={e => setDifficulty(e.target.value)} className="border p-1">
          <option value="">Todos</option>
          <option value="easy">Fácil</option>
          <option value="medium">Médio</option>
          <option value="hard">Difícil</option>
        </select>
      </div>
      <Table columns={["id", "fen", "theme", "difficulty"]} data={puzzles} />
    </div>
  );
}
