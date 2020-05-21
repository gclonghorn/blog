<template>
  <div id="app">
    <mynavbar></mynavbar>
    <br><br>
    <router-view></router-view>
    <el-backtop visibility-height="0" right="100" bottom="100"></el-backtop>
  </div>
</template>

<script>
import mynavbar from './components/Appcomponents/Navbar.vue'
export default {
  name: 'App',
  components: {
    mynavbar,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
