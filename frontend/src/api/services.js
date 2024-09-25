import axios from "axios";

export const fetchAllUser = () =>
  axios
    .get(`/api/users`)
    .then((res) => {
      return res.data;
    })
    .catch((error) => {
      console.error(error);
      throw error;
    });

export const fetchAllUserById = (id) =>
  axios
    .get(`/api/users/${id}`)
    .then((res) => {
      return res.data;
    })
    .catch((error) => {
      console.error(error);
      throw error;
    });

export const createUser = (data) =>
  axios
    .post(`/api/users/create/`, data)
    .then((res) => {
      return res.data;
    })
    .catch((error) => {
      console.error(error);
      throw error;
    });

export const apiLogin = (data) =>
  axios
    .post(`/api/auth/login/`, data)
    .then((res) => {
      return res.data;
    })
    .catch((error) => {
      console.error(error);
      throw error;
    });

export const apiRegister = (data) =>
  axios
    .post(`/api/auth/registration/`, data)
    .then((res) => {
      return res.data;
    })
    .catch((error) => {
      console.error(error);
      throw error;
    });
