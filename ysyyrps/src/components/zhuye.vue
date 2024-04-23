<template>
    <div class="zhuye">
        <el-carousel :autoplay="false" indicator-position="none" arrow="never" type="card">
        <el-carousel-item>
            <el-card class="box-card" @click="init('diary')">
                <template #header>
                    <span>日记</span>
                </template>
                <p>一个专属于你自己的日记本</p>
            </el-card>
        </el-carousel-item>
        <el-carousel-item>
            <el-card class="box-card" @click="init('myworld')">
                <template #header>
                    <span>我的世界</span>
                </template>
                <p>一个属于你的地方</p>
            </el-card>
        </el-carousel-item>   
        <el-carousel-item>
            <el-card class="box-card" @click="init('friends')" body-style="padding:10px;">
                <template #header>
                    <span>好友</span>
                </template>
                <p>相互信任、彼此真诚、相互尊重、可以分享快乐和悲伤的人</p>
            </el-card>
        </el-carousel-item>       
        </el-carousel>
    </div>

</template>

<script setup lang="ts">
import {useRouter} from "vue-router"
const router = useRouter()
const init = (str: string) => {
    router.push('/'+str)
}
</script>

<style scoped>
.zhuye{
    margin-top: 20px;  
}
.el-carousel__item {
    height: 80%;
}
.box-card{
    height: 100%;
}
</style>