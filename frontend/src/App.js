import { Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import "./index.css";
import LandingPage from "./page/LadingPage";
import LoginPage from "./page/LoginPage";
import RegisterPage from "./page/RegisterPage";
function App() {
  return (
    <div>
      {/* <Header /> */}
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/:id" element={<LandingPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>
    </div>
  );
}

export default App;
