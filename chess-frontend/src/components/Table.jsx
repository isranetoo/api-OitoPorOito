export default function Table({ columns, data }) {
  return (
    <div className="overflow-x-auto mt-4">
      <table className="min-w-full border border-gray-300 bg-white">
        <thead>
          <tr className="bg-gray-200">
            {columns.map((col) => (
              <th key={col} className="px-4 py-2 border border-gray-300">{col}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.length > 0 ? (
            data.map((row, idx) => (
              <tr key={idx} className="hover:bg-gray-100">
                {columns.map((col) => (
                  <td key={col} className="px-4 py-2 border border-gray-300">
                    {row[col] ?? "-"}
                  </td>
                ))}
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan={columns.length} className="text-center py-4">
                Nenhum dado encontrado
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
