import React, { useEffect, useState } from "react";
import ReactSpeedometer from "react-d3-speedometer";

function App() {
  const [speed, setSpeed] = useState(0);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/speed/");

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setSpeed(data.speed);
    };

    ws.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    return () => ws.close();
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "60px" }}>
      <h1>Live Speedometer</h1>

      <ReactSpeedometer
        maxValue={120}
        value={speed}
        needleColor="steelblue"
        startColor="green"
        segments={6}
        endColor="red"
        height={300}
      />

      <h2>{speed} km/h</h2>
    </div>
  );
}

export default App;
