<template>
    <div class="auth">

        <template v-if="!user">
            <a href @click.prevent="signInWithGoogle">Sign in with Google</a>
        </template>

        <template v-if="user">

            <!--<img :src="user.photoURL" alt="avatar" style="width: 30px; height: 30px; border-radius: 50%;">-->
            <a href @click.prevent="signOut">Sign Out</a>
        </template>

        <!-- <pre>{{ user }}</pre> -->
    </div>
</template>

<script>
    import { auth, provider } from "@/firebaseConfig";

    export default {
        name: "auth",

        data() {
            return {
                user: null
            };
        },

        // TODO: look at https://savvyapps.com/blog/definitive-guide-building-web-app-vuejs-firebase
        beforeCreate: function() {
            auth.onAuthStateChanged(user => {
                // console.log("user state:", user);
                if (user) {
                    this.user = user;
                }
            });
        },

        methods: {
            signInWithGoogle: function() {
                auth
                    .signInWithRedirect(provider)
                    .then(result => {
                        this.user = result.user;
                        console.log("?", this.user);
                    })
                    .catch(err => console.log(err));
            },
            signOut: function() {
                auth
                    .signOut()
                    .then(() => {
                        this.user = null;
                    })
                    .catch(err => console.log(err));
            }
        }
    };

</script>

<style scoped>
    div.auth {
        display: inline-block;
        padding: 10px;
        border: 1px solid lightgray;
    }
</style>
