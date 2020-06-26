<template>
  <div id="app">
    <myNavbar></myNavbar>
    <br><br>
    <router-view v-if="isRouterAlive"></router-view>
    <el-backtop visibility-height="0" right="100" bottom="100"></el-backtop>
  </div>
</template>

<script>
import myNavbar from './components/AppComponents/NavBar'
export default {
  name: 'App',
  components: {
    myNavbar
  },
  provide () {
    return {
      reload: this.reload
    }
  },
  data () {
    return {
      isRouterAlive: true
    }
  },
  methods: {
    reload () {
      this.isRouterAlive = false
      this.$nextTick(function () {
        this.isRouterAlive = true
      })
    }
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
