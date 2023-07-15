<template>
    <b-container fluid class="customContainer">
        <site-header />
        <Nuxt class="siteContainer" />
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