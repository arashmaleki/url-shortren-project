<template>
  <div class="centerForm">
    <b-card class="fixedForm" title="Edit Profile">
      <b-form @submit.prevent="update_user()" class="mt-4">
        <div class="d-flex">
          <b-form-group id="first-name" class="mr-3" label="First Name:" label-for="input-first-name">
            <b-form-input id="input-first-name" v-model="user.first_name" placeholder="First Name" required>
            </b-form-input>
          </b-form-group>

          <b-form-group id="last-name" label="Last Name:" label-for="input-last-name">
            <b-form-input id="input-last-name" v-model="user.last_name" placeholder="Last Name" required>
            </b-form-input>
          </b-form-group>
        </div>

        <b-form-group id="input-bio" label="bio:" label-for="input-bio">
          <b-form-textarea rows="5" id="input-bio" v-model="user.bio" placeholder="Bio">
          </b-form-textarea>
        </b-form-group>

        <b-overlay :show="is_loading">
          <b-button class="mt-3 mb-3 w-100" type="submit" variant="success">Edit Profile</b-button>
        </b-overlay>
        <div class="errorMessage textAlignCenter">
          {{ error }}
        </div>

      </b-form>
    </b-card>
  </div>
</template>

<script>
  export default {
    name: 'index',
    layout: 'default',
    data() {
      return {
        error: '',
        user: {},
        is_loading: false,
      }
    },
    mounted() {
      this.get_user()
    },
    methods: {
      async get_user() {
        let user_storage = await this.$auth.$storage.getUniversal('user')
        this.user = await this.$axios.$get(`/api/user/${user_storage.id}/`)
      },
      async update_user() {
        try {
          this.is_loading = true
          await this.$axios.$patch(`/api/user/${this.user.id}/`, this.user)
        } catch (error) {
          this.error = error.response.data
        }
        this.is_loading = false
      },
    },
  }
</script>