<template>
    <el-form
      ref="ruleFormRef"
      :model="ruleForm"
      :rules="rules"
      class="ruleForm"
      :size="formSize"
      status-icon
    >
      <el-form-item label="日期" required>
          <el-form-item prop="date">
            <el-date-picker
              v-model="ruleForm.date"
              type="date"
              label="选择日期"
              placeholder="选择日期"
              style="width: 100%"
            />
          </el-form-item>
      </el-form-item>
      <el-form-item label="标题" prop="title">
        <el-input v-model="ruleForm.title" />
      </el-form-item>

      <el-form-item label="内容" prop="content">
        <el-input 
        v-model="ruleForm.content" 
        type="textarea" 
        :rows="10"
        placeholder="请输入内容"
        />
      </el-form-item>
      <el-form-item style="margin-left: 18%;  text-align: center;">
        <el-button type="primary" @click="submitForm(ruleFormRef)">
          创建
        </el-button>
        <el-button @click="resetForm(ruleFormRef)" >重置</el-button>
        <el-button @click="back()" >返回</el-button>
      </el-form-item>
    </el-form>
  </template>
  
  <script lang="ts" setup>
  import { reactive, ref } from "vue";
  import type { FormInstance, FormRules } from "element-plus";
  import {useRouter} from "vue-router";
  import {create} from "../../api/write";
  import { ElMessage } from 'element-plus'
  const router = useRouter()
  
  interface RuleForm {
    title: string
    date: string
    content: string
  }
  
  const formSize = ref('default')
  const ruleFormRef = ref<FormInstance>()
  const ruleForm = reactive<RuleForm>({
    title: '',
    date: '',
    content: '',
  })

  const rules = reactive<FormRules<RuleForm>>({
    title: [
      { required: true, message: '标题不能为空', trigger: 'blur' },
      { min: 2,  message: '字数不少于2', trigger: 'blur' },
    ],
    date: [
      {
        type: 'date',
        required: true,
        message: '请选择日期',
        trigger: 'change',
      },
    ],
    content: [
      { required: true, message: '内容不能为空', trigger: 'blur' },
      { max: 6240,  message: '字数过多', trigger: 'blur' },
    ],
  })
  
  const submitForm = async (formEl: FormInstance | undefined) => {
    if (!formEl) return
    await formEl.validate((valid, fields) => {
      console.log(ruleForm.date)
      if (valid) {
        console.log('submit!')
        create({ title: ruleForm.title, pickdate: ruleForm.date, content: ruleForm.content })
        ElMessage({
          message: '创建成功',
          type: 'success',
        })        
        router.push('/diary')
      } else {
        console.log('error submit!', fields)
      }
    })
  }
  
  const resetForm = (formEl: FormInstance | undefined) => {
    if (!formEl) return
    formEl.resetFields()
  }
  const back = () => {
    router.go(-1)
  }

  </script>
<style scoped>
.el-form-item__content{
  margin-top: 2%;
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}
</style>
  