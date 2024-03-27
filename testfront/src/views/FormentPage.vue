<template>
  <v-card>
    <v-card-title>Étape 1 : Détails de l'entreprise</v-card-title>
    <v-card-text>
      <v-form ref="form" @submit.prevent="submitForm">
        <v-text-field
          v-model="entrepriseDetails.siret"
          label="SIRET"
          :rules="siretRules"
          required
        ></v-text-field>
        <v-text-field
          v-model="entrepriseDetails.raison"
          label="Raison sociale"
          :rules="raisonRules"
          required
        ></v-text-field>
        <v-text-field
          v-model="entrepriseDetails.adresse_postale"
          label="Adresse"
          :rules="adresseRules"
          required
        ></v-text-field>
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
      entrepriseDetails: {
        siret: '',
        raison: '',
        adresse_postale: ''
      },
      siretRules: [
        value => !!value || 'SIRET is required',
        value => /^\d{14}$/.test(value) || 'SIRET must be 14 digits long'
      ],
      raisonRules: [
        value => !!value || 'Raison sociale is required'
      ],
      adresseRules: [
        value => !!value || 'Adresse is required'
      ],
      errorMessage: ''
    };
  },
  methods: {
    ...mapActions(['createEnterprise']),
   async submitForm() {
    try {
      const enterpriseData = {
        raison: this.entrepriseDetails.raison,
        siret: this.entrepriseDetails.siret,
        adresse_postale: this.entrepriseDetails.adresse_postale,
        user: parseInt(this.$store.state.userId) // Assuming userId is a number
      };

      await this.createEnterprise(enterpriseData);
      // Move to the next step
      // Assuming you have a method to handle the step transition
      this.moveToNextStep();
    } catch (error) {
      // Handle form submission error
      this.errorMessage ='Failed to create enterprise';
    }
  },
  moveToNextStep() {
    this.$router.push('/commercial');
  }
}
};
</script>

<style>
/* Add your custom styles here */
</style>