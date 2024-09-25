import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";

export const ProtectedRoute = () => {
  const data = useAuth();

  if (!data?.user) {
    // user is not authenticated
    return <Navigate to="/login" />;
  }
  return <Outlet />;
};
