<template>
    <div class="inner-title">{{ route.query.title }}</div>
    <div class="content">
        {{ content }}
    </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import { getdairy } from '../../api/get'
import { ref,onMounted } from 'vue';
const route = useRoute();

const content = ref('hhhhhh');

onMounted(() => {
    getdairy({ id:route.query.id}).then((res:any) => {
        content.value = res.info.content;
      });
});  
//const router = useRouter();
</script>

<style scoped>
p {
    font-size:13px;
}
.inner-title{
    text-align: center;
    font-size:28px;
    margin-bottom:25px;
}
</style>