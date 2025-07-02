import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [form, setForm] = useState({
    rollno: "",
    name: "",
    subject: "Math",
    rating: "",
  });

  const submitFeedback = async () => {
    try {
      await axios.post("https://r914gka1e6.execute-api.us-east-1.amazonaws.com/feedback", form);
      alert("Submitted!");
    } catch (err) {
      alert("Submission failed");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="bg-white p-6 rounded-2xl shadow-xl w-full max-w-md">
        <h2 className="text-2xl font-semibold mb-6 text-center text-gray-800">
          Feedback Form
        </h2>

        <div className="space-y-4">
          <input
            className="w-full px-4 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Roll No"
            value={form.rollno}
            onChange={(e) => setForm({ ...form, rollno: e.target.value })}
          />

          <input
            className="w-full px-4 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Name"
            value={form.name}
            onChange={(e) => setForm({ ...form, name: e.target.value })}
          />

          <select
            className="w-full px-4 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={form.subject}
            onChange={(e) => setForm({ ...form, subject: e.target.value })}
          >
            <option value="Math">Cloud Computing</option>
            <option value="Science">Neural Networks</option>
            <option value="History">Internet Of Things</option>
            <option value="History">Competitive Programming</option>
          </select>

          <input
            className="w-full px-4 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Rating (1-5)"
            type="number"
            min="1"
            max="5"
            value={form.rating}
            onChange={(e) => setForm({ ...form, rating: e.target.value })}
          />

          <button
            onClick={submitFeedback}
            className="w-full bg-blue-600 text-white py-2 rounded-xl hover:bg-blue-700 transition duration-300"
          >
            Submit
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;


