import request from "../until/request";
// 获取日记列表
export function getdairy(data = {}) {
    return request({
        baseURL: import.meta.env.VITE_API,
        url: `/get_dairy/`,
        method: "post",
        data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
    });
}
