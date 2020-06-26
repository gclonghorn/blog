import axiosInstance from './index'

const axios = axiosInstance

// 登录
export const postUser = (username, password) => {
  return axios.post('http://127.0.0.1:8000/login/', {
    'username': username, 'password': password
  })
}

// 注册
export const postNewUser = (username, password, pwd2, tel, email) => {
  return axios.post('http://127.0.0.1:8000/users/', {
    'username': username, 'password': password, 'pwd2': pwd2, 'tel': tel, 'email': email
  })
}

// 修改个人信息
export const changeUserInfo = (id, username, password, email, intro) => { // 'head': url
  return axios.put('http://127.0.0.1:8000/users/' + id + '/', {
    'username': username, 'password': password, 'email': email, 'introduction': intro,
  })
}

// 他人获取个人信息，可能不返回
export const getUserInfo2 = (id) => {
  return axios.get('http://127.0.0.1:8000/users/', {
    params: {id: id}})
}

// 获取个人信息
export const getUserInfo = () => {
  return axios.get('http://127.0.0.1:8000/users/1')
}

// 获取所有类别（主页）
export const getCategory = () => {
  return axios.get('http://127.0.0.1:8000/category/')
}

// 编辑博客后提交
export const submitBlog = (title, body, category, excerpt) => { //  'image': image, 'file': file
  return axios.post(`http://127.0.0.1:8000/edit/`, {
    'title': title, 'body': JSON.stringify(body), 'category': category, 'excerpt': excerpt
  })
}

// 提交文章的评论
export const submitComment = (BlogID, body) => {
  return axios.post(`http://127.0.0.1:8000/comment/`, {
    'post': BlogID, 'body': JSON.stringify(body)
  })
}

// 提交评论的评论
export const submitComment2 = (BlogID, body, commentID) => {
  return axios.post(`http://127.0.0.1:8000/comment/`, {
    'post': BlogID, 'reply_comment': commentID, 'body': JSON.stringify(body)
  })
}

// 关注
export const toFollow = (authorID) => {
  return axios.post('http://127.0.0.1:8000/userfavs/', {
    'goods': authorID
  })
}

// 获得关注信息
export const getFollowInfo = () => {
  return axios.get('http://127.0.0.1:8000/userfavs/')
}

// 点赞
export const Like = (BlogID) => {
  return axios.post('http://127.0.0.1:8000/like/', {
    'post': BlogID
  })
}

// 获取点赞信息
export const getLikeInfo = () => {
  return axios.get('http://127.0.0.1:8000/like/')
}
