import { Outlet } from "react-router-dom";
import { useCookies } from "react-cookie";
import NotFound from "./NotFound";

export const ProtectedRouteAdmin = () => {
  const [cookies, setCookie] = useCookies(["role"]);

  if (cookies.role !== "admin") {
    return <NotFound />;
  }
  return <Outlet />;
};
