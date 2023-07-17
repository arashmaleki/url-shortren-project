<template>
  <div class="centerForm">
    <b-card class="fixedForm mt-5" title="Register">
      <b-form @submit.prevent="register()" class="mt-4">
        <div class="d-flex">
          <b-form-group id="first-name" class="mr-3" label="First Name:" label-for="input-first-name">
            <b-form-input id="input-first-name" v-model="user_data.first_name" placeholder="First Name" required>
            </b-form-input>
          </b-form-group>

          <b-form-group id="last-name" label="Last Name:" label-for="input-last-name">
            <b-form-input id="input-last-name" v-model="user_data.last_name" placeholder="Last Name" required>
            </b-form-input>
          </b-form-group>
        </div>

        <b-form-group id="input-username" label="Username:" label-for="input-username">
          <b-form-input id="input-username" v-model="user_data.username" placeholder="Username" required></b-form-input>
        </b-form-group>

        <b-form-group id="email" label="Email Address:" label-for="input-email">
          <b-form-input id="input-email" v-model="user_data.email" type="email" placeholder="Email" required>
          </b-form-input>
        </b-form-group>

        <b-form-group id="input-password" label="Password:" label-for="input-password">
          <b-form-input id="input-password" v-model="user_data.password" type="password" placeholder="Password"
            required>
          </b-form-input>
        </b-form-group>

        <b-overlay :show="is_loading">
          <b-button class="mt-3 mb-3 w-100" type="submit" variant="primary">Register</b-button>
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
    layout: 'empty',
    data() {
      return {
        user_data: {
          username: '',
          password: '',
          email: '',
          first_name: '',
          last_name: ''
        },
        error: '',
        is_loading: false,
      }
    },
    methods: {
      async register() {
        try {
          this.is_loading = true
          let response = await this.$axios.$post('/api/user/register/', this.user_data)
          this.$router.push({
            path: '/login'
          })
        } catch (error) {
          this.error = error.response.data
        }
        this.is_loading = false
      },
    },
  }
</script>