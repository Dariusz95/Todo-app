<!-- Formularz dodawania listy -->
<template>
  <div class="card h-100">
    <div class="form-group">
      <input v-model="name" type="email" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Nazwa listy">
    </div>
    <div class="form-group">
      <textarea v-model="description" type="email" class="form-control" id="description" aria-describedby="emailHelp"
                placeholder="Dodaj opis..."> </textarea>
    </div>

    <div>
      <button class="btn btn-outline-secondary" @click="$emit('removeForm', index)">Anuluj</button>
      <button class="btn btn-outline-secondary ml-2" @click="saveList">Zapisz</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "TodoCreate",
  data: () => {
    return {
      name: null,
      description: null
    }
  },
  props: ['index'],
  methods: {
    /**
     * Emituje event dodania listy z danymi listy
     */
    saveList() {
      const todoList = { name: this.name, description: this.description};
      this.$emit('saveList', {todoList, index: this.index});
    }
  }

}
</script>

<style scoped>

</style>
