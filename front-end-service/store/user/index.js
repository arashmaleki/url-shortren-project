export const state = () => ({
    authenticated_user: {},
    refresh_user_data: false
})

export const mutations = {
    set_user(state, value) {
        state.authenticated_user = value.user
        this.$auth.$storage.setUniversal('user', value.user)
    },
    remove_user(state) {
        state.authenticated_user = {}
        state.user_id = ''
    },
    toggle_refresh_user_data(state) {
        state.refresh_user_data = !state.refresh_user_data
    }
}