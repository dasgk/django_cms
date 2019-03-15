<template>
<el-container style=" position: absolute;top: 0;left: 0;width: 100%; height: 100%;">
  <el-header>Header</el-header>
  <el-container>
  <el-main>Main</el-main>
    <el-aside width="200px">Aside</el-aside>

  </el-container>
   <el-footer>Footer</el-footer>
</el-container>
</template>
<style>
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    height:10%;
  }
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
  }
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;

  }
</style>
