import Vue from 'vue'
import Router from 'vue-router'

import Splash from './views/Splash.vue'
import Todos from './views/Todos.vue'
import Todo from './views/Todo.vue'
import NotFound from './views/NotFound.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'splash',
            component: Splash
        },
        {
            path: '/todos',
            name: 'todos',
            component: Todos,
        },
        {
            path: '/done',
            name: 'Done',
            component: Todos,
            props: {
                done: true
            }
        },
        {
            path: '/todo/:id',
            name: 'Todo',
            component: Todo,
        },
        {
            path: '/404',
            name: '404',
            component: NotFound,
        },
        {
            path: '*',
            redirect: '/404',
        },
    ]
})
