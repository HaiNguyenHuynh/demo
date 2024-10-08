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
    .post(`/api/login`, data)
    .then((res) => {
      return res.data;
    })
    .catch((error) => {
      console.error(error);
      throw error;
    });

export const apiLogout = (data) =>
  axios
    .post(`/api/logout`, data)
    .then((res) => {
      return res.data;
    })
    .catch((error) => {
      console.error(error);
      throw error;
    });

export const apiRegister = (data) =>
  axios
    .post(`/api/register`, data)
    .then((res) => {
      return res.data;
    })
    .catch((error) => {
      console.error(error);
      throw error;
    });

export const apiCreateUser = (data) =>
  axios
    .post(`/api/users`, data)
    .then((res) => {
      return res.data;
    })
    .catch((error) => {
      console.error(error);
      throw error;
    });
