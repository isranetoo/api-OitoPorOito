export default function Table({ columns, data, onRowClick }) {
  return (
    <table className="w-full border-collapse bg-gray-800 text-white rounded-lg overflow-hidden">
      <thead className="bg-gray-700">
        <tr>
          {columns.map((col) => (
            <th key={col} className="px-4 py-2 text-left capitalize">
              {col.replace("_", " ")}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, idx) => (
          <tr
            key={idx}
            className={`border-b border-gray-600 hover:bg-gray-600 transition cursor-pointer`}
            onClick={() => onRowClick && onRowClick(row)} // clique na linha
          >
            {columns.map((col) => (
              <td key={col} className="px-4 py-2">
                {row[col]}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
