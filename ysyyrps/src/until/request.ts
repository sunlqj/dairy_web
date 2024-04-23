import axios from "axios";
const service = axios.create({
    baseURL: import.meta.env.VITE_API,
    timeout: 20000,
    headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
    },
});


//创建请求拦截器
//请求拦截器里可以加入需要的token等认证信息，现在还用不到，所以基本是空的
service.interceptors.request.use(
    (config) => {
        return config;
    },
    (error) => {
        console.log(error);
        return Promise.reject(error);
    }
);
//创建相应拦截器
service.interceptors.response.use(
    (response) => {
        const res = response.data;
        return res;
    },
    (error) => {
        console.log(error);
        return Promise.reject(error);
    }
);

export default service;