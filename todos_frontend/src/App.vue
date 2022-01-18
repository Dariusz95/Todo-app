<template>
  <div id="app">
    <Header></Header>
    <router-view/>
    <Footer full-name="Dariusz Bosko"></Footer>
  </div>
</template>

<style>

body {
  margin: 0;
  padding: 0;

}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}


#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
export default {
  components: {Footer, Header}
}
</script>
