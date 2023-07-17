<template>
    <div class="serendycityDeyails errorMessage">
        <h1 v-if="error.statusCode === 404">
            Ooops! {{ pageNotFound }}
        </h1>
        <h1 v-else>
            Ooops! {{ otherError }}
        </h1>
        <b-link class="errorMessage" to="/home">
            Home page
        </b-link>
    </div>
</template>

<script>
    export default {
        layout: 'default',
        props: {
            error: {
                type: Object,
                default: null
            }
        },
        data() {
            return {
                pageNotFound: 'Page Not Found.',
                otherError: 'An error occurred.'
            }
        },
        head() {
            const title =
                this.error.statusCode === 404 ? this.pageNotFound : this.otherError
            return {
                title
            }
        }
    }

</script>

<style scoped>
    h1 {
        font-size: 20px;
    }

</style>
