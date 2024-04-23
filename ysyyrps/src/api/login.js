import request from "@/until/request";

export function getLogin(data = {}) {
    return request({
        baseURL: import.meta.env.VITE_LOGIN,
        url: "/login_temporary/",
        method: "post",
        data: data,
    });
}