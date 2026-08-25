interface AnalysisPanelProps {
  analysis: string;
}

function AnalysisPanel({ analysis }: AnalysisPanelProps) {
  return (
    <div className="rounded-xl bg-white p-6 shadow">
      <h2 className="mb-6 text-xl font-bold">🥗 Nutrition Analysis</h2>

      {!analysis ? (
        <p className="text-gray-500">
          Your nutrition analysis will appear here after you analyze your report.
        </p>
      ) : (
        <section>
          <h3 className="mb-3 text-lg font-semibold">
            📋 AI Nutrition Analysis
          </h3>

          <div className="whitespace-pre-wrap rounded-lg bg-gray-50 p-4 text-gray-700">
            {analysis}
          </div>
        </section>
      )}

      <section className="mt-6">
        <h3 className="mb-2 text-lg font-semibold">
          ⚕ Disclaimer
        </h3>

        <p className="text-sm text-gray-500">
          This application provides AI-generated nutritional suggestions for
          educational purposes only. Always consult a qualified healthcare
          professional before making medical or dietary decisions.
        </p>
      </section>
    </div>
  );
}

export default AnalysisPanel;