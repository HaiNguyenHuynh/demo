import { Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import "./index.css";
import LoginPage from "./page/LoginPage";
import RegisterPage from "./page/RegisterPage";
import LandingPageNew from "./page/LandingPageNew";
import Footer from "./components/Footer";
import ManageUserPage from "./page/ManageUserPage";
import { ProtectedRoute } from "./page/Protect";
import NotFound from "./page/NotFound";
function App() {
  return (
    <div>
      <Header />
      <Routes>
        <Route path="/" element={<LandingPageNew />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route element={<ProtectedRoute />}>
          <Route path="/users" element={<ManageUserPage />} />
          <Route path="/users/:id" element={<ManageUserPage />} />
        </Route>
        <Route path="*" element={<NotFound />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
