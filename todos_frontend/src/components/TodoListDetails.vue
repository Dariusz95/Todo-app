// Komponent wyświetlający szczegóły wybranej listy
<template>
  <div class="container">
    <!-- Widok danych listy w trybie podglądu -->
    <div class="mt-4" v-if="!editing">
      <div class="d-flex align-items-center">
        <h3 class="m-0">{{ listName }}</h3>
        <button class="btn btn-warning ml-3" @click="editList">Edytuj</button>
      </div>
      <div class="d-flex">
        <p class="float-left">{{ listDescription }}</p>
      </div>
    </div>

    <!-- Widok formularza edycji listy -->
    <div class="form-inline mt-4" v-if="editing">
      <div class="input-group">
        <input
          v-model="listNameForm"
          type="text"
          class="form-control mb-2 mr-sm-2"
          placeholder="Nazwa"
        />
      </div>

      <div class="input-group mb-2 mr-sm-2">
        <input
          v-model="listDescriptionForm"
          type="text"
          class="form-control"
          placeholder="Opis"
        />
      </div>
      <button
        type="submit"
        class="btn btn-outline-secondary mb-2"
        @click="cancelEditing"
      >
        Anuluj
      </button>
      <button type="submit" class="btn btn-success mb-2 ml-2" @click="saveList">
        Zapisz
      </button>
    </div>

    <!-- List zadań -->
    <div class="todos mt-4 p-4 border" v-if="todos.length > 0">
      <!-- Pojedyncze zadanie -->
      <div class="todo" v-for="todo in todos" v-bind:key="todo.id">
        <div class="form-check m-2">
          <input
            type="checkbox"
            v-model="todo.done"
            @change="updateTodo(todo)"
            class="form-check-input"
          />
          <label class="form-check-label">{{ todo.name }} </label>
          <button
            class="btn btn-danger btn-sm ml-3"
            @click="deleteTodo(todo.id)"
          >
            Usuń
          </button>
        </div>
      </div>
    </div>

    <!-- Formualrz dodawania nowego zadania -->
    <form class="form-inline mt-2">
      <div class="input-group mb-2 mr-sm-2">
        <input
          v-model="todoNameForm"
          type="text"
          class="form-control"
          placeholder="Nazwa todo"
        />
      </div>
      <button
        type="button"
        class="btn btn-success mb-2"
        :disabled="!this.todoNameForm"
        @click="addTodo(todoNameForm)"
      >
        Dodaj
      </button>
    </form>
  </div>
</template>

<script>
import API from "@/api";
import axios from "axios";

export default {
  name: "TodoListDetails",
  data: () => {
    return {
      todoListUri: API + "/todo-list/",
      todosUri: API + "/todos/",
      listId: null,
      listName: "",
      listDescription: "",
      todos: [],
      todoNameForm: "",
      editing: false,
      listNameForm: "",
      listDescriptionForm: "",
    };
  },
  mounted() {
    // Pobieranie id listy z parametru url
    this.listId = this.$route.params.id;

    // Pobieranie zadań z API
    axios.get(this.todoListUri + this.listId).then((res) => {
      const data = res.data;
      this.listName = data.name;
      this.listDescription = data.description;
      this.todos = data.todos;
    });
  },
  methods: {
    //Aktualizuje wybrane zadanie
    updateTodo(todo) {
      axios.put(this.todosUri + todo.id + "/", todo).then();
    },
    //Dodaje nowe zadanie o podanej nazwie
    addTodo(name) {
      const payload = { name, list: +this.listId };
      console.log(payload);
      axios
        .post(this.todosUri, payload)
        .then((res) => this.todos.push(res.data));
      this.todoNameForm = "";
    },

    //Usuwa zadanie o podanym id
    deleteTodo(id) {
      axios.delete(this.todosUri + id + "/").then(() => {
        this.todos = this.todos.filter((todo) => todo.id !== id);
      });
    },

    //Uruchamia tryb edycji listy
    editList() {
      this.editing = true;
      this.listNameForm = this.listName;
      this.listDescriptionForm = this.listDescription;
    },
    // Wyłącza tryb edycji listy
    cancelEditing() {
      this.editing = false;
      this.listNameForm = "";
      this.listDescriptionForm = "";
    },
    // Zapisuje listę
    saveList() {
      const payload = {
        name: this.listNameForm,
        description: this.listDescriptionForm,
      };

      // Wysyłka nowych danych listy do API
      axios.put(this.todoListUri + this.listId + "/", payload).then((res) => {
        const { name, description } = res.data;
        this.listName = name;
        this.listDescription = description;
        this.cancelEditing();
      });
    },
  },
};
</script>

<style scoped></style>
