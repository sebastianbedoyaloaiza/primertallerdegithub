<template>
  <div class="container">
    <h1>Registro</h1>
    <form @submit.prevent="register">
      <input 
        v-model="registerData.email" 
        type="email" 
        placeholder="Correo" 
        required 
      />
      <input 
        v-model="registerData.password" 
        type="password" 
        placeholder="Contraseña" 
        required 
      />
      <button type="submit">Registrar</button>
    </form>

    <h1>Inicio de Sesión</h1>
    <form @submit.prevent="login">
      <input 
        v-model="loginData.email" 
        type="email" 
        placeholder="Correo" 
        required 
      />
      <input 
        v-model="loginData.password" 
        type="password" 
        placeholder="Contraseña" 
        required 
      />
      <button type="submit">Ingresar</button>
    </form>

    <p v-if="message" class="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      registerData: { email: "", password: "" },
      loginData: { email: "", password: "" },
      message: "",
    };
  },
  methods: {
    async register() {
      try {
        const res = await axios.post("http://localhost:5000/register", this.registerData);
        this.message = res.data.message;
      } catch (err) {
        this.message = err.response?.data?.message || "Error en el registro";
      }
    },
    async login() {
      try {
        const res = await axios.post("http://localhost:5000/login", this.loginData);
        this.message = res.data.message;
      } catch (err) {
        this.message = err.response?.data?.message || "Error en el inicio de sesión";
      }
    },
  },
};
</script>

<style>
.container {
  max-width: 400px;
  margin: 2rem auto;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  text-align: center;
  font-family: Arial, sans-serif;
}

input, button {
  display: block;
  width: 100%;
  margin: 8px 0;
  padding: 8px;
}

button {
  cursor: pointer;
  background: #42b883;
  border: none;
  color: white;
  font-weight: bold;
  border-radius: 4px;
}

button:hover {
  background: #2c9c70;
}

.message {
  margin-top: 1rem;
  font-weight: bold;
  color: #333;
}
</style>
