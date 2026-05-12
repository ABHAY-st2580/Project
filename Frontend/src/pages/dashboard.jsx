import { useState, useEffect } from "react";

export default function RecommendationDashboard() {
  const [comparison, setComparison] = useState(null);
  const [rules, setRules] = useState([]);
  const [support, setSupport] = useState(0.2);
  const [confidence, setConfidence] = useState(0.6);

  const token = localStorage.getItem("token");

  const fetchComparison = async () => {
    const res = await fetch("http://127.0.0.1:8000/insights/sales-comparison/", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await res.json();
    setComparison(data);
  };
    useEffect(() => {
      fetchComparison();
    }, []);
  const runAnalysis = async () => {
    const res = await fetch("http://127.0.0.1:8000/insights/dash/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        min_support: support,
        min_confidence: confidence,
      }),
    });

    const data = await res.json();
    console.log("API RESPONSE:", data);
    setRules(data.rules || []);
  };

  const maxConfidence = Math.max(...rules.map(r => r.confidence || 0), 0);

    if (!token) {
    return (
      <center className="w-full h-screen flex items-center justify-center text-gray-300">
        <button className="btn-blue">
          Please Login to View Dashboard
        </button>
      </center>
    );
  }
  return (
    <div className="p-6 text-gray-300 bg-[#020617] min-h-screen">

      <h1 className="text-xl mb-4">AI Tile Recommendations</h1>
      <div className="bg-[#0f172a] border border-gray-800 rounded-xl p-5 mb-6 font-extralight">

        <h2 className="text-lg text-gray-400 mb-4">
          Monthly Sales Comparison
        </h2>

        {comparison && (
          <div className="grid grid-cols-3 gap-4">

            {/* CURRENT */}
            <div className="card">
              <p className="text-lg text-gray-500">Current Month</p>
              <h2 className="text-lg">{comparison.current_month_sales}</h2>
            </div>

            {/* PREVIOUS */}
            <div className="card">
              <p className="text-lg text-gray-500">Previous Month</p>
              <h2 className="text-lg">{comparison.previous_month_sales}</h2>
            </div>

            {/* GROWTH */}
            <div className="card">
              <p className="text-lg text-gray-500">Growth</p>
              <h2
                className={`text-lg ${
                  comparison.growth_percentage >= 0
                    ? "text-green-400"
                    : "text-red-400"
                }`}
              >
                {comparison.growth_percentage}%
              </h2>
            </div>

          </div>
        )}

  {/* 🔷 SIMPLE BAR VISUAL */}
        {comparison && (
          <div className="mt-6">

            <div className="text-lg text-gray-500 mb-2">Visual Comparison</div>

            <div className="flex items-end gap-6 h-32">

              {/* CURRENT BAR */}
              <div className="flex flex-col items-center w-1/2">
                <div
                  className="bg-blue-500 w-16 rounded"
                  style={{
                    height: `${comparison.current_month_sales}px`,
                    maxHeight: "120px"
                  }}
                ></div>
                <p className="text-lg mt-1">Current</p>
              </div>

              {/* PREVIOUS BAR */}
              <div className="flex flex-col items-center w-1/2">
                <div
                  className="bg-gray-500 w-16 rounded"
                  style={{
                    height: `${comparison.previous_month_sales}px`,
                    maxHeight: "120px"
                  }}
                ></div>
                <p className="text-lg mt-1">Previous</p>
              </div>

            </div>
          </div>
        )}
        <hr className="my-6 border-gray-700" />
        {comparison && (
        <div className="grid grid-cols-2 gap-6 mb-6">

          {/* 🔷 TOP CURRENT */}
          <div className="card">
            <h2 className="text-lg text-gray-400 mb-3">
              <u>Top Tiles (Current Month)</u>
            </h2>

            {comparison.top_tiles_current.length === 0 ? (
              <p className="text-sm text-gray-500">No data</p>
            ) : (
              comparison.top_tiles_current.map((tile, i) => (
                <div key={i} className="flex justify-between text-sm mb-1">
                  <span>{tile[0]}</span>
                  <span className="text-blue-400">{tile[1]}</span>
                </div>
              ))
            )}
          </div>

          {/* 🔷 TOP PREVIOUS */}
          <div className="card">
            <h2 className="text-lg text-gray-400 mb-3">
              <u>Top Tiles (Previous Month)</u>
            </h2>

            {comparison.top_tiles_previous.length === 0 ? (
              <p className="text-sm text-gray-500">No data</p>
            ) : (
              comparison.top_tiles_previous.map((tile, i) => (
                <div key={i} className="flex justify-between text-sm mb-1">
                  <span>{tile[0]}</span>
                  <span className="text-gray-400">{tile[1]}</span>
                </div>
              ))
            )}
          </div>

          {/* 🔥 TRENDING UP */}
          <div className="card">
            <h2 className="text-lg text-green-400 mb-3">
              Trending Up
            </h2>

            {comparison.trending_up.length === 0 ? (
              <p className="text-sm text-gray-500">No data</p>
            ) : (
              comparison.trending_up.map((tile, i) => (
                <div key={i} className="flex justify-between text-sm mb-1">
                  <span>{tile.tile}</span>
                  <span className="text-green-400">+{tile.increase}</span>
                </div>
              ))
            )}
          </div>

          {/* 📉 TRENDING DOWN */}
          <div className="card">
            <h2 className="text-lg text-red-400 mb-3">
              Trending Down
            </h2>

            {comparison.trending_down.length === 0 ? (
              <p className="text-sm text-gray-500">No data</p>
            ) : (
              comparison.trending_down.map((tile, i) => (
                <div key={i} className="flex justify-between text-sm mb-1">
                  <span>{tile.tile}</span>
                  <span className="text-red-400">-{tile.decrease}</span>
                </div>
              ))
            )}
          </div>

        </div>
      )}
      </div>
      {/* 🔷 CONTROLS */}
      <div className="bg-[#0f172a] border border-gray-800 rounded-xl p-5 mb-6">

        <h2 className="text-sm text-gray-400 mb-4">Run Analysis</h2>

        <div className="grid grid-cols-3 gap-4 items-center">

          <div>
            <label className="text-xs text-gray-500">Min Support</label>
            <input
              type="range"
              min="0.1"
              max="1"
              step="0.1"
              value={support}
              onChange={(e) => setSupport(parseFloat(e.target.value))}
              className="w-full"
            />
            <p className="text-xs">{support}</p>
          </div>

          <div>
            <label className="text-xs text-gray-500">Min Confidence</label>
            <input
              type="range"
              min="0.1"
              max="1"
              step="0.1"
              value={confidence}
              onChange={(e) => setConfidence(parseFloat(e.target.value))}
              className="w-full"
            />
            <p className="text-xs">{confidence}</p>
          </div>

          <button
            onClick={runAnalysis}
            className="btn-blue mt-4"
          >
            Run Analysis
          </button>

        </div>
      </div>

      {/* 🔷 SUMMARY */}
      <div className="grid grid-cols-3 gap-4 mb-6">

        <div className="card">
          <p className="text-xs text-gray-500">Total Rules</p>
          <h2 className="text-lg">{rules.length}</h2>
        </div>

        <div className="card">
          <p className="text-xs text-gray-500">Top Confidence</p>
          <h2 className="text-lg">{maxConfidence.toFixed(2)}</h2>
        </div>

        <div className="card">
          <p className="text-xs text-gray-500">Strong Patterns</p>
          <h2 className="text-lg">
            {rules.filter(r => r.confidence > 0.8).length}
          </h2>
        </div>

      </div>

      {/* 🔷 RULES TABLE */}
      <div className="bg-[#0f172a] border border-gray-800 rounded-xl p-5">

        <h2 className="text-sm text-gray-400 mb-4">Recommendations</h2>

        <div className="max-h-[400px] overflow-y-auto">

          <table className="w-full table-fixed text-sm">

            <thead className="sticky top-0 bg-[#0f172a]">
              <tr className="text-gray-500 text-xs border-b border-gray-700">
                <th className="p-2 text-left w-[40%]">If Bought</th>
                <th className="p-2 text-left w-[40%]">Then Buy</th>
                <th className="p-2 text-right w-[20%]">Confidence</th>
              </tr>
            </thead>

            <tbody>
              {rules.map((rule, index) => (
                <tr key={index} className="border-b border-gray-800">

                  {/* IF */}
                  <td className="p-2">
                    <div className="flex flex-wrap gap-1">
                      {rule.if_bought.map((item, i) => (
                        <span key={i} className="tag-blue">
                          {item}
                        </span>
                      ))}
                    </div>
                  </td>

                  {/* THEN */}
                  <td className="p-2">
                    <div className="flex flex-wrap gap-1">
                      {rule.then_buy.map((item, i) => (
                        <span key={i} className="tag-green">
                          {item}
                        </span>
                      ))}
                    </div>
                  </td>

                  {/* CONFIDENCE */}
                  <td className="p-2 text-right">
                    <span
                      className={`px-2 py-1 rounded text-sm ${
                        rule.confidence > 0.8
                          ? "text-green-600"
                          : rule.confidence > 0.6
                          ? "text-yellow-600"
                          : "text-gray-600"
                      }`}
                    >
                      {rule.confidence.toFixed(2)}
                    </span>
                  </td>

                </tr>
              ))}
            </tbody>

          </table>

        </div>
      </div>
    </div>
  );
}