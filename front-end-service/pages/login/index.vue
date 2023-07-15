<template>
  <div>
    <b-form @submit="login">

      <b-form-group id="input-username" label="Username:" label-for="input-username">
        <b-form-input id="input-username" v-model="user.username" placeholder="Username" required></b-form-input>
      </b-form-group>

      <b-form-group id="input-password" label="Password:" label-for="input-password">
        <b-form-input id="input-password" v-model="user.password" type="password" placeholder="Password" required>
        </b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
  export default {
    name: 'index',
    layout: 'empty',
    data() {
      return {
        user: {
          username: '',
          password: ''
        },
        is_loading: false,
        error: '',
      }
    },
    methods: {
      async login() {
        this.is_loading = true
        this.$auth.login({
          data: this.user
        }).then((response) => {
          this.$auth.setUserToken(response.data.token)
          this.$auth.$storage.setUniversal('user', response.data.user)
          this.$auth.setUser(response.data.user)
          this.$store.commit('user/set_user', {
            user: response.data.user
          })
          this.$store.commit('user/toggle_refresh_user_data')
          this.$router.push({
            path: '/home'
          })
        }).catch((error) => {
          this.error = error
          localStorage.removeItem('auth.user')
          this.$auth.$storage.removeUniversal('auth.user')
          this.$auth.$storage.removeCookie('auth.user')
          this.$auth.logout()
        })
        this.is_loading = false
      }
    },
  }
</script>

<style scoped>

</style>