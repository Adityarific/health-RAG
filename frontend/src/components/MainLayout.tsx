import { useState } from "react";
import AnalysisPanel from "../components/AnalysisPanel";
import ReportInput from "../components/ReportInput";

function MainLayout() {
  const [analysis, setAnalysis] = useState("");

  return (
    <div className="flex justify-center min-h-screen py-6">
      <div className="w-1/2 pr-4">
        <ReportInput onAnalysis={setAnalysis} />
      </div>

      <div className="w-1/2 pl-4">
        <AnalysisPanel analysis={analysis} />
      </div>
    </div>
  );
}

export default MainLayout;