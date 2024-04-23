<template>
    <el-button style="width: 100%;height: 40px; margin-bottom: 20px;" @click="onAddItem"
    >写日记</el-button
  >
    <el-table 
    @row-click="handleRowClicked"
    :data="filterTableData"  
    height="500" 
    style="width: 100%;" 
    >
    <el-table-column fixed prop="pickdate" label="日期" />
    <el-table-column prop="title" label="标题" />
    <el-table-column align="right">
      <template #header>
        <el-input v-model="search" size="small" placeholder="搜索" />
      </template>
      <template #default="scope">
        
        <el-button
          size="small"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)"
          >删除</el-button
        >
      </template>
    </el-table-column>
    </el-table>
    <div class="pagination-block">
        <el-pagination
          v-model:current-page="currentPage"
          :hide-on-single-page="true"
          :small="small"
          :disabled="disabled"
          :background="background"
          layout="prev, pager, next"
          :total="totalnum"
          @current-change="handleCurrentChange"
        />
    </div>
  </template>
  
<script setup lang="ts">
import { computed,ref,onMounted } from 'vue';
import {useRouter} from "vue-router";
import {getLists} from "../../api/list";
import { ElMessage } from 'element-plus'
const router = useRouter();
const currentPage = ref(1);
const small = ref(false);
const background = ref(false);
const disabled = ref(false);
const totalnum = ref(1);

const handleCurrentChange = (val: number) => {
  // console.log(`current page: ${val}`)
  currentPage.value = val;
  getLists({ group_id: 1, page: val, num: 10 }).then((res:any) => {
    tableData1.value = res.info.content;
    });

}
const handleRowClicked = (row:any,column:any) => {
  console.log(column.id);
  let col = parseInt(column.id.split('_')[3])
  if(col % 3  != 0){
    // let target = router.resolve({ path:'/dairydetail',query:row});
    // window.open(target.href, "_blank");
    router.push({ path:'/dairydetail',query:row});
  }
}

interface Diary {
  date: string
  title: string
}

const search = ref('')
const filterTableData = computed(() =>
  tableData1.value.filter(
    (data) =>
      !search.value || 
      data.title.toLowerCase().includes(search.value.toLowerCase()) ||
      data.pickdate.includes(search.value)
  )
)
// const handleEdit = (index: number, row: Diary) => {
//   console.log(index, row)
// }
const handleDelete = (index: number, row: Diary) => {
  console.log(index, row);
  ElMessage({
          message: '为什么要删我的日记？？？',
          type: 'warning',
        })     
}

const onAddItem = () => {
  router.push('/creatediary');
}
const tableData1 = ref([{
                "pickdate": "2002-04-26",
                "title": "lqjyyds",
            },])


onMounted(() => {
    getLists({ group_id: 1, page: 1, num: 10 }).then((res:any) => {
      tableData1.value = res.info.content;
      totalnum.value = res.info.all_num;
      });
});  

// <el-button size="small" type="primary" @click="handleEdit(scope.$index, scope.row)"
// >编辑</el-button
// >
// <el-button size="small" type="primary" @click="handleEdit(scope.$index, scope.row)"
// >分享</el-button
// >
</script>

<style scoped>
* {
  font-size:16px;
}
.pagination-block{
  margin-top: 2%;
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}
</style>
