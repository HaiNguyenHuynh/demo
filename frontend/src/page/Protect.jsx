import { Navigate, Outlet } from "react-router-dom";
import { useLocalStorage } from "../hooks/LocalStorage";

export const ProtectedRoute = () => {
  const [credentials] = useLocalStorage("credentials");

  if (!credentials) {
    return <Navigate to="/login" />;
  }
  return <Outlet />;
};
