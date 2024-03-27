<template>
 <h1>test</h1>
 <v-card>
    <v-card-text>
   <v-text-field
  v-model="email"
  label="Email"
  required
  :rules="[
    v => !!v || 'Email is required',
    v => /.+@.+/.test(v) || 'Invalid email format'
  ]"
></v-text-field>

<v-text-field
  v-model="password"
  label="Password"
  type="password"
  required
  :rules="[
    v => !!v || 'Password is required',
    v => v.length >= 8 || 'Password must be at least 8 characters'
  ]"
></v-text-field>
      <v-btn color="primary" :disabled="!email || !password || errors.length" @click="loginUser">Login</v-btn>
      <v-alert v-if="errorMessage" type="error">{{ errorMessage }}</v-alert>
    </v-card-text>
      <router-link to="/register">Don't have an account? Register here</router-link>
</v-card>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  data() {
    return {
      email: '',
      password: '',
      errors: [],
      errorMessage: '',
    };
  },
 computed: {
    ...mapState(['loginError']),
  },
  methods: {
    ...mapActions(['login']),
    async loginUser() {
      this.errors = []; 
      try {
        await this.login({ email: this.email, password: this.password });
        this.$router.push('/home')
      } catch (error) {
       this.errorMessage = error.response.data.non_field_errors[0] || 'Login failed';
        console.log(error);
      }
    },
  },
};
</script>

<style scoped>
</style>