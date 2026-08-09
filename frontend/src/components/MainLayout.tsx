import AnalysisPanel from "../components/AnalysisPanel";
import ReportInput from "../components/ReportInput";

function MainLayout() {
  return (
    <div className="flex justify-center min-h-screen py-6.9">
        <div className="w-1/3 pr-4">
            <ReportInput />
        </div>
        <div className="w-1/2 pl-4">
            <AnalysisPanel />
        </div>
    </div>
  );
}

export default MainLayout;