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
          this.$router.push({
            path: '/home'
          })
        }
      },
      async get_long_url() {
        try {
          let response = await this.$axios.$get(`/api/shortener/redirect/${this.$route.params.id}`)
          return response.long_url
        } catch (error) {
          console.log(error);
        }
      },
      redirect(long_url) {
        window.location.href = long_url
      },
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