<template>
  <div>

  </div>
</template>

<script>
  export default {
    name: 'index',
    layout: 'default',
    data() {
      return {
        shortener_urls: [],
      }
    },
    mounted() {
      if (this.$auth.loggedIn) {
        this.get_user_urls()

      } else {
        this.$router.push({
          path: '/home'
        })
      }
    },
    methods: {
      async get_user_urls() {
        try {
          let response = await this.$axios.$get('/shortener')
          this.shortener_urls = response.results
        } catch (error) {

        }
      }
    },
  }
</script>

<style scoped>

</style>