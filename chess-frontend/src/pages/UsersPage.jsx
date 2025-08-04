import { useEffect, useState } from "react";
import axios from "axios";
import Table from "../components/Table";
import { useNavigate } from "react-router-dom";

export default function UsersPage() {
  const [users, setUsers] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/users")
      .then(res => setUsers(res.data.data || res.data))
      .catch(err => console.error(err));
  }, []);

  // Função que vai ser chamada ao clicar numa linha da tabela
  const handleRowClick = (user) => {
    if (user.username) {
      navigate(`/profile/${user.username}`);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Usuários</h1>
      <Table
        columns={["id", "username", "email", "country_code", "bio"]}
        data={users}
        onRowClick={handleRowClick} // passa para o Table
      />
    </div>
  );
}
