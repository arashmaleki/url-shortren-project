<template>
  <div class="centerForm redirectContent">
    redirecting ...
  </div>
</template>

<script>
  export default {
    name: 'index',
    layout: 'empty',
    mounted() {
      this.initial()
    },
    methods: {
      async initial() {
        if (this.$route.params.id) {
          let long_url = await this.get_long_url()
          this.redirect(long_url)
        } else {
          this.push_to_page('/home')
        }
      },
      async get_long_url() {
        try {
          let response = await this.$axios.$get(`/api/shortener/redirect/${this.$route.params.id}`)
          return response.long_url
        } catch (error) {
          this.push_to_page('/home')
        }
      },
      redirect(long_url) {
        if (long_url) {
          window.location.href = long_url
        }
      },
      push_to_page(route) {
        this.$router.push({
          path: route
        })
      }
    },
  }
</script>

<style scoped>
  .redirectContent {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>