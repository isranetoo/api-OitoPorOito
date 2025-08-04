import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import UsersPage from "./pages/UsersPage";
import GamesPage from "./pages/GamesPage";
import PuzzlesPage from "./pages/PuzzlesPage";
import TournamentsPage from "./pages/TournamentsPage";
import ClubsPage from "./pages/ClubsPage";
import TopPlayers from "./pages/TopPlayers";
import ProfilePage from "./pages/ProfilePage";

export default function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<h1 className="p-4">Bem-vindo ao Chess API Frontend</h1>} />
        <Route path="/users" element={<UsersPage />} />
        <Route path="/games" element={<GamesPage />} />
        <Route path="/puzzles" element={<PuzzlesPage />} />
        <Route path="/tournaments" element={<TournamentsPage />} />
        <Route path="/clubs" element={<ClubsPage />} />
        <Route path="/top-players" element={<TopPlayers />} />
        <Route path="/profile/:username" element={<ProfilePage />} />
        <Route path="*" element={<h1 className="p-4">Página não encontrada</h1>} />
      </Routes>
    </Router>
  );
}
