<!-- Stopka -->
<template>
  <div class="footer text-center">
    <div class="jumbotron jumbotron-fluid m-0">
      {{fullName}}
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  props: {
    fullName: String
  }
}
</script>

<style scoped>

</style>
