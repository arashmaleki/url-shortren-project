<template>
  <b-navbar toggleable="lg" type="light" variant="light">
    <b-navbar-brand to="/home">URL Shortener</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown right v-if="$auth.loggedIn">
          <template #button-content>
            <span>{{ $store.state.user.authenticated_user.username }}</span>
          </template>
          <b-dropdown-item>
            <b-nav-item to="/profile">
              Profile
            </b-nav-item>
          </b-dropdown-item>
          <b-dropdown-item @click="logout">
            <b-nav-item>
              Logout
            </b-nav-item>
          </b-dropdown-item>
        </b-nav-item-dropdown>
        <div v-else>
          <b-nav-item to="/login">
            login
          </b-nav-item>
        </div>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
  export default {
    name: 'site-header',
    data() {
      return {
        user: {},
      }
    },
    mounted() {
      if (this.$auth.loggedIn) {
        this.get_user_profile_data()
      }
    },
    watch: {
      '$store.state.user.refresh_user_data'(value) {
        if (value) {
          this.get_user_profile_data()
          this.$store.commit('user/toggle_refresh_user_data')
        }
      }
    },
    methods: {
      async logout() {
        localStorage.removeItem('auth.user')
        this.$auth.$storage.removeUniversal('auth.user')
        this.$auth.$storage.removeCookie('auth.user')
        await this.$auth.logout()
        this.$store.commit('user/remove_user')
      },
      async get_user_profile_data() {
        let user_storage = await this.$auth.$storage.getUniversal('user')
        this.user = await this.$axios.$get(`/api/user/${user_storage.id}/`)
        this.$auth.$storage.setUniversal('user', this.user)
        this.$store.commit('user/set_user', {
          user: this.user,
        })
      },
    },
  }
</script>