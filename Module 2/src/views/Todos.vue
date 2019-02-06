<template>
    <div class="todos">
        <h1 v-if="!done">To-dos</h1>
        <h1 v-else>Finished To-dos</h1>
        <form v-if="!done" v-on:submit.prevent="addTodo(todo)">
            <input v-model="todo" placeholder="To-do">
            <button type="submit">Add To-do</button>
        </form>
        <div v-for="(item, index) in filteredTodos" :key="index"><router-link :to="{path: '/todo/' + item.id }"><Todo :todo="item" style="white-space: nowrap; overflow: hidden"></Todo></router-link></div>
        <br/>
        <router-link class="toggle" v-if="!done" to="/done">Show Finished Items</router-link>
        <router-link class="toggle" v-else to="/todos">Show Unfinished Items</router-link>
    </div>
</template>

<script>
    import { auth, db } from "@/firebaseConfig"
    import Todo from '@/views/Todo.vue'

    export default {
        name: "Todos",
        components: {
            Todo
        },

        data() {
            return {
                user: "",
                todos: [],

                todo: "",
            }
        },

        props: {
            done: {
                type: Boolean,
                default: false
            },
        },

        computed: {
            filteredTodos: function() {
                return this.todos.filter(i => i.done === this.done);
            }
        },

        beforeCreate: function() {
            auth.onAuthStateChanged(user => {
                this.user = user;
                if (!user) {
                    this.$router.push("")
                } else {
                    this.$bind('todos', db.collection('users').doc(this.user.uid).collection('todos').orderBy('createdAt', 'desc'));
                }
            })
        },

        methods: {
            addTodo(todo) {
                let createdAt = new Date();
                let done = false;
                db.collection('users').doc(this.user.uid).collection('todos').add({todo, createdAt, done});
            },
            deleteTodo(id) {
                db.collection('users').doc(this.user.uid).collection('todos').doc(id).delete();
            },
        },
    }
</script>

<style scoped>
    a.toggle {
        display: inline-block;
        padding: 10px;
        border: 1px solid lightgray;
    }
</style>
