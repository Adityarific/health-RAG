function AnalysisPanel() {
  return (
    <div className="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
      <h2 className="mb-6 text-2xl font-semibold">
        🥗 Nutrition Analysis
      </h2>

      <div className="space-y-6">
        <section>
          <h3 className="mb-2 text-lg font-semibold">📋 Summary</h3>
          <p className="text-gray-600">
            Waiting for report analysis...
          </p>
        </section>

        <section>
          <h3 className="mb-2 text-lg font-semibold">
            ⚠ Detected Deficiencies
          </h3>

          <p className="text-gray-600">
            —
          </p>
        </section>

        <section>
          <h3 className="mb-2 text-lg font-semibold">
            🥦 Recommended Foods
          </h3>

          <p className="text-gray-600">
            —
          </p>
        </section>

        <section>
          <h3 className="mb-2 text-lg font-semibold">
            💡 Lifestyle Tips
          </h3>

          <p className="text-gray-600">
            —
          </p>
        </section>

        <section>
          <h3 className="mb-2 text-lg font-semibold">
            ⚕ Disclaimer
          </h3>

          <p className="text-sm text-gray-500">
            This application provides AI-generated nutritional
            suggestions for educational purposes only.
            Always consult a qualified healthcare professional
            before making medical or dietary decisions.
          </p>
        </section>
      </div>
    </div>
  );
}

export default AnalysisPanel;