import { createStore } from 'vuex';
import axios from 'axios';

const apiUrl = 'http://127.0.0.1:8000/api';

export default createStore({
  state: {
    userId: localStorage.getItem('userId') || null,
    isAuthenticated: localStorage.getItem('isAuthenticated') === 'true',
    accessToken: localStorage.getItem('accessToken') || null,
    refreshToken: localStorage.getItem('refreshToken') || null,
    loginError: '',
    siret: localStorage.getItem('siret') || null, 
  },
  mutations: {
    SET_AUTH_STATE(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
      localStorage.setItem('isAuthenticated', isAuthenticated);
    },
    SET_TOKENS(state, { accessToken, refreshToken }) {
      state.accessToken = accessToken;
      state.refreshToken = refreshToken;
      localStorage.setItem('accessToken', accessToken);
      localStorage.setItem('refreshToken', refreshToken);
    },
    SET_ERROR_MESSAGE(state, message) {
      state.errorMessage = message;
    },
    CLEAR_AUTH_STATE(state) {
      state.isAuthenticated = false;
      state.accessToken = null;
      state.refreshToken = null;
      localStorage.removeItem('isAuthenticated');
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      localStorage.removeItem('userId');
    },
    SET_USER_ID(state, userId) {
      state.userId = userId;
      localStorage.setItem('userId', userId);
    },
    SET_LOGIN_ERROR(state, errorMessage) {
      state.loginError = errorMessage;
    },
    SET_SIRET(state, siret) {
      state.siret = siret;
      localStorage.setItem('siret', siret); // Save siret to local storage
    },
  },
  actions: {
    async login({ commit }, { email, password }) {
      try {
        const response = await axios.post(`${apiUrl}/login/`, {
          email,
          password,
        });
    
        const { access: accessToken, refresh: refreshToken } = response.data.tokens;
        commit('SET_USER_ID', response.data.user_id);
        console.log(this.state.userId)
        commit('SET_TOKENS', { accessToken, refreshToken });
        commit('SET_AUTH_STATE', true);
      } catch (error) {
        commit('SET_LOGIN_ERROR', error.response?.data?.message || 'Login failed');
        throw error;
      }
        
      } ,
    async signup({ commit }, { email, password, firstName, lastName }) {
      try {
       
        const response = await axios.post(`${apiUrl}/register/`, {
          email,
          password,
          firstName,
          lastName,
        });
       
        const { message } = response.data;
        commit('SET_ERROR_MESSAGE', message || 'Signup functionality is not fully implemented');
      } catch (error) {
        commit('SET_ERROR_MESSAGE', error.response?.data?.message || 'Signup failed');
      }
    },
    logout({ commit }) {
      try {
        commit('CLEAR_AUTH_STATE');
      } catch (error) {
        console.error('Logout error:', error);
        
      }
    },
    async createEnterprise({ commit }, enterpriseDetails) {
      try {
        // Adjust the enterpriseDetails object to match the format
        const data = {
          raison: enterpriseDetails.raison,
          siret: enterpriseDetails.siret,
          adresse_postale: enterpriseDetails.adresse_postale,
          user: enterpriseDetails.user,
        };
    
        const response = await axios.post(`${apiUrl}/entreprise/create/`, data, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
          },
        });
        commit('SET_SIRET', enterpriseDetails.siret);
        commit('CLEAR_ERROR_MESSAGE');
        return response.data;
      } catch (error) {
        commit('SET_ERROR_MESSAGE', error.response?.data?.message || 'Failed to create enterprise');
        throw error;
      }
    },
    async createCommercial({ commit,state }, commercialDetails) {
      try {
        const siret = state.siret || localStorage.getItem('siret');
        if (!siret) {
          throw new Error('SIRET not found in local storage');
        }
        const enterpriseResponse = await axios.post(`${apiUrl}/entreprise/id/`, { siret }, {
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
          },
        });
        const data = {
          first_name: commercialDetails.first_name,
          last_name: commercialDetails.last_name,
          email: commercialDetails.email,
          phone_number: commercialDetails.phone_number,
          entreprise_id: enterpriseResponse.data.id, 
        };
        const response = await axios.post(`${apiUrl}/commerciaux/`, data, {
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
          },
          
        });
        return response.data;
      } catch (error) {
        commit('SET_ERROR_MESSAGE', error.response?.data?.message || 'Failed to create commercial');
        throw error;
      }
    },
    
  },
});