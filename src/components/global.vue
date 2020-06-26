<script>
let user_id = localStorage.getItem('user_id')?localStorage.getItem('user_id'):null
let username = localStorage.getItem('username')?localStorage.getItem('username'):null
let token = localStorage.getItem('token')?localStorage.getItem('token'):null
export default
{
  user_id,
  username,
  token
}
</script>
