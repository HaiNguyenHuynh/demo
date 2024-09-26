import { Navigate, Route, Routes } from "react-router-dom";
import "./index.css";
import LoginPage from "./page/LoginPage";
import RegisterPage from "./page/RegisterPage";
import LandingPageNew from "./page/LandingPageNew";
import ManageUserPage from "./page/ManageUserPage";
import { ProtectedRoute } from "./page/Protect";
import NotFound from "./page/NotFound";
import DefaultLayout from "./page/DefaultLayout";
import { ProtectedRouteAdmin } from "./page/ProtectAdminPage";
import AdminPage from "./page/AdminPage";
import { useCookies } from "react-cookie";
import UserOnly from "./page/UserOnly";
function App() {
  const [cookies] = useCookies(["role"]);
  const isLogin = cookies.role;

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
        <Route
          path="/login"
          element={isLogin ? <Navigate to="/" /> : <LoginPage />}
        />
        <Route
          path="/register"
          element={isLogin ? <Navigate to="/" /> : <RegisterPage />}
        />
        <Route element={<ProtectedRoute />}>
          <Route
            path="/user-only"
            element={
              <DefaultLayout>
                <UserOnly />
              </DefaultLayout>
            }
          />
        </Route>

        <Route element={<ProtectedRouteAdmin />}>
          <Route
            path="/users"
            element={
              <DefaultLayout>
                <ManageUserPage />
              </DefaultLayout>
            }
          />
          <Route
            path="/admin"
            element={
              <DefaultLayout>
                <AdminPage />
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
