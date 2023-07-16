<template>
  <div class="mt-4">
    <b-card>
      <b-form class="mb-4" @submit.prevent="submit_new_shortener_url()">

        <b-form-group id="input-long-url" label="URL:" label-for="input-long-url">
          <b-form-input class="ml-2 mr-2" id="input-long-url" v-model="new_long_url" placeholder="URL" required>
          </b-form-input>
        </b-form-group>

        <b-overlay :show="is_loading">
          <b-button type="submit" variant="success">Submit</b-button>
        </b-overlay>
        <div>
          {{ error }}
        </div>
      </b-form>

      <b-table :items="new_urls" :fields="fields" :per-page="page_size" show-empty bordered hover striped responsive
        small>
        <template #cell(copy)="row">
          <b-button variant="info" @click="copy_url(row.item.short_url)">Copy</b-button>
        </template>
        <template #cell(delete)="row">
          <b-button variant="danger" @click="delete_url(row.item.id, row.index)">Delete</b-button>
        </template>
      </b-table>
      <b-pagination-nav :link-gen="link_gen" :number-of-pages="total_pages" use-router align="center" />
    </b-card>
  </div>
</template>

<script>
  export default {
    name: 'shortener-url',
    data() {
      return {
        is_loading: false,
        error: '',
        new_long_url: '',
        new_urls: [],
        page_size: 10,
        total_pages: 1,
        fields: [{
            label: 'Long URL',
            key: 'long_url',
            class: 'text-center'
          },
          {
            label: 'Short URL',
            key: 'short_url',
            class: 'text-center'
          },
          {
            label: 'Copy',
            key: 'copy',
            class: 'text-center'
          },
          {
            label: 'Delete',
            key: 'delete',
            class: 'text-center'
          }
        ],
      }
    },
    watch: {
      '$route.query.page'(value) {
        this.get_user_urls()
      }
    },
    mounted() {
      this.get_user_urls()
    },
    methods: {
      async submit_new_shortener_url() {
        if (this.$auth.loggedIn) {
          this.is_loading = true
          try {
            let response = await this.$axios.$post('/api/shortener/', {
              long_url: this.new_long_url
            })
            this.get_user_urls()
          } catch (error) {
            this.error = error.response.data
          }
          this.is_loading = false
        } else {
          this.$router.push({
            path: '/login'
          })
        }
      },
      async get_user_urls() {
        if (this.$auth.loggedIn) {
          try {
            let response = await this.$axios.$get(
              `/api/shortener/?page=${this.$route.query.page ? this.$route.query.page : 1}`)
            this.new_urls = response.results
            this.total_pages = response.total_pages
          } catch (error) {}
        }
      },
      copy_url(url) {
        navigator.clipboard.writeText(url)
      },
      async delete_url(url_id, index) {
        try {
          let response = await this.$axios.$delete(`/api/shortener/${url_id}`)
          this.get_user_urls()
        } catch (error) {}
      },
      link_gen(page_number) {
        return page_number === 1 ? '?' : `?page=${page_number}`
      },
    },
  }
</script>