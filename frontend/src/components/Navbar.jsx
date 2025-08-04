import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-gray-900 text-white px-4 py-3 flex gap-4">
      <Link to="/">🏠 Home</Link>
      <Link to="/users">👤 Users</Link>
      <Link to="/games">♟ Games</Link>
      <Link to="/puzzles">🧩 Puzzles</Link>
      <Link to="/tournaments">🏆 Tournaments</Link>
      <Link to="/clubs">👥 Clubs</Link>
      <Link to="/top-players">🌟 Top Players</Link>
    </nav>
  );
}
