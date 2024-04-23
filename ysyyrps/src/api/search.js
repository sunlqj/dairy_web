import request from "@/until/request";
export function getCategory(data = {}) {
    // console.log("123", params);
    return request({
        baseURL: import.meta.env.VITE_APIB,
        url: "/Category_list/",
        method: "post",
        data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
    });   
}