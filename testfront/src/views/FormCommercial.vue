<template>
  <v-card>
    <v-card-title>Étape 2 : Détails du commercial</v-card-title>
    <v-card-text>
      <v-form ref="form" @submit.prevent="submitForm">
        <v-text-field v-model="commercialDetails.first_name" label="Prénom" :rules="[v => !!v || 'Prénom is required']"></v-text-field>
        <v-text-field v-model="commercialDetails.last_name" label="Nom" :rules="[v => !!v || 'Nom is required']"></v-text-field>
        <v-select v-model="commercialDetails.title" :items="titleOptions" label="État civil" required></v-select>
        <v-text-field v-model="commercialDetails.email" label="E-mail" :rules="emailRules" required></v-text-field>
        <v-text-field v-model="commercialDetails.phone_number" label="Numéro de téléphone" :rules="phoneRules" required></v-text-field>
        <v-btn color="primary" type="submit">Étape suivante</v-btn>
      </v-form>
      <v-alert v-if="errorMessage" type="error">{{ errorMessage }}</v-alert>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      commercialDetails: {
        first_name: '',
        last_name: '',
        title: '', // Added title property for civil status
        email: '',
        phone_number: '',
      },
      titleOptions: ['M.', 'Mme.'], // Options for the title select
      errorMessage: '',
    };
  },
  methods: {
    ...mapActions(['createCommercial']),
    async submitForm() {
      try {
        // Check if Prénom and Nom are not empty
        if (!this.commercialDetails.first_name || !this.commercialDetails.last_name) {
          throw new Error('Prénom and Nom are required');
        }

        // Check if title is selected
        if (!this.commercialDetails.title) {
          throw new Error('État civil is required');
        }
        
        await this.createCommercial(this.commercialDetails);
        // Move to the next step
        // Assuming you have a method to handle the step transition
        this.moveToNextStep();
      } catch (error) {
        // Handle form submission error
        this.errorMessage = error.message || 'Failed to create commercial details';
      }
    },
    moveToNextStep() {
      this.$router.push('/next-step');
    }
  },
  computed: {
    emailRules() {
      return [
        value => !!value || 'E-mail is required',
        value => /.+@.+\..+/.test(value) || 'Invalid e-mail format',
      ];
    },
    phoneRules() {
      return [
        value => !!value || 'Phone number is required',
        value => /^\d{10}$/.test(value) || 'Invalid phone number format (10 digits)',
      ];
    },
  }
};
</script>

<style>
/* Add your custom styles here */
</style>