import Vue from 'vue'
import Router from 'vue-router'
import SearchResult from '../components/SearchComponents/SearchResult'
import ViewMain from '../components/ViewComponents/ViewMain'
import EditBlog from '../components/EditComponents/EditBlog'
import MainPage from '../components/MainPageComponents/MainPage'
import Login from '../components/MainPageComponents/Login'
import Register from '../components/MainPageComponents/Regist'
import Classify from '../components/MainPageComponents/Classify'
import UserInfo from '../components/UserComponents/UserInfo'
import UserBlog from '../components/UserComponents/UserBlog'
import ChangeInfo from '../components/UserComponents/ChangeInfo'
import UploadedFiles from '../components/UserComponents/UploadedFiles'
import DeleteUser from '../components/UserComponents/DeleteUser'
import UpdateBlog from '../components/EditComponents/UpdateBlog'

Vue.use(Router)

const router = new Router({
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
      path: '/ViewMain/:AuthorName/:BlogTitle/:BlogId',//
      name: 'ViewMain',
      component: ViewMain,
      meta: {
        requireAuth: true//false//
      }
    },
    {
      path: '/EditBlog',
      name: 'EditBlog',
      component: EditBlog,
      meta: {
        requireAuth: true//false//
      }
    },
    {
      path: '/UpdateBlog/',
      name: 'UpdateBlog',
      component: UpdateBlog,
      meta: {
        requireAuth: true// false//
      }
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/Register',
      name: 'Register',
      component: Register
    },
    {
      path: '/Classify/:id',
      name: 'Classify',
      component: Classify
    },
    {
      path: '/UserCenter/UserInfo/:UserId/:RealUserId',
      name: 'UserInfo',
      component: UserInfo,
      meta: {
        requireAuth: true// false//
      }
    },
    {
      path: '/UserCenter/BlogList/:UserId/:RealUserId',
      name: 'UserBlog',
      component: UserBlog,
      meta: {
        requireAuth: true// false//
      }
    },
    {
      path: '/UserCenter/ChangeInfo/:UserId/:RealUserId',
      name: 'ChangeInfo',
      component: ChangeInfo,
      meta: {
        requireAuth: true// false//
      }
    },
    {
      path: '/UserCenter/UploadedFiles/:UserId/:RealUserId',
      name: 'UploadedFiles',
      component: UploadedFiles,
      meta: {
        requireAuth: true// false//
      }
    },
    {
      path: '/UserCenter/DeleteUser/:UserId/:RealUserId',
      name: 'DeleteUser',
      component: DeleteUser,
      meta: {
        requireAuth: true// false//
      }
    }
  ]
})

const originalPush = Router.prototype.push
Router.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}

// 导航守卫 使用router.beforeEach注册一个全局前置守卫，判断用户是否登录
/* router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    let token = localStorage.getItem('Authorization')// ???????????????????
    if (token) {
      next()
    } else {
      next({
        name: 'Login',
        params: {
          redirect: to.fullPath
        }
      })
    }
  } else {
    next()
  }
}) */

export default router
