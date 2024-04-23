import { defineConfig } from 'vite';
import { resolve } from 'path';
import { envResolver } from './config/index.js';
import { getPlugins } from './config/plugins';
// 分开打包
const splitDependencies = [];
// https://vitejs.dev/config/
export default defineConfig(({ mode }) => Object.assign(
  envResolver[mode](),
  {
    base: '/',
    server: {
      // 是否开启 https
      // https: true,
      // 端口号
      port: 9999,
      // 监听所有地址 127.0.0.1  localhost   192.168.1.x
      host: '0.0.0.0',
      // 服务启动时是否自动打开浏览器
      open: true,
      // 允许跨域
      cors: true,
      // 自定义代理规则
      proxy: {},
    },
    envDir: resolve(__dirname, 'config/env'),
    resolve: {
      alias: {
        '@': resolve(__dirname, 'src'),
      },
    },
    
    plugins: getPlugins(mode),
  }
  
));
