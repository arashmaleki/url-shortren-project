<template>
    <b-container fluid class="customContainer">
        <site-header />
        <Nuxt />
    </b-container>
</template>

<script>
    export default {
        name: 'default',
        components: {
            siteHeader: () => import(`~/components/SiteHeader`),
        }
    }
</script>