import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME || 'localhost';
  const protocol = codespaceName === 'localhost' ? 'http' : 'https';
  const endpoint = `${protocol}://${codespaceName}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboard(results);
        console.log('Leaderboard endpoint:', endpoint);
        console.log('Fetched leaderboard:', results);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  return (
    <div>
      <h2 className="mb-4">Leaderboard</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped table-bordered">
            <thead className="table-dark">
              <tr>
                <th>Team</th>
                <th>Points</th>
                <th>Rank</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry, idx) => (
                <tr key={idx}>
                  <td>{entry.team}</td>
                  <td>{entry.points}</td>
                  <td>{entry.rank}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
