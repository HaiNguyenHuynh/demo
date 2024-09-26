import { useCookies } from "react-cookie";
import { Navigate, Outlet } from "react-router-dom";

export const ProtectedRoute = () => {
  const [cookies] = useCookies(["role"]);

  if (!cookies.role) {
    return <Navigate to="/login" />;
  }
  return <Outlet />;
};
