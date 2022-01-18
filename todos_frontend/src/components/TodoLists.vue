//Lista list zadań -->
<template>
  <div class="container">
    <div class="todo-lists p-4">
      <div class="row">
        <div class="col-sm-12 col-md-4 col-lg-3" v-for="list in todoLists" v-bind:key="list.id">
          <!-- Widok listy zadan -->
          <TodoList
              v-on:deleteList="deleteTodoList"
              v-bind:list="list">
          </TodoList>
        </div>

        <!-- Formularze dodawnia nowej listy -->
        <div class="col-sm-12 col-md-4 col-lg-3" v-for="(form, index) in todoForms" v-bind:key="index">
          <TodoCreate v-bind:index="index" v-on:saveList="addTodoList" v-on:removeForm="removeForm"></TodoCreate>
        </div>
        <div class="col-sm-12 col-md-4 col-lg-3">
          <div class="card d-flex justify-content-center align-items-center add-todo-list">
            <button class="btn btn-outline-secondary" @click="addTodoForm">Dodaj</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import API from '../api';
import axios from 'axios';
import TodoList from "@/components/TodoList";
import TodoCreate from "@/components/TodoCreate";

export default {
  name: 'TodoLists',
  components: {TodoCreate, TodoList},
  data() {
    return {
      requestUri: API + '/todo-list/', // nakierowanie uri na /todo-list
      todoLists: [], // listy
      todoForms: [], // formularze

    }
  },
  mounted() {
    // Pobieranie list z API
    axios.get(this.requestUri).then(res => {
      this.todoLists = res.data
    })
  },
  methods: {
    /**
     * Dodawanie nowej listy zadań
     */
    addTodoList({todoList, index}) {
      // POST, dodajemy liste, usuwamy formularz
      axios.post(this.requestUri, todoList).then(res => {
            this.todoForms.splice(index, 1);
            this.todoLists.push({list: res.data, done_amount: 0, total: 0});
          }
      )
    },
    /**
     * Dodawanie formularza nowej listy
     */
    addTodoForm() {
      this.todoForms.push(1);
    },
    /**
     * Usuwanie listy o podanym id
     */
    deleteTodoList(id) {
      // Wysyłanie zapytania do usunięcia listy do API
      axios.delete(this.requestUri + id.toString()).then(() => {
            this.todoLists = this.todoLists.filter(list => list.list.id !== id)
          }
      )
    },
    /**
     * Usuwanie formularza dodawnia listy z podanego indeksu
     */
    removeForm(index) {
      this.todoForms.splice(index, 1);
    }
  }

}
</script>

<style scoped>
.add-todo-list {
  min-height: 170px;
  margin: 5px;
}
</style>
