
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const store = new Vuex.Store({

  state: {
    // 存储token
    Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : ''
  },

  mutations: {
    // 修改token，并将token存入localStorage
    changeLogin (state, user) {
      state.Authorization = user.Authorization
      localStorage.setItem('Authorization', user.Authorization)
    },
    logOut(state) {
      localStorage.removeItem('Authorization')
      localStorage.removeItem('user_id')
      localStorage.removeItem('username')
      localStorage.removeItem('token')
      state.Authorization = ''
    }
  },

  Actions: {
  }
})

export default store
