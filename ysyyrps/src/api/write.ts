import request from "../until/request"
//创建日记
export function create(data = {}) {
    return request({
        baseURL: import.meta.env.VITE_API,
        url: "/create_dairy/",
        method: "post",
        data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
    });
}