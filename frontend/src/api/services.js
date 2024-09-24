import axios from "axios";

export const fetchAllUser = () =>
  axios
    .get(`/api/users`)
    .then((res) => {
      return res.data;
    })
    .catch((error) => console.log(error));

export const fetchAllUserById = (id) =>
  axios
    .get(`/api/users/${id}`)
    .then((res) => {
      return res.data;
    })
    .catch((error) => console.log(error));

export const createUser = (data) =>
  axios
    .post(`/api/users/create/`, data)
    .then((res) => {
      return res.data;
    })
    .catch((error) => console.log(error));
