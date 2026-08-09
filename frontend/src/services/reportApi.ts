import api from "./api";

export const analyzeReport = async (report: string) => {
  const response = await api.post("/analyze", {
    report,
  });

  return response.data;
};