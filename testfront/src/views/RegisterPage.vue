<template>
  <h1>test register</h1>
  <v-card>
    <v-card-text>
      <v-text-field
        label="Email"
        v-model="email"
        required
        type="email"
        :rules="[email => !!email || 'Email is required', email => /^\S+@\S+\.\S+$/.test(email) || 'Invalid email format']"
      ></v-text-field>
      <v-text-field
        label="Password"
        v-model="password"
        type="password"
        required
        :rules="[
          password => !!password || 'Password is required',
          password => password.length >= 8 || 'Password must be at least 8 characters',
        ]"
      ></v-text-field>
      <v-text-field
        label="First Name"
        v-model="firstName"
        required
      ></v-text-field>
      <v-text-field
        label="Last Name"
        v-model="lastName"
        required
      ></v-text-field>
      <v-btn color="primary" @click="signupUser" :disabled="!email || !password || !firstName || !lastName">Signup</v-btn>
      <v-alert v-if="errorMessage" type="error">{{ errorMessage }}</v-alert>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      email: '',
      password: '',
      firstName: '',
      lastName: '',
      errorMessage: '',
    };
  },
  methods: {
    ...mapActions(['signup']),
    async signupUser() {
      try {
        await this.signup({
          email: this.email,
          password: this.password,
          firstName: this.firstName,
          lastName: this.lastName,
        });
        // Redirect to login after signup
        this.$router.push('/login');
      } catch (error) {
        this.errorMessage = error.response?.data?.message || 'Signup failed';
      }
    },
  },
};
</script>

<style scoped>
</style>