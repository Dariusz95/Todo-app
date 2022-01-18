<!-- Widok pojedynczej listy -->
<template>
  <div class="todo-list" @click.prevent="goToDetails">
    <div class="header bg-secondary">
      <h2 class="text-white"> {{ list.list.name }} </h2>
      <button class="btn btn-danger"  type="button" @click.stop.prevent="deleteList"> &times;</button>
    </div>
    <div class="counts">
      <b> {{ list.done_amount }} / {{ list.total }} </b>
    </div>
    <div class="content">
      {{ list.list.description }}
    </div>
  </div>
</template>

<script>
import router from "@/router";

export default {
  name: "TodoList",
  props: ['list'],
  methods: {
    /**
     * Przejście do szczegółów listy
     */
    goToDetails() {
      router.push({name: 'todo-list-details', params: {id: this.list.list.id}})
    },
    /**
     * Wysyła event do usunięcia listy
     */
    deleteList() {
      this.$emit('deleteList', this.list.list.id)
    }
  }
}
</script>

<style scoped>

.todo-list {
  padding: 20px;
  padding-top: 0;
  border: 1px solid black;
  border-radius: 20px;
  min-width: 200px;
}

.header {
  padding: 10px 7px;
  margin: 0 -20px;
  background: darkgray;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  display: flex;
  justify-content: space-between;
}

.content, .counts {
  padding: 10px;
}

h2 {
  margin: 0;
}
</style>
