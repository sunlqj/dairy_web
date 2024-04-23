import {createRouter,createWebHistory,RouteRecordRaw} from 'vue-router'

const routes:Array<RouteRecordRaw> = [
    {
        path:'/',
        component:()=> import('../views/layout.vue'),
        children: [
            {
                path: "",
                component: () =>
                    import ("../components/zhuye.vue"),
            },
        ]
    },
    {
        path: "/diary",
        component: () =>
            import ("../views/diary/diarylist.vue"),
    },
    {
        path: "/myworld",
        component: () =>
            import ("../components/zhuye.vue"),
    },
    {
        path: "/friends",
        component: () =>
            import ("../components/zhuye.vue"),
    },
    {
        path: "/creatediary",
        component: () =>
            import ("../views/diary/creatediary.vue"),
    },
    {
        path: "/dairydetail",
        component: () =>
            import ("../views/diary/dairydetail.vue"),
    },
    {
        path:'/login',
        component:()=> import('../components/login.vue')
    },
    {
        path:'/disclaimer',
        component:()=> import('../views/footer/disclaimer.vue')
    },
    {
        path:'/privacy-policy',
        component:()=> import('../views/footer/privacy-policy.vue')
    },
]

const router = createRouter({
    history:createWebHistory(),
    routes 
})

export default router