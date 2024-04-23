<template>
  <div class="hh">
    <p>一蓑烟雨任平生</p>
    <el-container>
          <el-main style="background-size: 100%;">
            <RouterView />
          </el-main>
    </el-container>  
    <el-footer>
            <beian />
    </el-footer> 
  </div>

</template>


<script setup lang="ts">
import beian from '../components/footer.vue'
</script>

<style scoped>
* {
  text-align: center;
}
p {
  font-size: 36px;
  color: #b60e0e;
}
</style>
