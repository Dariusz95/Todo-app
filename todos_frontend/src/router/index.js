import Vue from 'vue'
import VueRouter from 'vue-router'
import TodoListDetails from "@/components/TodoListDetails";
import TodoLists from "@/components/TodoLists";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: TodoLists
  },
  {
    path: '/list/:id',
    name: 'todo-list-details',
    component: TodoListDetails
  }
]

const router = new VueRouter({
  routes
})

export default router
