import Vue from 'vue'
import Router from 'vue-router'
import SearchResult from '../components/SearchComponents/SearchResult'
import ViewMain from '../components/ViewComponents/ViewMain'
import EditBlog from '../components/EditComponents/EditBlog'
import MainPage from '../components/MainPageComponents/MainPage'
import Login from '../components/MainPageComponents/Login'
import Regist from '../components/MainPageComponents/Regist'
import Classify from '../components/MainPageComponents/Classify'
import UserInfo from '../components/UserComponents/UserInfo'
import UserBlog from '../components/UserComponents/UserBlog'
import ChangeInfo from '../components/UserComponents/ChangeInfo'
import UploadedFiles from '../components/UserComponents/UploadedFiles'
import DeleteUser from '../components/UserComponents/DeleteUser'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/MainPage',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/SearchResult',
      name: 'SearchResult',
      component: SearchResult
    },
    {
      path: '/ViewMain',
      name: 'ViewMain',
      component: ViewMain
    },
    {
      path: '/EditBlog',
      name: 'EditBlog',
      component: EditBlog
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/Regist',
      name: 'Regist',
      component: Regist
    },
    {
      path: '/Classify/:id',
      name: 'Classify',
      component: Classify
    },
    {
      path: '/UserCenter/UserInfo',
      name: 'UserInfo',
      component: UserInfo
    },
    {
      path: '/UserCenter/BlogList',
      name: 'UserBlog',
      component: UserBlog
    },
    {
      path: '/UserCenter/ChangeInfo',
      name: 'ChangeInfo',
      component: ChangeInfo
    },
    {
      path: '/UserCenter/UploadedFiles',
      name: 'UploadedFiles',
      component: UploadedFiles
    },
    {
      path: '/UserCenter/DeleteUser',
      name: 'DeleteUser',
      component: DeleteUser
    }
  ]
})
