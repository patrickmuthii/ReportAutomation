import React, { useEffect, useState } from "react";
import { fetchReports } from "../api";

const Reports = () => {
  const [reports, setReports] = useState([]);

  useEffect(() => {
    fetchReports().then(data => setReports(data));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold text-blue-600">Reports</h2>
      <ul>
        {reports.map((report) => (
          <li key={report.id} className="p-4 bg-gray-100 my-2 rounded-lg">
            <strong>Title Number:</strong> {report.title_number} <br />
            <strong>Owner:</strong> {report.owner} <br />
            <strong>Market Value:</strong> ${report.market_value} <br />
            <strong>Remarks:</strong> {report.remarks}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Reports;
// Compare this snippet from Report/frontend/src/App.js: