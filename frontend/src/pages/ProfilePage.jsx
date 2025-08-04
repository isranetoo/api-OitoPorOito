import { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

export default function ProfilePage() {
  const { username } = useParams();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/profile/${username}`)
      .then(res => setProfile(res.data))
      .catch(err => console.error(err));
  }, [username]);

  if (!profile) return <p className="text-white p-4">Carregando...</p>;

  return (
    <div className="bg-gray-900 text-white min-h-screen p-6">
      {/* Header */}
      <div className="flex items-center mb-6">
        <img
          src={profile.profile_picture}
          alt={profile.username}
          className="w-20 h-20 rounded-full mr-4"
        />
        <div>
          <h1 className="text-2xl font-bold">{profile.name}</h1>
          <p className="text-gray-400">@{profile.username}</p>
          {profile.global_rank && (
            <p className="text-yellow-400 font-semibold">
              🌍 #{profile.global_rank} - {profile.federation} ({profile.global_rating})
            </p>
          )}
        </div>
      </div>

      {/* Ratings */}
      {profile.ratings && (
        <>
          <h2 className="text-xl font-semibold mb-2">Ratings</h2>
          <div className="grid grid-cols-2 gap-4 mb-6">
            <div className="bg-gray-800 p-4 rounded">Bullet: <span className="font-bold">{profile.ratings.bullet}</span></div>
            <div className="bg-gray-800 p-4 rounded">Blitz: <span className="font-bold">{profile.ratings.blitz}</span></div>
            <div className="bg-gray-800 p-4 rounded">Rapid: <span className="font-bold">{profile.ratings.rapid}</span></div>
            <div className="bg-gray-800 p-4 rounded">Diário: <span className="font-bold">{profile.ratings.daily}</span></div>
          </div>
        </>
      )}

      {/* Histórico de Partidas */}
      {profile.game_history && profile.game_history.length > 0 && (
        <>
          <h2 className="text-xl font-semibold mb-2">Histórico de Partidas</h2>
          <table className="w-full border-collapse">
            <thead className="bg-gray-800">
              <tr>
                <th className="px-4 py-2 text-left">Oponente</th>
                <th className="px-4 py-2">Modo</th>
                <th className="px-4 py-2">Resultado</th>
                <th className="px-4 py-2">Data</th>
              </tr>
            </thead>
            <tbody>
              {profile.game_history.map((game, idx) => (
                <tr key={idx} className="border-b border-gray-700">
                  <td className="px-4 py-2">{game.opponent}</td>
                  <td className="px-4 py-2 text-center">{game.mode}</td>
                  <td className={`px-4 py-2 text-center ${
                    game.result === "win"
                      ? "text-green-400"
                      : game.result === "loss"
                      ? "text-red-400"
                      : "text-yellow-400"
                  }`}>
                    {game.result}
                  </td>
                  <td className="px-4 py-2 text-center">
                    {new Date(game.played_at).toLocaleDateString()}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
    </div>
  );
}
