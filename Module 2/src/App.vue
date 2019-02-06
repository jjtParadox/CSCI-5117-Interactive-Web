<template>
    <div id="app">
        <nav>
            <Auth/>
        </nav>
        <router-view/>
    </div>
</template>

<script>
    import Auth from "@/components/Auth.vue"

    export default {
        name: 'app',
        components: {
            Auth
        }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }
    #app nav {
        text-align: right;
        margin-bottom: 20px;
    }
</style>
