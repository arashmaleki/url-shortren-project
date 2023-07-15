<template>
  <div>
    <b-form @submit="register">
      <b-form-group id="email" label="Email Address:" label-for="input-email">
        <b-form-input id="input-email" v-model="user_data.email" type="email" placeholder="Enter email" required>
        </b-form-input>
      </b-form-group>

      <b-form-group id="first-name" label="First Name:" label-for="input-first-name">
        <b-form-input id="input-first-name" v-model="user_data.first_name" placeholder="First Name" required>
        </b-form-input>
      </b-form-group>

      <b-form-group id="last-name" label="Last Name:" label-for="input-last-name">
        <b-form-input id="input-last-name" v-model="user_data.last_name" placeholder="Last Name" required>
        </b-form-input>
      </b-form-group>

      <b-form-group id="input-username" label="Username:" label-for="input-username">
        <b-form-input id="input-username" v-model="user_data.username" placeholder="Username" required></b-form-input>
      </b-form-group>

      <b-form-group id="input-password" label="Password:" label-for="input-password">
        <b-form-input id="input-password" v-model="user_data.password" type="password" placeholder="Password" required>
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
        user_data: {
          username: '',
          password: '',
          email: '',
          first_name: '',
          last_name: ''
        },
        error: '',
        is_loading: false
      }
    },
    methods: {
      async register() {
        this.is_loading = true
        try {
          let response = await this.$axios.$post('/users/register', this.user_data)
          this.$router.push({
            path: '/login'
          })
        } catch (error) {
          this.error = error
        }
        this.is_loading = false
      },
    },
  }
</script>