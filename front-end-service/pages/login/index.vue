<template>
  <div class="centerForm">
    <b-card class="mt-5" title="Login">
      <b-form @submit.prevent="login" class="mt-4">

        <b-form-group id="input-username" label="Username:" label-for="input-username">
          <b-form-input id="input-username" v-model="user.username" placeholder="Username" required></b-form-input>
        </b-form-group>

        <b-form-group id="input-password" label="Password:" label-for="input-password">
          <b-form-input id="input-password" v-model="user.password" type="password" placeholder="Password" required>
          </b-form-input>
        </b-form-group>

        <b-overlay :show="is_loading">
          <b-button class="mt-3 mb-2 w-100" type="submit" variant="primary">Login</b-button>
        </b-overlay>
      </b-form>
      <template #footer>
        <b-link to="/register">Don't have an account</b-link>
      </template>
    </b-card>
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
            user: response.data.user,
          })
          this.$router.push({
            path: '/home'
          })
        }).catch((error) => {
          this.error = error.response.data
          localStorage.removeItem('auth.user')
          this.$auth.$storage.removeUniversal('auth.user')
          this.$auth.$storage.removeCookie('auth.user')
          this.$auth.logout()
        })
        this.is_loading = false
      },
    },
  }
</script>

<style scoped>

</style>
