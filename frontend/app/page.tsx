'use client';

import { useState } from 'react';

export default function Home() {
  const [inputCode, setInputCode] = useState('');
  const [generatedCode, setGeneratedCode] = useState('');
  const [showPreview, setShowPreview] = useState(false);

function extractTemplate(code: string) {
  // Remove markdown fences if present
  const cleaned = code
    .replace(/```[\s\S]*?\n/g, "")
    .replace(/```/g, "");

  const match = cleaned.match(/template:\s*`([\s\S]*?)`/);

  return match ? match[1] : "";
}


  function handleGenerate() {
    if (!inputCode.trim()) return;

    // For now: simply set pasted code as generated output
    setGeneratedCode(inputCode);
    setShowPreview(false);
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white p-8">

      {/* HEADER */}
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-2">
          Guided Component Architect
        </h1>
        <p className="text-slate-400 mb-8">
          Paste your generated component code below and preview it instantly.
        </p>

        {/* INPUT SECTION */}
        <div className="bg-slate-800 rounded-2xl shadow-xl p-6 mb-8 border border-slate-700">

          <label className="block text-sm text-slate-400 mb-2">
            Paste Component Code
          </label>

          <textarea
            className="w-full h-56 bg-slate-900 border border-slate-700 rounded-lg p-4 text-sm font-mono text-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            placeholder="Paste your LLM generated HTML here..."
            value={inputCode}
            onChange={(e) => setInputCode(e.target.value)}
          />

          <div className="mt-4 flex justify-end">
            <button
              onClick={handleGenerate}
              className="bg-indigo-600 hover:bg-indigo-700 transition px-6 py-2 rounded-lg font-semibold shadow-md"
            >
              Generate
            </button>
          </div>
        </div>

        {/* OUTPUT SECTION */}
        {generatedCode && (
          <div className="bg-slate-800 rounded-2xl shadow-xl p-6 border border-slate-700">

            {/* Toggle Buttons */}
            <div className="flex gap-4 mb-6">
              <button
                onClick={() => setShowPreview(false)}
                className={`px-4 py-2 rounded-lg ${
                  !showPreview
                    ? 'bg-indigo-600'
                    : 'bg-slate-700 hover:bg-slate-600'
                }`}
              >
                View Code
              </button>

              <button
                onClick={() => setShowPreview(true)}
                className={`px-4 py-2 rounded-lg ${
                  showPreview
                    ? 'bg-green-600'
                    : 'bg-slate-700 hover:bg-slate-600'
                }`}
              >
                Live Preview
              </button>
            </div>

            {/* CODE VIEW */}
            {!showPreview && (
              <pre className="bg-slate-900 p-4 rounded-lg overflow-auto text-sm font-mono text-slate-300 border border-slate-700">
                {generatedCode}
              </pre>
            )}

            {/* LIVE PREVIEW */}
           {showPreview && (
  <div className="bg-white text-black p-6 rounded-lg border border-slate-300 shadow-inner">
    <div
      dangerouslySetInnerHTML={{
        __html: extractTemplate(generatedCode),
      }}
    />
  </div>
)}


          </div>
        )}

      </div>
    </div>
  );
}
