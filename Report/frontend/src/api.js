import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/reports/";

export const fetchReports = async () => {
  const response = await axios.get(API_URL);
  return response.data;
};

export const createReport = async (reportData) => {
  const response = await axios.post(API_URL, reportData);
  return response.data;
};
