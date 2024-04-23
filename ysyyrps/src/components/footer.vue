<template>
<div class="foot-bot-wrap">
    <div class="foot-bot-right">
        <div class="right-disclaimer">
            <router-link to="/disclaimer" target="_blank">法律声明</router-link>
            <router-link to="/privacy-policy" target="_blank">隐私政策</router-link>
            <a href="https://lqj0426.cn/api/beg" target="_blank">赞助与联系作者</a>
        </div>
        版权公告 © 2024-2024 LQJ / 以及其关联公司及特许人 版权所有
    </div>
    <div class="foot-bot-left">
        <a href="https://beian.miit.gov.cn/#/Integrated/index" target="_blank">浙ICP备2024060199号-1</a>
    </div>
</div>

</template>

<script setup lang="ts">

</script>

<style scoped>
a {
    color: #000000c7;
    margin-left: 20px;
}
.foot-bot-wrap{
    margin-top: 40px;
}
* {
    font-size: 12px; /* 设置默认字体大小为 8 像素 */
    font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
    margin-bottom: 5px;
    text-align: center;
}

</style>