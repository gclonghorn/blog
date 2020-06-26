// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import store from './store'

import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import VueQuillEditor from 'vue-quill-editor'
import global_ from './components/global'// 引用文件
import axios from 'axios'
import router from './router'
Vue.prototype.$axios = axios

Vue.use(VueQuillEditor)
Vue.prototype.GLOBAL = global_// 挂载到Vue实例上面

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.directive('title', {
  inserted: function (el, binding) {
    document.title = el.dataset.title
  }
})

export function isJSON(str) {
        if (typeof str == 'string') {
            try {
                let obj=JSON.parse(str);
                console.log('转换成功：'+obj);
                return true;
            } catch(e) {
                console.log('error：'+str+'------'+e);
                return false;
            }
        }
        console.log('It is not a string!')
 }

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store: store,
  components: { App },
  template: '<App/>',
  router,
})
