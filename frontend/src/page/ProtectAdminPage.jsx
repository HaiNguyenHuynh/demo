import { Outlet } from "react-router-dom";
import { useCookies } from "react-cookie";
import NotFound from "./NotFound";

export const ProtectedRouteAdmin = () => {
  const [cookies] = useCookies(["role"]);

  if (cookies.role !== "Admin") {
    return <NotFound />;
  }
  return <Outlet />;
};
