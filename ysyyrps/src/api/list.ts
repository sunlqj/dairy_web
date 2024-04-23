import request from "../until/request";
// 获取日记列表
export function getLists(data = {}) {
    return request({
        baseURL: import.meta.env.VITE_API,
        url: `/list/`,
        method: "post",
        data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
    });
}

