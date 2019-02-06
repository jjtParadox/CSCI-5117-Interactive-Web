<template>
    <div class="splash">
        <h1>Personal To-dos</h1>
        <h2>Please sign in above</h2>
    </div>
</template>

<script>
    import { auth } from "@/firebaseConfig"

    export default {
        name: "Splash",

        beforeCreate: function() {
            auth.onAuthStateChanged(user => {
                if (user) {
                    this.$router.push("todos")
                }
            })
        },
    }
</script>

<style scoped>

</style>
