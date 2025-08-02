import { useEffect, useState } from "react";
import axios from "axios";

export default function TopPlayers() {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/ratings")
      .then(res => setPlayers(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="p-6 bg-gray-900 min-h-screen text-white">
      <h1 className="text-3xl font-bold mb-6 text-yellow-400">🏆 Top 10 Players - August 2025</h1>
      <div className="overflow-x-auto">
        <table className="min-w-full border border-gray-700 rounded-lg overflow-hidden">
          <thead className="bg-gray-800">
            <tr>
              <th className="px-4 py-2">#</th>
              <th className="px-4 py-2 text-left">Name</th>
              <th className="px-4 py-2">Fed</th>
              <th className="px-4 py-2">Rating</th>
              <th className="px-4 py-2">B-Year</th>
            </tr>
          </thead>
          <tbody>
            {players.map((p) => (
              <tr key={p.rank} className="hover:bg-gray-700 transition">
                <td className="px-4 py-2 text-center font-bold">{p.rank}</td>
                <td className="px-4 py-2">{p.name}</td>
                <td className="px-4 py-2 text-center">{p.federation}</td>
                <td className="px-4 py-2 text-center text-yellow-400 font-bold">{p.rating}</td>
                <td className="px-4 py-2 text-center">{p.birth_year}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
