import axios from 'axios';

export const api = axios.create({
  baseURL: 'http://localhost:8000/api' || 'https://{{cookiecutter.domain_name}}/api/',
});

export const setToken = (token: string): void => {
  console.log(token);
  api.defaults.headers.common.Authorization = `Token ${token}`;
};

