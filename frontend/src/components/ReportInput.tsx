import { useState } from "react";
import { analyzeReport } from "../services/reportApi";
function ReportInput() {
  const [report, setReport] = useState("");

  const handleAnalyze = async () => {
    try {
      
      const result = await analyzeReport(report);
      console.log(result);
    } catch (error) {
      console.error("Error analyzing report:", error);
    }
  };

  return (
    <div className=" rounded-xl border border-gray-200 bg-white p-6 shadow-sm ">
      <h2 className="mb-4 text-2xl font-semibold">
        📄 Medical Report
      </h2>

      <p className="mb-4 text-gray-600">
        Paste your medical report below.
      </p>

      <textarea
        value={report}
        onChange={(e) => setReport(e.target.value)}
        placeholder="Paste your medical report here..."
        className="h-96 w-full resize-none rounded-lg border border-gray-300 p-4 outline-none focus:border-blue-500"
      />

      <button onClick={handleAnalyze} className="mt-6 w-full rounded-lg bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700">
        Analyze Report
      </button>
      

      {report && (
        <div className="mt-4 rounded-lg bg-gray-100 p-4">
          <h3 className="mb-2 font-semibold">Current Report:</h3>

          <pre className="whitespace-pre-wrap text-sm">
            {report}
          </pre>
        </div>
      )}
    </div>
  );
}

export default ReportInput;