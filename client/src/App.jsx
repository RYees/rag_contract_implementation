import React from "react";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import { Home, Chat } from "./pages/index";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <AppWithRouter />
      </BrowserRouter>
    </div>
  );
}

function AppWithRouter() {
  const location = useLocation();
  const [displayLocation, setDisplayLocation] = React.useState(location);
  const [transitionStage, setTransistionStage] = React.useState("fadeIn");

  React.useEffect(() => {
    if (location !== displayLocation) setTransistionStage("fadeOut");
  }, [location, displayLocation]);

  return (
    <>
      <div
        className={`${transitionStage}`}
        onAnimationEnd={() => {
          if (transitionStage === "fadeOut") {
            setTransistionStage("fadeIn");
            setDisplayLocation(location);
          }
        }}
      >
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/chat" element={<Chat />} />
        </Routes>
      </div>
    </>
  );
}

export default App;