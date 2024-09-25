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
import DefaultLayout from "./page/DefaultLayout";
function App() {
  return (
    <div>
      <Routes>
        <Route
          path="/"
          element={
            <DefaultLayout>
              <LandingPageNew />
            </DefaultLayout>
          }
        />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route element={<ProtectedRoute />}>
          <Route
            path="/users"
            element={
              <DefaultLayout>
                <ManageUserPage />
              </DefaultLayout>
            }
          />
          <Route
            path="/users/:id"
            element={
              <DefaultLayout>
                <ManageUserPage />
              </DefaultLayout>
            }
          />
        </Route>
        <Route
          path="*"
          element={
            <DefaultLayout>
              <NotFound />
            </DefaultLayout>
          }
        />
      </Routes>
      {/* <Footer /> */}
    </div>
  );
}

export default App;
